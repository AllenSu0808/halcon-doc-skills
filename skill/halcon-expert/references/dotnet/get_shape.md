# GetShape (Operator)

## Name

`GetShape` — Get the current region output shape.

## Signature

`static void HOperatorSet.GetShape(HTuple windowHandle, out HTuple displayShape)`

`string HWindow.GetShape()`

## Description

`GetShape` returns the shape in which regions are
displayed. The available shapes can be queried with
[`QueryShape`](query_shape.md) and then changed with [`SetShape`](set_shape.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`windowHandle`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Window handle.

**`displayShape`** (output_control)  string `→` [HTuple](HTuple.md) (*string*)

Current region output shape.

## Result

`GetShape` returns 2 (
H_MSG_TRUE)
if the window is valid.
Otherwise an exception is raised.

## Possible Predecessors

`QueryShape`

## Possible Successors

`SetShape`,
`DispRegion`

## See also

`SetShape`,
`QueryShape`,
`DispRegion`

## Module

Foundation
