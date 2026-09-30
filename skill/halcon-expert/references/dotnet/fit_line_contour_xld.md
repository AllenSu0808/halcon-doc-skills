# FitLineContourXld (Operator)

## Name

`FitLineContourXld` — Approximate XLD contours by line segments.

## Signature

`static void HOperatorSet.FitLineContourXld(HObject contours, HTuple algorithm, HTuple maxNumPoints, HTuple clippingEndPoints, HTuple iterations, HTuple clippingFactor, out HTuple rowBegin, out HTuple colBegin, out HTuple rowEnd, out HTuple colEnd, out HTuple nr, out HTuple nc, out HTuple dist)`

`void HXLDCont.FitLineContourXld(string algorithm, int maxNumPoints, int clippingEndPoints, int iterations, double clippingFactor, out HTuple rowBegin, out HTuple colBegin, out HTuple rowEnd, out HTuple colEnd, out HTuple nr, out HTuple nc, out HTuple dist)`

`void HXLDCont.FitLineContourXld(string algorithm, int maxNumPoints, int clippingEndPoints, int iterations, double clippingFactor, out double rowBegin, out double colBegin, out double rowEnd, out double colEnd, out double nr, out double nc, out double dist)`

## Description

`FitLineContourXld` approximates the XLD contours
*`contours`* by line segments. It does not perform a
segmentation of the input contours. Thus, one has to make sure that
each contour corresponds to one and only one line segment. The
operator returns for each contour the start point
(*`rowBegin`*, *`colBegin`*), the end point
(*`rowEnd`*, *`colEnd`*), and the regression line to the
contour given by the normal vector (*`nr`*, *`nc`*) of the
line and its distance *`dist`* from the origin, i.e., the line
equation is given by
$r\cdot\texttt{Nr}+c\cdot\texttt{Nc}-\texttt{Dist}=0$.

The algorithm used for the fitting of lines can be selected via
*`algorithm`*:

- ***"regression"*:** —

  Standard 'least squares' line fitting.
- ***"huber"*:** —

  Weighted 'least squares' line fitting, where the impact of outliers
  is decreased based on the approach of Huber (see below).
- ***"tukey"*:** —

  Weighted 'least squares' line fitting, where outliers
  are ignored based on the approach of Tukey (see below).
- ***"drop"*:** —

  'least squares' line fitting, where outliers are ignored. In
  particular, all contour points further away from the contour than the mean
  distance to the regression line multiplied with the *`clippingFactor`*
  (see below) are ignored for the calculation of the undistorted regression
  line.
- ***"gauss"*:** —

  Weighted 'least squares' line fitting, where the impact of outliers
  is decreased based on the mean value and the standard deviation of
  the distances of all contour points from the approximating line.

For *"huber"*, *"tukey"*, and *"drop"*
a robust error statistics is used to
estimate the standard deviation of the distances from the contour points
*without* outliers from the approximating line. The parameter
*`clippingFactor`* (a scaling factor for the standard deviation)
controls the amount of outliers: The smaller the value chosen for
*`clippingFactor`* the more outliers are detected. The detection of
outliers is repeated. The parameter *`iterations`* specifies the number
of iterations.
In the mode *"regression"* this value is ignored.
Note that in the approach of Tukey (*"tukey"*), the outliers are
removed before performing the approximation and all other points are weighted,
whereas in the approach of Huber (*"huber"*), the outliers still have
a small influence. Particularly,
for outliers the optimization is influenced linearly and for points with a
smaller distance it is influenced to the square.
In practice, the approach of Tukey is recommended.

To reduce the computational load, the fitting of lines can be
restricted to a subset of the contour points: If a value other than
-1 is assigned to *`maxNumPoints`*, only up to
*`maxNumPoints`* points - uniformly distributed over the
contour - are used.

The start point and the end point of a line segment is determined by
projecting the first and the last point of the corresponding contour
to the approximating line. Due to artifacts in the pre-processing
the start and end points of a contour might be faulty. Therefore, it
is possible to exclude *`clippingEndPoints`* points at the beginning
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

**`contours`** (input_object)  xld_cont(-array) `→` [HXLDCont](HXLDCont.md)

Input contours.

**`algorithm`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Algorithm for the fitting of lines.

Default:
"tukey"

List of values:
"drop", "gauss", "huber", "regression", "tukey"

**`maxNumPoints`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Maximum number of contour points used for the computation
(-1 for all points).

Default:
-1

Restriction:
`MaxNumPoints >= 2`

**`clippingEndPoints`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Number of points at the beginning and at the end of the
contours to be ignored for the fitting.

Default:
0

Restriction:
`ClippingEndPoints >= 0`

**`iterations`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Maximum number of iterations
(unused for *"regression"*).

Default:
5

Restriction:
`Iterations >= 0`

**`clippingFactor`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Clipping factor for the elimination of outliers
(typical values: *1.0* for *"huber"* and
*"drop"* and *2.0* for *"tukey"*).

Default:
2.0

Suggested values:
1.0, 1.5, 2.0, 2.5, 3.0

Restriction:
`ClippingFactor > 0`

**`rowBegin`** (output_control)  line.begin.y(-array) `→` [HTuple](HTuple.md) (*double*)

Row coordinates of the starting points of the line
segments.

**`colBegin`** (output_control)  line.begin.x(-array) `→` [HTuple](HTuple.md) (*double*)

Column coordinates of the starting points of the line
segments.

**`rowEnd`** (output_control)  line.end.y(-array) `→` [HTuple](HTuple.md) (*double*)

Row coordinates of the end points of the line
segments.

**`colEnd`** (output_control)  line.end.x(-array) `→` [HTuple](HTuple.md) (*double*)

Column coordinates of the end points of the line
segments.

**`nr`** (output_control)  number(-array) `→` [HTuple](HTuple.md) (*double*)

Line parameter: Row coordinate of the normal vector

**`nc`** (output_control)  number(-array) `→` [HTuple](HTuple.md) (*double*)

Line parameter: Column coordinate of the normal vector

**`dist`** (output_control)  number(-array) `→` [HTuple](HTuple.md) (*double*)

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

`FitLineContourXld` returns 2 (
H_MSG_TRUE)
if all parameter values
are correct, and line segments could be fitted to the input contours.
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

`DispLine`,
`LineOrientation`

## See also

`RegressContoursXld`,
`GetRegressParamsXld`

## Module

Foundation
