# intersection_line_circle (Operator)

## Name

`intersection_line_circle` — Calculate the intersection points of a line and a circle or circular arc

## Signature

`def intersection_line_circle(line_row_1: Union[float, int], line_column_1: Union[float, int], line_row_2: Union[float, int], line_column_2: Union[float, int], circle_row: Union[float, int], circle_column: Union[float, int], circle_radius: Union[float, int], circle_start_phi: float, circle_end_phi: float, circle_point_order: str) -> Tuple[Sequence[float], Sequence[float]]`

`def intersection_line_circle_s(line_row_1: Union[float, int], line_column_1: Union[float, int], line_row_2: Union[float, int], line_column_2: Union[float, int], circle_row: Union[float, int], circle_column: Union[float, int], circle_radius: Union[float, int], circle_start_phi: float, circle_end_phi: float, circle_point_order: str) -> Tuple[float, float]`

## Description

`intersection_line_circle` calculates the intersection points of
a line and a circle or circular arc. The line is defined by the points
(*`line_row_1`*,*`line_column_1`*) and
(*`line_row_2`*,*`line_column_2`*). The circle is defined
by its center (*`circle_row`*,*`circle_column`*) and its radius
*`circle_radius`*. In addition to that, a circular arc is characterized
by the angle of the start point *`circle_start_phi`*, the angle of the
end point *`circle_end_phi`*, and the point order
*`circle_point_order`* along the boundary.
If *`circle_point_order`* is set to *"positive"*, the circular arc
is defined counterclockwise.
If *`circle_point_order`* is set to *"negative"*, the circular arc
is defined clockwise.
The intersection points, if any, are returned in
(*`row`*,*`column`*).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`line_row_1`** (input_control)  point.y `→` Union[float, int]

Row coordinate of the first point of the line.

**`line_column_1`** (input_control)  point.x `→` Union[float, int]

Column coordinate of the first point of the line.

**`line_row_2`** (input_control)  point.y `→` Union[float, int]

Row coordinate of the second point of the line.

**`line_column_2`** (input_control)  point.x `→` Union[float, int]

Column coordinate of the second point of the line.

**`circle_row`** (input_control)  circle.center.y `→` Union[float, int]

Row coordinate of the center of the circle or
circular arc.

**`circle_column`** (input_control)  circle.center.x `→` Union[float, int]

Column coordinate of the center of the circle or
circular arc.

**`circle_radius`** (input_control)  circle.radius `→` Union[float, int]

Radius of the circle or circular arc.

**`circle_start_phi`** (input_control)  angle.rad `→` float

Angle of the start point of the circle or
circular arc [rad].

Default:
0.0

**`circle_end_phi`** (input_control)  angle.rad `→` float

Angle of the end point of the circle or
circular arc [rad].

Default:
6.28318

**`circle_point_order`** (input_control)  string `→` str

Point order along the circle or circular arc.

Default:
"positive"

List of values:
"negative", "positive"

**`row`** (output_control)  point.y(-array) `→` Sequence[float]

Row coordinates of the intersection points.

**`column`** (output_control)  point.x(-array) `→` Sequence[float]

Column coordinates of the intersection points.

## Result

If the parameters are valid, the operator `intersection_line_circle`
returns the value 2 (
H_MSG_TRUE)
.

## See also

`intersection_segment_circle`,
`intersection_circle_contour_xld`

## Module

Foundation
