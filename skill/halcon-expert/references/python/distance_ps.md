# distance_ps (Operator)

## Name

`distance_ps` — Calculate the distances between a point and a line segment.

## Signature

`def distance_ps(row: MaybeSequence[Union[float, int]], column: MaybeSequence[Union[float, int]], row_1: MaybeSequence[Union[float, int]], column_1: MaybeSequence[Union[float, int]], row_2: MaybeSequence[Union[float, int]], column_2: MaybeSequence[Union[float, int]]) -> Tuple[Sequence[float], Sequence[float]]`

`def distance_ps_s(row: MaybeSequence[Union[float, int]], column: MaybeSequence[Union[float, int]], row_1: MaybeSequence[Union[float, int]], column_1: MaybeSequence[Union[float, int]], row_2: MaybeSequence[Union[float, int]], column_2: MaybeSequence[Union[float, int]]) -> Tuple[float, float]`

## Description

The operator `distance_ps` calculates the minimum and
maximum distance between a point
(*`row`*,*`column`*) and a line segment which is represented
by the start point (*`row_1`*,*`column_1`*) and the
end point (*`row_2`*,*`column_2`*).
*`distance_max`* is the maximum distance between the point
and the end points of the line segment.
*`distance_min`* is identical to [`distance_pl`](distance_pl.md) in
the case that the point is “between” the two endpoints.
Otherwise, the minimum distance to one of the end points is used.

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

**`row`** (input_control)  point.y(-array) `→` MaybeSequence[Union[float, int]]

Row coordinate of the first point.

**`column`** (input_control)  point.x(-array) `→` MaybeSequence[Union[float, int]]

Column coordinate of the first point.

**`row_1`** (input_control)  point.y(-array) `→` MaybeSequence[Union[float, int]]

Row coordinate of the first point of the line segment.

**`column_1`** (input_control)  point.x(-array) `→` MaybeSequence[Union[float, int]]

Column coordinate of the first point of the line segment.

**`row_2`** (input_control)  point.y(-array) `→` MaybeSequence[Union[float, int]]

Row coordinate of the second point of the line segment.

**`column_2`** (input_control)  point.x(-array) `→` MaybeSequence[Union[float, int]]

Column coordinate of the second point of the line segment.

**`distance_min`** (output_control)  real(-array) `→` Sequence[float]

Minimum distance between the point and the
line segment.

**`distance_max`** (output_control)  real(-array) `→` Sequence[float]

Maximum distance between the point and the
line segment.

## Result

`distance_ps` returns 2 (
H_MSG_TRUE)
.

## Alternatives

`distance_pl`

## See also

`distance_pp`,
`distance_pr`

## Module

Foundation
