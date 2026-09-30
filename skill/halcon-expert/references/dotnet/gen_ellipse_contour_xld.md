# GenEllipseContourXld (Operator)

## Name

`GenEllipseContourXld` — Create an XLD contour that corresponds to an elliptic arc.

## Signature

`static void HOperatorSet.GenEllipseContourXld(out HObject contEllipse, HTuple row, HTuple column, HTuple phi, HTuple radius1, HTuple radius2, HTuple startPhi, HTuple endPhi, HTuple pointOrder, HTuple resolution)`

`void HXLDCont.GenEllipseContourXld(HTuple row, HTuple column, HTuple phi, HTuple radius1, HTuple radius2, HTuple startPhi, HTuple endPhi, HTuple pointOrder, double resolution)`

`void HXLDCont.GenEllipseContourXld(double row, double column, double phi, double radius1, double radius2, double startPhi, double endPhi, string pointOrder, double resolution)`

## Description

`GenEllipseContourXld` creates one or more elliptic arcs or
closed ellipses. Ellipses are specified by their center
(*`row`*, *`column`*), the orientation of the main axis
*`phi`*, the length of the larger half axis
*`radius1`*, and the length of the smaller half
axis *`radius2`*.
In addition to that, elliptic arcs are characterized by the angle
of the start point *`startPhi`*, the angle of the end point
*`endPhi`*, and the point order *`pointOrder`* along the
boundary.
Both the angle of the start point and the angle of the end point are
measured from the positive main axis specified with *`phi`*.
They correspond to the smallest surrounding circle of the ellipse.
The actual start and end point of the ellipse is the intersection of
the ellipse with the orthogonal projection of the corresponding circle
point onto the main axis.
Both angles refer to the coordinate system of the ellipse, i.e.
relative to the main axis and in a mathematical positive direction.
Thus, the two main poles correspond to the angles 0 and
$\pi$, the two minor poles to the angles
$\pi/2$ and $3\pi/2$. To create a closed ellipse
the values 0 and $2\pi$ (with positive
point order) have to be passed to the operator. All angles *`phi`*,
*`startPhi`*, *`endPhi`* take arbitrary values and are mapped
internally to the interval $[0,2\pi]$.
The resolution of the resulting contours *`contEllipse`* is
controlled via *`resolution`* containing the maximum Euclidean
distance between neighboring contour points. The resolution is set
to the smallest valid value, if the input value falls below this
value.

### Parameter Broadcasting

This operator supports parameter broadcasting.
This means that each parameter can be given as a tuple of length
*1* or *N*.
Parameters with tuple length *1* will be repeated internally
such that the number of created items is always *N*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`contEllipse`** (output_object)  xld_cont(-array) `→` [HXLDCont](HXLDCont.md)

Resulting contour.

**`row`** (input_control)  ellipse.center.y(-array) `→` [HTuple](HTuple.md) (*double*)

Row coordinate of the center of the ellipse.

Default:
200.0

**`column`** (input_control)  ellipse.center.x(-array) `→` [HTuple](HTuple.md) (*double*)

Column coordinate of the center of the ellipse.

Default:
200.0

**`phi`** (input_control)  ellipse.angle.rad(-array) `→` [HTuple](HTuple.md) (*double*)

Orientation of the main axis [rad].

Default:
0.0

**`radius1`** (input_control)  ellipse.radius1(-array) `→` [HTuple](HTuple.md) (*double*)

Length of the larger half axis.

Default:
100.0

Restriction:
`Radius1 > 0`

**`radius2`** (input_control)  ellipse.radius2(-array) `→` [HTuple](HTuple.md) (*double*)

Length of the smaller half axis.

Default:
50.0

Restriction:
`Radius2 >= 0 && Radius2 <= Radius1`

**`startPhi`** (input_control)  angle.rad(-array) `→` [HTuple](HTuple.md) (*double*)

Angle of the start point on the smallest surrounding circle
[rad].

Default:
0.0

**`endPhi`** (input_control)  angle.rad(-array) `→` [HTuple](HTuple.md) (*double*)

Angle of the end point on the smallest surrounding circle
[rad].

Default:
6.28318

**`pointOrder`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

point order along the boundary.

Default:
"positive"

List of values:
"negative", "positive"

**`resolution`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Resolution: Maximum distance between neighboring
contour points.

Default:
1.5

Restriction:
`Resolution >= 1.192e-7`

## Example (HDevelop)

```
draw_ellipse(WindowHandle,Row,Column,Phi,Radius1,Radius2)
gen_ellipse_contour_xld(Ellipse,Row,Column,Phi,Radius1,Radius2,0,6.28319, \
                        'positive',1.5)
length_xld(Ellipse,Length)
* Transform StartPhi so that the start point of the ellipse actually
* intersects the line through origin at the angle StartPhi measured from
* the positive main axis
affine_trans_point_2d ([1.0,0.0,0.0,0.0,1.0*Radius2/Radius1,0.0], \
                       sin(StartPhi), cos(StartPhi), Qx, Qy)
StartPhiEllipse := atan2(Qx,Qy)
```

## Result

`GenEllipseContourXld` returns 2 (
H_MSG_TRUE)
if all parameter values
are correct. If necessary, an exception is raised.

## Possible Predecessors

`DrawEllipse`

## Possible Successors

`DispXld`,
`GetPointsEllipse`

## Alternatives

`GenCircleContourXld`

## Module

Foundation
