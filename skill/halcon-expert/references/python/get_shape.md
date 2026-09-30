# get_shape (Operator)

## Name

`get_shape` — Get the current region output shape.

## Signature

`def get_shape(window_handle: HHandle) -> str`

## Description

`get_shape` returns the shape in which regions are
displayed. The available shapes can be queried with
[`query_shape`](query_shape.md) and then changed with [`set_shape`](set_shape.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`window_handle`** (input_control)  window `→` HHandle

Window handle.

**`display_shape`** (output_control)  string `→` str

Current region output shape.

## Result

`get_shape` returns 2 (
H_MSG_TRUE)
if the window is valid.
Otherwise an exception is raised.

## Possible Predecessors

`query_shape`

## Possible Successors

`set_shape`,
`disp_region`

## See also

`set_shape`,
`query_shape`,
`disp_region`

## Module

Foundation
