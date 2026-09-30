# get_string_extents (Operator)

## Name

`get_string_extents` — Get the spatial size of a string.

## Signature

`def get_string_extents(window_handle: HHandle, values: MaybeSequence[Union[str, float, int]]) -> Tuple[Union[int, float], Union[int, float], Union[int, float], Union[int, float]]`

## Description

`get_string_extents` queries width and height of the output
size of a string using the font of the window. Thereby strings with
multiple lines are treated as if concatenated into a single line.
In addition, the extension above and below the baseline is returned
(*`ascent`* and *`descent`*, respectively).

The sizes are measured in the coordinate system of the window (for
text windows in pixels). Using `get_string_extents`, it is
possible to determine text output and input independently from the
used font. The conversion from integer numbers and floating point
numbers to text strings is the same as in [`write_string`](write_string.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`window_handle`** (input_control)  window `→` HHandle

Window handle.

**`values`** (input_control)  string(-array) `→` MaybeSequence[Union[str, float, int]]

Values to consider.

Default:
"test_string"

**`ascent`** (output_control)  extent.y `→` Union[int, float]

Maximum height above baseline.

**`descent`** (output_control)  extent.y `→` Union[int, float]

Maximum extension below baseline.

**`width`** (output_control)  extent.x `→` Union[int, float]

Text width.

**`height`** (output_control)  extent.y `→` Union[int, float]

Text height.

## Result

`get_string_extents` returns 2 (
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

`get_font_extents`,
`set_tposition`,
`set_font`

## Module

Foundation
