# GetRegressParamsXld (Operator)

## Name

`GetRegressParamsXld` — Return XLD contour parameters.

## Signature

`static void HOperatorSet.GetRegressParamsXld(HObject contours, out HTuple length, out HTuple nx, out HTuple ny, out HTuple dist, out HTuple fpx, out HTuple fpy, out HTuple lpx, out HTuple lpy, out HTuple mean, out HTuple deviation)`

`HTuple HXLDCont.GetRegressParamsXld(out HTuple nx, out HTuple ny, out HTuple dist, out HTuple fpx, out HTuple fpy, out HTuple lpx, out HTuple lpy, out HTuple mean, out HTuple deviation)`

## Description

`GetRegressParamsXld` returns the following parameters for
all XLD contours given in *`contours`*:

- the number of contour points *`length`*,
- the coordinates *`nx`* and *`ny`* of the
  normal vector of the regression line (i.e., least-squares
  approximating line),
- the distance *`dist`* of the regression line to the
  origin
- the sub-pixel precise coordinates *`fpx`* and
  *`fpy`* of the perpendicular projection of the start
  point of the contour onto the regression line,
- the sub-pixel precise coordinates *`lpx`* and
  *`lpy`* of the perpendicular projection of the end
  point of the contour onto the regression line,
- the mean of the Euclidean distance of the contour points from
  the regression line,
- the standard deviation of these distances.

## Attention

Before the contour parameters can be returned by
`GetRegressParamsXld`, the parameters of the regression
line to the contour must be calculated by calling
[`RegressContoursXld`](regress_contours_xld.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`contours`** (input_object)  xld_cont-array `→` [HXLDCont](HXLDCont.md)

Input XLD contours.

**`length`** (output_control)  integer-array `→` [HTuple](HTuple.md) (*int* / long)

Number of contour points.

**`nx`** (output_control)  point.x-array `→` [HTuple](HTuple.md) (*double*)

X-coordinate of the normal vector of the
regression line.

**`ny`** (output_control)  point.y-array `→` [HTuple](HTuple.md) (*double*)

Y-coordinate of the normal vector of the
regression line.

**`dist`** (output_control)  number-array `→` [HTuple](HTuple.md) (*double*)

Distance of the regression line from the origin.

**`fpx`** (output_control)  point.x-array `→` [HTuple](HTuple.md) (*double*)

X-coordinate of the projection of the start point
of the contour onto the regression line.

**`fpy`** (output_control)  point.y-array `→` [HTuple](HTuple.md) (*double*)

Y-coordinate of the projection of the start point
of the contour onto the regression line.

**`lpx`** (output_control)  point.x-array `→` [HTuple](HTuple.md) (*double*)

X-coordinate of the projection of the end point
of the contour onto the regression line.

**`lpy`** (output_control)  point.y-array `→` [HTuple](HTuple.md) (*double*)

Y-coordinate of the projection of the end point
of the contour onto the regression line.

**`mean`** (output_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Mean distance of the contour points from the
regression line.

**`deviation`** (output_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Standard deviation of the distances from the
regression line.

## Possible Predecessors

`RegressContoursXld`

## Possible Successors

`DispLine`,
`LineOrientation`

## See also

`FitLineContourXld`,
`GetContourGlobalAttribXld`,
`QueryContourGlobalAttribsXld`,
`GetContourXld`,
`GetContourAttribXld`,
`GenContoursSkeletonXld`,
`LinesGauss`,
`LinesFacet`,
`EdgesSubPix`

## Module

Foundation
