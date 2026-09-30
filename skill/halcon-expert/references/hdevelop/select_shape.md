# select_shape (Operator)

## Name

`select_shape` — Choose regions with the aid of shape features.

## Signature

`select_shape(Regions : SelectedRegions : Features, Operation, Min, Max : )`

## Description

The operator `select_shape` chooses regions according to
shape. For each input region from *`Regions`* the indicated
features (*`Features`*) are calculated. If each
(*`Operation`* = *'and'*) or at least one (*`Operation`* =
*'or'*) of the calculated features is within the default limits
(*`Min`*,*`Max`*) the region is adapted into the output
(duplicated).
The parameters *`Min`* and *`Max`* can be set to
*'min'* or *'max'* in order to leave bottom and top limits,
respectively, open.

Condition: $Min_{i}\le Feature_{i}(Object)\le Max_{i}$

For an illustration of these features, please refer to the
documentation of this chapter ([Regions / Features](toc_regions_features.md)).

Possible values for *`Features`*:

- ***'area'*:** —

  Area of the object
- ***'row'*:** —

  Row index of the center
- ***'column'*:** —

  Column index of the center
- ***'width'*:** —

  Width of the region (parallel to the
  coordinate axes; see
  [`height_width_ratio`](height_width_ratio.md))
- ***'height'*:** —

  Height of the region (parallel to the
  coordinate axes; see
  [`height_width_ratio`](height_width_ratio.md))
- ***'ratio'*:** —

  Ratio of the height and width of the region
  (parallel to the coordinate axes; see
  [`height_width_ratio`](height_width_ratio.md))
- ***'row1'*:** —

  Row index of upper left corner
- ***'column1'*:** —

  Column index of upper left corner
- ***'row2'*:** —

  Row index of lower right corner
- ***'column2'*:** —

  Column index of lower right corner
- ***'circularity'*:** —

  Circularity (see [`circularity`](circularity.md))
- ***'compactness'*:** —

  Compactness (see [`compactness`](compactness.md))
- ***'contlength'*:** —

  Total length of contour
  (see operator [`contlength`](contlength.md))
- ***'convexity'*:** —

  Convexity (see [`convexity`](convexity.md))
- ***'rectangularity'*:** —

  Rectangularity (see [`rectangularity`](rectangularity.md))
- ***'ra'*:** —

  Main radius of the equivalent ellipse
  (see [`elliptic_axis`](elliptic_axis.md))
- ***'rb'*:** —

  Secondary radius of the equivalent ellipse
  (see [`elliptic_axis`](elliptic_axis.md))
- ***'phi'*:** —

  Orientation of the equivalent ellipse
  (see [`elliptic_axis`](elliptic_axis.md))
- ***'anisometry'*:** —

  Anisometry (see [`eccentricity`](eccentricity.md))
- ***'bulkiness'*:** —

  Bulkiness (see operator [`eccentricity`](eccentricity.md))
- ***'struct_factor'*:** —

  Structure Factor (see operator
  [`eccentricity`](eccentricity.md))
- ***'outer_radius'*:** —

  Radius of smallest surrounding circle
  (see [`smallest_circle`](smallest_circle.md))
- ***'inner_radius'*:** —

  Radius of largest inner circle
  (see [`inner_circle`](inner_circle.md))
- ***'inner_width'*:** —

  Width of the largest axis-parallel rectangle
  that fits into the region (see
  [`inner_rectangle1`](inner_rectangle1.md))
- ***'inner_height'*:** —

  Height of the largest axis-parallel
  rectangle that fits into the region
  (see [`inner_rectangle1`](inner_rectangle1.md))
- ***'dist_mean'*:** —

  Mean distance from the region border to the
  center (see operator [`roundness`](roundness.md))
- ***'dist_deviation'*:** —

  Deviation of the distance from the region
  border from the center
  (see operator [`roundness`](roundness.md))
- ***'roundness'*:** —

  Roundness (see operator [`roundness`](roundness.md))
- ***'num_sides'*:** —

  Number of polygon sides (see operator
  [`roundness`](roundness.md))
- ***'connect_num'*:** —

  Number of connection components
  (see operator [`connect_and_holes`](connect_and_holes.md))
- ***'holes_num'*:** —

  Number of holes
  (see operator [`connect_and_holes`](connect_and_holes.md))
- ***'area_holes'*:** —

  Area of the holes of the object
  (see operator [`area_holes`](area_holes.md))
