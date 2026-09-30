# DistEllipseContourPointsXld (Operator)

## Name

`DistEllipseContourPointsXld` — Compute the distances of all contour points to an ellipse.

## Signature

`static void HOperatorSet.DistEllipseContourPointsXld(HObject contour, HTuple distanceMode, HTuple clippingEndPoints, HTuple row, HTuple column, HTuple phi, HTuple radius1, HTuple radius2, out HTuple distances)`

`HTuple HXLDCont.DistEllipseContourPointsXld(string distanceMode, int clippingEndPoints, double row, double column, double phi, double radius1, double radius2)`

## Description

The operator `DistEllipseContourPointsXld` determines the
distances between points of a contour *`contour`* and an ellipse
specified by the center (*`row`*, *`column`*), the
orientation of the main axis *`phi`*,
the length of the larger half axis *`radius1`*, and the
length of the smaller half axis *`radius2`*.

The distance measure is the geometric distance, sometimes also called
orthogonal distance. The distances *`distances`* are returned for
all points of the contour.
Normally, the distance is a positive value. In this case
*`distanceMode`* equal to *"unsigned"* must be chosen.
If this option is switched to *"signed"* the distances can take
positive or negative sign, depending on whether the contour points lie
outside or inside the ellipse respectively.

Because of artifacts in the preprocessing, the start and end points
of a contour might be faulty. In this case, the operator
[`FitEllipseContourXld`](fit_ellipse_contour_xld.md) is typically called with the parameter
*`clippingEndPoints`* set to a value greater than zero to exclude
points at the beginning and the end of the contour from the computation.
In order to get the geometric distances of the same set of points as used
in the fitting process *`clippingEndPoints`* should take
the same value.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`contour`** (input_object)  xld_cont `→` [HXLDCont](HXLDCont.md)

Input contours.

**`distanceMode`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Mode for unsigned or signed distance values.

Default:
"unsigned"

List of values:
"signed", "unsigned"

**`clippingEndPoints`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Number of points at the beginning and the end of the
contours to be ignored for the computation of
distances.

Default:
0

Restriction:
`ClippingEndPoints >= 0`

**`row`** (input_control)  ellipse.center.y `→` [HTuple](HTuple.md) (*double*)

Row coordinate of the center of the ellipse.

**`column`** (input_control)  ellipse.center.x `→` [HTuple](HTuple.md) (*double*)

Column coordinate of the center of the ellipse.

**`phi`** (input_control)  ellipse.angle.rad `→` [HTuple](HTuple.md) (*double*)

Orientation of the main axis in radian.

Restriction:
`Phi >= 0 && Phi <= 6.283185307`

**`radius1`** (input_control)  ellipse.radius1 `→` [HTuple](HTuple.md) (*double*)

Length of the larger half axis.

Restriction:
`Radius1 > 0`

**`radius2`** (input_control)  ellipse.radius2 `→` [HTuple](HTuple.md) (*double*)

Length of the smaller half axis.

Restriction:
`Radius2 >= 0 && Radius2 <= Radius1`

**`distances`** (output_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Distances of the contour points to the ellipse.

## Result

`DistEllipseContourPointsXld` returns 2 (
H_MSG_TRUE)
if all parameter
values are correct. If necessary, an exception is raised.

## Possible Predecessors

`FitEllipseContourXld`

## Alternatives

`DistEllipseContourXld`

## Module

Foundation
