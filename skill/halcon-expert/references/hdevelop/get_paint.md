# get_paint (Operator)

## Name

`get_paint` — Get the current display mode for gray values.

## Signature

`get_paint( : : WindowHandle : Mode)`

## Description

`get_paint` returns the display mode for gray values in the
window. *`Mode`* is used by the operator
[`disp_image`](disp_image.md). `get_paint` is used for temporary
changes of the gray value display mode. The current value is queried,
then changed (with the operator [`set_paint`](set_paint.md)) and finally the
old value is written back. The available modes can be viewed with
the operator [`query_paint`](query_paint.md). *`Mode`* is the name
of the display mode. If a mode can be customized with parameters,
the parameter values are passed in a tuple after the mode name. The
order of values is the same as in [`set_paint`](set_paint.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`WindowHandle`** (input_control)  window `→`  (handle)

Window handle.

**`Mode`** (output_control)  string-array `→`  (string / integer / real)

Name and parameter values of the current display mode.

## Result

`get_paint` returns 2 (
H_MSG_TRUE)
if the window is valid.
Otherwise an exception is raised.

## Possible Predecessors

`query_paint`

## Possible Successors

`set_paint`,
`disp_region`,
`disp_image`

## See also

`set_paint`,
`query_paint`,
`disp_image`

## Module

Foundation
