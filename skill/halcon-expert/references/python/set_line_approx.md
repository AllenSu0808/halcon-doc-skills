# set_line_approx (Operator)

## Name

`set_line_approx` — Define the approximation error for contour display.

## Warning

**`set_line_approx` is obsolete and is only provided for
reasons of backward compatibility.**

## Signature

`def set_line_approx(window_handle: HHandle, approximation: int) -> None`

## Description

`set_line_approx` defines the approximation error for region and xld
contour display in the window *`window_handle`*. *`approximation`*
values greater than zero cause an approximation of line strokes using less
points. This may enable faster and in some cases smoother visualization. The
parameter describes the maximal deviation in pixels of the approximated
contour from the original contour (Ramer-Douglas-Peucker algorithm).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`window_handle`** (input_control)  window `→` HHandle

Window handle.

**`approximation`** (input_control)  integer `→` int

Maximum deviation from the original contour.

Default:
0

Value range:
`0
≤
approximation`

## Result

`set_line_approx` returns 2 (
H_MSG_TRUE)
if the parameter is
correct and the window is valid. Otherwise an exception is raised.

## Possible Predecessors

`get_line_approx`

## Possible Successors

`disp_region`

## Alternatives

`get_region_polygon`,
`disp_polygon`

## See also

`get_line_approx`,
`set_line_style`,
`set_draw`,
`disp_region`,
`disp_polygon`

## Module

Foundation
