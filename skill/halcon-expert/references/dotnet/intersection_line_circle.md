# IntersectionLineCircle (Operator)

## Name

`IntersectionLineCircle` — Calculate the intersection points of a line and a circle or circular arc

## Signature

`static void HOperatorSet.IntersectionLineCircle(HTuple lineRow1, HTuple lineColumn1, HTuple lineRow2, HTuple lineColumn2, HTuple circleRow, HTuple circleColumn, HTuple circleRadius, HTuple circleStartPhi, HTuple circleEndPhi, HTuple circlePointOrder, out HTuple row, out HTuple column)`

## Description

`IntersectionLineCircle` calculates the intersection points of
a line and a circle or circular arc. The line is defined by the points
(*`lineRow1`*,*`lineColumn1`*) and
(*`lineRow2`*,*`lineColumn2`*). The circle is defined
by its center (*`circleRow`*,*`circleColumn`*) and its radius
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

**`lineRow1`** (input_control)  point.y `→` [HTuple](HTuple.md) (*double* / int / long)

Row coordinate of the first point of the line.

**`lineColumn1`** (input_control)  point.x `→` [HTuple](HTuple.md) (*double* / int / long)

Column coordinate of the first point of the line.

**`lineRow2`** (input_control)  point.y `→` [HTuple](HTuple.md) (*double* / int / long)

Row coordinate of the second point of the line.

**`lineColumn2`** (input_control)  point.x `→` [HTuple](HTuple.md) (*double* / int / long)

Column coordinate of the second point of the line.

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

If the parameters are valid, the operator `IntersectionLineCircle`
returns the value 2 (
H_MSG_TRUE)
.

## See also

`IntersectionSegmentCircle`,
`IntersectionCircleContourXld`

## Module

Foundation
