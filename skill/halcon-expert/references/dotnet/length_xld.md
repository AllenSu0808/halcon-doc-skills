# LengthXld (Operator)

## Name

`LengthXld` — Length of contours or polygons.

## Signature

`static void HOperatorSet.LengthXld(HObject XLD, out HTuple length)`

`HTuple HXLD.LengthXld()`

## Description

`LengthXld` calculates the length of the contours or
polygons *`XLD`*. The length is calculated as the sum of the
Euclidean distances of successive points on the contour or polygon.
If more than one contour or polygon is passed, the results are stored
in tuples in the same order as the respective contours or polygons in
*`XLD`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`XLD`** (input_object)  xld(-array) `→` [HXLD](HXLD.md)

Contours or polygons to be examined.

**`length`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Length of the contour or polygon.

Assertion:
`Length >= 0`

## Complexity

Let n be the number of points of the contour or polygon.
Then the run time is O(n).

## Result

`LengthXld` returns 2 (
H_MSG_TRUE)
if the input is not empty. If
the input is empty the behavior can be set via
`set_system(::'no_object_result',<Result>:)`. If
necessary, an exception is raised.

## Possible Predecessors

`GenContoursSkeletonXld`,
`SmoothContoursXld`,
`GenPolygonsXld`

## See also

`AreaCenterXld`,
`MomentsAnyXld`,
`MomentsXld`,
`Contlength`

## Module

Foundation
