# gen_circle_contour_xld (Operator)

## Name

`gen_circle_contour_xld` — Create XLD contours corresponding to circles or circular arcs.

## Signature

`gen_circle_contour_xld( : ContCircle : Row, Column, Radius, StartPhi, EndPhi, PointOrder, Resolution : )`

## Description

`gen_circle_contour_xld` creates one or more circular arcs or
closed circles. Circles are specified by their center
(*`Row`*, *`Column`*) and their *`Radius`*.
In addition to that, circular arcs are characterized by the angle
of the start point *`StartPhi`*, the angle of the end point
*`EndPhi`*, and the *`PointOrder`* along the
boundary.
The resolution of the resulting contours *`ContCircle`* is
controlled via *`Resolution`* containing the Euclidean
distance in pixel between neighboring contour points. In general,
the distance between the second to last and the last point is smaller
than *`Resolution`*.

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

**`ContCircle`** (output_object)  xld_cont(-array) `→` object

Resulting contours.

**`Row`** (input_control)  circle.center.y(-array) `→`  (real)

Row coordinate of the center of the circles or
circular arcs.

Default:
200.0

**`Column`** (input_control)  circle.center.x(-array) `→`  (real)

Column coordinate of the center of the circles or
circular arcs.

Default:
200.0

**`Radius`** (input_control)  circle.radius(-array) `→`  (real)

Radius of the circles or circular arcs.

Default:
100.0

Restriction:
`Radius > 0`

**`StartPhi`** (input_control)  angle.rad(-array) `→`  (real)

Angle of the start points of the circles
or circular arcs [rad].

Default:
0.0

**`EndPhi`** (input_control)  angle.rad(-array) `→`  (real)

Angle of the end points of the circles
or circular arcs [rad].

Default:
6.28318

**`PointOrder`** (input_control)  string(-array) `→`  (string)

Point order along the circles or circular arcs.

Default:
'positive'

List of values:
'negative', 'positive'

**`Resolution`** (input_control)  real `→`  (real)

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
