# QueryTshape (Operator)

## Name

`QueryTshape` — Query all shapes available for text cursors.

## Warning

**`QueryTshape` is obsolete and is only provided for
reasons of backward compatibility.**

## Signature

`static void HOperatorSet.QueryTshape(HTuple windowHandle, out HTuple textCursor)`

`HTuple HWindow.QueryTshape()`

## Description

`QueryTshape` queries the available shapes of text
cursors for the output window. The retrieved shapes can be
used by the operator [`SetTshape`](set_tshape.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`windowHandle`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Window handle.

**`textCursor`** (output_control)  string-array `→` [HTuple](HTuple.md) (*string*)

Names of the available text cursors.

## Result

`QueryTshape` returns 2 (
H_MSG_TRUE)
.

## Possible Predecessors

`OpenWindow`

## Possible Successors

`SetTshape`,
`WriteString`,
`ReadString`

## See also

`SetTshape`,
`GetShape`,
`SetTposition`,
`WriteString`,
`ReadString`

## Module

Foundation
