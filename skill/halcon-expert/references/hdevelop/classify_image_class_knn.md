# classify_image_class_knn (Operator)

## Name

`classify_image_class_knn` — Classify an image with a k-Nearest-Neighbor classifier.

## Signature

`classify_image_class_knn(Image : ClassRegions, DistanceImage : KNNHandle, RejectionThreshold : )`

## Description

`classify_image_class_knn` performs a pixel classification
with a k-Nearest-Neighbor classifier (k-NN) *`KNNHandle`* on the
multichannel image *`Image`*. Before calling
`classify_image_class_knn` the k-NN classifier must be trained with
[`train_class_knn`](train_class_knn.md). *`Image`* must have `NumDim`
channels, as specified with [`create_class_knn`](create_class_knn.md). On output,
*`ClassRegions`* contains `NumClasses` regions as the
result of the classification. Note
that the order of the regions that are returned in
*`ClassRegions`* corresponds to the order of the classes as
defined by the training regions in
[`add_samples_image_class_knn`](add_samples_image_class_knn.md). The parameter
*`RejectionThreshold`* can be used to reject pixels that have
an uncertain classification. *`RejectionThreshold`* represents
a threshold on the distance to the nearest neighbor returned by the
classification. All pixels having a probability below
*`RejectionThreshold`* are not assigned to any class.
*`DistanceImage`* contains the distance of each pixel to its nearest
neighbor.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`Image`** (input_object)  (multichannel-)image `→` object (byte / cyclic / direction / int1 / int2 / uint2 / int4 / real)

Input image.

**`ClassRegions`** (output_object)  region-array `→` object (real)

Segmented classes.

**`DistanceImage`** (output_object)  image `→` object

Distance of the pixel's nearest neighbor.

**`KNNHandle`** (input_control)  class_knn `→`  (handle)

Handle of the k-NN classifier.

**`RejectionThreshold`** (input_control)  real `→`  (real)

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
