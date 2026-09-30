# FitCircleContourXld (Operator)

## Name

`FitCircleContourXld` — Approximate XLD contours by circles.

## Signature

`static void HOperatorSet.FitCircleContourXld(HObject contours, HTuple algorithm, HTuple maxNumPoints, HTuple maxClosureDist, HTuple clippingEndPoints, HTuple iterations, HTuple clippingFactor, out HTuple row, out HTuple column, out HTuple radius, out HTuple startPhi, out HTuple endPhi, out HTuple pointOrder)`

`void HXLDCont.FitCircleContourXld(string algorithm, int maxNumPoints, double maxClosureDist, int clippingEndPoints, int iterations, double clippingFactor, out HTuple row, out HTuple column, out HTuple radius, out HTuple startPhi, out HTuple endPhi, out HTuple pointOrder)`

`void HXLDCont.FitCircleContourXld(string algorithm, int maxNumPoints, double maxClosureDist, int clippingEndPoints, int iterations, double clippingFactor, out double row, out double column, out double radius, out double startPhi, out double endPhi, out string pointOrder)`

## Description

`FitCircleContourXld` approximates the XLD contours
*`contours`* by circles. It does not perform a segmentation of
the input contours. Thus, one has to make sure that each contour
corresponds to one and only one circle. The operator returns for
each contour the center (*`row`*, *`column`*), and the
*`radius`*.

The algorithm used for the fitting of circles can be selected via
*`algorithm`*:

- ***"algebraic"*** —

  This approach minimizes the algebraic distance between the contour
  points and the resulting circle.
- ***"ahuber"*** —

  Similar to *"algebraic"*. Here the contour points are weighted to
  decrease the impact of outliers based on the approach of Huber
  (see below).
- ***"atukey"*** —

  Similar to *"algebraic"*. Here the contour points are weighted
  and outliers are ignored based
  on the approach of Tukey
  (see below).
- ***"geometric"*** —

  This approach minimizes the geometric distance
  between the contour points and the resulting circle.
  The distance measure is statistically optimal, but takes more
  computational time.
  This option is recommended if the contour
  points are considerably distorted by noise.
- ***"geohuber"*** —

  Similar to *"geometric"*. Here the contour points are weighted
  to decrease the impact of outliers based on
  the approach of Huber (see below).
- ***"geotukey"*** —

  Similar to *"geometric"*. Here the contour points are weighted
  and outliers are ignored based on
  the approach of Tukey (see below).

For '*huber' and '*tukey' a robust error statistics is used to estimate the
standard deviation of the distances from the contour points *without*
outliers from the approximating circle. The parameter
*`clippingFactor`* (a scaling factor for the standard deviation)
controls the amount of outliers: the smaller the value chosen for
*`clippingFactor`* the more outliers are detected. In the Tukey
algorithm outliers are removed, whereas in the Huber algorithm
outliers are only damped, or more precisely they are weighted linearly.
Without any robust weighting the squares of the distances are taken as
error values in the optimization, i.e., a least square formulation.
In practice, the approach of Tukey is recommended.

The parameter *`iterations`* specifies the number of iterations for the
algorithms *"algebraic"*, *"ahuber"* and *"atukey"*.
This parameter is ignored for the algorithms *"geometric"*,
*"geohuber"* and *"geotukey"*.
If *`iterations`* is set to zero, the algorithm does
not perform iterative improvements on the fitted circle, but only checks if
the initial guess was already close enough depending on the chosen treatment
of outliers.

To reduce the computational load, the fitting of circles can be
restricted to a subset of the contour points: If a value other than
*-1* is assigned to *`maxNumPoints`*, only up to
*`maxNumPoints`* points - uniformly distributed over the
contour - are used.

For circular arcs, the points on the circle closest to the start
points and end points of the original contours are chosen as start
and end points. The corresponding angles referring to the X-axis are
returned in *`startPhi`* and *`endPhi`*, see also
[`GenEllipseContourXld`](gen_ellipse_contour_xld.md). Contours, for which the distance
between their start points and their end points is less or equal
*`maxClosureDist`* are considered to be closed. Thus, they are
approximated by circles instead of circular arcs. Due to artifacts
in the pre-processing the start and end points of a contour might be
faulty. Therefore, it is possible to exclude
*`clippingEndPoints`* points at the beginning and at the end of a
contour from the fitting of circles. However, they are still used
for the determination of *`startPhi`* and *`endPhi`*.

The minimum necessary number of contour points for fitting a circle
is three.
Therefore, it is required that the number of contour points is at least
$3+2\cdot\texttt{ClippingEndPoints}$.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`contours`** (input_object)  xld_cont(-array) `→` [HXLDCont](HXLDCont.md)

Input contours.

**`algorithm`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Algorithm for the fitting of circles.

Default:
"algebraic"

List of values:
"ahuber", "algebraic", "atukey", "geohuber", "geometric", "geotukey"

**`maxNumPoints`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Maximum number of contour points used for the
computation (-1 for all points).

Default:
-1

Restriction:
`MaxNumPoints >= 3`

**`maxClosureDist`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Maximum distance between the end points of a
contour to be considered as 'closed'.

Default:
0.0

Restriction:
`MaxClosureDist >= 0.0`

**`clippingEndPoints`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Number of points at the beginning and at the end of the
contours to be ignored for the fitting.

Default:
0

Restriction:
`ClippingEndPoints >= 0`

**`iterations`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Maximum number of iterations for the robust weighted
fitting.

Default:
3

Restriction:
`Iterations >= 0`

**`clippingFactor`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Clipping factor for the elimination of outliers
(typical: 1.0 for Huber and 2.0 for Tukey).

Default:
2.0

Suggested values:
1.0, 1.5, 2.0, 2.5, 3.0

Restriction:
`ClippingFactor > 0`

**`row`** (output_control)  circle.center.y(-array) `→` [HTuple](HTuple.md) (*double*)

Row coordinate of the center of the circle.

**`column`** (output_control)  circle.center.x(-array) `→` [HTuple](HTuple.md) (*double*)

Column coordinate of the center of the circle.

**`radius`** (output_control)  circle.radius(-array) `→` [HTuple](HTuple.md) (*double*)

Radius of circle.

**`startPhi`** (output_control)  angle.rad(-array) `→` [HTuple](HTuple.md) (*double*)

Angle of the start point [rad].

**`endPhi`** (output_control)  angle.rad(-array) `→` [HTuple](HTuple.md) (*double*)

Angle of the end point [rad].

**`pointOrder`** (output_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Point order along the boundary.

List of values:
"negative", "positive"

## Result

`FitCircleContourXld` returns 2 (
H_MSG_TRUE)
if all parameter values
are correct, and circles could be fitted to the input contours. If
the input is empty the behavior can be set via
`set_system('no_object_result',<Result>)`. If necessary, an
exception is raised.
If the parameter *`clippingFactor`* is chosen too small, i.e.,
all points are classified as outliers, the error 3264 is raised.

## Possible Predecessors

`GenContoursSkeletonXld`,
`LinesGauss`,
`LinesFacet`,
`EdgesSubPix`,
`SmoothContoursXld`

## Possible Successors

`GenEllipseContourXld`,
`DispCircle`,
`GetPointsEllipse`

## See also

`FitEllipseContourXld`,
`FitLineContourXld`,
`FitRectangle2ContourXld`

## Module

Foundation
