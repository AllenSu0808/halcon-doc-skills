# get_contour_style (Operator)

## Name

`get_contour_style` — Get the current contour display fill style.

## Signature

`get_contour_style( : : WindowHandle : Style)`

## Description

`get_contour_style` returns the contour fill style of the
output window as set with [`set_contour_style`](set_contour_style.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`WindowHandle`** (input_control)  window `→`  (handle)

Window handle.

**`Style`** (output_control)  string `→`  (string)

Current contour fill style.

## Result

`get_contour_style` returns 2 (
H_MSG_TRUE)
, if the window is valid.
Otherwise an exception is raised.

## Possible Successors

`set_contour_style`,
`disp_xld`

## See also

`set_contour_style`,
`disp_xld`

## Module

Foundation
