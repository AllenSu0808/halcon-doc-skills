# FitRectangle2ContourXld (Operator)

## Name

`FitRectangle2ContourXld` — Fit rectangles to XLD contours.

## Signature

`static void HOperatorSet.FitRectangle2ContourXld(HObject contours, HTuple algorithm, HTuple maxNumPoints, HTuple maxClosureDist, HTuple clippingEndPoints, HTuple iterations, HTuple clippingFactor, out HTuple row, out HTuple column, out HTuple phi, out HTuple length1, out HTuple length2, out HTuple pointOrder)`

`void HXLDCont.FitRectangle2ContourXld(string algorithm, int maxNumPoints, double maxClosureDist, int clippingEndPoints, int iterations, double clippingFactor, out HTuple row, out HTuple column, out HTuple phi, out HTuple length1, out HTuple length2, out HTuple pointOrder)`

`void HXLDCont.FitRectangle2ContourXld(string algorithm, int maxNumPoints, double maxClosureDist, int clippingEndPoints, int iterations, double clippingFactor, out double row, out double column, out double phi, out double length1, out double length2, out string pointOrder)`

## Description

`FitRectangle2ContourXld` fits rectangles to the
rectangular XLD contours given by *`contours`* and returns the
parameters of the rectangles in *`row`*, *`column`*
(center), *`phi`* (orientation), as well as *`length1`*
and *`length2`* (half edge lengths). The angle *`phi`* is
returned in radians and specifies the angle between the horizontal
axis and the edge with the half length *`length1`* in the
mathematically positive direction (counterclockwise). In addition,
the point order of the contour is returned in *`pointOrder`*.
*`pointOrder`* = *"positive"* means that the contour
is traversed in the mathematically positive direction
(counterclockwise).

The algorithm used for the fitting of the rectangles can be selected
via *`algorithm`*:

- ***"regression"*** —

  Standard least-squares line fitting.
- ***"huber"*** —

  Weighted least-squares line fitting, where the impact of outliers
  is decreased based on the approach of Huber (see below).
- ***"tukey"*** —

  Weighted least-squares line fitting, where
  outliers are ignored based on the approach of Tukey(see below).

For *"huber"* and *"tukey"*, a robust error statistics is used
to estimate the standard deviation of the distances of the contour points
from the approximating sides of the rectangle while ignoring outliers. The
standard deviation is computed separately for each side of the rectangle to
allow the processing of rectangles whose sides are not exactly perpendicular
to each other. The parameter *`clippingFactor`* (a scaling factor
relative to the standard deviation) controls the amount of outliers:
The smaller the value chosen for *`clippingFactor`* the more outliers
are detected. The detection of outliers is iterated. The parameter
*`iterations`* specifies the number of iterations. For
*`algorithm`* = *"regression"*, the values of the last two
parameters are ignored. Note that in the approach of Tukey (*"tukey"*),
the outliers are removed before performing the approximation and all other
points are weighted, whereas in the approach of Huber (*"huber"*),
the outliers still have a small influence. Particularly, for outliers the
optimization is influenced linearly and for points with a smaller distance it
is influenced to the square. For the algebraic approach, all distances of the
points influence the optimization to the square and thus are not robust
against outliers. In practice, the approach of Tukey is recommended.

To reduce the computational load, the fitting of rectangles can be
restricted to a subset of the contour points: If a value other than
*-1* is assigned to *`maxNumPoints`*, only up to
*`maxNumPoints`* points, uniformly distributed across the
contour, are used.

Depending on the processing used to create *`contours`*, the
start and end points of a contour may contain positional errors.
Therefore, it is possible to exclude *`clippingEndPoints`*
points at the beginning and at the end of a contour from the
rectangle fitting.

Contours, for which the distance between their start points and
their end points is <= *`maxClosureDist`* are
considered to be closed. For closed contours, the end point of the
contour is not used for the rectangle fitting because it would
receive twice the weight of the remaining points in the fit.

