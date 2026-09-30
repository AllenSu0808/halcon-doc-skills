# intersection_circles (Operator)

## Name

`intersection_circles` — Calculate the intersection points of two circles or circular arcs

## Signature

`intersection_circles( : : Circle1Row, Circle1Column, Circle1Radius, Circle1StartPhi, Circle1EndPhi, Circle1PointOrder, Circle2Row, Circle2Column, Circle2Radius, Circle2StartPhi, Circle2EndPhi, Circle2PointOrder : Row, Column, IsOverlapping)`

## Description

`intersection_circles` calculates the intersection points of two
circles or circular arcs. The points, if any, are returned in
(*`Row`*,*`Column`*). The circles are defined by their center
(*`Circle1Row`*,*`Circle1Column`*), and
(*`Circle2Row`*,*`Circle2Column`*) respectively, and their radii
*`Circle1Radius`*, and *`Circle2Radius`* respectively.
In addition to that, a circular arc is characterized by the angle of the
start point (*`Circle1StartPhi`*,*`Circle2StartPhi`*),
the angle of the end point (*`Circle1EndPhi`*,*`Circle2EndPhi`*),
and the point order (*`Circle1PointOrder`*,*`Circle2PointOrder`*)
along the boundary.
If *`Circle1PointOrder`* is set to *'positive'*, the circular arc
is defined counterclockwise.
If *`Circle1PointOrder`* is set to *'negative'*, the circular arc
is defined clockwise.
The same applies for *`Circle2PointOrder`*.
If both circles or circular arcs have a part in common
*`IsOverlapping`* returns the value 1, otherwise 0 is returned.
In this case the endpoints of the mutual arc are returned in
(*`Row`*,*`Column`*).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Circle1Row`** (input_control)  circle.center.y `→`  (real / integer)

Row coordinate of the center of the first circle or
circular arc.

**`Circle1Column`** (input_control)  circle.center.x `→`  (real / integer)

Column coordinate of the center of the first circle or
circular arc.

**`Circle1Radius`** (input_control)  circle.radius `→`  (real / integer)

Radius of the first circle or circular arc.

**`Circle1StartPhi`** (input_control)  angle.rad `→`  (real)

Angle of the start point of the first circle or
circular arc [rad].

Default:
0.0

**`Circle1EndPhi`** (input_control)  angle.rad `→`  (real)

Angle of the end point of the first circle or
circular arc [rad].

Default:
6.28318

**`Circle1PointOrder`** (input_control)  string `→`  (string)

Point order along the first circle or circular arc.

Default:
'positive'

List of values:
'negative', 'positive'

**`Circle2Row`** (input_control)  circle.center.y `→`  (real / integer)

Row coordinate of the center of the second circle or
circular arc.

**`Circle2Column`** (input_control)  circle.center.x `→`  (real / integer)

Column coordinate of the center of the second circle or
circular arc.

**`Circle2Radius`** (input_control)  circle.radius `→`  (real / integer)

Radius of the second circle or circular arc.

**`Circle2StartPhi`** (input_control)  angle.rad `→`  (real)

Angle of the start point of the second circle or
circular arc [rad].

Default:
0.0

**`Circle2EndPhi`** (input_control)  angle.rad `→`  (real)

Angle of the end point of the second circle or
circular arc [rad].

Default:
6.28318

**`Circle2PointOrder`** (input_control)  string `→`  (string)

Point order along the second circle or circular arc.

Default:
'positive'

List of values:
'negative', 'positive'

**`Row`** (output_control)  point.y(-array) `→`  (real)

Row coordinates of the intersection points.

**`Column`** (output_control)  point.x(-array) `→`  (real)

Column coordinates of the intersection points.

**`IsOverlapping`** (output_control)  integer `→`  (integer)

Do both circles or circular arcs have a part in common?

## Result

If the parameters are valid, the operator `intersection_circles`
returns the value 2 (
H_MSG_TRUE)
.

## Module

Foundation
