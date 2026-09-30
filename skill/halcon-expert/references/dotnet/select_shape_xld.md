# SelectShapeXld (Operator)

## Name

`SelectShapeXld` — Select contours or polygons using shape features.

## Signature

`static void HOperatorSet.SelectShapeXld(HObject XLD, out HObject selectedXLD, HTuple features, HTuple operation, HTuple min, HTuple max)`

`HXLD HXLD.SelectShapeXld(HTuple features, string operation, HTuple min, HTuple max)`

`HXLD HXLD.SelectShapeXld(string features, string operation, double min, double max)`

`HXLDCont HXLDCont.SelectShapeXld(HTuple features, string operation, HTuple min, HTuple max)`

`HXLDCont HXLDCont.SelectShapeXld(string features, string operation, double min, double max)`

`HXLDPoly HXLDPoly.SelectShapeXld(HTuple features, string operation, HTuple min, HTuple max)`

`HXLDPoly HXLDPoly.SelectShapeXld(string features, string operation, double min, double max)`

`HXLDPara HXLDPara.SelectShapeXld(HTuple features, string operation, HTuple min, HTuple max)`

`HXLDPara HXLDPara.SelectShapeXld(string features, string operation, double min, double max)`

`HXLDModPara HXLDModPara.SelectShapeXld(HTuple features, string operation, HTuple min, HTuple max)`

`HXLDModPara HXLDModPara.SelectShapeXld(string features, string operation, double min, double max)`

`HXLDExtPara HXLDExtPara.SelectShapeXld(HTuple features, string operation, HTuple min, HTuple max)`

`HXLDExtPara HXLDExtPara.SelectShapeXld(string features, string operation, double min, double max)`

## Description

The operator `SelectShapeXld` selects contours or polygons
according to their shape. For each input contour or polygon in
*`XLD`* the indicated features (*`features`*) are
calculated. If each (*`operation`* = *"and"*) or at least one
(*`operation`* = *"or"*) of the calculated features is within the
limits (*`min`*,*`max`*) the contour respectively polygon
is copied into the output.
The parameters *`min`* and *`max`* can be set to
*"min"* or *"max"* in order to leave bottom and top limits,
respectively, open.

Condition:
$$\texttt{Min}_{i}\le\texttt{Features}_{i}(Object)\le\texttt{Max}_{i}$$

Possible values for *`features`*:

(all features can be used with polygons as well)

- **'area':** —

  Area of the contour
  (see [`AreaCenterXld`](area_center_xld.md))
- **'area_points':** —

  Area of the contour points
  (see [`AreaCenterPointsXld`](area_center_points_xld.md))
- **'row':** —

  Row index of the center of gravity
  (see [`AreaCenterXld`](area_center_xld.md))
- **'column':** —

  Column index of the center of gravity
  (see [`AreaCenterXld`](area_center_xld.md))
- **'row_points':** —

  Row index of the center of gravity of the contour
  points (see [`AreaCenterPointsXld`](area_center_points_xld.md))
- **'column_points':** —

  Column index of the center of gravity of the contour
  points (see [`AreaCenterPointsXld`](area_center_points_xld.md))
- **'width':** —

  Width of the contour (see
  [`HeightWidthRatioXld`](height_width_ratio_xld.md))
- **'height':** —

  Height of the contour (see
  [`HeightWidthRatioXld`](height_width_ratio_xld.md))
- **'ratio':** —

  Ratio of the height and the width of the
  contour (see [`HeightWidthRatioXld`](height_width_ratio_xld.md))
- **'row1':** —

  Row coordinate of upper left corner
  (see [`SmallestRectangle1Xld`](smallest_rectangle1_xld.md))
- **'column1':** —

  Column coordinate of upper left corner
  (see [`SmallestRectangle1Xld`](smallest_rectangle1_xld.md))
- **'row2':** —

  Row coordinate of lower right corner
  (see [`SmallestRectangle1Xld`](smallest_rectangle1_xld.md))
- **'column2':** —

  Column coordinate of lower right corner
  (see [`SmallestRectangle1Xld`](smallest_rectangle1_xld.md))
- **'circularity':** —

  Circularity (see [`CircularityXld`](circularity_xld.md))
- **'compactness':** —

  Compactness (see [`CompactnessXld`](compactness_xld.md))
- **'rectangularity':** —

  Rectangularity (see [`RectangularityXld`](rectangularity_xld.md))
- **'contlength':** —

  Total length of contour
  (see [`LengthXld`](length_xld.md))
- **'convexity':** —

  Convexity (see [`ConvexityXld`](convexity_xld.md))
- **'ra':** —

  Major radius of the equivalent ellipse
  (see [`EllipticAxisXld`](elliptic_axis_xld.md))
- **'rb':** —

  Minor radius of the equivalent ellipse
  (see [`EllipticAxisXld`](elliptic_axis_xld.md))
- **'phi':** —

  Orientation of the equivalent ellipse
  (see [`EllipticAxisXld`](elliptic_axis_xld.md))
- **'ra_points':** —

  Major radius of the equivalent ellipse of the
  contour points (see [`EllipticAxisPointsXld`](elliptic_axis_points_xld.md))