The fitting of the rectangle to the contour is based on finding the
correspondence between the contour points and the four sides of the
rectangle. To enable a successful fit, there must be at least one
point that lies in the interior of the line segment that represents
the respective rectangle side, i.e., the point must not lie at the
ends of the line segment. Because of this, at least eight contour
points are necessary to fit the rectangle. A point is internally
assigned to the side of the rectangle to which it has the minimum
distance. For this, the currently optimal rectangle parameters,
i.e., the parameters used for the current iteration step, are used
internally. If no corresponding points are found for at least one
side of the rectangle, the rectangle parameters cannot be determined
uniquely. In this case, the error 3266 is returned. Because of
this, the caller of `FitRectangle2ContourXld` must ensure
that the input contours sufficiently resemble a rectangle. In
particular, none of the interior angles of the contour, if the
contour was approximated by four lines, should be smaller than 45
degrees or larger than 135 degrees. Because of the assignment of
contour points to the closest side of the rectangle this would mean
that at least one side of the rectangle would have no corresponding
points. Furthermore, *`clippingFactor`* should not be chosen
too small to avoid that the outlier suppression creates rectangle
sides without corresponding contour points. This can only happen
for *`algorithm`* = *"tukey"*. If the above
conditions are observed, `FitRectangle2ContourXld` returns
highly accurate rectangle parameters. If the outlier suppression
according to Tukey is used, `FitRectangle2ContourXld` can
be used to robustly fit rectangles, e.g., to rectangular contours
with rounded corners.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`contours`** (input_object)  xld_cont(-array) `→` [HXLDCont](HXLDCont.md)

Input contours.

**`algorithm`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Algorithm for fitting the rectangles.

Default:
"regression"

List of values:
"huber", "regression", "tukey"

**`maxNumPoints`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Maximum number of contour points used for the
computation (-1 for all points).

Default:
-1

Restriction:
`MaxNumPoints == -1 || MaxNumPoints >= 8`

**`maxClosureDist`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Maximum distance between the end points of a
contour to be considered as closed.

Default:
0.0

Restriction:
`MaxClosureDist >= 0.0`

**`clippingEndPoints`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Number of points at the beginning and at the end of the
contours to be ignored for the fitting.

Default:
0

Suggested values:
0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

Restriction:
`ClippingEndPoints >= 0`

**`iterations`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Maximum number of iterations
(not used for *"regression"*).

Default:
3

Restriction:
`Iterations >= 0`

**`clippingFactor`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Clipping factor for the elimination of outliers
(typical values: *1.0* for *"huber"* and
*2.0* for *"tukey"*).

Default:
2.0

Suggested values:
1.0, 1.5, 2.0, 2.5, 3.0

Restriction:
`ClippingFactor > 0`

**`row`** (output_control)  rectangle2.center.y(-array) `→` [HTuple](HTuple.md) (*double*)

Row coordinate of the center of the rectangle.

**`column`** (output_control)  rectangle2.center.x(-array) `→` [HTuple](HTuple.md) (*double*)

Column coordinate of the center of the rectangle.

**`phi`** (output_control)  rectangle2.angle.rad(-array) `→` [HTuple](HTuple.md) (*double*)

Orientation of the main axis of the rectangle [rad].

**`length1`** (output_control)  rectangle2.hwidth(-array) `→` [HTuple](HTuple.md) (*double*)

First radius (half length) of the rectangle.

**`length2`** (output_control)  rectangle2.hheight(-array) `→` [HTuple](HTuple.md) (*double*)

Second radius (half width) of the rectangle.

**`pointOrder`** (output_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Point order of the contour.

List of values:
"negative", "positive"

## Result

`FitRectangle2ContourXld` returns 2 (
H_MSG_TRUE)
if all parameter
values are correct, and rectangles could be fitted to the input
contours. If the input is empty the behavior can be set via
`set_system('no_object_result',<Result>)`. If necessary, an
exception is raised. If the parameter *`clippingFactor`* is
chosen too small, i.e., all points are classified as outliers, the
error 3266 is raised. If no points could be found for at least one
side of the rectangle, the error 3266 is raised as well.

## Possible Predecessors

`GenContoursSkeletonXld`,
`LinesGauss`,
`LinesFacet`,
`EdgesSubPix`,
`SmoothContoursXld`,
`UnionCollinearContoursXld`,
`UnionCollinearContoursExtXld`,
`UnionAdjacentContoursXld`

## Possible Successors

`DistRectangle2ContourPointsXld`,
`GenRectangle2ContourXld`

## Alternatives

`SmallestRectangle2Xld`

## See also

`FitLineContourXld`,
`FitCircleContourXld`,
`FitEllipseContourXld`

## Module

Foundation
