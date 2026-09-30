# distance_pr (Operator)

## Name

`distance_pr` — Calculate the distance between a point and a region.

## Signature

`distance_pr(Region : : Row, Column : DistanceMin, DistanceMax)`

## Description

The operator `distance_pr` calculates the distance
between a point and one region.
As input the coordinates of the points
(*`Row`*,*`Column`*) and a region are expected.
If a point is inside of the region, its minimum distance is zero.
The parameters
*`DistanceMin`* and *`DistanceMax`* return
the result of the calculation.

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

**`Region`** (input_object)  region(-array) `→` object

Input region.

**`Row`** (input_control)  point.y(-array) `→`  (real / integer)

Row coordinate of the point.

**`Column`** (input_control)  point.x(-array) `→`  (real / integer)

Column coordinate of the point.

**`DistanceMin`** (output_control)  real(-array) `→`  (real)

Minimum distance between the point and the region.

**`DistanceMax`** (output_control)  real(-array) `→`  (real)

Maximum distance between the point and the region.

## Example (HDevelop)

```
gen_circle (Circle, 200, 200, 100.5)
draw_point (WindowHandle, Row, Column)
gen_cross_contour_xld (Cross, Row, Column, 15, 0)
distance_pr (Circle, Row, Column, DistanceMin, DistanceMax)
```

## Result

`distance_pr` returns 2 (
H_MSG_TRUE)
.

## Alternatives

`distance_pc`,
`distance_lr`,
`distance_sr`,
`diameter_region`

## See also

`hamming_distance`,
`select_region_point`,
`test_region_point`,
`smallest_rectangle2`

## Module

Foundation
