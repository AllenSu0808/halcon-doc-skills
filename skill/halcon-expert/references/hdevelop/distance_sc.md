# distance_sc (Operator)

## Name

`distance_sc` — Calculate the distance between a line segment and one contour.

## Signature

`distance_sc(Contour : : Row1, Column1, Row2, Column2 : DistanceMin, DistanceMax)`

## Description

The operator `distance_sc` calculates the distance between
a line segment and the line segments of a contour.
*`Row1`*, *`Column1`*, *`Row2`*, *`Column2`*
are the start and end coordinates of a line segment,
*`Contour`* represents the input contour.
The parameters *`DistanceMin`* and *`DistanceMax`*
contain the resulting distances.

### Parameter Broadcasting

This operator supports parameter broadcasting.
This means that each parameter can be given as a tuple of length
*1* or *N*.
Parameters with tuple length *1* will be repeated internally
such that the number of distances is always *N*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Contour`** (input_object)  xld_cont(-array) `→` object

Input contour.

**`Row1`** (input_control)  point.y(-array) `→`  (real / integer)

Row coordinate of the first point of the line segment.

**`Column1`** (input_control)  point.x(-array) `→`  (real / integer)

Column coordinate of the first point of the line segment.

**`Row2`** (input_control)  point.y(-array) `→`  (real / integer)

Row coordinate of the second point of the line segment.

**`Column2`** (input_control)  point.x(-array) `→`  (real / integer)

Column coordinate of the second point of the line segment.

**`DistanceMin`** (output_control)  real(-array) `→`  (real)

Minimum distance between the line segment and
the contour.

**`DistanceMax`** (output_control)  real(-array) `→`  (real)

Maximum distance between the line segment and
the contour.

## Result

[`distance_sr`](distance_sr.md) returns 2 (
H_MSG_TRUE)
.

## Alternatives

`distance_lc`,
`distance_pc`,
`distance_cc`,
`distance_cc_min`

## See also

`distance_sr`,
`distance_lr`,
`distance_pr`,
`select_xld_point`,
`test_xld_point`

## Module

Foundation
