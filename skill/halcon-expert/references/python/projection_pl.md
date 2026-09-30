# projection_pl (Operator)

## Name

`projection_pl` — Calculate the projection of a point onto a line.

## Signature

`def projection_pl(row: MaybeSequence[Union[float, int]], column: MaybeSequence[Union[float, int]], row_1: MaybeSequence[Union[float, int]], column_1: MaybeSequence[Union[float, int]], row_2: MaybeSequence[Union[float, int]], column_2: MaybeSequence[Union[float, int]]) -> Tuple[Sequence[float], Sequence[float]]`

`def projection_pl_s(row: MaybeSequence[Union[float, int]], column: MaybeSequence[Union[float, int]], row_1: MaybeSequence[Union[float, int]], column_1: MaybeSequence[Union[float, int]], row_2: MaybeSequence[Union[float, int]], column_2: MaybeSequence[Union[float, int]]) -> Tuple[float, float]`

## Description

The operator `projection_pl` calculates the projection of a
point (*`row`*,*`column`*) onto a line which is
represented by the two points (*`row_1`*,*`column_1`*) and
(*`row_2`*,*`column_2`*). The coordinates of the projected
point are returned in *`row_proj`* and *`col_proj`*.

### Parameter Broadcasting

This operator supports parameter broadcasting.
This means that each parameter can be given as a tuple of length
*1* or *N*.
Parameters with tuple length *1* will be repeated internally
such that the number of projections is always *N*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`row`** (input_control)  point.y(-array) `→` MaybeSequence[Union[float, int]]

Row coordinate of the point.

**`column`** (input_control)  point.x(-array) `→` MaybeSequence[Union[float, int]]

Column coordinate of the point.

**`row_1`** (input_control)  point.y(-array) `→` MaybeSequence[Union[float, int]]

Row coordinate of the first point on the line.

**`column_1`** (input_control)  point.x(-array) `→` MaybeSequence[Union[float, int]]

Column coordinate of the first point on the line.

**`row_2`** (input_control)  point.y(-array) `→` MaybeSequence[Union[float, int]]

Row coordinate of the second point on the line.

**`column_2`** (input_control)  point.x(-array) `→` MaybeSequence[Union[float, int]]

Column coordinate of the second point on the line.

**`row_proj`** (output_control)  real(-array) `→` Sequence[float]

Row coordinate of the projected point.

**`col_proj`** (output_control)  real(-array) `→` Sequence[float]

Column coordinate of the projected point

## Result

`projection_pl` returns 2 (
H_MSG_TRUE)
.

## Module

Foundation
