# NewLine (Operator)

## Name

`NewLine` — Set the position of the text cursor to the beginning of the next line.

## Signature

`static void HOperatorSet.NewLine(HTuple windowHandle)`

`void HWindow.NewLine()`

## Description

`NewLine` sets the position of the text cursor to the beginning
of the next line. The new position depends on the current font. The left end
of the baseline for writing the following text string (not considering
descenders) is placed on this position.

If the next line does not fit into the window the content of the window is
scrolled by the height of one line in the upper direction. In order to
reach the correct new cursor position the font used in the next line must
be set before `NewLine` is called. The position is changed by the output or input of text
([`WriteString`](write_string.md), [`ReadString`](read_string.md))
or by an explicit change of position by ([`SetTposition`](set_tposition.md)).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`windowHandle`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Window handle.

## Result

`NewLine` returns 2 (
H_MSG_TRUE)
if the window is valid. Otherwise
an exception is raised.

## Possible Predecessors

`OpenWindow`,
`SetFont`,
`WriteString`

## Alternatives

`GetTposition`,
`GetStringExtents`,
`SetTposition`

## See also

`WriteString`,
`SetFont`

## Module

Foundation
