# GetTposition (Operator)

## Name

`GetTposition` — Get cursor position.

## Signature

`static void HOperatorSet.GetTposition(HTuple windowHandle, out HTuple row, out HTuple column)`

`void HWindow.GetTposition(out int row, out int column)`

## Description

`GetTposition` queries the current position of the text
cursor in the output window. The position is measured in the image
coordinate system. The next output of text in this window starts at
the cursor position. The left end of the baseline for writing the
next string (not considering descenders) is placed on this
position. The position is changed by the output or input of text
([`WriteString`](write_string.md), [`ReadString`](read_string.md)) or by an explicit change
of position by ([`SetTposition`](set_tposition.md), [`NewLine`](new_line.md)).

## Attention

If the output text does not fit completely into the window, an exception is
raised. This can be avoided by
`set_check('~text')`.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`windowHandle`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Window handle.

**`row`** (output_control)  point.y `→` [HTuple](HTuple.md) (*int* / long)

Row index of text cursor position.

**`column`** (output_control)  point.x `→` [HTuple](HTuple.md) (*int* / long)

Column index of text cursor position.

## Result

`GetTposition` returns 2 (
H_MSG_TRUE)
if the window is valid. Otherwise
an exception is raised.

## Possible Predecessors

`OpenWindow`,
`SetFont`

## Possible Successors

`SetTposition`,
`WriteString`,
`ReadString`,
`ReadChar`

## See also

`NewLine`,
`ReadString`,
`SetTposition`,
`WriteString`,
`SetCheck`

## Module

Foundation
