# select_gray (Operator)

## Name

`select_gray` — Select regions based on gray value features.

## Signature

`select_gray(Regions, Image : SelectedRegions : Features, Operation, Min, Max : )`

## Description

The operator `select_gray` has a number of regions
(*`Regions`*) as input. For each of these regions the
(*`Features`*) are calculated. The region is transferred (duplicated)
into the output *`SelectedRegions`*, if each
(*`Operation`* = *'and'*) or at least one (*`Operation`*
= *'or'*) of the calculated features is within the limits.
The limits are defined by the parameters *`Min`* and *`Max`*.
Thereby, *`Min`* and *`Max`* can also be set to *'min'*
or *'max'*, respectively, corresponding to setting the smallest
or largest value possible for this feature.
The parameter *`Image`* contains an image which returns the gray
values for calculating the features.

*Restriction:*

$$\texttt{Min}_{i}\le\texttt{Features}_{i}(\texttt{Regions},\texttt{Image})\le\texttt{Max}_{i}$$

Possible values for *`Features`*:

- *'area'*: Gray value volume of region
  (see [`area_center_gray`](area_center_gray.md))
- *'row'*: Row index of the center of gravity
  (see [`area_center_gray`](area_center_gray.md))
- *'column'*: Column index of the center of gravity
  (see [`area_center_gray`](area_center_gray.md))
- *'ra'*: Major axis of equivalent ellipse
  (see [`elliptic_axis_gray`](elliptic_axis_gray.md))
- *'rb'*: Minor axis of equivalent ellipse
  (see [`elliptic_axis_gray`](elliptic_axis_gray.md))
- *'phi'*: Orientation of equivalent ellipse
  (see [`elliptic_axis_gray`](elliptic_axis_gray.md))
- *'min'*: Minimum gray value
  (see [`min_max_gray`](min_max_gray.md))
- *'max'*: Maximum gray value
  (see [`min_max_gray`](min_max_gray.md))
- *'median'*: Median gray value
  (see [`min_max_gray`](min_max_gray.md), with `Percent`=*50*)
- *'mean'*: Mean gray value
  (see [`intensity`](intensity.md))
- *'deviation'*: Deviation of gray values
  (see [`intensity`](intensity.md))
- *'plane_deviation'*: Deviation from the approximating plane
  (see [`plane_deviation`](plane_deviation.md))
- *'anisotropy'*: Anisotropy
  (see [`entropy_gray`](entropy_gray.md))
- *'entropy'*: Entropy
  (see [`entropy_gray`](entropy_gray.md))
- *'fuzzy_entropy'*: Fuzzy entropy of region
  (see [`fuzzy_entropy`](fuzzy_entropy.md), with a fuzzy function from
  `Apar`=*0* to `Cpar`=*255*)
- *'fuzzy_perimeter'*: Fuzzy perimeter of region
  (see [`fuzzy_perimeter`](fuzzy_perimeter.md), with a fuzzy function from
  `Apar`=*0* to `Cpar`=*255*)
- *'moments_row'*: Mixed moments along a row
  (see [`moments_gray_plane`](moments_gray_plane.md))
- *'moments_column'*: Mixed moments along a column
  (see [`moments_gray_plane`](moments_gray_plane.md))
- *'alpha'*: Approximating plane, parameter Alpha
  (see [`moments_gray_plane`](moments_gray_plane.md))
- *'beta'*: Approximating plane, parameter Beta
  (see [`moments_gray_plane`](moments_gray_plane.md))

## Attention

Note that the operator `select_gray` only considers
the given *`Regions`* and ignores any previously set domain
of the input image *`Image`*.
If only one feature is used the value of *`Operation`* is
meaningless. Several features are processed in the order in which
they are entered. The maximum number of features is limited to 100.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`Regions`** (input_object)  region-array `→` object

Regions to be examined.

**`Image`** (input_object)  singlechannelimage `→` object (byte / direction / cyclic / int1 / int2 / uint2 / int4 / real)

Gray value image.

**`SelectedRegions`** (output_object)  region-array `→` object

Regions having features within the limits.

**`Features`** (input_control)  string(-array) `→`  (string)

Names of the features.

Default:
'mean'

List of values:
'alpha', 'anisotropy', 'area', 'beta', 'column', 'deviation', 'entropy', 'fuzzy_entropy', 'fuzzy_perimeter', 'max', 'mean', 'median', 'min', 'moments_column', 'moments_row', 'phi', 'plane_deviation', 'ra', 'rb', 'row'

**`Operation`** (input_control)  string `→`  (string)

Logical connection of features.

Default:
'and'

List of values:
'and', 'or'

**`Min`** (input_control)  number(-array) `→`  (real / integer / string)

Lower limit(s) of features or 'min'.

Default:
128.0

Suggested values:
0.5, 1.0, 10.0, 20.0, 50.0, 128.0, 255.0, 1000.0, 'min'

**`Max`** (input_control)  number(-array) `→`  (real / integer / string)

Upper limit(s) of features or 'max'.

Default:
255.0

Suggested values:
0.5, 1.0, 10.0, 20.0, 50.0, 128.0, 255.0, 1000.0, 'max'

## Complexity

If F is the area of the region and N the number of features
the runtime complexity is O(F * N).

## Result

The operator `select_gray` returns the value 2 (
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

`connection`,
`mean_image`,
`entropy_image`,
`sobel_amp`,
`median_separate`

## Possible Successors

`select_shape`,
`shape_trans`,
`reduce_domain`,
`count_obj`

## See also

`deviation_image`,
`entropy_gray`,
`intensity`,
`mean_image`,
`min_max_gray`,
`select_obj`

## Module

Foundation
