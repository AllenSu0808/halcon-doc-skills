# get_regress_params_xld (Operator)

## Name

`get_regress_params_xld` — Return XLD contour parameters.

## Signature

`def get_regress_params_xld(contours: HObject) -> Tuple[Sequence[int], Sequence[float], Sequence[float], Sequence[float], Sequence[float], Sequence[float], Sequence[float], Sequence[float], Sequence[float], Sequence[float]]`

## Description

`get_regress_params_xld` returns the following parameters for
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
`get_regress_params_xld`, the parameters of the regression
line to the contour must be calculated by calling
[`regress_contours_xld`](regress_contours_xld.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`contours`** (input_object)  xld_cont-array `→` HObject

Input XLD contours.

**`length`** (output_control)  integer-array `→` Sequence[int]

Number of contour points.

**`nx`** (output_control)  point.x-array `→` Sequence[float]

X-coordinate of the normal vector of the
regression line.

**`ny`** (output_control)  point.y-array `→` Sequence[float]

Y-coordinate of the normal vector of the
regression line.

**`dist`** (output_control)  number-array `→` Sequence[float]

Distance of the regression line from the origin.

**`fpx`** (output_control)  point.x-array `→` Sequence[float]

X-coordinate of the projection of the start point
of the contour onto the regression line.

**`fpy`** (output_control)  point.y-array `→` Sequence[float]

Y-coordinate of the projection of the start point
of the contour onto the regression line.

**`lpx`** (output_control)  point.x-array `→` Sequence[float]

X-coordinate of the projection of the end point
of the contour onto the regression line.

**`lpy`** (output_control)  point.y-array `→` Sequence[float]

Y-coordinate of the projection of the end point
of the contour onto the regression line.

**`mean`** (output_control)  real-array `→` Sequence[float]

Mean distance of the contour points from the
regression line.

**`deviation`** (output_control)  real-array `→` Sequence[float]

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