- ***'max_diameter'*:** —

  Maximum diameter of the region
  (see operator [`diameter_region`](diameter_region.md))
- ***'orientation'*:** —

  Orientation of the region
  (see operator [`orientation_region`](orientation_region.md))
- ***'euler_number'*:** —

  Euler number (see operator
  [`euler_number`](euler_number.md))
- ***'rect2_phi'*:** —

  Orientation of the smallest
  surrounding rectangle
  (see operator [`smallest_rectangle2`](smallest_rectangle2.md))
- ***'rect2_len1'*:** —

  Half the length of the smallest surrounding
  rectangle (see operator
  [`smallest_rectangle2`](smallest_rectangle2.md))
- ***'rect2_len2'*:** —

  Half the width of the smallest surrounding
  rectangle (see operator
  [`smallest_rectangle2`](smallest_rectangle2.md))
- ***'moments_m11'*:** —

  Geometric moments of the region
  (see operator
  [`moments_region_2nd`](moments_region_2nd.md))
- ***'moments_m20'*:** —

  Geometric moments of the region
  (see operator
  [`moments_region_2nd`](moments_region_2nd.md))
- ***'moments_m02'*:** —

  Geometric moments of the region
  (see operator
  [`moments_region_2nd`](moments_region_2nd.md))
- ***'moments_ia'*:** —

  Geometric moments of the region
  (see operator
  [`moments_region_2nd`](moments_region_2nd.md))
- ***'moments_ib'*:** —

  Geometric moments of the region
  (see operator
  [`moments_region_2nd`](moments_region_2nd.md))
- ***'moments_m11_invar'*:** —

  Geometric moments of the region
  (see operator
  [`moments_region_2nd_invar`](moments_region_2nd_invar.md))
- ***'moments_m20_invar'*:** —

  Geometric moments of the region
  (see operator
  [`moments_region_2nd_invar`](moments_region_2nd_invar.md))
- ***'moments_m02_invar'*:** —

  Geometric moments of the region
  (see operator
  [`moments_region_2nd_invar`](moments_region_2nd_invar.md))
- ***'moments_phi1'*:** —

  Geometric moments of the region
  (see operator
  [`moments_region_2nd_rel_invar`](moments_region_2nd_rel_invar.md))
- ***'moments_phi2'*:** —

  Geometric moments of the region
  (see operator
  [`moments_region_2nd_rel_invar`](moments_region_2nd_rel_invar.md))
- ***'moments_m21'*:** —

  Geometric moments of the region
  (see operator
  [`moments_region_3rd`](moments_region_3rd.md))
- ***'moments_m12'*:** —

  Geometric moments of the region
  (see operator
  [`moments_region_3rd`](moments_region_3rd.md))
- ***'moments_m03'*:** —

  Geometric moments of the region
  (see operator
  [`moments_region_3rd`](moments_region_3rd.md))
- ***'moments_m30'*:** —

  Geometric moments of the region
  (see operator
  [`moments_region_3rd`](moments_region_3rd.md))
- ***'moments_m21_invar'*:** —

  Geometric moments of the region
  (see operator
  [`moments_region_3rd_invar`](moments_region_3rd_invar.md))
- ***'moments_m12_invar'*:** —

  Geometric moments of the region
  (see operator
  [`moments_region_3rd_invar`](moments_region_3rd_invar.md))
- ***'moments_m03_invar'*:** —

  Geometric moments of the region
  (see operator
  [`moments_region_3rd_invar`](moments_region_3rd_invar.md))
- ***'moments_m30_invar'*:** —

  Geometric moments of the region
  (see operator
  [`moments_region_3rd_invar`](moments_region_3rd_invar.md))
- ***'moments_i1'*:** —

  Geometric moments of the region
  (see operator
  [`moments_region_central`](moments_region_central.md))
- ***'moments_i2'*:** —

  Geometric moments of the region
  (see operator
  [`moments_region_central`](moments_region_central.md))
- ***'moments_i3'*:** —

  Geometric moments of the region
  (see operator
  [`moments_region_central`](moments_region_central.md))
- ***'moments_i4'*:** —

  Geometric moments of the region
  (see operator
  [`moments_region_central`](moments_region_central.md))
- ***'moments_psi1'*:** —

  Geometric moments of the region
  (see operator
  [`moments_region_central_invar`](moments_region_central_invar.md))
