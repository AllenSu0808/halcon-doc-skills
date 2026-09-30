# RegionFeatures (Operator)

## Name

`RegionFeatures` — Calculate shape features of regions.

## Signature

`static void HOperatorSet.RegionFeatures(HObject regions, HTuple features, out HTuple value)`

`HTuple HRegion.RegionFeatures(HTuple features)`

`double HRegion.RegionFeatures(string features)`

## Description

The operator `RegionFeatures` calculates for each input
region from *`regions`* the indicated features
(*`features`*).

For an illustration of these features, please refer to the
documentation of this chapter ([Regions / Features](toc_regions_features.md)).

Possible values for *`features`*:

- ***"area"*:** —

  Area of the object
- ***"row"*:** —

  Row index of the center
- ***"column"*:** —

  Column index of the center
- ***"row1"*:** —

  Row index of upper left corner
- ***"column1"*:** —

  Column index of upper left corner
- ***"row2"*:** —

  Row index of lower right corner
- ***"column2"*:** —

  Column index of lower right corner
- ***"width"*:** —

  Width of the region (parallel to the
  coordinate axes)
- ***"height"*:** —

  Height of the region (parallel to the
  coordinate axes)
- ***"ratio"*:** —

  Ratio of the height and the width of the
  region (parallel to the coordinate axes)
- ***"circularity"*:** —

  Circularity (see [`Circularity`](circularity.md))
- ***"compactness"*:** —

  Compactness (see [`Compactness`](compactness.md))
- ***"contlength"*:** —

  Total length of contour (see operator
  [`Contlength`](contlength.md))
- ***"convexity"*:** —

  Convexity (see [`Convexity`](convexity.md))
- ***"rectangularity"*:** —

  Rectangularity (see [`Rectangularity`](rectangularity.md))
- ***"ra"*:** —

  Main radius of the equivalent ellipse
  (see [`EllipticAxis`](elliptic_axis.md))
- ***"rb"*:** —

  Secondary radius of the equivalent ellipse
  (see [`EllipticAxis`](elliptic_axis.md))
- ***"phi"*:** —

  Orientation of the equivalent ellipse
  (see [`EllipticAxis`](elliptic_axis.md))
- ***"anisometry"*:** —

  Anisometry (see [`Eccentricity`](eccentricity.md))
- ***"bulkiness"*:** —

  Bulkiness (see operator [`Eccentricity`](eccentricity.md))
- ***"struct_factor"*:** —

  Structure Factor (see operator [`Eccentricity`](eccentricity.md))
- ***"outer_radius"*:** —

  Radius of smallest surrounding circle
  (see [`SmallestCircle`](smallest_circle.md))
- ***"inner_radius"*:** —

  Radius of largest inner circle
  (see [`InnerCircle`](inner_circle.md))
- ***"inner_width"*:** —

  Width of the largest axis-parallel rectangle that
  fits into the region (see [`InnerRectangle1`](inner_rectangle1.md))
- ***"inner_height"*:** —

  Height of the largest axis-parallel rectangle that
  fits into the region (see [`InnerRectangle1`](inner_rectangle1.md))
- ***"dist_mean"*:** —

  Mean distance from the region border to the
  center (see operator [`Roundness`](roundness.md))
- ***"dist_deviation"*:** —

  Deviation of the distance from the region border
  to the center (see operator [`Roundness`](roundness.md))
- ***"roundness"*:** —

  Roundness (see operator [`Roundness`](roundness.md))
- ***"num_sides"*:** —

  Number of polygon sides (see operator
  [`Roundness`](roundness.md))
- ***"connect_num"*:** —

  Number of connection components
  (see operator [`ConnectAndHoles`](connect_and_holes.md))
- ***"holes_num"*:** —

  Number of holes
  (see operator [`ConnectAndHoles`](connect_and_holes.md))
- ***"area_holes"*:** —

  Area of the holes of the object
  (see operator [`AreaHoles`](area_holes.md))
- ***"max_diameter"*:** —

  Maximum diameter of the region
  (see operator [`DiameterRegion`](diameter_region.md))
- ***"orientation"*:** —

  Orientation of the region
  (see operator [`OrientationRegion`](orientation_region.md))
- ***"euler_number"*:** —

  Euler number (see operator [`EulerNumber`](euler_number.md))
- ***"rect2_phi"*:** —

  Orientation of the smallest surrounding rectangle
  (see operator [`SmallestRectangle2`](smallest_rectangle2.md))
- ***"rect2_len1"*:** —

  Half the length of the smallest surrounding
  rectangle (see operator [`SmallestRectangle2`](smallest_rectangle2.md))
- ***"rect2_len2"*:** —

  Half the width of the smallest surrounding
  rectangle (see operator [`SmallestRectangle2`](smallest_rectangle2.md))
- ***"moments_m11"*:** —

  Geometric moments of the region
  (see operator [`MomentsRegion2nd`](moments_region_2nd.md))
- ***"moments_m20"*:** —

  Geometric moments of the region
  (see operator [`MomentsRegion2nd`](moments_region_2nd.md))
- ***"moments_m02"*:** —

  Geometric moments of the region
  (see operator [`MomentsRegion2nd`](moments_region_2nd.md))
- ***"moments_ia"*:** —

  Geometric moments of the region
  (see operator [`MomentsRegion2nd`](moments_region_2nd.md))
- ***"moments_ib"*:** —

  Geometric moments of the region
  (see operator [`MomentsRegion2nd`](moments_region_2nd.md))
- ***"moments_m11_invar"*:** —

  Geometric moments of the region
  (see operator [`MomentsRegion2ndInvar`](moments_region_2nd_invar.md))
