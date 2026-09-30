# gen_circle_contour_xld (Operator)

## Name

`gen_circle_contour_xld` — Create XLD contours corresponding to circles or circular arcs.

## Signature

`def gen_circle_contour_xld(row: MaybeSequence[float], column: MaybeSequence[float], radius: MaybeSequence[float], start_phi: MaybeSequence[float], end_phi: MaybeSequence[float], point_order: MaybeSequence[str], resolution: float) -> HObject`

## Description

`gen_circle_contour_xld` creates one or more circular arcs or
closed circles. Circles are specified by their center
(*`row`*, *`column`*) and their *`radius`*.
In addition to that, circular arcs are characterized by the angle
of the start point *`start_phi`*, the angle of the end point
*`end_phi`*, and the *`point_order`* along the
boundary.
The resolution of the resulting contours *`cont_circle`* is
controlled via *`resolution`* containing the Euclidean
distance in pixel between neighboring contour points. In general,
the distance between the second to last and the last point is smaller
than *`resolution`*.

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

**`cont_circle`** (output_object)  xld_cont(-array) `→` HObject

Resulting contours.

**`row`** (input_control)  circle.center.y(-array) `→` MaybeSequence[float]

Row coordinate of the center of the circles or
circular arcs.

Default:
200.0

**`column`** (input_control)  circle.center.x(-array) `→` MaybeSequence[float]

Column coordinate of the center of the circles or
circular arcs.

Default:
200.0

**`radius`** (input_control)  circle.radius(-array) `→` MaybeSequence[float]

Radius of the circles or circular arcs.

Default:
100.0

Restriction:
`Radius > 0`

**`start_phi`** (input_control)  angle.rad(-array) `→` MaybeSequence[float]

Angle of the start points of the circles
or circular arcs [rad].

Default:
0.0

**`end_phi`** (input_control)  angle.rad(-array) `→` MaybeSequence[float]

Angle of the end points of the circles
or circular arcs [rad].

Default:
6.28318

**`point_order`** (input_control)  string(-array) `→` MaybeSequence[str]

Point order along the circles or circular arcs.

Default:
"positive"

List of values:
"negative", "positive"

**`resolution`** (input_control)  real `→` float

Distance between neighboring contour points.

Default:
1.0

Restriction:
`Resolution >= 0.00001`

## Example (HDevelop)

```
draw_circle (WindowHandle, Row, Column, Radius)
gen_circle_contour_xld (ContCircle, Row, Column, Radius, 0, \
                        rad(360) , 'positive', 1.0)
gen_region_contour_xld (ContCircle, Region, 'filled')
```

## Result

`gen_circle_contour_xld` returns 2 (
H_MSG_TRUE)
if all parameter values
are correct. If necessary, an exception is raised.

## Possible Predecessors

`draw_circle`

## Possible Successors

`disp_xld`

## Alternatives

`gen_ellipse_contour_xld`

## Module

Foundation
