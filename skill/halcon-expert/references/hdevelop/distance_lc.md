# distance_lc (Operator)

## Name

`distance_lc` — Calculate the distance between a line and one contour.

## Signature

`distance_lc(Contour : : Row1, Column1, Row2, Column2 : DistanceMin, DistanceMax)`

## Description

The operator `distance_lc` calculates the orthogonal
distance between a line and the segments of a contour.
As input the coordinates of two points on a line
(*`Row1`*,*`Column1`*,
*`Row2`*,*`Column2`*) and a contour (*`Contour`*)
are expected.
The parameters *`DistanceMin`* and *`DistanceMax`*
return the result of the calculation.

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

Row coordinate of the first point of the line.

**`Column1`** (input_control)  point.x(-array) `→`  (real / integer)

Column coordinate of the first point of the line.

**`Row2`** (input_control)  point.y(-array) `→`  (real / integer)

Row coordinate of the second point of the line.

**`Column2`** (input_control)  point.x(-array) `→`  (real / integer)

Column coordinate of the second point of the line.

**`DistanceMin`** (output_control)  real(-array) `→`  (real)

Minimum distance between the line and the contour.

**`DistanceMax`** (output_control)  real(-array) `→`  (real)

Maximum distance between the line and the contour.

## Result

`distance_lc` returns 2 (
H_MSG_TRUE)
.

## Alternatives

`distance_pc`,
`distance_sc`,
`distance_cc`,
`distance_cc_min`

## See also

`distance_lr`,
`distance_pr`,
`distance_sr`

## Module

Foundation
