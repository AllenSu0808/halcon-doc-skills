# DistRectangle2ContourPointsXld (Operator)

## Name

`DistRectangle2ContourPointsXld` — Compute the distances of all contour points to a rectangle.

## Signature

`static void HOperatorSet.DistRectangle2ContourPointsXld(HObject contour, HTuple clippingEndPoints, HTuple row, HTuple column, HTuple phi, HTuple length1, HTuple length2, out HTuple distances)`

`HTuple HXLDCont.DistRectangle2ContourPointsXld(int clippingEndPoints, double row, double column, double phi, double length1, double length2)`

## Description

`DistRectangle2ContourPointsXld` determines the Euclidean
distances between the points of a contour *`contour`* and a
rectangle of arbitrary orientation specified by the center
(*`row`*, *`column`*), the orientation *`phi`*, and
the half edge lengths *`length1`* and *`length2`*. The
angle *`phi`* must be given in radians and specifies the angle
between the horizontal axis and the edge with the half length
*`length1`* in the mathematically positive direction
(counterclockwise).

Depending on the processing used to create *`contour`*, the
start and end points of a contour may contain positional errors. In
this case, the operator [`FitRectangle2ContourXld`](fit_rectangle2_contour_xld.md) is
typically called with the parameter *`clippingEndPoints`* set
to a value greater than zero to exclude points at the beginning and
the end of the contour from the computation. To compute the
distances of the same set of points as used in the fitting process,
*`clippingEndPoints`* should be set to the same value as in
[`FitRectangle2ContourXld`](fit_rectangle2_contour_xld.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`contour`** (input_object)  xld_cont `→` [HXLDCont](HXLDCont.md)

Input contour.

**`clippingEndPoints`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Number of points at the beginning and the end of the
contours to be ignored for the computation of
distances.

Default:
0

Suggested values:
0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

Restriction:
`ClippingEndPoints >= 0`

**`row`** (input_control)  rectangle2.center.y `→` [HTuple](HTuple.md) (*double*)

Row coordinate of the center of the rectangle.

**`column`** (input_control)  rectangle2.center.x `→` [HTuple](HTuple.md) (*double*)

Column coordinate of the center of the rectangle.

**`phi`** (input_control)  rectangle2.angle.rad `→` [HTuple](HTuple.md) (*double*)

Orientation of the main axis of the rectangle [rad].

**`length1`** (input_control)  rectangle2.hwidth `→` [HTuple](HTuple.md) (*double*)

First radius (half length) of the rectangle.

Restriction:
`Length1 > 0`

**`length2`** (input_control)  rectangle2.hheight `→` [HTuple](HTuple.md) (*double*)

Second radius (half width) of the rectangle.

Restriction:
`Length2 >= 0`

**`distances`** (output_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Distances of the contour points to the rectangle.

## Result

`DistRectangle2ContourPointsXld` returns 2 (
H_MSG_TRUE)
if all
parameter values are correct. If necessary, an exception is
raised.

## Possible Predecessors

`FitRectangle2ContourXld`

## Module

Foundation
