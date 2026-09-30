# GetStringExtents (Operator)

## Name

`GetStringExtents` — Get the spatial size of a string.

## Signature

`static void HOperatorSet.GetStringExtents(HTuple windowHandle, HTuple values, out HTuple ascent, out HTuple descent, out HTuple width, out HTuple height)`

`HTuple HWindow.GetStringExtents(HTuple values, out HTuple descent, out HTuple width, out HTuple height)`

`int HWindow.GetStringExtents(string values, out int descent, out int width, out int height)`

## Description

`GetStringExtents` queries width and height of the output
size of a string using the font of the window. Thereby strings with
multiple lines are treated as if concatenated into a single line.
In addition, the extension above and below the baseline is returned
(*`ascent`* and *`descent`*, respectively).

The sizes are measured in the coordinate system of the window (for
text windows in pixels). Using `GetStringExtents`, it is
possible to determine text output and input independently from the
used font. The conversion from integer numbers and floating point
numbers to text strings is the same as in [`WriteString`](write_string.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`windowHandle`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Window handle.

**`values`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string* / double / int / long)

Values to consider.

Default:
"test_string"

**`ascent`** (output_control)  extent.y `→` [HTuple](HTuple.md) (*int* / long / double)

Maximum height above baseline.

**`descent`** (output_control)  extent.y `→` [HTuple](HTuple.md) (*int* / long / double)

Maximum extension below baseline.

**`width`** (output_control)  extent.x `→` [HTuple](HTuple.md) (*int* / long / double)

Text width.

**`height`** (output_control)  extent.y `→` [HTuple](HTuple.md) (*int* / long / double)

Text height.

## Result

`GetStringExtents` returns 2 (
H_MSG_TRUE)
if the window is valid.
Otherwise an exception is raised.

## Possible Predecessors

`OpenWindow`,
`SetFont`

## Possible Successors

`SetTposition`,
`WriteString`,
`ReadString`,
`ReadChar`

## See also

`GetFontExtents`,
`SetTposition`,
`SetFont`

## Module

Foundation
