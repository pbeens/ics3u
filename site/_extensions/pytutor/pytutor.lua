--[[
Embed a Python file in a Python Tutor step-through visualizer.

Usage:  {{< pytutor file="examples/spec_sheet.py" height="480" >}}

The path is relative to the document. The code is read at build time, so
the visualizer always shows the tested example file.
]]

local function url_encode(s)
  return (s:gsub("[^%w%-%._~]", function(c)
    return string.format("%%%02X", string.byte(c))
  end))
end

local function read_file(path)
  local f = io.open(path, "r")
  if not f then return nil end
  local content = f:read("a")
  f:close()
  return content
end

return {
  ["pytutor"] = function(args, kwargs, meta)
    local file = pandoc.utils.stringify(kwargs["file"] or "")
    local height = pandoc.utils.stringify(kwargs["height"] or "")
    if height == "" then height = "480" end
    if file == "" then
      return pandoc.Strong(pandoc.Str("pytutor: missing file argument"))
    end

    local doc_dir = pandoc.path.directory(quarto.doc.input_file)
    local code = read_file(pandoc.path.join({ doc_dir, file }))
    if not code then
      return pandoc.Strong(pandoc.Str("pytutor: file not found: " .. file))
    end
    code = code:gsub("%s+$", "")

    local params = "code=" .. url_encode(code)
      .. "&cumulative=false&curInstr=0&heapPrimitives=nevernest"
      .. "&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false"
    local embed = "https://pythontutor.com/iframe-embed.html#" .. params
      .. "&codeDivHeight=400&codeDivWidth=470"
    local full = "https://pythontutor.com/visualize.html#" .. params .. "&mode=display"

    if quarto.doc.is_format("html:js") then
      return pandoc.RawBlock("html",
        '<style>.reveal .pytutor-link{font-size:0.45em;margin-top:0;}</style>'
        .. '<div class="pytutor">'
        .. '<iframe src="' .. embed .. '" width="100%" height="' .. height
        .. '" frameborder="0" loading="lazy" title="Python Tutor visualizer"></iframe>'
        .. '<p class="pytutor-link"><a href="' .. full
        .. '" target="_blank" rel="noopener">Open in Python Tutor</a></p>'
        .. '</div>')
    end
    return pandoc.Para({ pandoc.Link("Step through this code in Python Tutor", full) })
  end
}
