# get_string_extents (Operator)

## Name

`get_string_extents` — Get the spatial size of a string.

## Signature

`get_string_extents( : : WindowHandle, Values : Ascent, Descent, Width, Height)`

## Description

`get_string_extents` queries width and height of the output
size of a string using the font of the window. Thereby strings with
multiple lines are treated as if concatenated into a single line.
In addition, the extension above and below the baseline is returned
(*`Ascent`* and *`Descent`*, respectively).

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

**`WindowHandle`** (input_control)  window `→`  (handle)

Window handle.

**`Values`** (input_control)  string(-array) `→`  (string / real / integer)

Values to consider.

Default:
'test_string'

**`Ascent`** (output_control)  extent.y `→`  (integer / real)

Maximum height above baseline.

**`Descent`** (output_control)  extent.y `→`  (integer / real)

Maximum extension below baseline.

**`Width`** (output_control)  extent.x `→`  (integer / real)

Text width.

**`Height`** (output_control)  extent.y `→`  (integer / real)

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
