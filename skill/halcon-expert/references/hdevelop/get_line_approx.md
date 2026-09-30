# get_line_approx (Operator)

## Name

`get_line_approx` — Get the current approximation error for contour display.

## Warning

**`get_line_approx` is obsolete and is only provided for
reasons of backward compatibility.**

## Signature

`get_line_approx( : : WindowHandle : Approximation)`

## Description

`get_line_approx` returns a parameter that controls the
approximation error for region contour display in the
window. It is used by the operator
[`disp_region`](disp_region.md). *`Approximation`* controls the polygon
approximation for contour display ( 0 <=> no approximation). *`Approximation`* is only
important for displaying the contour of objects, especially if a line
style was set with [`set_line_style`](set_line_style.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`WindowHandle`** (input_control)  window `→`  (handle)

Window handle.

**`Approximation`** (output_control)  string `→`  (integer)

Current approximation error for contour display.

## Result

`get_line_approx` returns 2 (
H_MSG_TRUE)
if the window is valid.
Otherwise an exception is raised.

## Possible Successors

`set_line_approx`,
`set_line_style`,
`disp_region`

## See also

`get_region_polygon`,
`set_line_approx`,
`set_line_style`,
`disp_region`

## Module

Foundation
