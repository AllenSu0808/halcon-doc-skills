# AreaIntersectionRectangle2 (Operator)

## Name

`AreaIntersectionRectangle2` — Calculate the intersection area of oriented rectangles.

## Signature

`static void HOperatorSet.AreaIntersectionRectangle2(HTuple rect1Row, HTuple rect1Column, HTuple rect1Phi, HTuple rect1Length1, HTuple rect1Length2, HTuple rect2Row, HTuple rect2Column, HTuple rect2Phi, HTuple rect2Length1, HTuple rect2Length2, out HTuple areaIntersection)`

## Description

`AreaIntersectionRectangle2` calculates the intersection area of two
oriented rectangles (i.e., of type rectangle2), which are defined by their
parameters (center (*`rect1Row`*, *`rect1Column`*), orientation
*`rect1Phi`*, and the half edge lengths *`rect1Length1`*
and *`rect1Length2`*) and
(center (*`rect2Row`*, *`rect2Column`*), orientation
*`rect2Phi`*, and the half edge lengths *`rect2Length1`* and
*`rect2Length2`*), respectively.
The intersection area is returned in *`areaIntersection`*.

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

**`rect1Row`** (input_control)  rectangle2.center.y(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Center row coordinate of the first rectangle.

**`rect1Column`** (input_control)  rectangle2.center.x(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Center column coordinate of the first rectangle.

**`rect1Phi`** (input_control)  rectangle2.angle.rad(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Angle between the positive horizontal axis and the first
edge of the first rectangle (in radians).

**`rect1Length1`** (input_control)  rectangle2.hwidth(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Half length of the first edge of the first rectangle.

**`rect1Length2`** (input_control)  rectangle2.hheight(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Half length of the second edge of the first rectangle.

**`rect2Row`** (input_control)  rectangle2.center.y(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Center row coordinate of the second rectangle.

**`rect2Column`** (input_control)  rectangle2.center.x(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Center column coordinate of the second rectangle.

**`rect2Phi`** (input_control)  rectangle2.angle.rad(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Angle between the positive horizontal axis and the first
edge of the second rectangle (in radians).

**`rect2Length1`** (input_control)  rectangle2.hwidth(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Half length of the first edge of the second rectangle.

**`rect2Length2`** (input_control)  rectangle2.hheight(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Half length of the second edge of the second rectangle.

**`areaIntersection`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Intersection area of the first rectangle with the second
rectangle.

## Result

If the parameters are valid, the operator
`AreaIntersectionRectangle2` returns the value 2 (
H_MSG_TRUE)
.

## See also

`GenRectangle2`,
`IntersectionSegments`,
`IntersectionSegmentLine`,
`IntersectionSegmentContourXld`,
`IntersectionLineContourXld`,
`IntersectionContoursXld`

## Module

Foundation
