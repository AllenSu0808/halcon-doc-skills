# get_draw (Operator)

## Name

`get_draw` — Get the current region fill mode.

## Signature

`get_draw( : : WindowHandle : Mode)`

## Description

`get_draw` returns the region fill mode of the
output window. It is used by operators as [`disp_region`](disp_region.md),
[`disp_circle`](disp_circle.md), [`disp_arrow`](disp_arrow.md),
[`disp_rectangle1`](disp_rectangle1.md), [`disp_rectangle2`](disp_rectangle2.md) etc.
The region fill mode is set with [`set_draw`](set_draw.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`WindowHandle`** (input_control)  window `→`  (handle)

Window handle.

**`Mode`** (output_control)  string `→`  (string)

Current region fill mode.

## Result

`get_draw` returns 2 (
H_MSG_TRUE)
, if the window is valid.
Otherwise an exception is raised.

## Possible Successors

`set_draw`,
`disp_region`

## See also

`set_draw`,
`disp_region`,
`set_paint`

## Module

Foundation
