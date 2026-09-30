# SetTposition (Operator)

## Name

`SetTposition` — Set the position of the text cursor.

## Signature

`static void HOperatorSet.SetTposition(HTuple windowHandle, HTuple row, HTuple column)`

`void HWindow.SetTposition(int row, int column)`

## Description

`SetTposition` sets the position of the text cursor in the
output window. The reference position is the upper left corner of an
upper case character.

The position is measured in the image coordinate system. The
position of the text cursor can be marked, e.g., by an underscore.
The next text output in this window starts at the cursor position.
The left end of the baseline for writing the following text string
(not considering descenders) is placed on this position.

The position is changed by the output or input of text
([`WriteString`](write_string.md), [`ReadString`](read_string.md)) or by an explicit change
of position by (`SetTposition`, [`NewLine`](new_line.md)). In order
to stop the display of the cursor, the operator [`SetTshape`](set_tshape.md)
with the parameter ”invisible” can be used.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`windowHandle`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Window handle.

**`row`** (input_control)  point.y `→` [HTuple](HTuple.md) (*int* / long)

Row index of text cursor position.

Default:
24

**`column`** (input_control)  point.x `→` [HTuple](HTuple.md) (*int* / long)

Column index of text cursor position.

Default:
12

## Result

`SetTposition` returns 2 (
H_MSG_TRUE)
if the window is valid. Otherwise
an exception is raised.

## Possible Predecessors

`OpenWindow`

## Possible Successors

`WriteString`,
`ReadString`

## Alternatives

`NewLine`

## See also

`ReadString`,
`WriteString`

## Module

Foundation
