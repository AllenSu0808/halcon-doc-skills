# DistancePs (Operator)

## Name

`DistancePs` — Calculate the distances between a point and a line segment.

## Signature

`static void HOperatorSet.DistancePs(HTuple row, HTuple column, HTuple row1, HTuple column1, HTuple row2, HTuple column2, out HTuple distanceMin, out HTuple distanceMax)`

`static void HMisc.DistancePs(HTuple row, HTuple column, HTuple row1, HTuple column1, HTuple row2, HTuple column2, out HTuple distanceMin, out HTuple distanceMax)`

`static void HMisc.DistancePs(double row, double column, double row1, double column1, double row2, double column2, out double distanceMin, out double distanceMax)`

## Description

The operator `DistancePs` calculates the minimum and
maximum distance between a point
(*`row`*,*`column`*) and a line segment which is represented
by the start point (*`row1`*,*`column1`*) and the
end point (*`row2`*,*`column2`*).
*`distanceMax`* is the maximum distance between the point
and the end points of the line segment.
*`distanceMin`* is identical to [`DistancePl`](distance_pl.md) in
the case that the point is “between” the two endpoints.
Otherwise, the minimum distance to one of the end points is used.

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

Row coordinate of the first point.

**`column`** (input_control)  point.x(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Column coordinate of the first point.

**`row1`** (input_control)  point.y(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Row coordinate of the first point of the line segment.

**`column1`** (input_control)  point.x(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Column coordinate of the first point of the line segment.

**`row2`** (input_control)  point.y(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Row coordinate of the second point of the line segment.

**`column2`** (input_control)  point.x(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Column coordinate of the second point of the line segment.

**`distanceMin`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Minimum distance between the point and the
line segment.

**`distanceMax`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Maximum distance between the point and the
line segment.

## Example (HDevelop)

```
dev_open_window (0, 0, 512, 512, 'black', WindowHandle)
draw_point (WindowHandle, Row, Column)
gen_cross_contour_xld (Cross, Row, Column, 15, 0)
draw_line (WindowHandle, Row1, Column1, Row2, Column2)
gen_contour_polygon_xld (Contour, [Row1,Row2], [Column1,Column2])
distance_ps (Row, Column, Row1, Column1, Row2, Column2, \
             DistanceMin, DistanceMax)
```

## Result

`DistancePs` returns 2 (
H_MSG_TRUE)
.

## Alternatives

`DistancePl`

## See also

`DistancePp`,
`DistancePr`

## Module

Foundation
