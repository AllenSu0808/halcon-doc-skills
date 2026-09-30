# learn_ndim_norm (Operator)

## Name

`learn_ndim_norm` — Construct classes for [`class_ndim_norm`](class_ndim_norm.md).

## Signature

`learn_ndim_norm(Foreground, Background, Image : : Metric, Distance, MinNumberPercent : Radius, Center, Quality)`

## Description

`learn_ndim_norm` generates classification clusters from the
region *`Foreground`* and the corresponding gray values in
the multi-channel image *`Image`*, which can be used in
[`class_ndim_norm`](class_ndim_norm.md). *`Background`* determines a class
of pixels not to be found in [`class_ndim_norm`](class_ndim_norm.md). This
parameter may be empty (empty object).

The parameter *`Distance`* determines the maximum distance
*`Radius`* of the clusters. It describes the minimum distance
between two cluster centers. If the parameter *`Distance`*
is small the (small) hyper-cubes or hyper-spheres can approximate
the feature space well. Simultaneously the runtime during
classification increases.

The ratio of the number of pixels in a cluster to the total number
of pixels (in percent) must be larger than the value of
*`MinNumberPercent`*, otherwise the cluster is not returned.
*`MinNumberPercent`* serves to eliminate outliers in the
training set. If it is chosen too large many clusters are
suppressed.

Two different clustering procedures can be selected: The minimum
Euclidean distance algorithm (n-dimensional hyper-spheres) and the maximum
algorithm (n-dimensional hyper-cubes) for describing the pixels of
the image to classify in the n-dimensional histogram (parameter
*`Metric`*). The Euclidean metric usually yields the better
results, but takes longer to compute. The parameter
*`Quality`* returns the quality of the clustering. It is a
measure of overlap between the rejection class and the classificator
classes. Values larger than 0 denote the corresponding ratio of
overlap. If no rejection region is given, its value is set to 1.
The regions in *`Background`* do not influence on the
clustering. They are merely used to check the results that can be
expected.

## Execution Information

- Multithreading type: exclusive (runs in parallel only with independent operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Foreground`** (input_object)  region(-array) `→` object

Foreground pixels to be trained.

**`Background`** (input_object)  region(-array) `→` object

Background pixels to be trained (rejection class).

**`Image`** (input_object)  (multichannel-)image(-array) `→` object (byte)

Multi-channel training image.

**`Metric`** (input_control)  string `→`  (string)

Metric to be used.

Default:
'euclid'

List of values:
'euclid', 'maximum'

**`Distance`** (input_control)  number `→`  (real / integer)

Maximum cluster radius.

Default:
10.0

Suggested values:
1.0, 2.0, 3.0, 4.0, 6.0, 8.0, 10.0, 13.0, 17.0, 24.0, 30.0, 40.0

Value range:
`1.0
≤
Distance` (lin)

Minimum increment:
0.01

Recommended increment:
1.0

**`MinNumberPercent`** (input_control)  number `→`  (real / integer)

The ratio of the number of pixels in a cluster to the
total number of pixels (in percent) must be larger than
MinNumberPercent (otherwise the cluster is not output).

Default:
0.01

Suggested values:
0.001, 0.05, 0.1, 0.2, 0.5, 1.0, 2.0, 5.0, 10.0

Value range:
`0.0
≤
MinNumberPercent
≤
100.0` (lin)

Minimum increment:
0.01

Recommended increment:
0.1

**`Radius`** (output_control)  real-array `→`  (real)

Cluster radii or half edge lengths.

**`Center`** (output_control)  real-array `→`  (real)

Coordinates of all cluster centers.

**`Quality`** (output_control)  real `→`  (real)

Overlap of the rejection class with the classified
objects (1: no overlap).

Assertion:
`0 <= Quality && Quality <= 1`

## Result

`learn_ndim_norm` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. The behavior with respect to the input images can be
determined by setting the values of the flags
*'no_object_result'* and *'empty_region_result'*
with [`set_system`](set_system.md). If necessary, an exception is raised.

## Possible Predecessors

`min_max_gray`,
`sobel_amp`,
`binomial_filter`,
`gauss_filter`,
`reduce_domain`,
`diff_of_gauss`

## Possible Successors

`class_ndim_norm`,
`connection`,
`dilation1`,
`erosion1`,
`opening`,
`closing`,
`rank_region`,
`shape_trans`,
`skeleton`

## See also

`class_ndim_norm`,
`histo_2dim`

## References

P. Haberäcker, “Digitale Bildverarbeitung”;
Hanser-Studienbücher, München, Wien, 1987

## Module

Foundation
