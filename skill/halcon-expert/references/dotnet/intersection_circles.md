# IntersectionCircles (Operator)

## Name

`IntersectionCircles` — Calculate the intersection points of two circles or circular arcs

## Signature

`static void HOperatorSet.IntersectionCircles(HTuple circle1Row, HTuple circle1Column, HTuple circle1Radius, HTuple circle1StartPhi, HTuple circle1EndPhi, HTuple circle1PointOrder, HTuple circle2Row, HTuple circle2Column, HTuple circle2Radius, HTuple circle2StartPhi, HTuple circle2EndPhi, HTuple circle2PointOrder, out HTuple row, out HTuple column, out HTuple isOverlapping)`

## Description

`IntersectionCircles` calculates the intersection points of two
circles or circular arcs. The points, if any, are returned in
(*`row`*,*`column`*). The circles are defined by their center
(*`circle1Row`*,*`circle1Column`*), and
(*`circle2Row`*,*`circle2Column`*) respectively, and their radii
*`circle1Radius`*, and *`circle2Radius`* respectively.
In addition to that, a circular arc is characterized by the angle of the
start point (*`circle1StartPhi`*,*`circle2StartPhi`*),
the angle of the end point (*`circle1EndPhi`*,*`circle2EndPhi`*),
and the point order (*`circle1PointOrder`*,*`circle2PointOrder`*)
along the boundary.
If *`circle1PointOrder`* is set to *"positive"*, the circular arc
is defined counterclockwise.
If *`circle1PointOrder`* is set to *"negative"*, the circular arc
is defined clockwise.
The same applies for *`circle2PointOrder`*.
If both circles or circular arcs have a part in common
*`isOverlapping`* returns the value 1, otherwise 0 is returned.
In this case the endpoints of the mutual arc are returned in
(*`row`*,*`column`*).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`circle1Row`** (input_control)  circle.center.y `→` [HTuple](HTuple.md) (*double* / int / long)

Row coordinate of the center of the first circle or
circular arc.

**`circle1Column`** (input_control)  circle.center.x `→` [HTuple](HTuple.md) (*double* / int / long)

Column coordinate of the center of the first circle or
circular arc.

**`circle1Radius`** (input_control)  circle.radius `→` [HTuple](HTuple.md) (*double* / int / long)

Radius of the first circle or circular arc.

**`circle1StartPhi`** (input_control)  angle.rad `→` [HTuple](HTuple.md) (*double*)

Angle of the start point of the first circle or
circular arc [rad].

Default:
0.0

**`circle1EndPhi`** (input_control)  angle.rad `→` [HTuple](HTuple.md) (*double*)

Angle of the end point of the first circle or
circular arc [rad].

Default:
6.28318

**`circle1PointOrder`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Point order along the first circle or circular arc.

Default:
"positive"

List of values:
"negative", "positive"

**`circle2Row`** (input_control)  circle.center.y `→` [HTuple](HTuple.md) (*double* / int / long)

Row coordinate of the center of the second circle or
circular arc.

**`circle2Column`** (input_control)  circle.center.x `→` [HTuple](HTuple.md) (*double* / int / long)

Column coordinate of the center of the second circle or
circular arc.

**`circle2Radius`** (input_control)  circle.radius `→` [HTuple](HTuple.md) (*double* / int / long)

Radius of the second circle or circular arc.

**`circle2StartPhi`** (input_control)  angle.rad `→` [HTuple](HTuple.md) (*double*)

Angle of the start point of the second circle or
circular arc [rad].

Default:
0.0

**`circle2EndPhi`** (input_control)  angle.rad `→` [HTuple](HTuple.md) (*double*)

Angle of the end point of the second circle or
circular arc [rad].

Default:
6.28318

**`circle2PointOrder`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Point order along the second circle or circular arc.

Default:
"positive"

List of values:
"negative", "positive"

**`row`** (output_control)  point.y(-array) `→` [HTuple](HTuple.md) (*double*)

Row coordinates of the intersection points.

**`column`** (output_control)  point.x(-array) `→` [HTuple](HTuple.md) (*double*)

Column coordinates of the intersection points.

**`isOverlapping`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Do both circles or circular arcs have a part in common?

## Result

If the parameters are valid, the operator `IntersectionCircles`
returns the value 2 (
H_MSG_TRUE)
.

## Module

Foundation
