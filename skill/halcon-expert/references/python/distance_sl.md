# distance_sl (Operator)

## Name

`distance_sl` — Calculate the distances between a line segment and a line.

## Signature

`def distance_sl(row_a1: MaybeSequence[Union[float, int]], column_a1: MaybeSequence[Union[float, int]], row_a2: MaybeSequence[Union[float, int]], column_a2: MaybeSequence[Union[float, int]], row_b1: MaybeSequence[Union[float, int]], column_b1: MaybeSequence[Union[float, int]], row_b2: MaybeSequence[Union[float, int]], column_b2: MaybeSequence[Union[float, int]]) -> Tuple[Sequence[float], Sequence[float]]`

`def distance_sl_s(row_a1: MaybeSequence[Union[float, int]], column_a1: MaybeSequence[Union[float, int]], row_a2: MaybeSequence[Union[float, int]], column_a2: MaybeSequence[Union[float, int]], row_b1: MaybeSequence[Union[float, int]], column_b1: MaybeSequence[Union[float, int]], row_b2: MaybeSequence[Union[float, int]], column_b2: MaybeSequence[Union[float, int]]) -> Tuple[float, float]`

## Description

The operator `distance_sl` calculates the minimum and maximum
orthogonal distance between a line segment and a line.
As input the coordinates of two points on the line segment
(*`row_a1`*,*`column_a1`*,*`row_a2`*,*`column_a2`*)
and on the line
(*`row_b1`*,*`column_b1`*,*`row_b2`*,*`column_b2`*)
are expected. The parameters *`distance_min`* and
*`distance_max`* return the result of the calculation. If the line
segments are intersecting, *`distance_min`* returns zero.

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

**`row_a1`** (input_control)  point.y(-array) `→` MaybeSequence[Union[float, int]]

Row coordinate of the first point of the line segment.

**`column_a1`** (input_control)  point.x(-array) `→` MaybeSequence[Union[float, int]]

Column coordinate of the first point of the line segment.

**`row_a2`** (input_control)  point.y(-array) `→` MaybeSequence[Union[float, int]]

Row coordinate of the second point of the line segment.

**`column_a2`** (input_control)  point.x(-array) `→` MaybeSequence[Union[float, int]]

Column coordinate of the second point of the line segment.

**`row_b1`** (input_control)  point.y(-array) `→` MaybeSequence[Union[float, int]]

Row coordinate of the first point of the line.

**`column_b1`** (input_control)  point.x(-array) `→` MaybeSequence[Union[float, int]]

Column coordinate of the first point of the line.

**`row_b2`** (input_control)  point.y(-array) `→` MaybeSequence[Union[float, int]]

Row coordinate of the second point of the line.

**`column_b2`** (input_control)  point.x(-array) `→` MaybeSequence[Union[float, int]]

Column coordinate of the second point of the line.

**`distance_min`** (output_control)  real(-array) `→` Sequence[float]

Minimum distance between the line segment and
the line.

**`distance_max`** (output_control)  real(-array) `→` Sequence[float]

Maximum distance between the line segment and
the line.

## Result

`distance_sl` returns 2 (
H_MSG_TRUE)
.

## Alternatives

`distance_pl`

## See also

`distance_ps`,
`distance_pp`

## Module

Foundation
