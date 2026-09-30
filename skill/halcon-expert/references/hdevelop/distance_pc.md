# distance_pc (Operator)

## Name

`distance_pc` — Calculate the distance between a point and one contour.

## Signature

`distance_pc(Contour : : Row, Column : DistanceMin, DistanceMax)`

## Description

The operator `distance_pc` calculates the distance between one or
several points and a single contour. As input the coordinates of the points
(*`Row`*,*`Column`*) and the contour (*`Contour`*) are
expected. The parameters *`DistanceMin`* and *`DistanceMax`*
return the result of the calculation. Note that the result corresponds to the
distances between the points and the segments of the contour and not the
distances between the points and the base points of the contour (see also
[`distance_contours_xld`](distance_contours_xld.md)).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`Contour`** (input_object)  xld_cont `→` object

Input contour.

**`Row`** (input_control)  point.y(-array) `→`  (real / integer)

Row coordinate of the point.

**`Column`** (input_control)  point.x(-array) `→`  (real / integer)

Column coordinate of the point.

**`DistanceMin`** (output_control)  real(-array) `→`  (real)

Minimum distance between the point and the contour.

**`DistanceMax`** (output_control)  real(-array) `→`  (real)

Maximum distance between the point and the contour.

## Result

`distance_pc` returns 2 (
H_MSG_TRUE)
.

## Alternatives

`distance_lc`,
`distance_sc`,
`distance_cc`,
`distance_cc_min`

## See also

`distance_pr`,
`distance_lr`,
`distance_sr`,
`hamming_distance`,
`select_xld_point`,
`test_xld_point`

## Module

Foundation
