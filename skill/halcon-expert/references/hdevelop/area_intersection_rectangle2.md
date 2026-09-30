# area_intersection_rectangle2 (Operator)

## Name

`area_intersection_rectangle2` — Calculate the intersection area of oriented rectangles.

## Signature

`area_intersection_rectangle2( : : Rect1Row, Rect1Column, Rect1Phi, Rect1Length1, Rect1Length2, Rect2Row, Rect2Column, Rect2Phi, Rect2Length1, Rect2Length2 : AreaIntersection)`

## Description

`area_intersection_rectangle2` calculates the intersection area of two
oriented rectangles (i.e., of type rectangle2), which are defined by their
parameters (center (*`Rect1Row`*, *`Rect1Column`*), orientation
*`Rect1Phi`*, and the half edge lengths *`Rect1Length1`*
and *`Rect1Length2`*) and
(center (*`Rect2Row`*, *`Rect2Column`*), orientation
*`Rect2Phi`*, and the half edge lengths *`Rect2Length1`* and
*`Rect2Length2`*), respectively.
The intersection area is returned in *`AreaIntersection`*.

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

**`Rect1Row`** (input_control)  rectangle2.center.y(-array) `→`  (real / integer)

Center row coordinate of the first rectangle.

**`Rect1Column`** (input_control)  rectangle2.center.x(-array) `→`  (real / integer)

Center column coordinate of the first rectangle.

**`Rect1Phi`** (input_control)  rectangle2.angle.rad(-array) `→`  (real / integer)

Angle between the positive horizontal axis and the first
edge of the first rectangle (in radians).

**`Rect1Length1`** (input_control)  rectangle2.hwidth(-array) `→`  (real / integer)

Half length of the first edge of the first rectangle.

**`Rect1Length2`** (input_control)  rectangle2.hheight(-array) `→`  (real / integer)

Half length of the second edge of the first rectangle.

**`Rect2Row`** (input_control)  rectangle2.center.y(-array) `→`  (real / integer)

Center row coordinate of the second rectangle.

**`Rect2Column`** (input_control)  rectangle2.center.x(-array) `→`  (real / integer)

Center column coordinate of the second rectangle.

**`Rect2Phi`** (input_control)  rectangle2.angle.rad(-array) `→`  (real / integer)

Angle between the positive horizontal axis and the first
edge of the second rectangle (in radians).

**`Rect2Length1`** (input_control)  rectangle2.hwidth(-array) `→`  (real / integer)

Half length of the first edge of the second rectangle.

**`Rect2Length2`** (input_control)  rectangle2.hheight(-array) `→`  (real / integer)

Half length of the second edge of the second rectangle.

**`AreaIntersection`** (output_control)  real(-array) `→`  (real)

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
