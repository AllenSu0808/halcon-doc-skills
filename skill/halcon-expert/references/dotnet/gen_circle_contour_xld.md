# GenCircleContourXld (Operator)

## Name

`GenCircleContourXld` — Create XLD contours corresponding to circles or circular arcs.

## Signature

`static void HOperatorSet.GenCircleContourXld(out HObject contCircle, HTuple row, HTuple column, HTuple radius, HTuple startPhi, HTuple endPhi, HTuple pointOrder, HTuple resolution)`

`void HXLDCont.GenCircleContourXld(HTuple row, HTuple column, HTuple radius, HTuple startPhi, HTuple endPhi, HTuple pointOrder, double resolution)`

`void HXLDCont.GenCircleContourXld(double row, double column, double radius, double startPhi, double endPhi, string pointOrder, double resolution)`

## Description

`GenCircleContourXld` creates one or more circular arcs or
closed circles. Circles are specified by their center
(*`row`*, *`column`*) and their *`radius`*.
In addition to that, circular arcs are characterized by the angle
of the start point *`startPhi`*, the angle of the end point
*`endPhi`*, and the *`pointOrder`* along the
boundary.
The resolution of the resulting contours *`contCircle`* is
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

**`contCircle`** (output_object)  xld_cont(-array) `→` [HXLDCont](HXLDCont.md)

Resulting contours.

**`row`** (input_control)  circle.center.y(-array) `→` [HTuple](HTuple.md) (*double*)

Row coordinate of the center of the circles or
circular arcs.

Default:
200.0

**`column`** (input_control)  circle.center.x(-array) `→` [HTuple](HTuple.md) (*double*)

Column coordinate of the center of the circles or
circular arcs.

Default:
200.0

**`radius`** (input_control)  circle.radius(-array) `→` [HTuple](HTuple.md) (*double*)

Radius of the circles or circular arcs.

Default:
100.0

Restriction:
`Radius > 0`

**`startPhi`** (input_control)  angle.rad(-array) `→` [HTuple](HTuple.md) (*double*)

Angle of the start points of the circles
or circular arcs [rad].

Default:
0.0

**`endPhi`** (input_control)  angle.rad(-array) `→` [HTuple](HTuple.md) (*double*)

Angle of the end points of the circles
or circular arcs [rad].

Default:
6.28318

**`pointOrder`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Point order along the circles or circular arcs.

Default:
"positive"

List of values:
"negative", "positive"

**`resolution`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

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

`GenCircleContourXld` returns 2 (
H_MSG_TRUE)
if all parameter values
are correct. If necessary, an exception is raised.

## Possible Predecessors

`DrawCircle`

## Possible Successors

`DispXld`

## Alternatives

`GenEllipseContourXld`

## Module

Foundation
