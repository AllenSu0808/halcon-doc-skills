# get_points_ellipse (Operator)

## Name

`get_points_ellipse` — Calculate points on the perimeter of an ellipse.

## Signature

`get_points_ellipse( : : Angle, Row, Column, Phi, Radius1, Radius2 : RowPoint, ColPoint)`

## Description

`get_points_ellipse` returns the point
(*`RowPoint`*,*`ColPoint`*) on the specified ellipse
corresponding to the angle in *`Angle`*.
With the parameter *`Angle`* you are setting the eccentric anomaly,
which denotes the angle used for the parametric equation (see the
figure below) and refers to the main axis of the ellipse.
The ellipse itself is characterized by
the center (*`Row`*, *`Column`*), the orientation of the
main axis *`Phi`* relative to the horizontal axis, the length of
the larger (*`Radius1`*) and the smaller half
axis (*`Radius2`*). The angles are measured counter clockwise in
radiant.

![figure](../assets/d20dc1241860050e.svg)

The point `P` with its coordinates *`RowPoint`* and
*`ColPoint`* belongs to the ellipse (orange).
It is determined over the angle
`a` and the lengths of the half axis `r1` (*`Radius1`*)
and `r2` (*`Radius2`*). For simplicity of the visualization
and angle *`Phi`*=*0* was used.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Angle`** (input_control)  angle.rad(-array) `→`  (real)

Angle corresponding to the resulting point [rad].

Default:
0

Restriction:
`Angle >= 0 && Angle <= 6.283185307`

**`Row`** (input_control)  ellipse.center.y `→`  (real)

Row coordinate of the center of the ellipse.

**`Column`** (input_control)  ellipse.center.x `→`  (real)

Column coordinate of the center of the ellipse.

**`Phi`** (input_control)  ellipse.angle.rad `→`  (real)

Orientation of the main axis [rad].

Restriction:
`Phi >= 0 && Phi <= 6.283185307`

**`Radius1`** (input_control)  ellipse.radius1 `→`  (real)

Length of the larger half axis.

Restriction:
`Radius1 > 0`

**`Radius2`** (input_control)  ellipse.radius2 `→`  (real)

Length of the smaller half axis.

Restriction:
`Radius2 >= 0`

**`RowPoint`** (output_control)  point.y(-array) `→`  (real)

Row coordinate of the point on the ellipse.

**`ColPoint`** (output_control)  point.x(-array) `→`  (real)

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
