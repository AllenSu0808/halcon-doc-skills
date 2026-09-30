# distance_pr (Operator)

## Name

`distance_pr` — Calculate the distance between a point and a region.

## Signature

`def distance_pr(region: HObject, row: MaybeSequence[Union[float, int]], column: MaybeSequence[Union[float, int]]) -> Tuple[Sequence[float], Sequence[float]]`

`def distance_pr_s(region: HObject, row: MaybeSequence[Union[float, int]], column: MaybeSequence[Union[float, int]]) -> Tuple[float, float]`

## Description

The operator `distance_pr` calculates the distance
between a point and one region.
As input the coordinates of the points
(*`row`*,*`column`*) and a region are expected.
If a point is inside of the region, its minimum distance is zero.
The parameters
*`distance_min`* and *`distance_max`* return
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

**`region`** (input_object)  region(-array) `→` HObject

Input region.

**`row`** (input_control)  point.y(-array) `→` MaybeSequence[Union[float, int]]

Row coordinate of the point.

**`column`** (input_control)  point.x(-array) `→` MaybeSequence[Union[float, int]]

Column coordinate of the point.

**`distance_min`** (output_control)  real(-array) `→` Sequence[float]

Minimum distance between the point and the region.

**`distance_max`** (output_control)  real(-array) `→` Sequence[float]

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
