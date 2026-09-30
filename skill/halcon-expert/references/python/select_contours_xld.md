# select_contours_xld (Operator)

## Name

`select_contours_xld` — Select XLD contours according to several features.

## Signature

`def select_contours_xld(contours: HObject, feature: str, min_1: float, max_1: float, min_2: float, max_2: float) -> HObject`

## Description

`select_contours_xld` selects XLD contours from the input
contours *`contours`* according to the following features
(parameter *`feature`*):

- ***"contour_length"*:** —

  all contours whose length is smaller
  than *`min_1`* or larger than *`max_1`*
  are not returned (*`min_2`* and
  *`max_2`* have no influence here).
- ***"maximum_extent"*:** —

  all contours whose maximum extent (as
  measured by their eight extremal
  points in row and column direction,
  according to Haralick and Shapiro:
  Computer and Robot Vision,
  Addison-Wesley 1992, chapter 3.2) is
  smaller than *`min_1`* or larger
  than *`max_1`* are not returned
  (*`min_2`* and *`max_2`* have
  no influence here).
- ***"direction"*:** —

  only contours for which the direction of
  the regression line is between
  *`min_1`* and *`max_1`* (in
  radians, counter-clockwise) are returned.
  *`min_1`* and *`max_1`* are
  mapped to the range of [0,2*PI[.
  (*`min_2`* and *`max_2`* have
  no influence here).
- ***"curvature"*:** —

  only contours for which the mean distance
  from the regression line lies between
  *`min_1`* and *`max_1`*, and
  for which the standard deviation of the
  distances is between *`min_2`* and
  *`max_2`* are returned.
- ***"closed"*:** —

  only contours for which the distance between
  their start point and their end point is less or equal
  *`max_1`* pixels are returned. (*`min_1`*,
  *`min_2`* and *`max_2`* have no influence
  here.)
- ***"open"*:** —

  only contours for which the distance between their
  start point and their end point is greater than
  *`min_1`* pixels are returned. (*`max_1`*,
  *`min_2`* and *`max_2`* have no influence
  here).

If *`min_1`* = *`max_1`* = 0 or *`min_2`* =
*`max_2`* = 0 is used for the selection according to curvature,
the respective feature has no influence on the selection.

## Attention

Before contour can be filtered by `select_contours_xld`
according to *"direction"* or *"curvature"*, the parameters of
the regression lines to the contours must be calculated with
[`regress_contours_xld`](regress_contours_xld.md). If this has not been done,
`select_contours_xld` calls [`regress_contours_xld`](regress_contours_xld.md)
internally with the parameters `mode` = *"no"* and
`iterations` = *1*. If a different mode should be
used, [`regress_contours_xld`](regress_contours_xld.md) must be called explicitly.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`contours`** (input_object)  xld_cont-array `→` HObject

Input XLD contours.

**`selected_contours`** (output_object)  xld_cont-array `→` HObject

Output XLD contours.

**`feature`** (input_control)  string `→` str

Feature to select contours with.

Default:
"contour_length"

List of values:
"closed", "contour_length", "curvature", "direction", "maximum_extent", "open"

**`min_1`** (input_control)  real `→` float

Lower threshold.

Default:
0.5

**`max_1`** (input_control)  real `→` float

Upper threshold.

Default:
200.0

**`min_2`** (input_control)  real `→` float

Lower threshold.

Default:
-0.5

**`max_2`** (input_control)  real `→` float

Upper threshold.

Default:
0.5

## Possible Predecessors

`regress_contours_xld`

## See also

`get_contour_xld`,
`get_contour_attrib_xld`,
`gen_contours_skeleton_xld`,
`lines_gauss`,
`lines_facet`,
`edges_sub_pix`,
`get_regress_params_xld`,
`get_contour_global_attrib_xld`,
`query_contour_global_attribs_xld`

## References

R. Haralick, L. Shapiro: “Computer and Robot Vision” Vol. 1;
Kapitel 3.2, Addison-Wesley 1992

## Module

Foundation
