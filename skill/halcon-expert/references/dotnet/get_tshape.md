# GetTshape (Operator)

## Name

`GetTshape` — Get the shape of the text cursor.

## Warning

**`GetTshape` is obsolete and is only provided for
reasons of backward compatibility.**

## Signature

`static void HOperatorSet.GetTshape(HTuple windowHandle, out HTuple textCursor)`

`string HWindow.GetTshape()`

## Description

`GetTshape` queries the shape of the text cursor for the
output window. A new cursor shape is set by the operator
[`SetTshape`](set_tshape.md).

A text cursor marks the current position for text output (which can also
be invisible). It is different from the mouse cursor (although both will
be called ”cursor” if the context makes misconceptions impossible).
The available shapes for the text cursor can be queried with
[`QueryTshape`](query_tshape.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`windowHandle`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Window handle.

**`textCursor`** (output_control)  string `→` [HTuple](HTuple.md) (*string*)

Name of the current text cursor.

## Result

`GetTshape` returns 2 (
H_MSG_TRUE)
if the window is valid. Otherwise an
exception is raised.

## Possible Predecessors

`OpenWindow`,
`SetFont`

## Possible Successors

`SetTshape`,
`SetTposition`,
`WriteString`,
`ReadString`,
`ReadChar`

## See also

`SetTshape`,
`QueryTshape`,
`WriteString`,
`ReadString`

## Module

Foundation
