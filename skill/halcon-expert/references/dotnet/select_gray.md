# SelectGray (Operator)

## Name

`SelectGray` — Select regions based on gray value features.

## Signature

`static void HOperatorSet.SelectGray(HObject regions, HObject image, out HObject selectedRegions, HTuple features, HTuple operation, HTuple min, HTuple max)`

`HRegion HRegion.SelectGray(HImage image, HTuple features, string operation, HTuple min, HTuple max)`

`HRegion HRegion.SelectGray(HImage image, string features, string operation, double min, double max)`

## Description

The operator `SelectGray` has a number of regions
(*`regions`*) as input. For each of these regions the
(*`features`*) are calculated. The region is transferred (duplicated)
into the output *`selectedRegions`*, if each
(*`operation`* = *"and"*) or at least one (*`operation`*
= *"or"*) of the calculated features is within the limits.
The limits are defined by the parameters *`min`* and *`max`*.
Thereby, *`min`* and *`max`* can also be set to *"min"*
or *"max"*, respectively, corresponding to setting the smallest
or largest value possible for this feature.
The parameter *`image`* contains an image which returns the gray
values for calculating the features.

*Restriction:*

$$\texttt{Min}_{i}\le\texttt{Features}_{i}(\texttt{Regions},\texttt{Image})\le\texttt{Max}_{i}$$

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
- *"mean"*: Mean gray value
  (see [`Intensity`](intensity.md))
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

Note that the operator `SelectGray` only considers
the given *`regions`* and ignores any previously set domain
of the input image *`image`*.
If only one feature is used the value of *`operation`* is
meaningless. Several features are processed in the order in which
they are entered. The maximum number of features is limited to 100.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`regions`** (input_object)  region-array `→` [HRegion](HRegion.md)

Regions to be examined.

**`image`** (input_object)  singlechannelimage `→` [HImage](HImage.md) (byte / direction / cyclic / int1 / int2 / uint2 / int4 / real)

Gray value image.

**`selectedRegions`** (output_object)  region-array `→` [HRegion](HRegion.md)

Regions having features within the limits.

**`features`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Names of the features.

Default:
"mean"

List of values:
"alpha", "anisotropy", "area", "beta", "column", "deviation", "entropy", "fuzzy_entropy", "fuzzy_perimeter", "max", "mean", "median", "min", "moments_column", "moments_row", "phi", "plane_deviation", "ra", "rb", "row"

**`operation`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Logical connection of features.

Default:
"and"

List of values:
"and", "or"

**`min`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*double* / int / long / string)

Lower limit(s) of features or 'min'.

Default:
128.0

Suggested values:
0.5, 1.0, 10.0, 20.0, 50.0, 128.0, 255.0, 1000.0, "min"

**`max`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*double* / int / long / string)

Upper limit(s) of features or 'max'.

Default:
255.0

Suggested values:
0.5, 1.0, 10.0, 20.0, 50.0, 128.0, 255.0, 1000.0, "max"

## Complexity

If F is the area of the region and N the number of features
the runtime complexity is O(F * N).

## Result

The operator `SelectGray` returns the value 2 (
H_MSG_TRUE)
if the
input image has the defined gray values and the parameters are
correct. The behavior in case of empty input (no input images
available) is set via the operator
`set_system(::'no_object_result',<Result>:)`,
the behavior in case of empty region is set via
`set_system(::'empty_region_result',<Result>:)`.
If necessary an exception is raised.

## Possible Predecessors

`Connection`,
`MeanImage`,
`EntropyImage`,
`SobelAmp`,
`MedianSeparate`

## Possible Successors

`SelectShape`,
`ShapeTrans`,
`ReduceDomain`,
`CountObj`

## See also

`DeviationImage`,
`EntropyGray`,
`Intensity`,
`MeanImage`,
`MinMaxGray`,
`SelectObj`

## Module

Foundation
