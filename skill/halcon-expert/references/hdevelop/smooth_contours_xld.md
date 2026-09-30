# smooth_contours_xld (Operator)

## Name

`smooth_contours_xld` — Smooth an XLD contour.

## Signature

`smooth_contours_xld(Contours : SmoothedContours : NumRegrPoints : )`

## Description

`smooth_contours_xld` smooths the input XLD contours
*`Contours`* and returns the smoothed contours in
*`SmoothedContours`*. The smoothing is done by projecting
the contours' points onto a local regression line (i.e., a
least-squares approximating line), which is computed from
*`NumRegrPoints`* on each side of the current contour point.
This operator should be called, for example, before contours are
scaled.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Contours`** (input_object)  xld_cont-array `→` object

Contour to be smoothed.

**`SmoothedContours`** (output_object)  xld_cont-array `→` object

Smoothed contour.

**`NumRegrPoints`** (input_control)  integer `→`  (integer)

Number of points used to calculate the regression
line.

Default:
5

Suggested values:
3, 5, 7, 9

Restriction:
`NumRegrPoints >= 3 && odd(NumRegrPoints)`

## Possible Predecessors

`gen_contours_skeleton_xld`,
`lines_gauss`,
`lines_facet`,
`edges_sub_pix`

## Possible Successors

`affine_trans_contour_xld`,
`gen_polygons_xld`,
`local_max_contours_xld`

## See also

`get_contour_xld`

## Module

Foundation
