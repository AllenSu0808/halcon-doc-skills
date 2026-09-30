# get_points_ellipse (Operator)

## Name

`get_points_ellipse` — Calculate points on the perimeter of an ellipse.

## Signature

`def get_points_ellipse(angle: MaybeSequence[float], row: float, column: float, phi: float, radius_1: float, radius_2: float) -> Tuple[Sequence[float], Sequence[float]]`

`def get_points_ellipse_s(angle: MaybeSequence[float], row: float, column: float, phi: float, radius_1: float, radius_2: float) -> Tuple[float, float]`

## Description

`get_points_ellipse` returns the point
(*`row_point`*,*`col_point`*) on the specified ellipse
corresponding to the angle in *`angle`*.
With the parameter *`angle`* you are setting the eccentric anomaly,
which denotes the angle used for the parametric equation (see the
figure below) and refers to the main axis of the ellipse.
The ellipse itself is characterized by
the center (*`row`*, *`column`*), the orientation of the
main axis *`phi`* relative to the horizontal axis, the length of
the larger (*`radius_1`*) and the smaller half
axis (*`radius_2`*). The angles are measured counter clockwise in
radiant.

![figure](../assets/d20dc1241860050e.svg)

The point `P` with its coordinates *`row_point`* and
*`col_point`* belongs to the ellipse (orange).
It is determined over the angle
`a` and the lengths of the half axis `r1` (*`radius_1`*)
and `r2` (*`radius_2`*). For simplicity of the visualization
and angle *`phi`*=*0* was used.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`angle`** (input_control)  angle.rad(-array) `→` MaybeSequence[float]

Angle corresponding to the resulting point [rad].

Default:
0

Restriction:
`Angle >= 0 && Angle <= 6.283185307`

**`row`** (input_control)  ellipse.center.y `→` float

Row coordinate of the center of the ellipse.

**`column`** (input_control)  ellipse.center.x `→` float

Column coordinate of the center of the ellipse.

**`phi`** (input_control)  ellipse.angle.rad `→` float

Orientation of the main axis [rad].

Restriction:
`Phi >= 0 && Phi <= 6.283185307`

**`radius_1`** (input_control)  ellipse.radius1 `→` float

Length of the larger half axis.

Restriction:
`Radius1 > 0`

**`radius_2`** (input_control)  ellipse.radius2 `→` float

Length of the smaller half axis.

Restriction:
`Radius2 >= 0`

**`row_point`** (output_control)  point.y(-array) `→` Sequence[float]

Row coordinate of the point on the ellipse.

**`col_point`** (output_control)  point.x(-array) `→` Sequence[float]

Column coordinates of the point on the ellipse.

## Example (HDevelop)

```
draw_ellipse(WindowHandle,Row,Column,Phi,Radius1,Radius2)
get_points_ellipse([0,3.14],Row,Column,Phi,Radius1,Radius2,\
                   RowPoint,ColPoint)
```

## Result

`get_points_ellipse` returns 2 (
H_MSG_TRUE)
if all parameter
values are correct. If necessary, an exception is raised.

## Possible Predecessors

`fit_ellipse_contour_xld`,
`draw_ellipse`,
`gen_ellipse_contour_xld`

## See also

`gen_ellipse_contour_xld`

## Module

Foundation
