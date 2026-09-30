# ProjectionPl (Operator)

## Name

`ProjectionPl` — Calculate the projection of a point onto a line.

## Signature

`static void HOperatorSet.ProjectionPl(HTuple row, HTuple column, HTuple row1, HTuple column1, HTuple row2, HTuple column2, out HTuple rowProj, out HTuple colProj)`

`static void HMisc.ProjectionPl(HTuple row, HTuple column, HTuple row1, HTuple column1, HTuple row2, HTuple column2, out HTuple rowProj, out HTuple colProj)`

`static void HMisc.ProjectionPl(double row, double column, double row1, double column1, double row2, double column2, out double rowProj, out double colProj)`

## Description

The operator `ProjectionPl` calculates the projection of a
point (*`row`*,*`column`*) onto a line which is
represented by the two points (*`row1`*,*`column1`*) and
(*`row2`*,*`column2`*). The coordinates of the projected
point are returned in *`rowProj`* and *`colProj`*.

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

**`row`** (input_control)  point.y(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Row coordinate of the point.

**`column`** (input_control)  point.x(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Column coordinate of the point.

**`row1`** (input_control)  point.y(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Row coordinate of the first point on the line.

**`column1`** (input_control)  point.x(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Column coordinate of the first point on the line.

**`row2`** (input_control)  point.y(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Row coordinate of the second point on the line.

**`column2`** (input_control)  point.x(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Column coordinate of the second point on the line.

**`rowProj`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Row coordinate of the projected point.

**`colProj`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

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

`ProjectionPl` returns 2 (
H_MSG_TRUE)
.

## Module

Foundation
