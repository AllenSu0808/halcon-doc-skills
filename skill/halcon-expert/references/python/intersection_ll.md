# intersection_ll (Operator)

## Name

`intersection_ll` — Calculate the intersection point of two lines.

## Warning

**`intersection_ll` is obsolete and is only provided for
reasons of backward compatibility. New applications should use the
operator [`intersection_lines`](intersection_lines.md) of the chapter Tools / Geometry instead.**

## Signature

`def intersection_ll(row_a1: MaybeSequence[Union[float, int]], column_a1: MaybeSequence[Union[float, int]], row_a2: MaybeSequence[Union[float, int]], column_a2: MaybeSequence[Union[float, int]], row_b1: MaybeSequence[Union[float, int]], column_b1: MaybeSequence[Union[float, int]], row_b2: MaybeSequence[Union[float, int]], column_b2: MaybeSequence[Union[float, int]]) -> Tuple[Sequence[float], Sequence[float], Sequence[int]]`

`def intersection_ll_s(row_a1: MaybeSequence[Union[float, int]], column_a1: MaybeSequence[Union[float, int]], row_a2: MaybeSequence[Union[float, int]], column_a2: MaybeSequence[Union[float, int]], row_b1: MaybeSequence[Union[float, int]], column_b1: MaybeSequence[Union[float, int]], row_b2: MaybeSequence[Union[float, int]], column_b2: MaybeSequence[Union[float, int]]) -> Tuple[float, float, int]`

## Description

The operator `intersection_ll` calculates the intersection point
of two lines. As input the two points on each line are expected
(*`row_a1`*,*`column_a1`*,
*`row_a2`*,*`column_a2`*) and
(*`row_b1`*,*`column_b1`*,
*`row_b2`*,*`column_b2`*).
The parameters *`row`* and *`column`* return the
result of the calculation.
If the lines are parallel, the values of *`row`* and *`column`*
are undefined and *`is_parallel`* is 1. Otherwise, *`is_parallel`*
is 0.

## Attention

If the lines are parallel the values of *`row`* and
*`column`* are undefined.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`row_a1`** (input_control)  point.y(-array) `→` MaybeSequence[Union[float, int]]

Row coordinate of the first point of the first line.

**`column_a1`** (input_control)  point.x(-array) `→` MaybeSequence[Union[float, int]]

Column coordinate of the first point of the
first line.

**`row_a2`** (input_control)  point.y(-array) `→` MaybeSequence[Union[float, int]]

Row coordinate of the second point of the first line.

**`column_a2`** (input_control)  point.x(-array) `→` MaybeSequence[Union[float, int]]

Column coordinate of the second point of the
first line.

**`row_b1`** (input_control)  point.y(-array) `→` MaybeSequence[Union[float, int]]

Row coordinate of the first point of the second line.

**`column_b1`** (input_control)  point.x(-array) `→` MaybeSequence[Union[float, int]]

Column coordinate of the first point of the
second line.

**`row_b2`** (input_control)  point.y(-array) `→` MaybeSequence[Union[float, int]]

Row coordinate of the second point of the second line.

**`column_b2`** (input_control)  point.x(-array) `→` MaybeSequence[Union[float, int]]

Column coordinate of the second point of the
second line.

**`row`** (output_control)  point.y(-array) `→` Sequence[float]

Row coordinate of the intersection point.

**`column`** (output_control)  point.x(-array) `→` Sequence[float]

Column coordinate of the intersection point.

**`is_parallel`** (output_control)  number(-array) `→` Sequence[int]

Are the two lines parallel?

## Result

`intersection_ll` returns 2 (
H_MSG_TRUE)
.

## Module

Foundation
