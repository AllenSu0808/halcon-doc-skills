# length_xld (Operator)

## Name

`length_xld` — Length of contours or polygons.

## Signature

`def length_xld(xld: HObject) -> Sequence[float]`

`def length_xld_s(xld: HObject) -> float`

## Description

`length_xld` calculates the length of the contours or
polygons *`xld`*. The length is calculated as the sum of the
Euclidean distances of successive points on the contour or polygon.
If more than one contour or polygon is passed, the results are stored
in tuples in the same order as the respective contours or polygons in
*`xld`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`xld`** (input_object)  xld(-array) `→` HObject

Contours or polygons to be examined.

**`length`** (output_control)  real(-array) `→` Sequence[float]

Length of the contour or polygon.

Assertion:
`Length >= 0`

## Complexity

Let n be the number of points of the contour or polygon.
Then the run time is O(n).

## Result

`length_xld` returns 2 (
H_MSG_TRUE)
if the input is not empty. If
the input is empty the behavior can be set via
`set_system(::'no_object_result',<Result>:)`. If
necessary, an exception is raised.

## Possible Predecessors

`gen_contours_skeleton_xld`,
`smooth_contours_xld`,
`gen_polygons_xld`

## See also

`area_center_xld`,
`moments_any_xld`,
`moments_xld`,
`contlength`

## Module

Foundation
