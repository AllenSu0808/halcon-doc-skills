# select_shape_xld (Operator)

## Name

`select_shape_xld` — Select contours or polygons using shape features.

## Signature

`select_shape_xld(XLD : SelectedXLD : Features, Operation, Min, Max : )`

## Description

The operator `select_shape_xld` selects contours or polygons
according to their shape. For each input contour or polygon in
*`XLD`* the indicated features (*`Features`*) are
calculated. If each (*`Operation`* = *'and'*) or at least one
(*`Operation`* = *'or'*) of the calculated features is within the
limits (*`Min`*,*`Max`*) the contour respectively polygon
is copied into the output.
The parameters *`Min`* and *`Max`* can be set to
*'min'* or *'max'* in order to leave bottom and top limits,
respectively, open.

Condition:
$$\texttt{Min}_{i}\le\texttt{Features}_{i}(Object)\le\texttt{Max}_{i}$$

Possible values for *`Features`*:

(all features can be used with polygons as well)

- **'area':** —

  Area of the contour
  (see [`area_center_xld`](area_center_xld.md))
- **'area_points':** —

  Area of the contour points
  (see [`area_center_points_xld`](area_center_points_xld.md))
- **'row':** —

  Row index of the center of gravity
  (see [`area_center_xld`](area_center_xld.md))
- **'column':** —

  Column index of the center of gravity
  (see [`area_center_xld`](area_center_xld.md))
- **'row_points':** —

  Row index of the center of gravity of the contour
  points (see [`area_center_points_xld`](area_center_points_xld.md))
- **'column_points':** —

  Column index of the center of gravity of the contour
  points (see [`area_center_points_xld`](area_center_points_xld.md))
- **'width':** —

  Width of the contour (see
  [`height_width_ratio_xld`](height_width_ratio_xld.md))
- **'height':** —

  Height of the contour (see
  [`height_width_ratio_xld`](height_width_ratio_xld.md))
- **'ratio':** —

  Ratio of the height and the width of the
  contour (see [`height_width_ratio_xld`](height_width_ratio_xld.md))
- **'row1':** —

  Row coordinate of upper left corner
  (see [`smallest_rectangle1_xld`](smallest_rectangle1_xld.md))
- **'column1':** —

  Column coordinate of upper left corner
  (see [`smallest_rectangle1_xld`](smallest_rectangle1_xld.md))
- **'row2':** —

  Row coordinate of lower right corner
  (see [`smallest_rectangle1_xld`](smallest_rectangle1_xld.md))
- **'column2':** —

  Column coordinate of lower right corner
  (see [`smallest_rectangle1_xld`](smallest_rectangle1_xld.md))
- **'circularity':** —

  Circularity (see [`circularity_xld`](circularity_xld.md))
- **'compactness':** —

  Compactness (see [`compactness_xld`](compactness_xld.md))
- **'rectangularity':** —

  Rectangularity (see [`rectangularity_xld`](rectangularity_xld.md))
- **'contlength':** —

  Total length of contour
  (see [`length_xld`](length_xld.md))
- **'convexity':** —

  Convexity (see [`convexity_xld`](convexity_xld.md))
- **'ra':** —

  Major radius of the equivalent ellipse
  (see [`elliptic_axis_xld`](elliptic_axis_xld.md))
- **'rb':** —

  Minor radius of the equivalent ellipse
  (see [`elliptic_axis_xld`](elliptic_axis_xld.md))
- **'phi':** —

  Orientation of the equivalent ellipse
  (see [`elliptic_axis_xld`](elliptic_axis_xld.md))
- **'ra_points':** —

  Major radius of the equivalent ellipse of the
  contour points (see [`elliptic_axis_points_xld`](elliptic_axis_points_xld.md))
- **'rb_points':** —

  Minor radius of the equivalent ellipse of the
  contour points (see [`elliptic_axis_points_xld`](elliptic_axis_points_xld.md))
- **'phi_points':** —

  Orientation of the equivalent ellipse of the
  contour points (see [`elliptic_axis_points_xld`](elliptic_axis_points_xld.md))
- **'anisometry:'** —

  Anisometry (see [`eccentricity_xld`](eccentricity_xld.md))
- **'anisometry_points:'** —

  Anisometry of the contour points
  (see [`eccentricity_points_xld`](eccentricity_points_xld.md))
- **'bulkiness:'** —

  Bulkiness (see [`eccentricity_xld`](eccentricity_xld.md))
