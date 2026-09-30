# FitEllipseContourXld (Operator)

## Name

`FitEllipseContourXld` — Approximate XLD contours by ellipses or elliptic arcs.

## Signature

`static void HOperatorSet.FitEllipseContourXld(HObject contours, HTuple algorithm, HTuple maxNumPoints, HTuple maxClosureDist, HTuple clippingEndPoints, HTuple vossTabSize, HTuple iterations, HTuple clippingFactor, out HTuple row, out HTuple column, out HTuple phi, out HTuple radius1, out HTuple radius2, out HTuple startPhi, out HTuple endPhi, out HTuple pointOrder)`

`void HXLDCont.FitEllipseContourXld(string algorithm, int maxNumPoints, double maxClosureDist, int clippingEndPoints, int vossTabSize, int iterations, double clippingFactor, out HTuple row, out HTuple column, out HTuple phi, out HTuple radius1, out HTuple radius2, out HTuple startPhi, out HTuple endPhi, out HTuple pointOrder)`

`void HXLDCont.FitEllipseContourXld(string algorithm, int maxNumPoints, double maxClosureDist, int clippingEndPoints, int vossTabSize, int iterations, double clippingFactor, out double row, out double column, out double phi, out double radius1, out double radius2, out double startPhi, out double endPhi, out string pointOrder)`

## Description

`FitEllipseContourXld` approximates the XLD contours
*`contours`* by elliptic arcs or closed ellipses. It does not
perform a segmentation of the input contours. Thus, one has to make sure
that each contour corresponds to one and only one elliptic structure.
The operator returns for each contour the center
(*`row`*, *`column`*), the orientation of the main
axis *`phi`*, the length of the larger half axis *`radius1`*,
and the length of the smaller half axis *`radius2`* of the underlying
ellipse. In addition to that, the angle corresponding to the start point
and the end point *`startPhi`*, *`endPhi`*,
and the point order along the boundary *`pointOrder`*
is returned for elliptic arcs. These parameters are set to
0, $2\pi$, and 'positive' for closed ellipses.
The algorithm used for the fitting of ellipses can be selected via
*`algorithm`*:

- ***"fitzgibbon"*** —

  This approach minimizes the algebraic distance
  $$ax_{i}^{2}+bx_{i}y_{i}+cy_{i}^{2}+dx_{i}+ey_{i}+f$$
  between the contour points $(x_{i},y_{i})$ and the resulting
  ellipse. The constraint $4ac-b^{2}=1$ guarantees that the
  resulting polynomial characterizes an ellipse (instead of a hyperbola or a
  parabola).
- ***"fhuber"*** —

  Similar to *"fitzgibbon"*. Here the contour points are weighted
  to decrease the impact of outliers based on
  the approach of Huber (see below).
- ***"ftukey"*** —

  Similar to *"fitzgibbon"*. Here the contour points are weighted
  and outliers are ignored based on
  the approach of Tukey (see below).
- ***"geometric"*** —

  This approach minimizes the geometric distance
  between the contour points and the resulting ellipse.
  The distance measure is statistically optimal, but takes more
  computational time, because the computation is an iterative process.
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
- ***"voss"*** —

  Each input contour is transformed in an affine standard position.
  Based on the moments of the transformed contour (that is of the
  enclosed image region) the standard circular segment is chosen
  whose standard position matches best with the standard position
  of the contour. The ellipse corresponding to the standard
  position of the selected circular segment is re-transformed
  based on the affine transformation which produced the standard position
  of the contour resulting in the ellipse matching the original contour.
  *`vossTabSize`* standard circular segments are used for
  this computation. To speed up the process the corresponding moments
  and other data is stored in a table which is created during the
  first call (with a specific value for *`vossTabSize`*) to
  `FitEllipseContourXld`.
- ***"focpoints"*** —

  Each point P on an ellipse satisfies the constraint that the sum
  of distances to the focal points $F_{1},F_{2}$ equals twice the
  length of the larger half axis a. In this approach, the deviation
  $PF_{1}+PF_{2}-2a$ is minimized for all contour
  points by a least squares optimization.
- ***"fphuber"*** —

  Similar to *"focpoints"*. Here a *weighted* least squares
  optimization is done to decrease the impact of outliers based on
  the approach of Huber (see below).
- ***"fptukey"*** —

  Similar to *"focpoints"*. Here a *weighted* least squares
  optimization is done and outliers are ignored based on
  the approach of Tukey (see below).

For *'*huber'* and *'*tukey'* a robust error statistics is used
to estimate the standard deviation of the distances from the contour points
*without* outliers from the approximating ellipse. The parameter
*`clippingFactor`* (a scaling factor for the standard deviation)
controls the amount of outliers: the smaller the value chosen for
*`clippingFactor`* the more points are classified as outliers.
Every contour point is individually weighted and contributes according to
its weight in the fitting process. The bundle of robust weighting and
fitting can be iterated. The overall number of iterations is
given by *`iterations`*. This parameter is of relevance for all
algorithms except the two based on the geometric distance,
i.e., *"geohuber"* and *"geotukey"*, where this parameter
is ignored. If the algorithm does
not find a fitting ellipse within this number of iterations, it fits a line;
in this case *`radius2`* is zero.
In the Tukey algorithm outliers are removed, whereas in the Huber algorithm
outliers are only damped, or more precisely they are weighted linearly.
Without any robust weighting the squares of the distances are taken as
error values in the optimization, i.e., a least square formulation.
In practice, the approach of Tukey is recommended.

