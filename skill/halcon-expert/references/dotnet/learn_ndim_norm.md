# LearnNdimNorm (Operator)

## Name

`LearnNdimNorm` — Construct classes for [`ClassNdimNorm`](class_ndim_norm.md).

## Signature

`static void HOperatorSet.LearnNdimNorm(HObject foreground, HObject background, HObject image, HTuple metric, HTuple distance, HTuple minNumberPercent, out HTuple radius, out HTuple center, out HTuple quality)`

`HTuple HImage.LearnNdimNorm(HRegion foreground, HRegion background, string metric, HTuple distance, HTuple minNumberPercent, out HTuple center, out double quality)`

`HTuple HImage.LearnNdimNorm(HRegion foreground, HRegion background, string metric, double distance, double minNumberPercent, out HTuple center, out double quality)`

`HTuple HRegion.LearnNdimNorm(HRegion background, HImage image, string metric, HTuple distance, HTuple minNumberPercent, out HTuple center, out double quality)`

`HTuple HRegion.LearnNdimNorm(HRegion background, HImage image, string metric, double distance, double minNumberPercent, out HTuple center, out double quality)`

## Description

`LearnNdimNorm` generates classification clusters from the
region *`foreground`* and the corresponding gray values in
the multi-channel image *`image`*, which can be used in
[`ClassNdimNorm`](class_ndim_norm.md). *`background`* determines a class
of pixels not to be found in [`ClassNdimNorm`](class_ndim_norm.md). This
parameter may be empty (empty object).

The parameter *`distance`* determines the maximum distance
*`radius`* of the clusters. It describes the minimum distance
between two cluster centers. If the parameter *`distance`*
is small the (small) hyper-cubes or hyper-spheres can approximate
the feature space well. Simultaneously the runtime during
classification increases.

The ratio of the number of pixels in a cluster to the total number
of pixels (in percent) must be larger than the value of
*`minNumberPercent`*, otherwise the cluster is not returned.
*`minNumberPercent`* serves to eliminate outliers in the
training set. If it is chosen too large many clusters are
suppressed.

Two different clustering procedures can be selected: The minimum
Euclidean distance algorithm (n-dimensional hyper-spheres) and the maximum
algorithm (n-dimensional hyper-cubes) for describing the pixels of
the image to classify in the n-dimensional histogram (parameter
*`metric`*). The Euclidean metric usually yields the better
results, but takes longer to compute. The parameter
*`quality`* returns the quality of the clustering. It is a
measure of overlap between the rejection class and the classificator
classes. Values larger than 0 denote the corresponding ratio of
overlap. If no rejection region is given, its value is set to 1.
The regions in *`background`* do not influence on the
clustering. They are merely used to check the results that can be
expected.

## Execution Information

- Multithreading type: exclusive (runs in parallel only with independent operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`foreground`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Foreground pixels to be trained.

**`background`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Background pixels to be trained (rejection class).

**`image`** (input_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte)

Multi-channel training image.

**`metric`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Metric to be used.

Default:
"euclid"

List of values:
"euclid", "maximum"

**`distance`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / int / long)

Maximum cluster radius.

Default:
10.0

Suggested values:
1.0, 2.0, 3.0, 4.0, 6.0, 8.0, 10.0, 13.0, 17.0, 24.0, 30.0, 40.0

Value range:
`1.0
≤
distance` (lin)

Minimum increment:
0.01

Recommended increment:
1.0

**`minNumberPercent`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / int / long)

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
minNumberPercent
≤
100.0` (lin)

Minimum increment:
0.01

Recommended increment:
0.1

**`radius`** (output_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Cluster radii or half edge lengths.

**`center`** (output_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Coordinates of all cluster centers.

**`quality`** (output_control)  real `→` [HTuple](HTuple.md) (*double*)

Overlap of the rejection class with the classified
objects (1: no overlap).

Assertion:
`0 <= Quality && Quality <= 1`

## Result

`LearnNdimNorm` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. The behavior with respect to the input images can be
determined by setting the values of the flags
*"no_object_result"* and *"empty_region_result"*
with [`SetSystem`](set_system.md). If necessary, an exception is raised.

## Possible Predecessors

`MinMaxGray`,
`SobelAmp`,
`BinomialFilter`,
`GaussFilter`,
`ReduceDomain`,
`DiffOfGauss`

## Possible Successors

`ClassNdimNorm`,
`Connection`,
`Dilation1`,
`Erosion1`,
`Opening`,
`Closing`,
`RankRegion`,
`ShapeTrans`,
`Skeleton`

## See also

`ClassNdimNorm`,
`Histo2dim`

## References

P. Haberäcker, “Digitale Bildverarbeitung”;
Hanser-Studienbücher, München, Wien, 1987

## Module

Foundation