- **'struct_factor:'** —

  Structure factor
  (see [`eccentricity_xld`](eccentricity_xld.md))
- **'outer_radius':** —

  Radius of smallest enclosing circle
  (see [`smallest_circle_xld`](smallest_circle_xld.md))
- **'max_diameter':** —

  Maximum diameter of the contour
  (see [`diameter_xld`](diameter_xld.md))
- **'orientation':** —

  Orientation of the contour
  (see [`orientation_xld`](orientation_xld.md))
- **'orientation_points':** —

  Orientation of the contour points
  (see [`orientation_points_xld`](orientation_points_xld.md))
- **'rect2_phi':** —

  Orientation of the smallest surrounding rectangle
  (see [`smallest_rectangle2_xld`](smallest_rectangle2_xld.md))
- **'rect2_len1':** —

  Half the length of the smallest surrounding
  rectangle
  (see [`smallest_rectangle2_xld`](smallest_rectangle2_xld.md))
- **'rect2_len2':** —

  Half the width of the smallest surrounding
  rectangle
  (see [`smallest_rectangle2_xld`](smallest_rectangle2_xld.md))
- **'moments_m11', 'moments_m20', 'moments_m02':** —

  Geometric moments of the contour
  (see [`moments_region_2nd`](moments_region_2nd.md))
- **'moments_m11_points', 'moments_m20_points', 'moments_m02_points':** —

  Geometric moments of the contour points
  (see [`moments_points_xld`](moments_points_xld.md))

If only one feature (*`Features`*) is used the value of
*`Operation`* is meaningless. Several features are processed in
the sequence in which they are entered.The use of some features
requires that the input contour respectively polygon must not
intersect itself, otherwise the results are not meaningful (Whether
the input contour or polygon intersects itself or not can be
determined with [`test_self_intersection_xld`](test_self_intersection_xld.md)).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`XLD`** (input_object)  xld-array `→` object

Contours or polygons to be examined.

**`SelectedXLD`** (output_object)  xld-array `→` object

Contours or polygons fulfilling the condition(s).

**`Features`** (input_control)  string(-array) `→`  (string)

Shape features to be checked.

Default:
'area'

List of values:
'anisometry', 'anisometry_points', 'area', 'area_points', 'bulkiness', 'circularity', 'column', 'column1', 'column2', 'column_points', 'compactness', 'contlength', 'convexity', 'height', 'max_diameter', 'moments_m02', 'moments_m02_points', 'moments_m11', 'moments_m11_points', 'moments_m20', 'moments_m20_points', 'orientation', 'orientation_points', 'outer_radius', 'phi', 'phi_points', 'ra', 'ra_points', 'ratio', 'rb', 'rb_points', 'rect2_len1', 'rect2_len2', 'rect2_phi', 'rectangularity', 'row', 'row1', 'row2', 'row_points', 'struct_factor', 'width'

**`Operation`** (input_control)  string `→`  (string)

Operation type between the individual features.

Default:
'and'

List of values:
'and', 'or'

**`Min`** (input_control)  real(-array) `→`  (real / integer / string)

Lower limits of the features or 'min'.

Default:
150.0

Minimum increment:
0.001

Recommended increment:
1.0

**`Max`** (input_control)  real(-array) `→`  (real / integer / string)

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

The operator `select_shape_xld` returns the value 2 (
H_MSG_TRUE)
if the
input is not empty. The behavior in case of empty input (no input
objects available) is set via the operator
`set_system('no_object_result',<Result>)`. If necessary an
exception is raised.

## Possible Predecessors

`gen_contours_skeleton_xld`,
`edges_sub_pix`,
`threshold_sub_pix`,
`gen_contour_polygon_xld`,
`test_self_intersection_xld`

## Possible Successors

`shape_trans_xld`,
`count_obj`

## See also

`area_center_xld`,
`area_center_points_xld`,
`circularity_xld`,
`compactness_xld`,
`convexity_xld`,
`elliptic_axis_xld`,
`elliptic_axis_points_xld`,
`eccentricity_xld`,
`eccentricity_points_xld`,
`rectangularity_xld`,
`smallest_circle_xld`,
`smallest_rectangle1_xld`,
`smallest_rectangle2_xld`,
`diameter_xld`,
`orientation_xld`,
`orientation_points_xld`,
`moments_xld`,
`moments_points_xld`,
`select_obj`

## Module

Foundation