To reduce the computational load, the fitting of ellipses can be
restricted to a subset of the contour points: If a value other than
*-1* is assigned to *`maxNumPoints`*, only up to
*`maxNumPoints`* points - uniformly distributed over the
contour - are used.

For elliptic arcs, the points on the ellipse closest to the
start points and end points of the original contours are chosen
as start and end points. The corresponding angles referring to the
main axis of the ellipse are returned in *`startPhi`* and
*`endPhi`*, see also [`GenEllipseContourXld`](gen_ellipse_contour_xld.md).
Contours, for which the distance between their start points and
their end points is less or equal *`maxClosureDist`*
are considered to be closed. Thus, they are approximated by
ellipses instead of elliptic arcs. The *"focpoints"* algorithms
determine the initial parameters for the optimization for closed contours in
a faster and less accurate way than for open contours.
As a result, in some cases more
*`iterations`* may be necessary when applied to closed contours.
Due to artifacts in the pre-processing the start and end points
of a contour might be faulty. Therefore, it is possible to
exclude *`clippingEndPoints`* points at the beginning and at the
end of a contour from the fitting of ellipses. However, they are still
used for the determination of *`startPhi`* and
*`endPhi`*.

The minimum necessary number of contour points for fitting an ellipse
is five.
Therefore, it is required that the number of contour points is at least
$5+2\cdot\texttt{ClippingEndPoints}$.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`contours`** (input_object)  xld_cont(-array) `→` [HXLDCont](HXLDCont.md)

Input contours.

**`algorithm`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Algorithm for the fitting of ellipses.

Default:
"fitzgibbon"

List of values:
"fhuber", "fitzgibbon", "focpoints", "fphuber", "fptukey", "ftukey", "geohuber", "geometric", "geotukey", "voss"

**`maxNumPoints`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Maximum number of contour points used for the
computation (-1 for all points).

Default:
-1

Restriction:
`MaxNumPoints >= 5`

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

**`vossTabSize`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Number of circular segments used for the Voss approach.

Default:
200

Restriction:
`VossTabSize >= 25 && VossTabSize <= 5000`

**`iterations`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Maximum number of iterations for the robust weighted
fitting.

Default:
3

Restriction:
`Iterations >= 0`

**`clippingFactor`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Clipping factor for the elimination of outliers
(typical: 1.0 for '*huber' and 2.0 for '*tukey').

Default:
2.0

Suggested values:
1.0, 1.5, 2.0, 2.5, 3.0

Restriction:
`ClippingFactor > 0`

**`row`** (output_control)  ellipse.center.y(-array) `→` [HTuple](HTuple.md) (*double*)

Row coordinate of the center of the ellipse.

**`column`** (output_control)  ellipse.center.x(-array) `→` [HTuple](HTuple.md) (*double*)

Column coordinate of the center of the ellipse.

**`phi`** (output_control)  ellipse.angle.rad(-array) `→` [HTuple](HTuple.md) (*double*)

Orientation of the main axis [rad].

**`radius1`** (output_control)  ellipse.radius1(-array) `→` [HTuple](HTuple.md) (*double*)

Length of the larger half axis.

**`radius2`** (output_control)  ellipse.radius2(-array) `→` [HTuple](HTuple.md) (*double*)

Length of the smaller half axis.

**`startPhi`** (output_control)  angle.rad(-array) `→` [HTuple](HTuple.md) (*double*)

Angle of the start point [rad].

**`endPhi`** (output_control)  angle.rad(-array) `→` [HTuple](HTuple.md) (*double*)

Angle of the end point [rad].

**`pointOrder`** (output_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

point order along the boundary.

List of values:
"negative", "positive"

## Example (HDevelop)

```
read_image (Image, 'caltab')
find_caltab (Image, CalPlate, 'caltab_800mm.descr', 3, 112, 5)
reduce_domain (Image, CalPlate, ImageReduced)
edges_sub_pix (ImageReduced, Edges, 'lanser2', 0.5, 20, 40)
select_contours_xld (Edges, EdgesClosed, 'closed', 0, 2.0, 0, 0)
select_contours_xld (EdgesClosed, EdgesMarks, 'length', 20, 80, 0, 0)
fit_ellipse_contour_xld (EdgesMarks, 'fitzgibbon', -1, 2, 0, 200, 3, 2.0, \
                         Row, Column, Phi, Radius1, Radius2, StartPhi, \
                         EndPhi, PointOrder)
gen_ellipse_contour_xld (EllMarks, Row, Column, Phi, Radius1, Radius2, \
                         StartPhi, EndPhi, PointOrder, 1.5)
length_xld(EllMarks,Length)
```

## Result

`FitEllipseContourXld` returns 2 (
H_MSG_TRUE)
if all parameter values
are correct, and ellipses could be fitted to the input contours.
If the input is empty the behavior can be set via
`set_system('no_object_result',<Result>)`.
If necessary, an exception is raised.
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
`DispEllipse`,
`GetPointsEllipse`

## See also

`FitLineContourXld`,
`FitCircleContourXld`,
`FitRectangle2ContourXld`

## Module

Foundation
