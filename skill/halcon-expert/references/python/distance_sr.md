# distance_sr (Operator)

## Name

`distance_sr` — Calculate the distance between a line segment and one region.

## Signature

`def distance_sr(region: HObject, row_1: MaybeSequence[Union[float, int]], column_1: MaybeSequence[Union[float, int]], row_2: MaybeSequence[Union[float, int]], column_2: MaybeSequence[Union[float, int]]) -> Tuple[Sequence[float], Sequence[float]]`

`def distance_sr_s(region: HObject, row_1: MaybeSequence[Union[float, int]], column_1: MaybeSequence[Union[float, int]], row_2: MaybeSequence[Union[float, int]], column_2: MaybeSequence[Union[float, int]]) -> Tuple[float, float]`

## Description

The operator `distance_sr` calculates the distance between
a line segment and a region.
*`row_1`*, *`column_1`*, *`row_2`*, *`column_2`*
are the start and end coordinates of a line segment.
The parameters *`distance_min`* and *`distance_max`*
contain the resulting distances.

### Parameter Broadcasting

This operator supports parameter broadcasting.
This means that each parameter can be given as a tuple of length
*1* or *N*.
Parameters with tuple length *1* will be repeated internally
such that the number of distances is always *N*.

## Attention

To enhance `distance_sr`,
holes are ignored.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`region`** (input_object)  region(-array) `→` HObject

Input region.

**`row_1`** (input_control)  point.y(-array) `→` MaybeSequence[Union[float, int]]

Row coordinate of the first point of the line segment.

**`column_1`** (input_control)  point.x(-array) `→` MaybeSequence[Union[float, int]]

Column coordinate of the first point of the line segment.

**`row_2`** (input_control)  point.y(-array) `→` MaybeSequence[Union[float, int]]

Row coordinate of the second point of the line segment.

**`column_2`** (input_control)  point.x(-array) `→` MaybeSequence[Union[float, int]]

Column coordinate of the second point of the line segment.

**`distance_min`** (output_control)  real(-array) `→` Sequence[float]

Minimum distance between the line segment and
the region.

**`distance_max`** (output_control)  real(-array) `→` Sequence[float]

Maximum distance between the line segment and
the region.

## Result

`distance_sr` returns 2 (
H_MSG_TRUE)
.

## Alternatives

`distance_sc`,
`distance_lr`,
`distance_pr`,
`diameter_region`

## See also

`hamming_distance`,
`select_region_point`,
`test_region_point`,
`smallest_rectangle2`

## Module

Foundation
