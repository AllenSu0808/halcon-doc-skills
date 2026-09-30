# get_font_extents (Operator)

## Name

`get_font_extents` — Get the maximum size of all characters of a font.

## Signature

`get_font_extents( : : WindowHandle : MaxAscent, MaxDescent, MaxWidth, MaxHeight)`

## Description

`get_font_extents` queries the maximum width
(*`MaxWidth`*), height (*`MaxHeight`*), and extension
above and below the baseline (*`MaxAscent`* and
*`MaxDescent`*, respectively) of the font that is currently set
for the window *`WindowHandle`*. The sizes are measured in
pixels.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`WindowHandle`** (input_control)  window `→`  (handle)

Window handle.

**`MaxAscent`** (output_control)  extent.y `→`  (integer / real)

Maximum height above baseline.

**`MaxDescent`** (output_control)  extent.y `→`  (integer / real)

Maximum extension below baseline.

**`MaxWidth`** (output_control)  extent.x `→`  (integer / real)

Maximum character width.

**`MaxHeight`** (output_control)  extent.y `→`  (integer / real)

Maximum character height.

## Result

`get_font_extents` returns 2 (
H_MSG_TRUE)
if the window is valid.
Otherwise an exception is raised.

## Possible Predecessors

`open_window`,
`set_font`

## Possible Successors

`set_tposition`,
`write_string`,
`read_string`,
`read_char`

## See also

`get_string_extents`,
`set_tposition`,
`set_font`

## Module

Foundation
