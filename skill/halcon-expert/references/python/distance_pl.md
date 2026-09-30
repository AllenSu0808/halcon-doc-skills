# distance_pl (Operator)

## Name

`distance_pl` — Calculate the distance between one point and one line.

## Signature

`def distance_pl(row: MaybeSequence[Union[float, int]], column: MaybeSequence[Union[float, int]], row_1: MaybeSequence[Union[float, int]], column_1: MaybeSequence[Union[float, int]], row_2: MaybeSequence[Union[float, int]], column_2: MaybeSequence[Union[float, int]]) -> Sequence[float]`

`def distance_pl_s(row: MaybeSequence[Union[float, int]], column: MaybeSequence[Union[float, int]], row_1: MaybeSequence[Union[float, int]], column_1: MaybeSequence[Union[float, int]], row_2: MaybeSequence[Union[float, int]], column_2: MaybeSequence[Union[float, int]]) -> float`

## Description

The operator `distance_pl` calculates the orthogonal distance
between points (*`row`*,*`column`*) and lines,
given by two arbitrary points on the line.
The result is passed in *`distance`*.

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

Row coordinate of the point.

**`column`** (input_control)  point.x(-array) `→` MaybeSequence[Union[float, int]]

Column of the point.

**`row_1`** (input_control)  point.y(-array) `→` MaybeSequence[Union[float, int]]

Row coordinate of the first point of the line.

**`column_1`** (input_control)  point.x(-array) `→` MaybeSequence[Union[float, int]]

Column coordinate of the first point of the line.

**`row_2`** (input_control)  point.y(-array) `→` MaybeSequence[Union[float, int]]

Row coordinate of the second point of the line.

**`column_2`** (input_control)  point.x(-array) `→` MaybeSequence[Union[float, int]]

Column coordinate of the second point of the line.

**`distance`** (output_control)  real(-array) `→` Sequence[float]

Distance between the points.

## Result

`distance_pl` returns 2 (
H_MSG_TRUE)
.

## Alternatives

`distance_ps`

## See also

`distance_pp`,
`distance_pr`

## Module

Foundation
