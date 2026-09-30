# SetLineApprox (Operator)

## Name

`SetLineApprox` — Define the approximation error for contour display.

## Warning

**`SetLineApprox` is obsolete and is only provided for
reasons of backward compatibility.**

## Signature

`static void HOperatorSet.SetLineApprox(HTuple windowHandle, HTuple approximation)`

`void HWindow.SetLineApprox(int approximation)`

## Description

`SetLineApprox` defines the approximation error for region and xld
contour display in the window *`windowHandle`*. *`approximation`*
values greater than zero cause an approximation of line strokes using less
points. This may enable faster and in some cases smoother visualization. The
parameter describes the maximal deviation in pixels of the approximated
contour from the original contour (Ramer-Douglas-Peucker algorithm).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`windowHandle`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Window handle.

**`approximation`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Maximum deviation from the original contour.

Default:
0

Value range:
`0
≤
approximation`

## Example (HDevelop)

```
* Calling...
set_line_approx(WindowHandle,Approximation)
set_draw(WindowHandle,'margin')
disp_region(Obj,WindowHandle)

* ...corresponds with
get_region_polygon(Obj,Approximation,Row,Col)
disp_polygon(WindowHandle,Row,Col)
```

## Result

`SetLineApprox` returns 2 (
H_MSG_TRUE)
if the parameter is
correct and the window is valid. Otherwise an exception is raised.

## Possible Predecessors

`GetLineApprox`

## Possible Successors

`DispRegion`

## Alternatives

`GetRegionPolygon`,
`DispPolygon`

## See also

`GetLineApprox`,
`SetLineStyle`,
`SetDraw`,
`DispRegion`,
`DispPolygon`

## Module

Foundation
