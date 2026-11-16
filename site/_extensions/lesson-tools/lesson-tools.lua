--[[
Lesson page helpers.

{{< lesson-code >}}  or  {{< lesson-code lesson="01" hide="exit_ticket" >}}
  (lesson= for a non-lesson page; hide= skips files whose names contain that text)
  Lists every example program for this lesson (examples/lLL_*.py, where LL is
  the lesson number from the file name lesson-LL-*.qmd), with a .py download,
  the matching notebook on GitHub (notebooks/MM-LL-name.ipynb, built by
  scripts/build_notebooks.py), and Open in Callysto | Colab links.

{{< feedback >}}
  A short feedback paragraph with a link that opens the GitHub feedback form,
  prefilled with this page's title and address.
]]

local REPO = "https://github.com/pbeens/ics3u"
local REPO_PATH = "pbeens/ics3u"
local BRANCH = "main"
local SITE = "https://peter.beens.ca/ics3u/"

local function url_encode(s)
  return (s:gsub("[^%w%-%._~]", function(c)
    return string.format("%%%02X", string.byte(c))
  end))
end

local function lesson_numbers(kwargs)
  local input = quarto.doc.input_file
  local file = pandoc.path.filename(input)
  local dir = pandoc.path.filename(pandoc.path.directory(input))
  local lesson = pandoc.utils.stringify(kwargs["lesson"] or "")
  if lesson == "" then lesson = file:match("^lesson%-(%d%d)%-") end
  return dir:match("^module%-(%d%d)%-"), lesson, pandoc.path.directory(input)
end

local function nice_name(name)
  local label = name:gsub("_", " ")
  label = label:gsub("^%l", string.upper):gsub("%f[%a][Cc]pu%f[%A]", "CPU")
  local mistake = label:match("^Mistake (.+)$")
  if mistake then label = "Mistake: " .. mistake end
  return label
end

local function link(text, href, attrs)
  return pandoc.Link(text, href, "", attrs or {})
end

local function lesson_code(kwargs)
  local module, lesson, dir = lesson_numbers(kwargs)
  if not module or not lesson then
    return pandoc.Strong(pandoc.Str("lesson-code: not a lesson page"))
  end
  local hide = pandoc.utils.stringify(kwargs["hide"] or "")
  local files = {}
  for _, f in ipairs(pandoc.system.list_directory(pandoc.path.join({ dir, "examples" }))) do
    if f:match("^l" .. lesson .. "_.+%.py$") and (hide == "" or not f:find(hide, 1, true)) then
      table.insert(files, f)
    end
  end
  table.sort(files)
  if #files == 0 then return pandoc.Para({}) end

  local header = { { pandoc.Plain("Program") }, { pandoc.Plain("Python file") },
                   { pandoc.Plain("Notebook") }, { pandoc.Plain("Open notebook in") } }
  local rows = {}
  for _, f in ipairs(files) do
    local name = f:match("^l%d%d_(.+)%.py$")
    local nb = "notebooks/" .. module .. "-" .. lesson .. "-" .. name:gsub("_", "-") .. ".ipynb"
    local callysto = "https://hub.callysto.ca/jupyter/hub/user-redirect/git-pull?repo="
      .. url_encode(REPO) .. "&branch=" .. BRANCH .. "&subPath=" .. nb .. "&depth=1"
    local colab = "https://colab.research.google.com/github/" .. REPO_PATH .. "/blob/" .. BRANCH .. "/" .. nb
    table.insert(rows, {
      { pandoc.Plain(nice_name(name)) },
      { pandoc.Plain(link({ pandoc.Code(f) }, "examples/" .. f, { download = f })) },
      { pandoc.Plain(link("View or download", REPO .. "/blob/" .. BRANCH .. "/" .. nb)) },
      { pandoc.Plain({ link("Callysto", callysto), pandoc.Str(" | "), link("Colab", colab) }) },
    })
  end
  return pandoc.utils.from_simple_table(pandoc.SimpleTable(
    {}, { "AlignDefault", "AlignDefault", "AlignDefault", "AlignDefault" }, { 0, 0, 0, 0 }, header, rows))
end

local function feedback(meta)
  local title = pandoc.utils.stringify(meta.title or "")
  local rel = pandoc.path.make_relative(quarto.doc.input_file, quarto.project.directory)
  local page = SITE .. rel:gsub("%.qmd$", ".html")
  local href = REPO .. "/issues/new?template=feedback.yml&title="
    .. url_encode("[" .. title .. "] ") .. "&page=" .. url_encode(page)
  local div = pandoc.Div({
    pandoc.Para({ pandoc.Str("Found a mistake, a code example that doesn't run, or an idea that would make this lesson better? Feedback from teachers and students is always appreciated.") }),
    pandoc.Para({ link({ pandoc.Strong("Report an error or suggest a change") }, href,
      { target = "_blank", rel = "noopener" }),
      pandoc.Str(" opens a short form on GitHub with this lesson already filled in. Please don't post answers to worksheets, quizzes, or tests: issues are public.") }),
  }, pandoc.Attr("", { "feedback-section" }))
  return div
end

return {
  ["lesson-code"] = function(args, kwargs, meta) return lesson_code(kwargs) end,
  ["feedback"] = function(args, kwargs, meta) return feedback(meta) end,
}
