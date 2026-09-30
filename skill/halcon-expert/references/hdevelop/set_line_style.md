# set_line_style (Operator)

## Name

`set_line_style` — Define a contour output pattern.

## Signature

`set_line_style( : : WindowHandle, Style : )`

## Description

`set_line_style` defines the output pattern of the margin of
regions and of XLD contours. The information is used by operators like
[`disp_region`](disp_region.md), [`disp_line`](disp_line.md), [`disp_polygon`](disp_polygon.md) etc. The
current value can be queried with [`get_line_style`](get_line_style.md).
*`Style`* contains up to five pairs of values. The first value is
the length of the visible contour part, the second is the length of
the invisible part. The value pairs are used cyclical for contour
output.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`WindowHandle`** (input_control)  window `→`  (handle)

Window handle.

**`Style`** (input_control)  integer-array `→`  (integer)

Contour pattern.

Default:
[]

Value range:
`1
≤
Style
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

`set_line_style` returns 2 (
H_MSG_TRUE)
if the parameter is
correct and the window is valid. Otherwise an exception is raised.

## Possible Predecessors

`get_line_style`

## Possible Successors

`disp_region`

## See also

`get_line_style`,
`set_line_approx`,
`disp_region`

## Module

Foundation
