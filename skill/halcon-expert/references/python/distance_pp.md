# distance_pp (Operator)

## Name

`distance_pp` — Calculate the distance between two points.

## Signature

`def distance_pp(row_1: MaybeSequence[Union[float, int]], column_1: MaybeSequence[Union[float, int]], row_2: MaybeSequence[Union[float, int]], column_2: MaybeSequence[Union[float, int]]) -> Sequence[float]`

`def distance_pp_s(row_1: MaybeSequence[Union[float, int]], column_1: MaybeSequence[Union[float, int]], row_2: MaybeSequence[Union[float, int]], column_2: MaybeSequence[Union[float, int]]) -> float`

## Description

The operator `distance_pp` calculates the distance between pairs
of points
according to the following formula:
$$\text{Distance} = \sqrt{(\text{Row1} - \text{Row2})^{2} + (\text{Column1} - \text{Column2})^{2}}$$ ![figure](../assets/b6cc3cc605b60bc7.svg)
The result is returned in *`distance`*.

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

**`row_1`** (input_control)  point.y(-array) `→` MaybeSequence[Union[float, int]]

Row coordinate of the first point.

**`column_1`** (input_control)  point.x(-array) `→` MaybeSequence[Union[float, int]]

Column coordinate of the first point.

**`row_2`** (input_control)  point.y(-array) `→` MaybeSequence[Union[float, int]]

Row coordinate of the second point.

**`column_2`** (input_control)  point.x(-array) `→` MaybeSequence[Union[float, int]]

Column coordinate of the second point.

**`distance`** (output_control)  real(-array) `→` Sequence[float]

Distance between the points.

## Result

`distance_pp` returns 2 (
H_MSG_TRUE)
.

## Alternatives

`distance_ps`

## See also

`distance_pl`,
`distance_pr`

## Module

Foundation
