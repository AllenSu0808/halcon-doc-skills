# disp_polygon (Operator)

## Name

`disp_polygon` — Displays a polyline.

## Signature

`disp_polygon( : : WindowHandle, Row, Column : )`

## Description

`disp_polygon` displays a polyline with the row coordinates
*`Row`* and the column coordinates *`Column`* in the
output window. The parameters *`Row`* and *`Column`* have to
be provided as tuples. Straight lines are drawn between the given points.
The start and the end of the polyline are not connected.

The operators used to control the display of regions
(e.g., [`set_color`](set_color.md), [`set_gray`](set_gray.md), [`set_draw`](set_draw.md),
[`set_line_width`](set_line_width.md)) can also be used with polylines.

## Attention

The given coordinates must lie within the window.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`WindowHandle`** (input_control)  window `→`  (handle)

Window handle.

**`Row`** (input_control)  polygon.y-array `→`  (integer / real)

Row index

Default:
[16,80,80]

Suggested values:
0, 64, 128, 256, 511

Value range:
`0
≤
Row
≤
511` (lin)

Minimum increment:
1

Recommended increment:
10

**`Column`** (input_control)  polygon.x-array `→`  (integer / real)

Column index

Default:
[48,16,80]

Suggested values:
0, 64, 128, 256, 511

Value range:
`0
≤
Column
≤
511` (lin)

Minimum increment:
1

Recommended increment:
10

## Example (C)

```
/* display a rectangle */

disp_rectangle1_margin1(Htuple WindowHandle,
                        Hlong Row1, long Column1,
                        Hlong Row2, long Column2)
{
  Htuple Row, Col;
  create_tuple(&Row,4);
  create_tuple(&Col,4);

  set_i(Row,Row1,0);
  set_i(Col,Column1,0);

  set_i(Row,Row1,1);
  set_i(Col,Column2,1);

  set_i(Row,Row2,2);
  set_i(Col,Column2,2);

  set_i(Row,Row2,3);
  set_i(Col,Column1,3);

  set_i(Row,Row1,4);
  set_i(Col,Column1,4);

  T_disp_polygon(WindowHandle,Row,Col);

}
```

## Result

`disp_polygon` returns 2 (
H_MSG_TRUE)
.

## Possible Predecessors

`open_window`,
`set_rgb`,
`set_lut`,
`set_hsi`,
`set_draw`,
`set_color`,
`set_colored`,
`set_line_width`

## Alternatives

`disp_line`,
`gen_region_polygon`,
`disp_region`

## See also

`open_window`,
`set_color`,
`set_rgb`,
`set_hsi`,
`set_line_width`

## Module

Foundation
