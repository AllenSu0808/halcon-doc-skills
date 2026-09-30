# DistEllipseContourXld (Operator)

## Name

`DistEllipseContourXld` — Compute the distance of contours to an ellipse.

## Signature

`static void HOperatorSet.DistEllipseContourXld(HObject contours, HTuple mode, HTuple maxNumPoints, HTuple clippingEndPoints, HTuple row, HTuple column, HTuple phi, HTuple radius1, HTuple radius2, out HTuple minDist, out HTuple maxDist, out HTuple avgDist, out HTuple sigmaDist)`

`void HXLDCont.DistEllipseContourXld(string mode, int maxNumPoints, int clippingEndPoints, double row, double column, double phi, double radius1, double radius2, out HTuple minDist, out HTuple maxDist, out HTuple avgDist, out HTuple sigmaDist)`

`void HXLDCont.DistEllipseContourXld(string mode, int maxNumPoints, int clippingEndPoints, double row, double column, double phi, double radius1, double radius2, out double minDist, out double maxDist, out double avgDist, out double sigmaDist)`

## Description

`DistEllipseContourXld` determines the distance
between the contours in *`contours`* and an ellipse
specified by the center (*`row`*, *`column`*), the
orientation of the main axis *`phi`*,
the length of the larger half axis *`radius1`*, and the
length of the smaller half axis *`radius2`*. Different
measures for the distance of a contour point
$X=(x_{i},y_{i})$ to the ellipse are
available (*`mode`*):

- ***"geometric"*** —

  The underlying distance measure is the geometric distance between a point
  on the contour and the ellipse. This measure is also called
  orthogonal or Euclidean distance.
- ***"algebraic"*** —

  The distance is measured by the algebraic distance
  $$ax_{i}^{2}+bx_{i}y_{i}+cy_{i}^{2}+dx_{i}+ey_{i}+f$$, where the
  parameters a - f describing the ellipse are normalized in order
  to obtain *`radius2`* as distance of the center of the
  ellipse. This measure shows a *high curvature bias*: Near points of
  high curvature on the ellipse (like the poles on the main axis)
  the distance is smaller than near points with low curvature.
- ***"focpoints"*** —

  The distance is measured by the deviation
  $XF_{1}+XF_{2}-2a$,
  where $F_{1},F_{2}$ are the focal points and a corresponds to
  *`radius1`*. This measure shows a *low curvature bias*:
  Near points of high curvature on the ellipse (like the poles on the main
  axis) the distance is larger than near points with low curvature.
- ***"bisec"*** —

  The distance is measured by the distance between X and the
  intersection of the angular bisector of the two lines through X and the
  focal points with the ellipse. This is a good approximation of
  the orthogonal distance from X to the ellipse.
  The accuracy of the approximation depends on both the aspect ratio of the
  ellipse and the distance.

The operator returns the minimum absolute distance *`minDist`*,
the maximum absolute distance *`maxDist`*, the average
absolute distance *`avgDist`*, and the standard deviation of
the absolute distances *`sigmaDist`* of all contour points.

To reduce the computational load, the computation of the distances
can be restricted to a subset of the contour points: If a value other
than -1 is assigned to *`maxNumPoints`*, only up to
*`maxNumPoints`* points - uniformly distributed over the
contour - are used.
Due to artifacts in the pre-processing the start and end points
of a contour might be faulty. Therefore, it is possible to
exclude *`clippingEndPoints`* points at the beginning and at
the end of a contour from the computation.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`contours`** (input_object)  xld_cont(-array) `→` [HXLDCont](HXLDCont.md)

Input contours.

**`mode`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Method for the determination of the distances.

Default:
"geometric"

List of values:
"algebraic", "bisec", "focpoints", "geometric"

**`maxNumPoints`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Maximum number of contour points used for the
computation (-1 for all points).

Default:
-1

Restriction:
`MaxNumPoints >= 3`

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

**`minDist`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Minimum distance.

**`maxDist`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Maximum distance.

**`avgDist`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Mean distance.

**`sigmaDist`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Standard deviation of the distance.

## Example (HDevelop)

```
read_image (Image, 'caltab')
find_caltab (Image, CalPlate, 'caltab_big.descr', 3, 112, 5)
reduce_domain (Image, CalPlate, ImageReduced)
edges_sub_pix (ImageReduced, Edges, 'lanser2', 0.5, 20, 40)
select_contours_xld (Edges, EdgesClosed, 'closed', 0, 2.0, 0, 0)
select_contours_xld (EdgesClosed, EdgesMarks, 'contour_length', 20, 100, \
                     0, 0)
fit_ellipse_contour_xld (EdgesMarks, 'fitzgibbon', -1, 2, 0, 200, 3, 2.0, \
                         Row, Column, Phi, Radius1, Radius2, StartPhi, \
                         EndPhi, PointOrder)
for i := 0 to |Row|-1 by 1
    select_obj (EdgesMarks, ObjectSelected, i+1)
    dist_ellipse_contour_xld (ObjectSelected, 'bisec', -1, 0, Row[i], \
                              Column[i], Phi[i], Radius1[i], Radius2[i], \
                              MinDist, MaxDist, AvgDist, SigmaDist)
endfor
```

## Result

`DistEllipseContourXld` returns 2 (
H_MSG_TRUE)
if all parameter
values are correct. If necessary, an exception is raised.

## Possible Predecessors

`FitEllipseContourXld`

## Alternatives

`DistEllipseContourPointsXld`

## Module

Foundation
