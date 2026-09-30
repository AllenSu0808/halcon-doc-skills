# write_string (Operator)

## Name

`write_string` — Print text in a window.

## Signature

`write_string( : : WindowHandle, String : )`

## Description

`write_string` prints *`String`* in the output
window starting at the current cursor position. The output text has to fit
within the right window boundary (the width of the string can be queried
by [`get_string_extents`](get_string_extents.md)).

The font currently assigned to the window will used. The text cursor is
positioned at the end of the text.

`write_string` can output all three types of data used in HALCON .
The conversion to a string is guided by the following rules:

- strings are not converted.
- integer numbers are converted without any spaces before or
  after the number.
- floating numbers are printed (if possible) with a floating point
  and without an exponent.
- the resulting strings are concatenated without spaces.

For buffering of texts see [`set_system`](set_system.md) with the flag
'flush_graphic'.

## Attention

If clipping at the window boundary is desired, exceptions can be switched
off by `set_check('~text')`.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`WindowHandle`** (input_control)  window `→`  (handle)

Window handle.

**`String`** (input_control)  string(-array) `→`  (string / integer / real)

Tuple of output values (all types).

Default:
'hello'

## Result

`write_string` returns 2 (
H_MSG_TRUE)
if the window is valid and the
output text fits within the current line (see [`set_check`](set_check.md)).
Otherwise an exception is raised.

## Possible Predecessors

`open_window`,
`set_font`,
`get_string_extents`

## Alternatives

`fwrite_string`

## See also

`set_tposition`,
`get_string_extents`,
`set_font`,
`set_system`,
`set_check`

## Module

Foundation
