# distance_cc_min_points (Operator)

## Name

`distance_cc_min_points` — Calculate the minimum distance between two contours and the points used for
the calculation.

## Signature

`distance_cc_min_points(Contour1, Contour2 : : Mode : DistanceMin, Row1, Column1, Row2, Column2)`

## Description

`distance_cc_min_points` calculates the minimum distance between
*`Contour1`* and *`Contour2`*.
The minimum distance is returned in *`DistanceMin`*.
In comparison to [`distance_cc_min`](distance_cc_min.md), this operator also returns the
points on the contours that provide the minimum distance.
The point on *`Contour1`* is returned in *`Row1`* and
*`Column1`*; the point on *`Contour2`* is returned in
*`Row2`* and *`Column2`*.

The parameter *`Mode`* sets the type of computing the distance.
*'fast_point_to_segment'* calculates the distance between the line
segments adjacent to the closest contour points, and
*'point_to_segment'* determines the actual minimum distance between
the contour segments.

While *'fast_point_to_segment'* is an efficient algorithm
with a complexity of n*log(n), *'point_to_segment'* has
quadratic complexity and thus takes a longer time to execute,
especially for contours with many line segments.

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

**`Contour1`** (input_object)  xld_cont(-array) `→` object

First input contour.

**`Contour2`** (input_object)  xld_cont(-array) `→` object

Second input contour.

**`Mode`** (input_control)  string(-array) `→`  (string)

Distance calculation mode.

Default:
'fast_point_to_segment'

List of values:
'fast_point_to_segment', 'point_to_segment'

**`DistanceMin`** (output_control)  number(-array) `→`  (real)

Minimum distance between the two contours.

**`Row1`** (output_control)  point.y(-array) `→`  (real)

Row coordinate of the point on *`Contour1`*.

**`Column1`** (output_control)  point.x(-array) `→`  (real)

Column coordinate of the point on *`Contour1`*.

**`Row2`** (output_control)  point.y(-array) `→`  (real)

Row coordinate of the point on *`Contour2`*.

**`Column2`** (output_control)  point.x(-array) `→`  (real)

Column coordinate of the point on *`Contour2`*.

## Example (C)

```
gen_contour_polygon_rounded_xld(Cont1, [0,100,100,0,0], [0,0,100,100,0],
                                [50,50,50,50,50], 0.5);
gen_contour_polygon_rounded_xld(Cont2, [41,91,91,41,41], [41,41,91,91,41],
                                [25,25,25,25,25], 0.5);
distance_cc_min_points(Cont1, Cont2, "fast_point_to_segment", &distance_min,
                       &Row1, &Column1, &Row2, &Column2);
```

## Result

`distance_cc_min_points` returns 2 (
H_MSG_TRUE)
.

## Alternatives

`distance_sc`,
`distance_pc`,
`distance_cc`,
`distance_contours_xld`,
`distance_cc_min`

## See also

`distance_sr`,
`distance_pr`

## Module

Foundation
