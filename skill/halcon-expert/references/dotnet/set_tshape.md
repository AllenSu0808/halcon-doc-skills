# SetTshape (Operator)

## Name

`SetTshape` — Set the shape of the text cursor.

## Warning

**`SetTshape` is obsolete and is only provided for
reasons of backward compatibility.**

## Signature

`static void HOperatorSet.SetTshape(HTuple windowHandle, HTuple textCursor)`

`void HWindow.SetTshape(string textCursor)`

## Description

`SetTshape` sets the shape and the display mode of the text
cursor of the output window.

A text cursor marks the current position for text output. It is different
from the mouse cursor (although both will be called 'cursor', if the context
makes misconceptions impossible). The available shapes for the text cursor
can be queried with [`QueryTshape`](query_tshape.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`windowHandle`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Window handle.

**`textCursor`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Name of cursor shape.

Default:
"invisible"

## Result

`SetTshape` returns 2 (
H_MSG_TRUE)
if the window is valid and the
given cursor shape is defined for this window. Otherwise an
exception is raised.

## Possible Predecessors

`OpenWindow`,
`QueryTshape`,
`GetTshape`

## Possible Successors

`WriteString`,
`ReadString`

## See also

`GetTshape`,
`QueryTshape`,
`WriteString`,
`ReadString`

## Module

Foundation
