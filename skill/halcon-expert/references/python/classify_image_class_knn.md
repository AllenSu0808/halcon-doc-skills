# classify_image_class_knn (Operator)

## Name

`classify_image_class_knn` — Classify an image with a k-Nearest-Neighbor classifier.

## Signature

`def classify_image_class_knn(image: HObject, knnhandle: HHandle, rejection_threshold: float) -> Tuple[HObject, HObject]`

## Description

`classify_image_class_knn` performs a pixel classification
with a k-Nearest-Neighbor classifier (k-NN) *`knnhandle`* on the
multichannel image *`image`*. Before calling
`classify_image_class_knn` the k-NN classifier must be trained with
[`train_class_knn`](train_class_knn.md). *`image`* must have `num_dim`
channels, as specified with [`create_class_knn`](create_class_knn.md). On output,
*`class_regions`* contains `num_classes` regions as the
result of the classification. Note
that the order of the regions that are returned in
*`class_regions`* corresponds to the order of the classes as
defined by the training regions in
[`add_samples_image_class_knn`](add_samples_image_class_knn.md). The parameter
*`rejection_threshold`* can be used to reject pixels that have
an uncertain classification. *`rejection_threshold`* represents
a threshold on the distance to the nearest neighbor returned by the
classification. All pixels having a probability below
*`rejection_threshold`* are not assigned to any class.
*`distance_image`* contains the distance of each pixel to its nearest
neighbor.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`image`** (input_object)  (multichannel-)image `→` HObject (byte / cyclic / direction / int1 / int2 / uint2 / int4 / real)

Input image.

**`class_regions`** (output_object)  region-array `→` HObject (real)

Segmented classes.

**`distance_image`** (output_object)  image `→` HObject

Distance of the pixel's nearest neighbor.

**`knnhandle`** (input_control)  class_knn `→` HHandle

Handle of the k-NN classifier.

**`rejection_threshold`** (input_control)  real `→` float

Threshold for the rejection of the classification.

Default:
0.5

Suggested values:
0.0, 0.1, 0.2, 0.3, 5.0, 10.0, 255.0

Restriction:
`RejectionThreshold >= 0.0`

## Example (HDevelop)

```
read_image (Image, 'ic')
gen_rectangle1 (Board, 80, 320, 110, 350)
gen_rectangle1 (Capacitor, 359, 263, 371, 302)
gen_rectangle1 (Resistor, 200, 252, 290, 256)
gen_rectangle1 (IC, 180, 135, 216, 165)
concat_obj (Board, Capacitor, Classes)
concat_obj (Classes, Resistor, Classes)
concat_obj (Classes, IC, Classes)
create_class_knn (3, KNNHandle)
add_samples_image_class_knn (Image, Classes, KNNHandle)
get_sample_num_class_knn (KNNHandle, NumSamples)
train_class_knn (KNNHandle, [], [])
classify_image_class_knn (Image, ClassRegions, DistanceImage, \
                          KNNHandle, 0.5)
dev_display (ClassRegions)
```

## Result

If the parameters are valid, the operator
`classify_image_class_knn` returns the value 2 (
H_MSG_TRUE)
. If
necessary an exception is raised.

## Possible Predecessors

`train_class_knn`,
`read_class_knn`

## Alternatives

`classify_image_class_svm`,
`classify_image_class_mlp`,
`classify_image_class_gmm`,
`classify_image_class_lut`,
`class_ndim_norm`,
`class_2dim_sup`

## See also

`add_samples_image_class_knn`,
`create_class_knn`

## Module

Foundation
