# dist_ellipse_contour_xld (Operator)

## Name

`dist_ellipse_contour_xld` — Compute the distance of contours to an ellipse.

## Signature

`dist_ellipse_contour_xld(Contours : : Mode, MaxNumPoints, ClippingEndPoints, Row, Column, Phi, Radius1, Radius2 : MinDist, MaxDist, AvgDist, SigmaDist)`

## Description

`dist_ellipse_contour_xld` determines the distance
between the contours in *`Contours`* and an ellipse
specified by the center (*`Row`*, *`Column`*), the
orientation of the main axis *`Phi`*,
the length of the larger half axis *`Radius1`*, and the
length of the smaller half axis *`Radius2`*. Different
measures for the distance of a contour point
$X=(x_{i},y_{i})$ to the ellipse are
available (*`Mode`*):

- ***'geometric'*** —

  The underlying distance measure is the geometric distance between a point
  on the contour and the ellipse. This measure is also called
  orthogonal or Euclidean distance.
- ***'algebraic'*** —

  The distance is measured by the algebraic distance
  $$ax_{i}^{2}+bx_{i}y_{i}+cy_{i}^{2}+dx_{i}+ey_{i}+f$$, where the
  parameters a - f describing the ellipse are normalized in order
  to obtain *`Radius2`* as distance of the center of the
  ellipse. This measure shows a *high curvature bias*: Near points of
  high curvature on the ellipse (like the poles on the main axis)
  the distance is smaller than near points with low curvature.
- ***'focpoints'*** —

  The distance is measured by the deviation
  $XF_{1}+XF_{2}-2a$,
  where $F_{1},F_{2}$ are the focal points and a corresponds to
  *`Radius1`*. This measure shows a *low curvature bias*:
  Near points of high curvature on the ellipse (like the poles on the main
  axis) the distance is larger than near points with low curvature.
- ***'bisec'*** —

  The distance is measured by the distance between X and the
  intersection of the angular bisector of the two lines through X and the
  focal points with the ellipse. This is a good approximation of
  the orthogonal distance from X to the ellipse.
  The accuracy of the approximation depends on both the aspect ratio of the
  ellipse and the distance.

The operator returns the minimum absolute distance *`MinDist`*,
the maximum absolute distance *`MaxDist`*, the average
absolute distance *`AvgDist`*, and the standard deviation of
the absolute distances *`SigmaDist`* of all contour points.

To reduce the computational load, the computation of the distances
can be restricted to a subset of the contour points: If a value other
than -1 is assigned to *`MaxNumPoints`*, only up to
*`MaxNumPoints`* points - uniformly distributed over the
contour - are used.
Due to artifacts in the pre-processing the start and end points
of a contour might be faulty. Therefore, it is possible to
exclude *`ClippingEndPoints`* points at the beginning and at
the end of a contour from the computation.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Contours`** (input_object)  xld_cont(-array) `→` object

Input contours.

**`Mode`** (input_control)  string `→`  (string)

Method for the determination of the distances.

Default:
'geometric'

List of values:
'algebraic', 'bisec', 'focpoints', 'geometric'

**`MaxNumPoints`** (input_control)  integer `→`  (integer)

Maximum number of contour points used for the
computation (-1 for all points).

Default:
-1

Restriction:
`MaxNumPoints >= 3`

**`ClippingEndPoints`** (input_control)  integer `→`  (integer)

Number of points at the beginning and the end of the
contours to be ignored for the computation of
distances.

Default:
0

Restriction:
`ClippingEndPoints >= 0`

**`Row`** (input_control)  ellipse.center.y `→`  (real)

Row coordinate of the center of the ellipse.

**`Column`** (input_control)  ellipse.center.x `→`  (real)

Column coordinate of the center of the ellipse.

**`Phi`** (input_control)  ellipse.angle.rad `→`  (real)

Orientation of the main axis in radian.

Restriction:
`Phi >= 0 && Phi <= 6.283185307`

**`Radius1`** (input_control)  ellipse.radius1 `→`  (real)

Length of the larger half axis.

Restriction:
`Radius1 > 0`

**`Radius2`** (input_control)  ellipse.radius2 `→`  (real)

Length of the smaller half axis.

Restriction:
`Radius2 >= 0 && Radius2 <= Radius1`

**`MinDist`** (output_control)  real(-array) `→`  (real)

Minimum distance.

**`MaxDist`** (output_control)  real(-array) `→`  (real)

Maximum distance.

**`AvgDist`** (output_control)  real(-array) `→`  (real)

Mean distance.

**`SigmaDist`** (output_control)  real(-array) `→`  (real)

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

`dist_ellipse_contour_xld` returns 2 (
H_MSG_TRUE)
if all parameter
values are correct. If necessary, an exception is raised.

## Possible Predecessors

`fit_ellipse_contour_xld`

## Alternatives

`dist_ellipse_contour_points_xld`

## Module

Foundation
