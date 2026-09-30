# distance_pc (Operator)

## Name

`distance_pc` — Calculate the distance between a point and one contour.

## Signature

`def distance_pc(contour: HObject, row: MaybeSequence[Union[float, int]], column: MaybeSequence[Union[float, int]]) -> Tuple[Sequence[float], Sequence[float]]`

`def distance_pc_s(contour: HObject, row: MaybeSequence[Union[float, int]], column: MaybeSequence[Union[float, int]]) -> Tuple[float, float]`

## Description

The operator `distance_pc` calculates the distance between one or
several points and a single contour. As input the coordinates of the points
(*`row`*,*`column`*) and the contour (*`contour`*) are
expected. The parameters *`distance_min`* and *`distance_max`*
return the result of the calculation. Note that the result corresponds to the
distances between the points and the segments of the contour and not the
distances between the points and the base points of the contour (see also
[`distance_contours_xld`](distance_contours_xld.md)).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`contour`** (input_object)  xld_cont `→` HObject

Input contour.

**`row`** (input_control)  point.y(-array) `→` MaybeSequence[Union[float, int]]

Row coordinate of the point.

**`column`** (input_control)  point.x(-array) `→` MaybeSequence[Union[float, int]]

Column coordinate of the point.

**`distance_min`** (output_control)  real(-array) `→` Sequence[float]

Minimum distance between the point and the contour.

**`distance_max`** (output_control)  real(-array) `→` Sequence[float]

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
