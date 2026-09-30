# gen_ellipse_contour_xld (Operator)

## Name

`gen_ellipse_contour_xld` — Create an XLD contour that corresponds to an elliptic arc.

## Signature

`def gen_ellipse_contour_xld(row: MaybeSequence[float], column: MaybeSequence[float], phi: MaybeSequence[float], radius_1: MaybeSequence[float], radius_2: MaybeSequence[float], start_phi: MaybeSequence[float], end_phi: MaybeSequence[float], point_order: MaybeSequence[str], resolution: float) -> HObject`

## Description

`gen_ellipse_contour_xld` creates one or more elliptic arcs or
closed ellipses. Ellipses are specified by their center
(*`row`*, *`column`*), the orientation of the main axis
*`phi`*, the length of the larger half axis
*`radius_1`*, and the length of the smaller half
axis *`radius_2`*.
In addition to that, elliptic arcs are characterized by the angle
of the start point *`start_phi`*, the angle of the end point
*`end_phi`*, and the point order *`point_order`* along the
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
*`start_phi`*, *`end_phi`* take arbitrary values and are mapped
internally to the interval $[0,2\pi]$.
The resolution of the resulting contours *`cont_ellipse`* is
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

**`cont_ellipse`** (output_object)  xld_cont(-array) `→` HObject

Resulting contour.

**`row`** (input_control)  ellipse.center.y(-array) `→` MaybeSequence[float]

Row coordinate of the center of the ellipse.

Default:
200.0

**`column`** (input_control)  ellipse.center.x(-array) `→` MaybeSequence[float]

Column coordinate of the center of the ellipse.

Default:
200.0

**`phi`** (input_control)  ellipse.angle.rad(-array) `→` MaybeSequence[float]

Orientation of the main axis [rad].

Default:
0.0

**`radius_1`** (input_control)  ellipse.radius1(-array) `→` MaybeSequence[float]

Length of the larger half axis.

Default:
100.0

Restriction:
`Radius1 > 0`

**`radius_2`** (input_control)  ellipse.radius2(-array) `→` MaybeSequence[float]

Length of the smaller half axis.

Default:
50.0

Restriction:
`Radius2 >= 0 && Radius2 <= Radius1`

**`start_phi`** (input_control)  angle.rad(-array) `→` MaybeSequence[float]

Angle of the start point on the smallest surrounding circle
[rad].

Default:
0.0

**`end_phi`** (input_control)  angle.rad(-array) `→` MaybeSequence[float]

Angle of the end point on the smallest surrounding circle
[rad].

Default:
6.28318

**`point_order`** (input_control)  string(-array) `→` MaybeSequence[str]

point order along the boundary.

Default:
"positive"

List of values:
"negative", "positive"

**`resolution`** (input_control)  real `→` float

Resolution: Maximum distance between neighboring
contour points.

Default:
1.5

Restriction:
`Resolution >= 1.192e-7`

## Result

`gen_ellipse_contour_xld` returns 2 (
H_MSG_TRUE)
if all parameter values
are correct. If necessary, an exception is raised.

## Possible Predecessors

`draw_ellipse`

## Possible Successors

`disp_xld`,
`get_points_ellipse`

## Alternatives

`gen_circle_contour_xld`

## Module

Foundation
