--[[
Predict-and-step visualizer for a Python example file.

Usage:  {{< stepper file="examples/l01_computer_report.py" >}}
        {{< stepper file="examples/l09_greeter.py" input="Sam|8" >}}

input= gives the answers typed at each input() prompt, separated by |. The
box shows each answer after its prompt, as a terminal would.

The path is relative to the document. The code is read at build time, so the
widget always shows the tested example file. Python runs in the browser
(Pyodide), so any module Pyodide supports works, including platform.
]]

local function read_file(path)
  local f = io.open(path, "r")
  if not f then return nil end
  local content = f:read("a")
  f:close()
  return content
end

local function html_escape(s)
  return (s:gsub("&", "&amp;"):gsub("<", "&lt;"):gsub(">", "&gt;"))
end

return {
  ["stepper"] = function(args, kwargs, meta)
    local file = pandoc.utils.stringify(kwargs["file"] or "")
    if file == "" then
      return pandoc.Strong(pandoc.Str("stepper: missing file argument"))
    end

    local doc_dir = pandoc.path.directory(quarto.doc.input_file)
    local code = read_file(pandoc.path.join({ doc_dir, file }))
    if not code then
      return pandoc.Strong(pandoc.Str("stepper: file not found: " .. file))
    end
    code = code:gsub("%s+$", "")

    if not quarto.doc.is_format("html:js") then
      return pandoc.CodeBlock(code, pandoc.Attr("", { "python" }))
    end

    quarto.doc.add_html_dependency({
      name = "stepper",
      version = "1.0.0",
      scripts = { "stepper.js" },
      stylesheets = { "stepper.css" },
    })

    local input = pandoc.utils.stringify(kwargs["input"] or "")
    local input_attr = ""
    if input ~= "" then
      input_attr = ' data-input="' .. html_escape(input):gsub('"', "&quot;") .. '"'
    end

    return pandoc.RawBlock("html",
      '<div class="stepper"' .. input_attr .. '><pre class="stepper-source" hidden>'
      .. html_escape(code) .. '</pre></div>')
  end
}