- ***'moments_psi2'*:** —

  Geometric moments of the region
  (see operator
  [`moments_region_central_invar`](moments_region_central_invar.md))
- ***'moments_psi3'*:** —

  Geometric moments of the region
  (see operator
  [`moments_region_central_invar`](moments_region_central_invar.md))
- ***'moments_psi4'*:** —

  Geometric moments of the region
  (see operator
  [`moments_region_central_invar`](moments_region_central_invar.md))

If only one feature (*`Features`*) is used the value of
*`Operation`* is meaningless. Several features are processed in
the sequence in which they are entered.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`Regions`** (input_object)  region-array `→` object

Regions to be examined.

**`SelectedRegions`** (output_object)  region-array `→` object

Regions fulfilling the condition.

**`Features`** (input_control)  string(-array) `→`  (string)

Shape features to be checked.

Default:
'area'

List of values:
'anisometry', 'area', 'area_holes', 'bulkiness', 'circularity', 'column', 'column1', 'column2', 'compactness', 'connect_num', 'contlength', 'convexity', 'dist_deviation', 'dist_mean', 'euler_number', 'height', 'holes_num', 'inner_height', 'inner_radius', 'inner_width', 'max_diameter', 'moments_i1', 'moments_i2', 'moments_i3', 'moments_i4', 'moments_ia', 'moments_ib', 'moments_m02', 'moments_m02_invar', 'moments_m03', 'moments_m03_invar', 'moments_m11', 'moments_m11_invar', 'moments_m12', 'moments_m12_invar', 'moments_m20', 'moments_m20_invar', 'moments_m21', 'moments_m21_invar', 'moments_m30', 'moments_m30_invar', 'moments_phi1', 'moments_phi2', 'moments_psi1', 'moments_psi2', 'moments_psi3', 'moments_psi4', 'num_sides', 'orientation', 'outer_radius', 'phi', 'ra', 'ratio', 'rb', 'rect2_len1', 'rect2_len2', 'rect2_phi', 'rectangularity', 'roundness', 'row', 'row1', 'row2', 'struct_factor', 'width'

**`Operation`** (input_control)  string `→`  (string)

Linkage type of the individual features.

Default:
'and'

List of values:
'and', 'or'

**`Min`** (input_control)  real(-array) `→`  (real / integer / string)

Lower limits of the features or 'min'.

Default:
150.0

Value range:
`0.0
≤
Min
≤
99999.0`

Minimum increment:
0.001

Recommended increment:
1.0

**`Max`** (input_control)  real(-array) `→`  (real / integer / string)

Upper limits of the features or 'max'.

Default:
99999.0

Value range:
`0.0
≤
Max
≤
99999.0`

Minimum increment:
0.001

Recommended increment:
1.0

Restriction:
`Max >= Min`

## Example (HDevelop)

```
* Where are the eyes of the Mandrill?
read_image(Image,'monkey')
threshold(Image,Region,128,255)
connection(Region,ConnectedRegions)
select_shape(ConnectedRegions,Eyes,['area','max_diameter'],\
             'and',[500,30.0],[1000,50.0])
dev_display(Eyes)
```

## Result

The operator `select_shape` returns the value 2 (
H_MSG_TRUE)
if the
input is not empty. The behavior in case of empty input (no input
objects available) is set via the operator
`set_system('no_object_result',<Result>)`. The behavior in
case of empty region (the region is the empty set) is set via
`set_system('empty_region_result',<Result>)`. If necessary an
exception is raised.

## Possible Predecessors

`threshold`,
`regiongrowing`,
`connection`,
`runlength_features`

## Possible Successors

`select_gray`,
`shape_trans`,
`reduce_domain`,
`count_obj`

## Alternatives

`select_shape_std`

## See also

`area_center`,
`circularity`,
`compactness`,
`contlength`,
`convexity`,
`rectangularity`,
`elliptic_axis`,
`eccentricity`,
`inner_circle`,
`smallest_circle`,
`smallest_rectangle1`,
`smallest_rectangle2`,
`inner_rectangle1`,
`roundness`,
`connect_and_holes`,
`area_holes`,
`diameter_region`,
`orientation_region`,
`moments_region_2nd`,
`moments_region_2nd_invar`,
`moments_region_2nd_rel_invar`,
`moments_region_3rd`,
`moments_region_3rd_invar`,
`moments_region_central`,
`moments_region_central_invar`,
`select_obj`

## Module

Foundation
