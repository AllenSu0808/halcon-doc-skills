# select_contours_xld (Operator)

## Name

`select_contours_xld` — Select XLD contours according to several features.

## Signature

`select_contours_xld(Contours : SelectedContours : Feature, Min1, Max1, Min2, Max2 : )`

## Description

`select_contours_xld` selects XLD contours from the input
contours *`Contours`* according to the following features
(parameter *`Feature`*):

- ***'contour_length'*:** —

  all contours whose length is smaller
  than *`Min1`* or larger than *`Max1`*
  are not returned (*`Min2`* and
  *`Max2`* have no influence here).
- ***'maximum_extent'*:** —

  all contours whose maximum extent (as
  measured by their eight extremal
  points in row and column direction,
  according to Haralick and Shapiro:
  Computer and Robot Vision,
  Addison-Wesley 1992, chapter 3.2) is
  smaller than *`Min1`* or larger
  than *`Max1`* are not returned
  (*`Min2`* and *`Max2`* have
  no influence here).
- ***'direction'*:** —

  only contours for which the direction of
  the regression line is between
  *`Min1`* and *`Max1`* (in
  radians, counter-clockwise) are returned.
  *`Min1`* and *`Max1`* are
  mapped to the range of [0,2*PI[.
  (*`Min2`* and *`Max2`* have
  no influence here).
- ***'curvature'*:** —

  only contours for which the mean distance
  from the regression line lies between
  *`Min1`* and *`Max1`*, and
  for which the standard deviation of the
  distances is between *`Min2`* and
  *`Max2`* are returned.
- ***'closed'*:** —

  only contours for which the distance between
  their start point and their end point is less or equal
  *`Max1`* pixels are returned. (*`Min1`*,
  *`Min2`* and *`Max2`* have no influence
  here.)
- ***'open'*:** —

  only contours for which the distance between their
  start point and their end point is greater than
  *`Min1`* pixels are returned. (*`Max1`*,
  *`Min2`* and *`Max2`* have no influence
  here).

If *`Min1`* = *`Max1`* = 0 or *`Min2`* =
*`Max2`* = 0 is used for the selection according to curvature,
the respective feature has no influence on the selection.

## Attention

Before contour can be filtered by `select_contours_xld`
according to *'direction'* or *'curvature'*, the parameters of
the regression lines to the contours must be calculated with
[`regress_contours_xld`](regress_contours_xld.md). If this has not been done,
`select_contours_xld` calls [`regress_contours_xld`](regress_contours_xld.md)
internally with the parameters `Mode` = *'no'* and
`Iterations` = *1*. If a different mode should be
used, [`regress_contours_xld`](regress_contours_xld.md) must be called explicitly.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Contours`** (input_object)  xld_cont-array `→` object

Input XLD contours.

**`SelectedContours`** (output_object)  xld_cont-array `→` object

Output XLD contours.

**`Feature`** (input_control)  string `→`  (string)

Feature to select contours with.

Default:
'contour_length'

List of values:
'closed', 'contour_length', 'curvature', 'direction', 'maximum_extent', 'open'

**`Min1`** (input_control)  real `→`  (real)

Lower threshold.

Default:
0.5

**`Max1`** (input_control)  real `→`  (real)

Upper threshold.

Default:
200.0

**`Min2`** (input_control)  real `→`  (real)

Lower threshold.

Default:
-0.5

**`Max2`** (input_control)  real `→`  (real)

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
