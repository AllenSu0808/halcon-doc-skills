# area_intersection_rectangle2 (Operator)

## Name

`area_intersection_rectangle2` — Calculate the intersection area of oriented rectangles.

## Signature

`def area_intersection_rectangle2(rect_1row: MaybeSequence[Union[float, int]], rect_1column: MaybeSequence[Union[float, int]], rect_1phi: MaybeSequence[Union[float, int]], rect_1length_1: MaybeSequence[Union[float, int]], rect_1length_2: MaybeSequence[Union[float, int]], rect_2row: MaybeSequence[Union[float, int]], rect_2column: MaybeSequence[Union[float, int]], rect_2phi: MaybeSequence[Union[float, int]], rect_2length_1: MaybeSequence[Union[float, int]], rect_2length_2: MaybeSequence[Union[float, int]]) -> Sequence[float]`

`def area_intersection_rectangle2_s(rect_1row: MaybeSequence[Union[float, int]], rect_1column: MaybeSequence[Union[float, int]], rect_1phi: MaybeSequence[Union[float, int]], rect_1length_1: MaybeSequence[Union[float, int]], rect_1length_2: MaybeSequence[Union[float, int]], rect_2row: MaybeSequence[Union[float, int]], rect_2column: MaybeSequence[Union[float, int]], rect_2phi: MaybeSequence[Union[float, int]], rect_2length_1: MaybeSequence[Union[float, int]], rect_2length_2: MaybeSequence[Union[float, int]]) -> float`

## Description

`area_intersection_rectangle2` calculates the intersection area of two
oriented rectangles (i.e., of type rectangle2), which are defined by their
parameters (center (*`rect_1row`*, *`rect_1column`*), orientation
*`rect_1phi`*, and the half edge lengths *`rect_1length_1`*
and *`rect_1length_2`*) and
(center (*`rect_2row`*, *`rect_2column`*), orientation
*`rect_2phi`*, and the half edge lengths *`rect_2length_1`* and
*`rect_2length_2`*), respectively.
The intersection area is returned in *`area_intersection`*.

### Parameter Broadcasting

This operator supports parameter broadcasting.
This means that each parameter can be given as a tuple of length
*1* or *N*.
Parameters with tuple length *1* will be repeated internally
such that the number of results is always *N*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`rect_1row`** (input_control)  rectangle2.center.y(-array) `→` MaybeSequence[Union[float, int]]

Center row coordinate of the first rectangle.

**`rect_1column`** (input_control)  rectangle2.center.x(-array) `→` MaybeSequence[Union[float, int]]

Center column coordinate of the first rectangle.

**`rect_1phi`** (input_control)  rectangle2.angle.rad(-array) `→` MaybeSequence[Union[float, int]]

Angle between the positive horizontal axis and the first
edge of the first rectangle (in radians).

**`rect_1length_1`** (input_control)  rectangle2.hwidth(-array) `→` MaybeSequence[Union[float, int]]

Half length of the first edge of the first rectangle.

**`rect_1length_2`** (input_control)  rectangle2.hheight(-array) `→` MaybeSequence[Union[float, int]]

Half length of the second edge of the first rectangle.

**`rect_2row`** (input_control)  rectangle2.center.y(-array) `→` MaybeSequence[Union[float, int]]

Center row coordinate of the second rectangle.

**`rect_2column`** (input_control)  rectangle2.center.x(-array) `→` MaybeSequence[Union[float, int]]

Center column coordinate of the second rectangle.

**`rect_2phi`** (input_control)  rectangle2.angle.rad(-array) `→` MaybeSequence[Union[float, int]]

Angle between the positive horizontal axis and the first
edge of the second rectangle (in radians).

**`rect_2length_1`** (input_control)  rectangle2.hwidth(-array) `→` MaybeSequence[Union[float, int]]

Half length of the first edge of the second rectangle.

**`rect_2length_2`** (input_control)  rectangle2.hheight(-array) `→` MaybeSequence[Union[float, int]]

Half length of the second edge of the second rectangle.

**`area_intersection`** (output_control)  real(-array) `→` Sequence[float]

Intersection area of the first rectangle with the second
rectangle.

## Result

If the parameters are valid, the operator
`area_intersection_rectangle2` returns the value 2 (
H_MSG_TRUE)
.

## See also

`gen_rectangle2`,
`intersection_segments`,
`intersection_segment_line`,
`intersection_segment_contour_xld`,
`intersection_line_contour_xld`,
`intersection_contours_xld`

## Module

Foundation
