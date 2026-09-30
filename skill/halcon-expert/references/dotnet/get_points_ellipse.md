# GetPointsEllipse (Operator)

## Name

`GetPointsEllipse` — Calculate points on the perimeter of an ellipse.

## Signature

`static void HOperatorSet.GetPointsEllipse(HTuple angle, HTuple row, HTuple column, HTuple phi, HTuple radius1, HTuple radius2, out HTuple rowPoint, out HTuple colPoint)`

`static void HMisc.GetPointsEllipse(HTuple angle, double row, double column, double phi, double radius1, double radius2, out HTuple rowPoint, out HTuple colPoint)`

`static void HMisc.GetPointsEllipse(double angle, double row, double column, double phi, double radius1, double radius2, out double rowPoint, out double colPoint)`

## Description

`GetPointsEllipse` returns the point
(*`rowPoint`*,*`colPoint`*) on the specified ellipse
corresponding to the angle in *`angle`*.
With the parameter *`angle`* you are setting the eccentric anomaly,
which denotes the angle used for the parametric equation (see the
figure below) and refers to the main axis of the ellipse.
The ellipse itself is characterized by
the center (*`row`*, *`column`*), the orientation of the
main axis *`phi`* relative to the horizontal axis, the length of
the larger (*`radius1`*) and the smaller half
axis (*`radius2`*). The angles are measured counter clockwise in
radiant.

![figure](../assets/d20dc1241860050e.svg)

The point `P` with its coordinates *`rowPoint`* and
*`colPoint`* belongs to the ellipse (orange).
It is determined over the angle
`a` and the lengths of the half axis `r1` (*`radius1`*)
and `r2` (*`radius2`*). For simplicity of the visualization
and angle *`phi`*=*0* was used.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`angle`** (input_control)  angle.rad(-array) `→` [HTuple](HTuple.md) (*double*)

Angle corresponding to the resulting point [rad].

Default:
0

Restriction:
`Angle >= 0 && Angle <= 6.283185307`

**`row`** (input_control)  ellipse.center.y `→` [HTuple](HTuple.md) (*double*)

Row coordinate of the center of the ellipse.

**`column`** (input_control)  ellipse.center.x `→` [HTuple](HTuple.md) (*double*)

Column coordinate of the center of the ellipse.

**`phi`** (input_control)  ellipse.angle.rad `→` [HTuple](HTuple.md) (*double*)

Orientation of the main axis [rad].

Restriction:
`Phi >= 0 && Phi <= 6.283185307`

**`radius1`** (input_control)  ellipse.radius1 `→` [HTuple](HTuple.md) (*double*)

Length of the larger half axis.

Restriction:
`Radius1 > 0`

**`radius2`** (input_control)  ellipse.radius2 `→` [HTuple](HTuple.md) (*double*)

Length of the smaller half axis.

Restriction:
`Radius2 >= 0`

**`rowPoint`** (output_control)  point.y(-array) `→` [HTuple](HTuple.md) (*double*)

Row coordinate of the point on the ellipse.

**`colPoint`** (output_control)  point.x(-array) `→` [HTuple](HTuple.md) (*double*)

Column coordinates of the point on the ellipse.

## Example (HDevelop)

```
draw_ellipse(WindowHandle,Row,Column,Phi,Radius1,Radius2)
get_points_ellipse([0,3.14],Row,Column,Phi,Radius1,Radius2,\
                   RowPoint,ColPoint)
```

## Result

`GetPointsEllipse` returns 2 (
H_MSG_TRUE)
if all parameter
values are correct. If necessary, an exception is raised.

## Possible Predecessors

`FitEllipseContourXld`,
`DrawEllipse`,
`GenEllipseContourXld`

## See also

`GenEllipseContourXld`

## Module

Foundation
