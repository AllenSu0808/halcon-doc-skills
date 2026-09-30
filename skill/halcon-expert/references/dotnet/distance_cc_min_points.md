# DistanceCcMinPoints (Operator)

## Name

`DistanceCcMinPoints` — Calculate the minimum distance between two contours and the points used for
the calculation.

## Signature

`static void HOperatorSet.DistanceCcMinPoints(HObject contour1, HObject contour2, HTuple mode, out HTuple distanceMin, out HTuple row1, out HTuple column1, out HTuple row2, out HTuple column2)`

`HTuple HXLDCont.DistanceCcMinPoints(HXLDCont contour2, HTuple mode, out HTuple row1, out HTuple column1, out HTuple row2, out HTuple column2)`

`double HXLDCont.DistanceCcMinPoints(HXLDCont contour2, string mode, out double row1, out double column1, out double row2, out double column2)`

## Description

`DistanceCcMinPoints` calculates the minimum distance between
*`contour1`* and *`contour2`*.
The minimum distance is returned in *`distanceMin`*.
In comparison to [`DistanceCcMin`](distance_cc_min.md), this operator also returns the
points on the contours that provide the minimum distance.
The point on *`contour1`* is returned in *`row1`* and
*`column1`*; the point on *`contour2`* is returned in
*`row2`* and *`column2`*.

The parameter *`mode`* sets the type of computing the distance.
*"fast_point_to_segment"* calculates the distance between the line
segments adjacent to the closest contour points, and
*"point_to_segment"* determines the actual minimum distance between
the contour segments.

While *"fast_point_to_segment"* is an efficient algorithm
with a complexity of n*log(n), *"point_to_segment"* has
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

**`contour1`** (input_object)  xld_cont(-array) `→` [HXLDCont](HXLDCont.md)

First input contour.

**`contour2`** (input_object)  xld_cont(-array) `→` [HXLDCont](HXLDCont.md)

Second input contour.

**`mode`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Distance calculation mode.

Default:
"fast_point_to_segment"

List of values:
"fast_point_to_segment", "point_to_segment"

**`distanceMin`** (output_control)  number(-array) `→` [HTuple](HTuple.md) (*double*)

Minimum distance between the two contours.

**`row1`** (output_control)  point.y(-array) `→` [HTuple](HTuple.md) (*double*)

Row coordinate of the point on *`contour1`*.

**`column1`** (output_control)  point.x(-array) `→` [HTuple](HTuple.md) (*double*)

Column coordinate of the point on *`contour1`*.

**`row2`** (output_control)  point.y(-array) `→` [HTuple](HTuple.md) (*double*)

Row coordinate of the point on *`contour2`*.

**`column2`** (output_control)  point.x(-array) `→` [HTuple](HTuple.md) (*double*)

Column coordinate of the point on *`contour2`*.

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

`DistanceCcMinPoints` returns 2 (
H_MSG_TRUE)
.

## Alternatives

`DistanceSc`,
`DistancePc`,
`DistanceCc`,
`DistanceContoursXld`,
`DistanceCcMin`

## See also

`DistanceSr`,
`DistancePr`

## Module

Foundation
