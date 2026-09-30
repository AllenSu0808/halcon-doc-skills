# distance_cc_min (Operator)

## Name

`distance_cc_min` — Calculate the minimum distance between two contours.

## Signature

`distance_cc_min(Contour1, Contour2 : : Mode : DistanceMin)`

## Description

`distance_cc_min` calculates the minimum distance between
two contours *`Contour1`* and *`Contour2`*.
The minimum distance is returned in *`DistanceMin`*.

The parameter *`Mode`* sets the type of computing the distance.
*'point_to_point'* determines the distance between the closest
contour points, *'fast_point_to_segment'* calculates the
distance between the line segments adjacent to these points, and
*'point_to_segment'* determines the actual minimum
distance between the contour segments.

While *'point_to_point'* and *'fast_point_to_segment'*
are efficient algorithms with a complexity of n*log(n),
*'point_to_segment'* has quadratic complexity and thus
takes a longer time to execute, especially for contours with many line
segments.

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
'fast_point_to_segment', 'point_to_point', 'point_to_segment'

**`DistanceMin`** (output_control)  number(-array) `→`  (real)

Minimum distance between the two contours.

## Example (C)

```
gen_contour_polygon_rounded_xld(Cont1, [0,100,100,0,0], [0,0,100,100,0],
                                [50,50,50,50,50], 0.5);
gen_contour_polygon_rounded_xld(Cont2, [41,91,91,41,41], [41,41,91,91,41],
                                [25,25,25,25,25], 0.5);
distance_cc_min(Cont1, Cont2, "fast_point_to_segment", &distance_min);
```

## Result

`distance_cc_min` returns 2 (
H_MSG_TRUE)
.

## Alternatives

`distance_sc`,
`distance_pc`,
`distance_cc`,
`distance_contours_xld`

## See also

`distance_sr`,
`distance_pr`

## Module

Foundation
