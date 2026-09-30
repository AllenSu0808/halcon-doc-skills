# distance_lc (Operator)

## Name

`distance_lc` — Calculate the distance between a line and one contour.

## Signature

`def distance_lc(contour: HObject, row_1: MaybeSequence[Union[float, int]], column_1: MaybeSequence[Union[float, int]], row_2: MaybeSequence[Union[float, int]], column_2: MaybeSequence[Union[float, int]]) -> Tuple[Sequence[float], Sequence[float]]`

`def distance_lc_s(contour: HObject, row_1: MaybeSequence[Union[float, int]], column_1: MaybeSequence[Union[float, int]], row_2: MaybeSequence[Union[float, int]], column_2: MaybeSequence[Union[float, int]]) -> Tuple[float, float]`

## Description

The operator `distance_lc` calculates the orthogonal
distance between a line and the segments of a contour.
As input the coordinates of two points on a line
(*`row_1`*,*`column_1`*,
*`row_2`*,*`column_2`*) and a contour (*`contour`*)
are expected.
The parameters *`distance_min`* and *`distance_max`*
return the result of the calculation.

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

**`contour`** (input_object)  xld_cont(-array) `→` HObject

Input contour.

**`row_1`** (input_control)  point.y(-array) `→` MaybeSequence[Union[float, int]]

Row coordinate of the first point of the line.

**`column_1`** (input_control)  point.x(-array) `→` MaybeSequence[Union[float, int]]

Column coordinate of the first point of the line.

**`row_2`** (input_control)  point.y(-array) `→` MaybeSequence[Union[float, int]]

Row coordinate of the second point of the line.

**`column_2`** (input_control)  point.x(-array) `→` MaybeSequence[Union[float, int]]

Column coordinate of the second point of the line.

**`distance_min`** (output_control)  real(-array) `→` Sequence[float]

Minimum distance between the line and the contour.

**`distance_max`** (output_control)  real(-array) `→` Sequence[float]

Maximum distance between the line and the contour.

## Result

`distance_lc` returns 2 (
H_MSG_TRUE)
.

## Alternatives

`distance_pc`,
`distance_sc`,
`distance_cc`,
`distance_cc_min`

## See also

`distance_lr`,
`distance_pr`,
`distance_sr`

## Module

Foundation
