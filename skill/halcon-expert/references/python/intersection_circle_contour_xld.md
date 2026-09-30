# intersection_circle_contour_xld (Operator)

## Name

`intersection_circle_contour_xld` — Calculate the intersection points of a circle or circular arc and an
XLD contour

## Signature

`def intersection_circle_contour_xld(contour: HObject, circle_row: Union[float, int], circle_column: Union[float, int], circle_radius: Union[float, int], circle_start_phi: float, circle_end_phi: float, circle_point_order: str) -> Tuple[Sequence[float], Sequence[float]]`

`def intersection_circle_contour_xld_s(contour: HObject, circle_row: Union[float, int], circle_column: Union[float, int], circle_radius: Union[float, int], circle_start_phi: float, circle_end_phi: float, circle_point_order: str) -> Tuple[float, float]`

## Description

`intersection_circle_contour_xld` calculates the intersection points
of a circle or circular arc and the XLD *`contour`*.
The circle is defined by its center
(*`circle_row`*,*`circle_column`*) and its radius
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

**`contour`** (input_object)  xld_cont `→` HObject

XLD contour.

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

If the parameters are valid, the operator
`intersection_circle_contour_xld` returns the value 2 (
H_MSG_TRUE)
.

## Alternatives

`intersection_segment_circle`

## See also

`intersection_line_circle`

## Module

Foundation
