# distance_cc (Operator)

## Name

`distance_cc` — Calculate the distance between two contours.

## Signature

`distance_cc(Contour1, Contour2 : : Mode : DistanceMin, DistanceMax)`

## Description

The operator `distance_cc` calculates the minimum and maximum
distance between the base points of two contours (*`Contour1`*
and *`Contour2`*).
The parameters *`DistanceMin`* and *`DistanceMax`*
contain the resulting distance.

The parameter *`Mode`* sets the type of computing the
distance: *'point_to_point'* only determines the minimum and
maximum distance between the base points of the contours. This results in
faster algorithm, but may lead to inaccurate minimum
distances. In contrast, *'point_to_segment'* determines the
actual minimum distance between the contour segments.

In both cases, the search algorithm has a quadratic complexity (n*n).
If only the minimum distance is required, the operator
[`distance_cc_min`](distance_cc_min.md) can be used alternatively since it offers
algorithms with a complexity of n*log(n).

### Parameter Broadcasting

This operator supports parameter broadcasting.
This means that each parameter can be given as a tuple of length
*1* or *N*.
Parameters with tuple length *1* will be repeated internally
such that the number of computed distances is always *N*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Contour1`** (input_object)  xld_cont(-array) `→` object

First input contour.

**`Contour2`** (input_object)  xld_cont(-array) `→` object

Second input contour.

**`Mode`** (input_control)  string(-array) `→`  (string)

Distance calculation mode.

Default:
'point_to_point'

List of values:
'point_to_point', 'point_to_segment'

**`DistanceMin`** (output_control)  real(-array) `→`  (real)

Minimum distance between both contours.

**`DistanceMax`** (output_control)  real(-array) `→`  (real)

Maximum distance between both contours.

## Example (C)

```
gen_contour_polygon_rounded_xld(Cont1, [0,100,100,0,0], [0,0,100,100,0],
                                [50,50,50,50,50], 0.5);
gen_contour_polygon_rounded_xld(Cont2, [41,91,91,41,41], [41,41,91,91,41],
                                [25,25,25,25,25], 0.5);
distance_cc(Cont1, Cont2, 'point_to_point', &distance_min, &distance_max);
```

## Result

`distance_cc` returns 2 (
H_MSG_TRUE)
.

## Alternatives

`distance_sc`,
`distance_pc`,
`distance_cc_min`,
`distance_contours_xld`

## See also

`distance_sr`,
`distance_pr`

## Module

Foundation
