# IntersectionCircleContourXld (Operator)

## Name

`IntersectionCircleContourXld` — Calculate the intersection points of a circle or circular arc and an
XLD contour

## Signature

`static void HOperatorSet.IntersectionCircleContourXld(HObject contour, HTuple circleRow, HTuple circleColumn, HTuple circleRadius, HTuple circleStartPhi, HTuple circleEndPhi, HTuple circlePointOrder, out HTuple row, out HTuple column)`

## Description

`IntersectionCircleContourXld` calculates the intersection points
of a circle or circular arc and the XLD *`contour`*.
The circle is defined by its center
(*`circleRow`*,*`circleColumn`*) and its radius
*`circleRadius`*. In addition to that, a circular arc is characterized
by the angle of the start point *`circleStartPhi`*, the angle of the
end point *`circleEndPhi`*, and the point order
*`circlePointOrder`* along the boundary.
If *`circlePointOrder`* is set to *"positive"*, the circular arc
is defined counterclockwise.
If *`circlePointOrder`* is set to *"negative"*, the circular arc
is defined clockwise.
The intersection points, if any, are returned in
(*`row`*,*`column`*).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`contour`** (input_object)  xld_cont `→` [HXLDCont](HXLDCont.md)

XLD contour.

**`circleRow`** (input_control)  circle.center.y `→` [HTuple](HTuple.md) (*double* / int / long)

Row coordinate of the center of the circle or
circular arc.

**`circleColumn`** (input_control)  circle.center.x `→` [HTuple](HTuple.md) (*double* / int / long)

Column coordinate of the center of the circle or
circular arc.

**`circleRadius`** (input_control)  circle.radius `→` [HTuple](HTuple.md) (*double* / int / long)

Radius of the circle or circular arc.

**`circleStartPhi`** (input_control)  angle.rad `→` [HTuple](HTuple.md) (*double*)

Angle of the start point of the circle or
circular arc [rad].

Default:
0.0

**`circleEndPhi`** (input_control)  angle.rad `→` [HTuple](HTuple.md) (*double*)

Angle of the end point of the circle or
circular arc [rad].

Default:
6.28318

**`circlePointOrder`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Point order along the circle or circular arc.

Default:
"positive"

List of values:
"negative", "positive"

**`row`** (output_control)  point.y(-array) `→` [HTuple](HTuple.md) (*double*)

Row coordinates of the intersection points.

**`column`** (output_control)  point.x(-array) `→` [HTuple](HTuple.md) (*double*)

Column coordinates of the intersection points.

## Result

If the parameters are valid, the operator
`IntersectionCircleContourXld` returns the value 2 (
H_MSG_TRUE)
.

## Alternatives

`IntersectionSegmentCircle`

## See also

`IntersectionLineCircle`

## Module

Foundation
