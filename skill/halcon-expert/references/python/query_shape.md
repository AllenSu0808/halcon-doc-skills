# query_shape (Operator)

## Name

`query_shape` — Query the region display modes.

## Signature

`def query_shape() -> Sequence[str]`

## Description

`query_shape` returns the names of all region display
modes (e.g., 'original', 'circle', 'rectangle1',
'rectangle2', 'ellipse', etc.) for the window. They are used
by [`set_shape`](set_shape.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`display_shape`** (output_control)  string-array `→` Sequence[str]

region display mode names.

## Result

`query_shape` returns 2 (
H_MSG_TRUE)
, if the window is valid.
Otherwise an exception is raised.

## Possible Successors

`get_shape`,
`set_shape`,
`disp_region`

## See also

`set_shape`,
`get_shape`,
`disp_region`

## Module

Foundation
