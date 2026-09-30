# DistancePl (Operator)

## Name

`DistancePl` — Calculate the distance between one point and one line.

## Signature

`static void HOperatorSet.DistancePl(HTuple row, HTuple column, HTuple row1, HTuple column1, HTuple row2, HTuple column2, out HTuple distance)`

`static HTuple HMisc.DistancePl(HTuple row, HTuple column, HTuple row1, HTuple column1, HTuple row2, HTuple column2)`

`static double HMisc.DistancePl(double row, double column, double row1, double column1, double row2, double column2)`

## Description

The operator `DistancePl` calculates the orthogonal distance
between points (*`row`*,*`column`*) and lines,
given by two arbitrary points on the line.
The result is passed in *`distance`*.

### Parameter Broadcasting

This operator supports parameter broadcasting.
This means that each parameter can be given as a tuple of length
*1* or *N*.
Parameters with tuple length *1* will be repeated internally
such that the number of computed distances is always *N*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`row`** (input_control)  point.y(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Row coordinate of the point.

**`column`** (input_control)  point.x(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Column of the point.

**`row1`** (input_control)  point.y(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Row coordinate of the first point of the line.

**`column1`** (input_control)  point.x(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Column coordinate of the first point of the line.

**`row2`** (input_control)  point.y(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Row coordinate of the second point of the line.

**`column2`** (input_control)  point.x(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Column coordinate of the second point of the line.

**`distance`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Distance between the points.

## Example (HDevelop)

```
dev_open_window (0, 0, 512, 512, 'black', WindowHandle)
draw_point (WindowHandle, Row, Column)
gen_cross_contour_xld (Cross, Row, Column, 15, 0)
draw_line (WindowHandle, Row1, Column1, Row2, Column2)
gen_contour_polygon_xld (Contour, [Row1,Row2], [Column1,Column2])
distance_pl (Row, Column, Row1, Column1, Row2, Column2, Distance)
```

## Result

`DistancePl` returns 2 (
H_MSG_TRUE)
.

## Alternatives

`DistancePs`

## See also

`DistancePp`,
`DistancePr`

## Module

Foundation
