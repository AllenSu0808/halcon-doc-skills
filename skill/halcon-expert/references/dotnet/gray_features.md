# GrayFeatures (Operator)

## Name

`GrayFeatures` — Calculates gray value features for a set of regions.

## Signature

`static void HOperatorSet.GrayFeatures(HObject regions, HObject image, HTuple features, out HTuple value)`

`HTuple HRegion.GrayFeatures(HImage image, HTuple features)`

`double HRegion.GrayFeatures(HImage image, string features)`

## Description

`GrayFeatures` has a set of regions
(*`regions`*) as input. For each of these regions the
features (*`features`*) are calculated and returned in *`value`*.

Possible values for *`features`*:

- *"area"*: Gray value volume of region
  (see [`AreaCenterGray`](area_center_gray.md))
- *"row"*: Row index of the center of gravity
  (see [`AreaCenterGray`](area_center_gray.md))
- *"column"*: Column index of the center of gravity
  (see [`AreaCenterGray`](area_center_gray.md))
- *"ra"*: Major axis of equivalent ellipse
  (see [`EllipticAxisGray`](elliptic_axis_gray.md))
- *"rb"*: Minor axis of equivalent ellipse
  (see [`EllipticAxisGray`](elliptic_axis_gray.md))
- *"phi"*: Orientation of equivalent ellipse
  (see [`EllipticAxisGray`](elliptic_axis_gray.md))
- *"min"*: Minimum gray value
  (see [`MinMaxGray`](min_max_gray.md))
- *"max"*: Maximum gray value
  (see [`MinMaxGray`](min_max_gray.md))
- *"median"*: Median gray value
  (see [`MinMaxGray`](min_max_gray.md), with `percent`=*50*)
- *"mean"*:Mean gray value (see [`Intensity`](intensity.md))
- *"deviation"*: Deviation of gray values
  (see [`Intensity`](intensity.md))
- *"plane_deviation"*: Deviation from the approximating plane
  (see [`PlaneDeviation`](plane_deviation.md))
- *"anisotropy"*: Anisotropy
  (see [`EntropyGray`](entropy_gray.md))
- *"entropy"*: Entropy
  (see [`EntropyGray`](entropy_gray.md))
- *"fuzzy_entropy"*: Fuzzy entropy of region
  (see [`FuzzyEntropy`](fuzzy_entropy.md), with a fuzzy function from
  `apar`=*0* to `cpar`=*255*)
- *"fuzzy_perimeter"*: Fuzzy perimeter of region
  (see [`FuzzyPerimeter`](fuzzy_perimeter.md), with a fuzzy function from
  `apar`=*0* to `cpar`=*255*)
- *"moments_row"*: Mixed moments along a row
  (see [`MomentsGrayPlane`](moments_gray_plane.md))
- *"moments_column"*: Mixed moments along a column
  (see [`MomentsGrayPlane`](moments_gray_plane.md))
- *"alpha"*: Approximating plane, parameter Alpha
  (see [`MomentsGrayPlane`](moments_gray_plane.md))
- *"beta"*: Approximating plane, parameter Beta
  (see [`MomentsGrayPlane`](moments_gray_plane.md))

## Attention

Several features are processed in the order in which
they are entered.

Note that the operator `GrayFeatures` only considers
the given *`regions`* and ignores any previously set domain
of the input image *`image`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`regions`** (input_object)  region-array `→` [HRegion](HRegion.md)

Regions to be examined.

**`image`** (input_object)  singlechannelimage `→` [HImage](HImage.md) (byte / direction / cyclic / int1 / int2 / uint2 / int4 / real)

Gray value image.

**`features`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Names of the features.

Default:
"mean"

List of values:
"alpha", "anisotropy", "area", "beta", "column", "deviation", "entropy", "fuzzy_entropy", "fuzzy_perimeter", "max", "mean", "median", "min", "moments_column", "moments_row", "phi", "plane_deviation", "ra", "rb", "row"

**`value`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Values of the features.

## Complexity

If F is the area of the region and N the number of features
the runtime complexity is O(F * N).

## Result

The operator `GrayFeatures` returns the value 2 (
H_MSG_TRUE)
if the
input image has the defined gray values and the parameters are
correct. If necessary an exception is raised.

## Possible Predecessors

`Connection`,
`MeanImage`,
`EntropyImage`,
`SobelAmp`,
`MedianSeparate`

## Possible Successors

`SelectGray`,
`ShapeTrans`,
`ReduceDomain`,
`CountObj`

## See also

`SelectGray`,
`DeviationImage`,
`EntropyGray`,
`Intensity`,
`MeanImage`,
`MinMaxGray`,
`SelectObj`

## Module

Foundation
