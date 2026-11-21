/*
  Predict-and-step visualizer.

  Each .stepper element holds its Python source in a hidden <pre>. The widget
  shows the code, a prediction box, and Step / Run all / Start over buttons.
  On the first Step, Python (Pyodide) runs the whole program once with a line
  tracer, recording the output and variables after every line. The buttons
  then move through those recorded steps.
*/
(function () {
  "use strict";

  const PYODIDE_URL = "https://cdn.jsdelivr.net/pyodide/v0.28.1/full/";
  const MAX_STEPS = 2000;
  let pyodidePromise = null;

  const TRACER = `
import sys, io, types, json

def __stepper_trace(src, max_steps, inputs=None):
    events = []
    out = io.StringIO()
    g = {"__name__": "__main__"}
    answers = list(inputs or [])

    def typed_input(prompt=""):
        out.write(str(prompt))
        if not answers:
            raise EOFError("this box has no more typed answers")
        answer = answers.pop(0)
        out.write(answer + "\\n")
        return answer

    g["input"] = typed_input

    def snapshot(line):
        variables = {}
        for k, v in g.items():
            if k.startswith("__") or isinstance(v, types.ModuleType) or callable(v):
                continue
            variables[k] = repr(v)
        events.append({"line": line, "out": out.getvalue(), "vars": variables})

    def tracer(frame, event, arg):
        if frame.f_code.co_filename != "<student>":
            return None
        if event == "line":
            if len(events) >= max_steps:
                raise RuntimeError("Stopped after too many steps")
            snapshot(frame.f_lineno)
        return tracer

    error = None
    old_stdout = sys.stdout
    sys.stdout = out
    try:
        code = compile(src, "<student>", "exec")
        sys.settrace(tracer)
        exec(code, g)
    except SyntaxError as e:
        error = {"type": type(e).__name__, "message": str(e.msg), "line": e.lineno}
    except Exception as e:
        tb = e.__traceback__
        line = None
        while tb is not None:
            if tb.tb_frame.f_code.co_filename == "<student>":
                line = tb.tb_lineno
            tb = tb.tb_next
        error = {"type": type(e).__name__, "message": str(e), "line": line}
    finally:
        sys.settrace(None)
        sys.stdout = old_stdout
    snapshot(None)
    return json.dumps({"events": events, "error": error})
`;

  function loadPython() {
    if (!pyodidePromise) {
      pyodidePromise = new Promise((resolve, reject) => {
        const start = () =>
          window.loadPyodide({ indexURL: PYODIDE_URL })
            .then(async (py) => { await py.runPythonAsync(TRACER); resolve(py); })
            .catch(reject);
        if (window.loadPyodide) { start(); return; }
        const s = document.createElement("script");
        s.src = PYODIDE_URL + "pyodide.js";
        s.onload = start;
        s.onerror = () => reject(new Error("Could not load Python"));
        document.head.appendChild(s);
      });
    }
    return pyodidePromise;
  }

  function el(tag, cls, text) {
    const e = document.createElement(tag);
    if (cls) e.className = cls;
    if (text !== undefined) e.textContent = text;
    return e;
  }

  function build(root) {
    const sourceEl = root.querySelector(".stepper-source");
    const source = sourceEl.textContent;
    const inputs = root.dataset.input ? root.dataset.input.split("|") : [];
    sourceEl.remove();
    const lines = source.split("\n");

    // Code panel
    const codePanel = el("div", "stepper-code");
    const lineEls = lines.map((text, i) => {
      const row = el("div", "stepper-line");
      row.appendChild(el("span", "stepper-arrow", ""));
      row.appendChild(el("span", "stepper-num", String(i + 1)));
      row.appendChild(el("span", "stepper-text", text || " "));
      codePanel.appendChild(row);
      return row;
    });
    const legend = el("div", "stepper-legend");
    legend.innerHTML = '<span class="stepper-key stepper-key-ran"></span> line that just ran' +
      ' &nbsp; <span class="stepper-key stepper-key-next">&#10140;</span> next line to run';

    // Controls
    const controls = el("div", "stepper-controls");
    const btnStep = el("button", "stepper-btn stepper-btn-primary", "Step ▶");
    const btnBack = el("button", "stepper-btn", "◀ Back");
    const btnAll = el("button", "stepper-btn", "Run all ▶▶");
    const btnReset = el("button", "stepper-btn", "Start over");
    [btnStep, btnBack, btnAll, btnReset].forEach((b) => { b.type = "button"; controls.appendChild(b); });
    const status = el("div", "stepper-status", "Read the code and write your prediction, then press Step.");

    // Side panel
    const side = el("div", "stepper-side");
    side.appendChild(el("div", "stepper-label", "Your prediction"));
    const prediction = el("textarea", "stepper-prediction");
    prediction.rows = Math.min(Math.max(lines.length - 2, 3), 8);
    prediction.placeholder = "What will this program print?";
    prediction.spellcheck = false;
    side.appendChild(prediction);
    side.appendChild(el("div", "stepper-label", "Output"));
    const output = el("pre", "stepper-output", "");
    side.appendChild(output);
    const varsLabel = el("div", "stepper-label", "Variables");
    const varsBox = el("div", "stepper-vars");
    side.appendChild(varsLabel);
    side.appendChild(varsBox);
    varsLabel.hidden = true;
    varsBox.hidden = true;

    const left = el("div", "stepper-left");
    left.appendChild(codePanel);
    left.appendChild(legend);
    if (inputs.length) {
      left.appendChild(el("div", "stepper-inputs",
        "When the program asks for input, this box types: " + inputs.join(", ")));
    }

    const body = el("div", "stepper-body");
    body.appendChild(left);
    body.appendChild(side);
    root.appendChild(body);
    root.appendChild(controls);
    root.appendChild(status);

    let trace = null;   // { events, error }
    let step = 0;       // number of lines that have run

    function render() {
      lineEls.forEach((r) => { r.classList.remove("ran", "next", "error"); r.firstChild.textContent = ""; });
      if (!trace) {
        output.textContent = "";
        varsBox.innerHTML = "";
        btnBack.disabled = true;
        btnStep.disabled = false;
        btnAll.disabled = false;
        return;
      }
      const ev = trace.events;
      const total = ev.length - 1;            // final snapshot has line null
      const state = ev[step];
      const ranLine = step > 0 ? ev[step - 1].line : null;
      const nextLine = state.line;
      if (ranLine) lineEls[ranLine - 1].classList.add("ran");
      if (nextLine) { lineEls[nextLine - 1].classList.add("next"); lineEls[nextLine - 1].firstChild.textContent = "➜"; }

      output.textContent = state.out;
      const names = Object.keys(state.vars);
      const anyVars = ev.some((e) => Object.keys(e.vars).length > 0);
      varsLabel.hidden = !anyVars;
      varsBox.hidden = !anyVars;
      varsBox.innerHTML = "";
      if (anyVars) {
        if (names.length === 0) {
          varsBox.appendChild(el("div", "stepper-empty", "(none yet)"));
        } else {
          const table = el("table", "stepper-vars-table");
          names.forEach((n) => {
            const tr = el("tr");
            tr.appendChild(el("td", "stepper-var-name", n));
            tr.appendChild(el("td", "stepper-var-value", state.vars[n]));
            table.appendChild(tr);
          });
          varsBox.appendChild(table);
        }
      }

      const finished = step >= total;
      btnStep.disabled = finished;
      btnAll.disabled = finished;
      btnBack.disabled = step === 0;
      if (finished && trace.error) {
        if (trace.error.line) lineEls[trace.error.line - 1].classList.add("error");
        status.textContent = `Stopped with an error on line ${trace.error.line || "?"}: ` +
          `${trace.error.type}: ${trace.error.message}`;
        status.classList.add("stepper-status-error");
      } else {
        status.classList.remove("stepper-status-error");
        status.textContent = finished
          ? "Finished. Compare the output with your prediction."
          : `Step ${step} of ${total}. Press Step to run the next line.`;
      }
    }

    async function ensureTrace() {
      if (trace) return true;
      status.textContent = "Loading Python… (the first time can take a few seconds)";
      btnStep.disabled = btnAll.disabled = true;
      try {
        const py = await loadPython();
        py.globals.set("__stepper_src", source);
        py.globals.set("__stepper_inputs", JSON.stringify(inputs));
        const json = await py.runPythonAsync(`__stepper_trace(__stepper_src, ${MAX_STEPS}, json.loads(__stepper_inputs))`);
        trace = JSON.parse(json);
        step = 0;
        return true;
      } catch (err) {
        status.textContent = "Could not run Python here: " + err.message;
        btnStep.disabled = btnAll.disabled = false;
        return false;
      }
    }

    btnStep.addEventListener("click", async () => {
      if (!(await ensureTrace())) return;
      step = Math.min(step + 1, trace.events.length - 1);
      render();
    });
    btnAll.addEventListener("click", async () => {
      if (!(await ensureTrace())) return;
      step = trace.events.length - 1;
      render();
    });
    btnBack.addEventListener("click", () => {
      if (!trace) return;
      step = Math.max(step - 1, 0);
      render();
    });
    btnReset.addEventListener("click", () => {
      trace = null;
      step = 0;
      status.classList.remove("stepper-status-error");
      status.textContent = "Read the code and write your prediction, then press Step.";
      render();
    });

    render();
  }

  function init() {
    document.querySelectorAll(".stepper").forEach((root) => {
      if (!root.dataset.ready) { root.dataset.ready = "1"; build(root); }
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
