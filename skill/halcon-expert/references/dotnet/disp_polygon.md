# DispPolygon (Operator)

## Name

`DispPolygon` — Displays a polyline.

## Signature

`static void HOperatorSet.DispPolygon(HTuple windowHandle, HTuple row, HTuple column)`

`void HWindow.DispPolygon(HTuple row, HTuple column)`

## Description

`DispPolygon` displays a polyline with the row coordinates
*`row`* and the column coordinates *`column`* in the
output window. The parameters *`row`* and *`column`* have to
be provided as tuples. Straight lines are drawn between the given points.
The start and the end of the polyline are not connected.

The operators used to control the display of regions
(e.g., [`SetColor`](set_color.md), [`SetGray`](set_gray.md), [`SetDraw`](set_draw.md),
[`SetLineWidth`](set_line_width.md)) can also be used with polylines.

## Attention

The given coordinates must lie within the window.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`windowHandle`** (input_control)  window `→` [HWindow](HWindow.md), [HTuple](HTuple.md) (*IntPtr*)

Window handle.

**`row`** (input_control)  polygon.y-array `→` [HTuple](HTuple.md) (*int* / long / double)

Row index

Default:
[16,80,80]

Suggested values:
0, 64, 128, 256, 511

Value range:
`0
≤
row
≤
511` (lin)

Minimum increment:
1

Recommended increment:
10

**`column`** (input_control)  polygon.x-array `→` [HTuple](HTuple.md) (*int* / long / double)

Column index

Default:
[48,16,80]

Suggested values:
0, 64, 128, 256, 511

Value range:
`0
≤
column
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

`DispPolygon` returns 2 (
H_MSG_TRUE)
.

## Possible Predecessors

`OpenWindow`,
`SetRgb`,
`SetLut`,
`SetHsi`,
`SetDraw`,
`SetColor`,
`SetColored`,
`SetLineWidth`

## Alternatives

`DispLine`,
`GenRegionPolygon`,
`DispRegion`

## See also

`OpenWindow`,
`SetColor`,
`SetRgb`,
`SetHsi`,
`SetLineWidth`

## Module

Foundation
