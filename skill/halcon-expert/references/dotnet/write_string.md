# WriteString (Operator)

## Name

`WriteString` — Print text in a window.

## Signature

`static void HOperatorSet.WriteString(HTuple windowHandle, HTuple stringVal)`

`void HWindow.WriteString(HTuple stringVal)`

`void HWindow.WriteString(string stringVal)`

## Description

`WriteString` prints *`stringVal`* in the output
window starting at the current cursor position. The output text has to fit
within the right window boundary (the width of the string can be queried
by [`GetStringExtents`](get_string_extents.md)).

The font currently assigned to the window will used. The text cursor is
positioned at the end of the text.

`WriteString` can output all three types of data used in HALCON .
The conversion to a string is guided by the following rules:

- strings are not converted.
- integer numbers are converted without any spaces before or
  after the number.
- floating numbers are printed (if possible) with a floating point
  and without an exponent.
- the resulting strings are concatenated without spaces.

For buffering of texts see [`SetSystem`](set_system.md) with the flag
'flush_graphic'.

## Attention

If clipping at the window boundary is desired, exceptions can be switched
off by `set_check('~text')`.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`windowHandle`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Window handle.

**`stringVal`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string* / int / long / double)

Tuple of output values (all types).

Default:
"hello"

## Result

`WriteString` returns 2 (
H_MSG_TRUE)
if the window is valid and the
output text fits within the current line (see [`SetCheck`](set_check.md)).
Otherwise an exception is raised.

## Possible Predecessors

`OpenWindow`,
`SetFont`,
`GetStringExtents`

## Alternatives

`FwriteString`

## See also

`SetTposition`,
`GetStringExtents`,
`SetFont`,
`SetSystem`,
`SetCheck`

## Module

Foundation
