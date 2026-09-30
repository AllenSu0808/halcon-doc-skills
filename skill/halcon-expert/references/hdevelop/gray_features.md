# gray_features (Operator)

## Name

`gray_features` — Calculates gray value features for a set of regions.

## Signature

`gray_features(Regions, Image : : Features : Value)`

## Description

`gray_features` has a set of regions
(*`Regions`*) as input. For each of these regions the
features (*`Features`*) are calculated and returned in *`Value`*.

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
- *'mean'*:Mean gray value (see [`intensity`](intensity.md))
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

Several features are processed in the order in which
they are entered.

Note that the operator `gray_features` only considers
the given *`Regions`* and ignores any previously set domain
of the input image *`Image`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`Regions`** (input_object)  region-array `→` object

Regions to be examined.

**`Image`** (input_object)  singlechannelimage `→` object (byte / direction / cyclic / int1 / int2 / uint2 / int4 / real)

Gray value image.

**`Features`** (input_control)  string(-array) `→`  (string)

Names of the features.

Default:
'mean'

List of values:
'alpha', 'anisotropy', 'area', 'beta', 'column', 'deviation', 'entropy', 'fuzzy_entropy', 'fuzzy_perimeter', 'max', 'mean', 'median', 'min', 'moments_column', 'moments_row', 'phi', 'plane_deviation', 'ra', 'rb', 'row'

**`Value`** (output_control)  real(-array) `→`  (real)

Values of the features.

## Complexity

If F is the area of the region and N the number of features
the runtime complexity is O(F * N).

## Result

The operator `gray_features` returns the value 2 (
H_MSG_TRUE)
if the
input image has the defined gray values and the parameters are
correct. If necessary an exception is raised.

## Possible Predecessors

`connection`,
`mean_image`,
`entropy_image`,
`sobel_amp`,
`median_separate`

## Possible Successors

`select_gray`,
`shape_trans`,
`reduce_domain`,
`count_obj`

## See also

`select_gray`,
`deviation_image`,
`entropy_gray`,
`intensity`,
`mean_image`,
`min_max_gray`,
`select_obj`

## Module

Foundation
