# SetLineStyle (Operator)

## Name

`SetLineStyle` — Define a contour output pattern.

## Signature

`static void HOperatorSet.SetLineStyle(HTuple windowHandle, HTuple style)`

`void HWindow.SetLineStyle(HTuple style)`

## Description

`SetLineStyle` defines the output pattern of the margin of
regions and of XLD contours. The information is used by operators like
[`DispRegion`](disp_region.md), [`DispLine`](disp_line.md), [`DispPolygon`](disp_polygon.md) etc. The
current value can be queried with [`GetLineStyle`](get_line_style.md).
*`style`* contains up to five pairs of values. The first value is
the length of the visible contour part, the second is the length of
the invisible part. The value pairs are used cyclical for contour
output.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`windowHandle`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Window handle.

**`style`** (input_control)  integer-array `→` [HTuple](HTuple.md) (*int* / long)

Contour pattern.

Default:
[]

Value range:
`1
≤
style
≤
120`

## Example (HDevelop)

```
* stroke line: X-Windows
set_line_style(WindowHandle,[20,7])
* point-stroke line: X-Windows
set_line_style(WindowHandle,[20,7,3,7])
* passing line (standard)
set_line_style(WindowHandle,[])
```

## Result

`SetLineStyle` returns 2 (
H_MSG_TRUE)
if the parameter is
correct and the window is valid. Otherwise an exception is raised.

## Possible Predecessors

`GetLineStyle`

## Possible Successors

`DispRegion`

## See also

`GetLineStyle`,
`SetLineApprox`,
`DispRegion`

## Module

Foundation
