# fit_circle_contour_xld (Operator)

## Name

`fit_circle_contour_xld` — Approximate XLD contours by circles.

## Signature

`fit_circle_contour_xld(Contours : : Algorithm, MaxNumPoints, MaxClosureDist, ClippingEndPoints, Iterations, ClippingFactor : Row, Column, Radius, StartPhi, EndPhi, PointOrder)`

## Description

`fit_circle_contour_xld` approximates the XLD contours
*`Contours`* by circles. It does not perform a segmentation of
the input contours. Thus, one has to make sure that each contour
corresponds to one and only one circle. The operator returns for
each contour the center (*`Row`*, *`Column`*), and the
*`Radius`*.

The algorithm used for the fitting of circles can be selected via
*`Algorithm`*:

- ***'algebraic'*** —

  This approach minimizes the algebraic distance between the contour
  points and the resulting circle.
- ***'ahuber'*** —

  Similar to *'algebraic'*. Here the contour points are weighted to
  decrease the impact of outliers based on the approach of Huber
  (see below).
- ***'atukey'*** —

  Similar to *'algebraic'*. Here the contour points are weighted
  and outliers are ignored based
  on the approach of Tukey
  (see below).
- ***'geometric'*** —

  This approach minimizes the geometric distance
  between the contour points and the resulting circle.
  The distance measure is statistically optimal, but takes more
  computational time.
  This option is recommended if the contour
  points are considerably distorted by noise.
- ***'geohuber'*** —

  Similar to *'geometric'*. Here the contour points are weighted
  to decrease the impact of outliers based on
  the approach of Huber (see below).
- ***'geotukey'*** —

  Similar to *'geometric'*. Here the contour points are weighted
  and outliers are ignored based on
  the approach of Tukey (see below).

For '*huber' and '*tukey' a robust error statistics is used to estimate the
standard deviation of the distances from the contour points *without*
outliers from the approximating circle. The parameter
*`ClippingFactor`* (a scaling factor for the standard deviation)
controls the amount of outliers: the smaller the value chosen for
*`ClippingFactor`* the more outliers are detected. In the Tukey
algorithm outliers are removed, whereas in the Huber algorithm
outliers are only damped, or more precisely they are weighted linearly.
Without any robust weighting the squares of the distances are taken as
error values in the optimization, i.e., a least square formulation.
In practice, the approach of Tukey is recommended.

The parameter *`Iterations`* specifies the number of iterations for the
algorithms *'algebraic'*, *'ahuber'* and *'atukey'*.
This parameter is ignored for the algorithms *'geometric'*,
*'geohuber'* and *'geotukey'*.
If *`Iterations`* is set to zero, the algorithm does
not perform iterative improvements on the fitted circle, but only checks if
the initial guess was already close enough depending on the chosen treatment
of outliers.

To reduce the computational load, the fitting of circles can be
restricted to a subset of the contour points: If a value other than
*-1* is assigned to *`MaxNumPoints`*, only up to
*`MaxNumPoints`* points - uniformly distributed over the
contour - are used.

For circular arcs, the points on the circle closest to the start
points and end points of the original contours are chosen as start
and end points. The corresponding angles referring to the X-axis are
returned in *`StartPhi`* and *`EndPhi`*, see also
[`gen_ellipse_contour_xld`](gen_ellipse_contour_xld.md). Contours, for which the distance
between their start points and their end points is less or equal
*`MaxClosureDist`* are considered to be closed. Thus, they are
approximated by circles instead of circular arcs. Due to artifacts
in the pre-processing the start and end points of a contour might be
faulty. Therefore, it is possible to exclude
*`ClippingEndPoints`* points at the beginning and at the end of a
contour from the fitting of circles. However, they are still used
for the determination of *`StartPhi`* and *`EndPhi`*.

The minimum necessary number of contour points for fitting a circle
is three.
Therefore, it is required that the number of contour points is at least
$3+2\cdot\texttt{ClippingEndPoints}$.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Contours`** (input_object)  xld_cont(-array) `→` object

Input contours.

**`Algorithm`** (input_control)  string `→`  (string)

Algorithm for the fitting of circles.

Default:
'algebraic'

List of values:
'ahuber', 'algebraic', 'atukey', 'geohuber', 'geometric', 'geotukey'

**`MaxNumPoints`** (input_control)  integer `→`  (integer)

Maximum number of contour points used for the
computation (-1 for all points).

Default:
-1

Restriction:
`MaxNumPoints >= 3`

**`MaxClosureDist`** (input_control)  real `→`  (real)

Maximum distance between the end points of a
contour to be considered as 'closed'.

Default:
0.0

Restriction:
`MaxClosureDist >= 0.0`

**`ClippingEndPoints`** (input_control)  integer `→`  (integer)

Number of points at the beginning and at the end of the
contours to be ignored for the fitting.

Default:
0

Restriction:
`ClippingEndPoints >= 0`

**`Iterations`** (input_control)  integer `→`  (integer)

Maximum number of iterations for the robust weighted
fitting.

Default:
3

Restriction:
`Iterations >= 0`

**`ClippingFactor`** (input_control)  real `→`  (real)

Clipping factor for the elimination of outliers
(typical: 1.0 for Huber and 2.0 for Tukey).

Default:
2.0

Suggested values:
1.0, 1.5, 2.0, 2.5, 3.0

Restriction:
`ClippingFactor > 0`

**`Row`** (output_control)  circle.center.y(-array) `→`  (real)

Row coordinate of the center of the circle.

**`Column`** (output_control)  circle.center.x(-array) `→`  (real)

Column coordinate of the center of the circle.

**`Radius`** (output_control)  circle.radius(-array) `→`  (real)

Radius of circle.

**`StartPhi`** (output_control)  angle.rad(-array) `→`  (real)

Angle of the start point [rad].

**`EndPhi`** (output_control)  angle.rad(-array) `→`  (real)

Angle of the end point [rad].

**`PointOrder`** (output_control)  string(-array) `→`  (string)

Point order along the boundary.

List of values:
'negative', 'positive'

## Result

`fit_circle_contour_xld` returns 2 (
H_MSG_TRUE)
if all parameter values
are correct, and circles could be fitted to the input contours. If
the input is empty the behavior can be set via
`set_system('no_object_result',<Result>)`. If necessary, an
exception is raised.
If the parameter *`ClippingFactor`* is chosen too small, i.e.,
all points are classified as outliers, the error 3264 is raised.

## Possible Predecessors

`gen_contours_skeleton_xld`,
`lines_gauss`,
`lines_facet`,
`edges_sub_pix`,
`smooth_contours_xld`

## Possible Successors

`gen_ellipse_contour_xld`,
`disp_circle`,
`get_points_ellipse`

## See also

`fit_ellipse_contour_xld`,
`fit_line_contour_xld`,
`fit_rectangle2_contour_xld`

## Module

Foundation
