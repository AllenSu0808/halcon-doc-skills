# projection_pl (Operator)

## Name

`projection_pl` — Calculate the projection of a point onto a line.

## Signature

`projection_pl( : : Row, Column, Row1, Column1, Row2, Column2 : RowProj, ColProj)`

## Description

The operator `projection_pl` calculates the projection of a
point (*`Row`*,*`Column`*) onto a line which is
represented by the two points (*`Row1`*,*`Column1`*) and
(*`Row2`*,*`Column2`*). The coordinates of the projected
point are returned in *`RowProj`* and *`ColProj`*.

### Parameter Broadcasting

This operator supports parameter broadcasting.
This means that each parameter can be given as a tuple of length
*1* or *N*.
Parameters with tuple length *1* will be repeated internally
such that the number of projections is always *N*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`Row`** (input_control)  point.y(-array) `→`  (real / integer)

Row coordinate of the point.

**`Column`** (input_control)  point.x(-array) `→`  (real / integer)

Column coordinate of the point.

**`Row1`** (input_control)  point.y(-array) `→`  (real / integer)

Row coordinate of the first point on the line.

**`Column1`** (input_control)  point.x(-array) `→`  (real / integer)

Column coordinate of the first point on the line.

**`Row2`** (input_control)  point.y(-array) `→`  (real / integer)

Row coordinate of the second point on the line.

**`Column2`** (input_control)  point.x(-array) `→`  (real / integer)

Column coordinate of the second point on the line.

**`RowProj`** (output_control)  real(-array) `→`  (real)

Row coordinate of the projected point.

**`ColProj`** (output_control)  real(-array) `→`  (real)

Column coordinate of the projected point

## Example (HDevelop)

```
dev_open_window (0, 0, 512, 512, 'black', WindowHandle)
Row1 := 300
Column1 := 200
Row2 := 140
Column2 := 400
Rows := 300
Columns := 170
dev_set_color ('cadet blue')
gen_contour_polygon_xld (Contour, [Row1,Row2], [Column1,Column2])
Offset := 0
for Rows := 40 to 280 by 40
  dev_set_color ('red')
  gen_cross_contour_xld (Point,Rows+Offset, Columns, 6, 0)
  projection_pl (Rows+Offset, Columns, Row1, Column1, Row2, Column2, \
                 RowProj, ColProj)
  dev_set_color ('blue')
  gen_cross_contour_xld (RowP, RowProj, ColProj, 6, 0)
  Offset := Offset+30
endfor
```

## Result

`projection_pl` returns 2 (
H_MSG_TRUE)
.

## Module

Foundation
