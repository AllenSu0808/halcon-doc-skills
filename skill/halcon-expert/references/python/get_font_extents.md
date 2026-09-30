# get_font_extents (Operator)

## Name

`get_font_extents` — Get the maximum size of all characters of a font.

## Signature

`def get_font_extents(window_handle: HHandle) -> Tuple[Union[int, float], Union[int, float], Union[int, float], Union[int, float]]`

## Description

`get_font_extents` queries the maximum width
(*`max_width`*), height (*`max_height`*), and extension
above and below the baseline (*`max_ascent`* and
*`max_descent`*, respectively) of the font that is currently set
for the window *`window_handle`*. The sizes are measured in
pixels.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`window_handle`** (input_control)  window `→` HHandle

Window handle.

**`max_ascent`** (output_control)  extent.y `→` Union[int, float]

Maximum height above baseline.

**`max_descent`** (output_control)  extent.y `→` Union[int, float]

Maximum extension below baseline.

**`max_width`** (output_control)  extent.x `→` Union[int, float]

Maximum character width.

**`max_height`** (output_control)  extent.y `→` Union[int, float]

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