- **'rb_points':** —

  Minor radius of the equivalent ellipse of the
  contour points (see [`EllipticAxisPointsXld`](elliptic_axis_points_xld.md))
- **'phi_points':** —

  Orientation of the equivalent ellipse of the
  contour points (see [`EllipticAxisPointsXld`](elliptic_axis_points_xld.md))
- **'anisometry:'** —

  Anisometry (see [`EccentricityXld`](eccentricity_xld.md))
- **'anisometry_points:'** —

  Anisometry of the contour points
  (see [`EccentricityPointsXld`](eccentricity_points_xld.md))
- **'bulkiness:'** —

  Bulkiness (see [`EccentricityXld`](eccentricity_xld.md))
- **'struct_factor:'** —

  Structure factor
  (see [`EccentricityXld`](eccentricity_xld.md))
- **'outer_radius':** —

  Radius of smallest enclosing circle
  (see [`SmallestCircleXld`](smallest_circle_xld.md))
- **'max_diameter':** —

  Maximum diameter of the contour
  (see [`DiameterXld`](diameter_xld.md))
- **'orientation':** —

  Orientation of the contour
  (see [`OrientationXld`](orientation_xld.md))
- **'orientation_points':** —

  Orientation of the contour points
  (see [`OrientationPointsXld`](orientation_points_xld.md))
- **'rect2_phi':** —

  Orientation of the smallest surrounding rectangle
  (see [`SmallestRectangle2Xld`](smallest_rectangle2_xld.md))
- **'rect2_len1':** —

  Half the length of the smallest surrounding
  rectangle
  (see [`SmallestRectangle2Xld`](smallest_rectangle2_xld.md))
- **'rect2_len2':** —

  Half the width of the smallest surrounding
  rectangle
  (see [`SmallestRectangle2Xld`](smallest_rectangle2_xld.md))
- **'moments_m11', 'moments_m20', 'moments_m02':** —

  Geometric moments of the contour
  (see [`MomentsRegion2nd`](moments_region_2nd.md))
- **'moments_m11_points', 'moments_m20_points', 'moments_m02_points':** —

  Geometric moments of the contour points
  (see [`MomentsPointsXld`](moments_points_xld.md))

If only one feature (*`features`*) is used the value of
*`operation`* is meaningless. Several features are processed in
the sequence in which they are entered.The use of some features
requires that the input contour respectively polygon must not
intersect itself, otherwise the results are not meaningful (Whether
the input contour or polygon intersects itself or not can be
determined with [`TestSelfIntersectionXld`](test_self_intersection_xld.md)).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`XLD`** (input_object)  xld-array `→` [HXLD](HXLD.md)

Contours or polygons to be examined.

**`selectedXLD`** (output_object)  xld-array `→` [HXLD](HXLD.md)

Contours or polygons fulfilling the condition(s).

**`features`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Shape features to be checked.

Default:
"area"

List of values:
"anisometry", "anisometry_points", "area", "area_points", "bulkiness", "circularity", "column", "column1", "column2", "column_points", "compactness", "contlength", "convexity", "height", "max_diameter", "moments_m02", "moments_m02_points", "moments_m11", "moments_m11_points", "moments_m20", "moments_m20_points", "orientation", "orientation_points", "outer_radius", "phi", "phi_points", "ra", "ra_points", "ratio", "rb", "rb_points", "rect2_len1", "rect2_len2", "rect2_phi", "rectangularity", "row", "row1", "row2", "row_points", "struct_factor", "width"

**`operation`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Operation type between the individual features.

Default:
"and"

List of values:
"and", "or"

**`min`** (input_control)  real(-array) `→` [HTuple](HTuple.md) (*double* / int / long / string)

Lower limits of the features or 'min'.

Default:
150.0

Minimum increment:
0.001

Recommended increment:
1.0

**`max`** (input_control)  real(-array) `→` [HTuple](HTuple.md) (*double* / int / long / string)

Upper limits of the features or 'max'.

Default:
99999.0

Minimum increment:
0.001

Recommended increment:
1.0

Restriction:
`Max >= Min`

## Result

The operator `SelectShapeXld` returns the value 2 (
H_MSG_TRUE)
if the
input is not empty. The behavior in case of empty input (no input
objects available) is set via the operator
`set_system('no_object_result',<Result>)`. If necessary an
exception is raised.

## Possible Predecessors

`GenContoursSkeletonXld`,
`EdgesSubPix`,
`ThresholdSubPix`,
`GenContourPolygonXld`,
`TestSelfIntersectionXld`

## Possible Successors

`ShapeTransXld`,
`CountObj`

## See also

`AreaCenterXld`,
`AreaCenterPointsXld`,
`CircularityXld`,
`CompactnessXld`,
`ConvexityXld`,
`EllipticAxisXld`,
`EllipticAxisPointsXld`,
`EccentricityXld`,
`EccentricityPointsXld`,
`RectangularityXld`,
`SmallestCircleXld`,
`SmallestRectangle1Xld`,
`SmallestRectangle2Xld`,
`DiameterXld`,
`OrientationXld`,
`OrientationPointsXld`,
`MomentsXld`,
`MomentsPointsXld`,
`SelectObj`

## Module

Foundation
