# distance_ps (Operator)

## Name

`distance_ps` — Calculate the distances between a point and a line segment.

## Signature

`distance_ps( : : Row, Column, Row1, Column1, Row2, Column2 : DistanceMin, DistanceMax)`

## Description

The operator `distance_ps` calculates the minimum and
maximum distance between a point
(*`Row`*,*`Column`*) and a line segment which is represented
by the start point (*`Row1`*,*`Column1`*) and the
end point (*`Row2`*,*`Column2`*).
*`DistanceMax`* is the maximum distance between the point
and the end points of the line segment.
*`DistanceMin`* is identical to [`distance_pl`](distance_pl.md) in
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

**`Row`** (input_control)  point.y(-array) `→`  (real / integer)

Row coordinate of the first point.

**`Column`** (input_control)  point.x(-array) `→`  (real / integer)

Column coordinate of the first point.

**`Row1`** (input_control)  point.y(-array) `→`  (real / integer)

Row coordinate of the first point of the line segment.

**`Column1`** (input_control)  point.x(-array) `→`  (real / integer)

Column coordinate of the first point of the line segment.

**`Row2`** (input_control)  point.y(-array) `→`  (real / integer)

Row coordinate of the second point of the line segment.

**`Column2`** (input_control)  point.x(-array) `→`  (real / integer)

Column coordinate of the second point of the line segment.

**`DistanceMin`** (output_control)  real(-array) `→`  (real)

Minimum distance between the point and the
line segment.

**`DistanceMax`** (output_control)  real(-array) `→`  (real)

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

`distance_ps` returns 2 (
H_MSG_TRUE)
.

## Alternatives

`distance_pl`

## See also

`distance_pp`,
`distance_pr`

## Module

Foundation
