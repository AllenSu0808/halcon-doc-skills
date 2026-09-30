# get_regress_params_xld (Operator)

## Name

`get_regress_params_xld` — Return XLD contour parameters.

## Signature

`get_regress_params_xld(Contours : : : Length, Nx, Ny, Dist, Fpx, Fpy, Lpx, Lpy, Mean, Deviation)`

## Description

`get_regress_params_xld` returns the following parameters for
all XLD contours given in *`Contours`*:

- the number of contour points *`Length`*,
- the coordinates *`Nx`* and *`Ny`* of the
  normal vector of the regression line (i.e., least-squares
  approximating line),
- the distance *`Dist`* of the regression line to the
  origin
- the sub-pixel precise coordinates *`Fpx`* and
  *`Fpy`* of the perpendicular projection of the start
  point of the contour onto the regression line,
- the sub-pixel precise coordinates *`Lpx`* and
  *`Lpy`* of the perpendicular projection of the end
  point of the contour onto the regression line,
- the mean of the Euclidean distance of the contour points from
  the regression line,
- the standard deviation of these distances.

## Attention

Before the contour parameters can be returned by
`get_regress_params_xld`, the parameters of the regression
line to the contour must be calculated by calling
[`regress_contours_xld`](regress_contours_xld.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Contours`** (input_object)  xld_cont-array `→` object

Input XLD contours.

**`Length`** (output_control)  integer-array `→`  (integer)

Number of contour points.

**`Nx`** (output_control)  point.x-array `→`  (real)

X-coordinate of the normal vector of the
regression line.

**`Ny`** (output_control)  point.y-array `→`  (real)

Y-coordinate of the normal vector of the
regression line.

**`Dist`** (output_control)  number-array `→`  (real)

Distance of the regression line from the origin.

**`Fpx`** (output_control)  point.x-array `→`  (real)

X-coordinate of the projection of the start point
of the contour onto the regression line.

**`Fpy`** (output_control)  point.y-array `→`  (real)

Y-coordinate of the projection of the start point
of the contour onto the regression line.

**`Lpx`** (output_control)  point.x-array `→`  (real)

X-coordinate of the projection of the end point
of the contour onto the regression line.

**`Lpy`** (output_control)  point.y-array `→`  (real)

Y-coordinate of the projection of the end point
of the contour onto the regression line.

**`Mean`** (output_control)  real-array `→`  (real)

Mean distance of the contour points from the
regression line.

**`Deviation`** (output_control)  real-array `→`  (real)

Standard deviation of the distances from the
regression line.

## Possible Predecessors

`regress_contours_xld`

## Possible Successors

`disp_line`,
`line_orientation`

## See also

`fit_line_contour_xld`,
`get_contour_global_attrib_xld`,
`query_contour_global_attribs_xld`,
`get_contour_xld`,
`get_contour_attrib_xld`,
`gen_contours_skeleton_xld`,
`lines_gauss`,
`lines_facet`,
`edges_sub_pix`

## Module

Foundation
