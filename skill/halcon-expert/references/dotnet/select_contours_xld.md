# SelectContoursXld (Operator)

## Name

`SelectContoursXld` — Select XLD contours according to several features.

## Signature

`static void HOperatorSet.SelectContoursXld(HObject contours, out HObject selectedContours, HTuple feature, HTuple min1, HTuple max1, HTuple min2, HTuple max2)`

`HXLDCont HXLDCont.SelectContoursXld(string feature, double min1, double max1, double min2, double max2)`

## Description

`SelectContoursXld` selects XLD contours from the input
contours *`contours`* according to the following features
(parameter *`feature`*):

- ***"contour_length"*:** —

  all contours whose length is smaller
  than *`min1`* or larger than *`max1`*
  are not returned (*`min2`* and
  *`max2`* have no influence here).
- ***"maximum_extent"*:** —

  all contours whose maximum extent (as
  measured by their eight extremal
  points in row and column direction,
  according to Haralick and Shapiro:
  Computer and Robot Vision,
  Addison-Wesley 1992, chapter 3.2) is
  smaller than *`min1`* or larger
  than *`max1`* are not returned
  (*`min2`* and *`max2`* have
  no influence here).
- ***"direction"*:** —

  only contours for which the direction of
  the regression line is between
  *`min1`* and *`max1`* (in
  radians, counter-clockwise) are returned.
  *`min1`* and *`max1`* are
  mapped to the range of [0,2*PI[.
  (*`min2`* and *`max2`* have
  no influence here).
- ***"curvature"*:** —

  only contours for which the mean distance
  from the regression line lies between
  *`min1`* and *`max1`*, and
  for which the standard deviation of the
  distances is between *`min2`* and
  *`max2`* are returned.
- ***"closed"*:** —

  only contours for which the distance between
  their start point and their end point is less or equal
  *`max1`* pixels are returned. (*`min1`*,
  *`min2`* and *`max2`* have no influence
  here.)
- ***"open"*:** —

  only contours for which the distance between their
  start point and their end point is greater than
  *`min1`* pixels are returned. (*`max1`*,
  *`min2`* and *`max2`* have no influence
  here).

If *`min1`* = *`max1`* = 0 or *`min2`* =
*`max2`* = 0 is used for the selection according to curvature,
the respective feature has no influence on the selection.

## Attention

Before contour can be filtered by `SelectContoursXld`
according to *"direction"* or *"curvature"*, the parameters of
the regression lines to the contours must be calculated with
[`RegressContoursXld`](regress_contours_xld.md). If this has not been done,
`SelectContoursXld` calls [`RegressContoursXld`](regress_contours_xld.md)
internally with the parameters `mode` = *"no"* and
`iterations` = *1*. If a different mode should be
used, [`RegressContoursXld`](regress_contours_xld.md) must be called explicitly.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`contours`** (input_object)  xld_cont-array `→` [HXLDCont](HXLDCont.md)

Input XLD contours.

**`selectedContours`** (output_object)  xld_cont-array `→` [HXLDCont](HXLDCont.md)

Output XLD contours.

**`feature`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Feature to select contours with.

Default:
"contour_length"

List of values:
"closed", "contour_length", "curvature", "direction", "maximum_extent", "open"

**`min1`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Lower threshold.

Default:
0.5

**`max1`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Upper threshold.

Default:
200.0

**`min2`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Lower threshold.

Default:
-0.5

**`max2`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Upper threshold.

Default:
0.5

## Possible Predecessors

`RegressContoursXld`

## See also

`GetContourXld`,
`GetContourAttribXld`,
`GenContoursSkeletonXld`,
`LinesGauss`,
`LinesFacet`,
`EdgesSubPix`,
`GetRegressParamsXld`,
`GetContourGlobalAttribXld`,
`QueryContourGlobalAttribsXld`

## References

R. Haralick, L. Shapiro: “Computer and Robot Vision” Vol. 1;
Kapitel 3.2, Addison-Wesley 1992

## Module

Foundation
