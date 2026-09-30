# fit_line_contour_xld (Operator)

## Name

`fit_line_contour_xld` — Approximate XLD contours by line segments.

## Signature

`fit_line_contour_xld(Contours : : Algorithm, MaxNumPoints, ClippingEndPoints, Iterations, ClippingFactor : RowBegin, ColBegin, RowEnd, ColEnd, Nr, Nc, Dist)`

## Description

`fit_line_contour_xld` approximates the XLD contours
*`Contours`* by line segments. It does not perform a
segmentation of the input contours. Thus, one has to make sure that
each contour corresponds to one and only one line segment. The
operator returns for each contour the start point
(*`RowBegin`*, *`ColBegin`*), the end point
(*`RowEnd`*, *`ColEnd`*), and the regression line to the
contour given by the normal vector (*`Nr`*, *`Nc`*) of the
line and its distance *`Dist`* from the origin, i.e., the line
equation is given by
$r\cdot\texttt{Nr}+c\cdot\texttt{Nc}-\texttt{Dist}=0$.

The algorithm used for the fitting of lines can be selected via
*`Algorithm`*:

- ***'regression'*:** —

  Standard 'least squares' line fitting.
- ***'huber'*:** —

  Weighted 'least squares' line fitting, where the impact of outliers
  is decreased based on the approach of Huber (see below).
- ***'tukey'*:** —

  Weighted 'least squares' line fitting, where outliers
  are ignored based on the approach of Tukey (see below).
- ***'drop'*:** —

  'least squares' line fitting, where outliers are ignored. In
  particular, all contour points further away from the contour than the mean
  distance to the regression line multiplied with the *`ClippingFactor`*
  (see below) are ignored for the calculation of the undistorted regression
  line.
- ***'gauss'*:** —

  Weighted 'least squares' line fitting, where the impact of outliers
  is decreased based on the mean value and the standard deviation of
  the distances of all contour points from the approximating line.

For *'huber'*, *'tukey'*, and *'drop'*
a robust error statistics is used to
estimate the standard deviation of the distances from the contour points
*without* outliers from the approximating line. The parameter
*`ClippingFactor`* (a scaling factor for the standard deviation)
controls the amount of outliers: The smaller the value chosen for
*`ClippingFactor`* the more outliers are detected. The detection of
outliers is repeated. The parameter *`Iterations`* specifies the number
of iterations.
In the mode *'regression'* this value is ignored.
Note that in the approach of Tukey (*'tukey'*), the outliers are
removed before performing the approximation and all other points are weighted,
whereas in the approach of Huber (*'huber'*), the outliers still have
a small influence. Particularly,
for outliers the optimization is influenced linearly and for points with a
smaller distance it is influenced to the square.
In practice, the approach of Tukey is recommended.

To reduce the computational load, the fitting of lines can be
restricted to a subset of the contour points: If a value other than
-1 is assigned to *`MaxNumPoints`*, only up to
*`MaxNumPoints`* points - uniformly distributed over the
contour - are used.

The start point and the end point of a line segment is determined by
projecting the first and the last point of the corresponding contour
to the approximating line. Due to artifacts in the pre-processing
the start and end points of a contour might be faulty. Therefore, it
is possible to exclude *`ClippingEndPoints`* points at the beginning
and at the end of a contour from the line fitting. However, they are
still used for the determination of the start point and the end
point of the line segment.

The minimum necessary number of contour points for fitting a line is two.
Therefore, it is required that the number of contour points is at least
$2+2\cdot\texttt{ClippingEndPoints}$.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Contours`** (input_object)  xld_cont(-array) `→` object

Input contours.

**`Algorithm`** (input_control)  string `→`  (string)

Algorithm for the fitting of lines.

Default:
'tukey'

List of values:
'drop', 'gauss', 'huber', 'regression', 'tukey'

**`MaxNumPoints`** (input_control)  integer `→`  (integer)

Maximum number of contour points used for the computation
(-1 for all points).

Default:
-1

Restriction:
`MaxNumPoints >= 2`

**`ClippingEndPoints`** (input_control)  integer `→`  (integer)

Number of points at the beginning and at the end of the
contours to be ignored for the fitting.

Default:
0

Restriction:
`ClippingEndPoints >= 0`

**`Iterations`** (input_control)  integer `→`  (integer)

Maximum number of iterations
(unused for *'regression'*).

Default:
5

Restriction:
`Iterations >= 0`

**`ClippingFactor`** (input_control)  real `→`  (real)

Clipping factor for the elimination of outliers
(typical values: *1.0* for *'huber'* and
*'drop'* and *2.0* for *'tukey'*).

Default:
2.0

Suggested values:
1.0, 1.5, 2.0, 2.5, 3.0

Restriction:
`ClippingFactor > 0`

**`RowBegin`** (output_control)  line.begin.y(-array) `→`  (real)

Row coordinates of the starting points of the line
segments.

**`ColBegin`** (output_control)  line.begin.x(-array) `→`  (real)

Column coordinates of the starting points of the line
segments.

**`RowEnd`** (output_control)  line.end.y(-array) `→`  (real)

Row coordinates of the end points of the line
segments.

**`ColEnd`** (output_control)  line.end.x(-array) `→`  (real)

Column coordinates of the end points of the line
segments.

**`Nr`** (output_control)  number(-array) `→`  (real)

Line parameter: Row coordinate of the normal vector

**`Nc`** (output_control)  number(-array) `→`  (real)

Line parameter: Column coordinate of the normal vector

**`Dist`** (output_control)  number(-array) `→`  (real)

Line parameter: Distance of the line from the origin

## Example (HDevelop)

```
read_image (Image, 'mreut')
edges_sub_pix (Image, Edges, 'lanser2', 0.5, 20, 40)
gen_polygons_xld (Edges, Polygons, 'ramer', 2)
split_contours_xld (Polygons, Contours, 'polygon', 1, 5)
fit_line_contour_xld (Contours, 'regression', -1, 0, 5, 2, RowBegin, \
                      ColBegin, RowEnd, ColEnd, Nr, Nc, Dist)
```

## Result

`fit_line_contour_xld` returns 2 (
H_MSG_TRUE)
if all parameter values
are correct, and line segments could be fitted to the input contours.
If the input is empty the behavior can be set via
`set_system('no_object_result',<Result>)`.
If necessary, an exception is raised.
If the parameter *`ClippingFactor`* is chosen too small, i.e.,
all points are classified as outliers, the error 3264 is raised.

## Possible Predecessors

`gen_contours_skeleton_xld`,
`lines_gauss`,
`lines_facet`,
`edges_sub_pix`,
`smooth_contours_xld`

## Possible Successors

`disp_line`,
`line_orientation`

## See also

`regress_contours_xld`,
`get_regress_params_xld`

## Module

Foundation
