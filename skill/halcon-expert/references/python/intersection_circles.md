# intersection_circles (Operator)

## Name

`intersection_circles` — Calculate the intersection points of two circles or circular arcs

## Signature

`def intersection_circles(circle_1row: Union[float, int], circle_1column: Union[float, int], circle_1radius: Union[float, int], circle_1start_phi: float, circle_1end_phi: float, circle_1point_order: str, circle_2row: Union[float, int], circle_2column: Union[float, int], circle_2radius: Union[float, int], circle_2start_phi: float, circle_2end_phi: float, circle_2point_order: str) -> Tuple[Sequence[float], Sequence[float], int]`

`def intersection_circles_s(circle_1row: Union[float, int], circle_1column: Union[float, int], circle_1radius: Union[float, int], circle_1start_phi: float, circle_1end_phi: float, circle_1point_order: str, circle_2row: Union[float, int], circle_2column: Union[float, int], circle_2radius: Union[float, int], circle_2start_phi: float, circle_2end_phi: float, circle_2point_order: str) -> Tuple[float, float, int]`

## Description

`intersection_circles` calculates the intersection points of two
circles or circular arcs. The points, if any, are returned in
(*`row`*,*`column`*). The circles are defined by their center
(*`circle_1row`*,*`circle_1column`*), and
(*`circle_2row`*,*`circle_2column`*) respectively, and their radii
*`circle_1radius`*, and *`circle_2radius`* respectively.
In addition to that, a circular arc is characterized by the angle of the
start point (*`circle_1start_phi`*,*`circle_2start_phi`*),
the angle of the end point (*`circle_1end_phi`*,*`circle_2end_phi`*),
and the point order (*`circle_1point_order`*,*`circle_2point_order`*)
along the boundary.
If *`circle_1point_order`* is set to *"positive"*, the circular arc
is defined counterclockwise.
If *`circle_1point_order`* is set to *"negative"*, the circular arc
is defined clockwise.
The same applies for *`circle_2point_order`*.
If both circles or circular arcs have a part in common
*`is_overlapping`* returns the value 1, otherwise 0 is returned.
In this case the endpoints of the mutual arc are returned in
(*`row`*,*`column`*).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`circle_1row`** (input_control)  circle.center.y `→` Union[float, int]

Row coordinate of the center of the first circle or
circular arc.

**`circle_1column`** (input_control)  circle.center.x `→` Union[float, int]

Column coordinate of the center of the first circle or
circular arc.

**`circle_1radius`** (input_control)  circle.radius `→` Union[float, int]

Radius of the first circle or circular arc.

**`circle_1start_phi`** (input_control)  angle.rad `→` float

Angle of the start point of the first circle or
circular arc [rad].

Default:
0.0

**`circle_1end_phi`** (input_control)  angle.rad `→` float

Angle of the end point of the first circle or
circular arc [rad].

Default:
6.28318

**`circle_1point_order`** (input_control)  string `→` str

Point order along the first circle or circular arc.

Default:
"positive"

List of values:
"negative", "positive"

**`circle_2row`** (input_control)  circle.center.y `→` Union[float, int]

Row coordinate of the center of the second circle or
circular arc.

**`circle_2column`** (input_control)  circle.center.x `→` Union[float, int]

Column coordinate of the center of the second circle or
circular arc.

**`circle_2radius`** (input_control)  circle.radius `→` Union[float, int]

Radius of the second circle or circular arc.

**`circle_2start_phi`** (input_control)  angle.rad `→` float

Angle of the start point of the second circle or
circular arc [rad].

Default:
0.0

**`circle_2end_phi`** (input_control)  angle.rad `→` float

Angle of the end point of the second circle or
circular arc [rad].

Default:
6.28318

**`circle_2point_order`** (input_control)  string `→` str

Point order along the second circle or circular arc.

Default:
"positive"

List of values:
"negative", "positive"

**`row`** (output_control)  point.y(-array) `→` Sequence[float]

Row coordinates of the intersection points.

**`column`** (output_control)  point.x(-array) `→` Sequence[float]

Column coordinates of the intersection points.

**`is_overlapping`** (output_control)  integer `→` int

Do both circles or circular arcs have a part in common?

## Result

If the parameters are valid, the operator `intersection_circles`
returns the value 2 (
H_MSG_TRUE)
.

## Module

Foundation