- ***"moments_m20_invar"*:** —

  Geometric moments of the region
  (see operator [`MomentsRegion2ndInvar`](moments_region_2nd_invar.md))
- ***"moments_m02_invar"*:** —

  Geometric moments of the region
  (see operator [`MomentsRegion2ndInvar`](moments_region_2nd_invar.md))
- ***"moments_phi1"*:** —

  Geometric moments of the region
  (see operator [`MomentsRegion2ndRelInvar`](moments_region_2nd_rel_invar.md))
- ***"moments_phi2"*:** —

  Geometric moments of the region
  (see operator [`MomentsRegion2ndRelInvar`](moments_region_2nd_rel_invar.md))
- ***"moments_m21"*:** —

  Geometric moments of the region
  (see operator [`MomentsRegion3rd`](moments_region_3rd.md))
- ***"moments_m12"*:** —

  Geometric moments of the region
  (see operator [`MomentsRegion3rd`](moments_region_3rd.md))
- ***"moments_m03"*:** —

  Geometric moments of the region
  (see operator [`MomentsRegion3rd`](moments_region_3rd.md))
- ***"moments_m30"*:** —

  Geometric moments of the region
  (see operator [`MomentsRegion3rd`](moments_region_3rd.md))
- ***"moments_m21_invar"*:** —

  Geometric moments of the region
  (see operator [`MomentsRegion3rdInvar`](moments_region_3rd_invar.md))
- ***"moments_m12_invar"*:** —

  Geometric moments of the region
  (see operator [`MomentsRegion3rdInvar`](moments_region_3rd_invar.md))
- ***"moments_m03_invar"*:** —

  Geometric moments of the region
  (see operator [`MomentsRegion3rdInvar`](moments_region_3rd_invar.md))
- ***"moments_m30_invar"*:** —

  Geometric moments of the region
  (see operator [`MomentsRegion3rdInvar`](moments_region_3rd_invar.md))
- ***"moments_i1"*:** —

  Geometric moments of the region
  (see operator [`MomentsRegionCentral`](moments_region_central.md))
- ***"moments_i2"*:** —

  Geometric moments of the region
  (see operator [`MomentsRegionCentral`](moments_region_central.md))
- ***"moments_i3"*:** —

  Geometric moments of the region
  (see operator [`MomentsRegionCentral`](moments_region_central.md))
- ***"moments_i4"*:** —

  Geometric moments of the region
  (see operator [`MomentsRegionCentral`](moments_region_central.md))
- ***"moments_psi1"*:** —

  Geometric moments of the region
  (see operator [`MomentsRegionCentralInvar`](moments_region_central_invar.md))
- ***"moments_psi2"*:** —

  Geometric moments of the region
  (see operator [`MomentsRegionCentralInvar`](moments_region_central_invar.md))
- ***"moments_psi3"*:** —

  Geometric moments of the region
  (see operator [`MomentsRegionCentralInvar`](moments_region_central_invar.md))
- ***"moments_psi4"*:** —

  Geometric moments of the region
  (see operator [`MomentsRegionCentralInvar`](moments_region_central_invar.md))

Several features are processed in the sequence in which they are entered.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`regions`** (input_object)  region-array `→` [HRegion](HRegion.md)

Regions to be examined.

**`features`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Shape features to be calculated.

Default:
"area"

List of values:
"anisometry", "area", "area_holes", "bulkiness", "circularity", "column", "column1", "column2", "compactness", "connect_num", "contlength", "convexity", "dist_deviation", "dist_mean", "euler_number", "height", "holes_num", "inner_height", "inner_radius", "inner_width", "max_diameter", "moments_i1", "moments_i2", "moments_i3", "moments_i4", "moments_ia", "moments_ib", "moments_m02", "moments_m02_invar", "moments_m03", "moments_m03_invar", "moments_m11", "moments_m11_invar", "moments_m12", "moments_m12_invar", "moments_m20", "moments_m20_invar", "moments_m21", "moments_m21_invar", "moments_m30", "moments_m30_invar", "moments_phi1", "moments_phi2", "moments_psi1", "moments_psi2", "moments_psi3", "moments_psi4", "num_sides", "orientation", "outer_radius", "phi", "ra", "ratio", "rb", "rect2_len1", "rect2_len2", "rect2_phi", "rectangularity", "roundness", "row", "row1", "row2", "struct_factor", "width"

**`value`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

The calculated features.

## Example (HDevelop)

```
read_image(Image,'monkey')
threshold(Image,S1,160,255)
connection(S1,S2)
region_features(S2,['area','anisometry'],Value)
```

## Result

The operator `RegionFeatures` returns the value 2 (
H_MSG_TRUE)
if the input is not empty. If necessary an exception is raised.

## Possible Predecessors

`Threshold`,
`Regiongrowing`,
`Connection`,
`RunlengthFeatures`

## Possible Successors

`SelectShape`,
`SelectGray`,
`ShapeTrans`,
`ReduceDomain`,
`CountObj`

## See also

`AreaCenter`,
`Circularity`,
`Compactness`,
`Contlength`,
`Convexity`,
`Rectangularity`,
`EllipticAxis`,
`Eccentricity`,
`InnerCircle`,
`SmallestCircle`,
`SmallestRectangle1`,
`SmallestRectangle2`,
`InnerRectangle1`,
`Roundness`,
`ConnectAndHoles`,
`AreaHoles`,
`DiameterRegion`,
`OrientationRegion`,
`MomentsRegion2nd`,
`MomentsRegion2ndInvar`,
`MomentsRegion2ndRelInvar`,
`MomentsRegion3rd`,
`MomentsRegion3rdInvar`,
`MomentsRegionCentral`,
`MomentsRegionCentralInvar`,
`SelectObj`,
`SelectShape`

## Module

Foundation
