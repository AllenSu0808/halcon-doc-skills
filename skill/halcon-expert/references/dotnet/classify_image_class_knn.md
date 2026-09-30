# ClassifyImageClassKnn (Operator)

## Name

`ClassifyImageClassKnn` — Classify an image with a k-Nearest-Neighbor classifier.

## Signature

`static void HOperatorSet.ClassifyImageClassKnn(HObject image, out HObject classRegions, out HObject distanceImage, HTuple KNNHandle, HTuple rejectionThreshold)`

`HRegion HImage.ClassifyImageClassKnn(out HImage distanceImage, HClassKnn KNNHandle, double rejectionThreshold)`

`HRegion HClassKnn.ClassifyImageClassKnn(HImage image, out HImage distanceImage, double rejectionThreshold)`

## Description

`ClassifyImageClassKnn` performs a pixel classification
with a k-Nearest-Neighbor classifier (k-NN) *`KNNHandle`* on the
multichannel image *`image`*. Before calling
`ClassifyImageClassKnn` the k-NN classifier must be trained with
[`TrainClassKnn`](train_class_knn.md). *`image`* must have `numDim`
channels, as specified with [`CreateClassKnn`](create_class_knn.md). On output,
*`classRegions`* contains `numClasses` regions as the
result of the classification. Note
that the order of the regions that are returned in
*`classRegions`* corresponds to the order of the classes as
defined by the training regions in
[`AddSamplesImageClassKnn`](add_samples_image_class_knn.md). The parameter
*`rejectionThreshold`* can be used to reject pixels that have
an uncertain classification. *`rejectionThreshold`* represents
a threshold on the distance to the nearest neighbor returned by the
classification. All pixels having a probability below
*`rejectionThreshold`* are not assigned to any class.
*`distanceImage`* contains the distance of each pixel to its nearest
neighbor.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`image`** (input_object)  (multichannel-)image `→` [HImage](HImage.md) (byte / cyclic / direction / int1 / int2 / uint2 / int4 / real)

Input image.

**`classRegions`** (output_object)  region-array `→` [HRegion](HRegion.md) (real)

Segmented classes.

**`distanceImage`** (output_object)  image `→` [HImage](HImage.md)

Distance of the pixel's nearest neighbor.

**`KNNHandle`** (input_control)  class_knn `→` [HClassKnn](HClassKnn.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the k-NN classifier.

**`rejectionThreshold`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

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
`ClassifyImageClassKnn` returns the value 2 (
H_MSG_TRUE)
. If
necessary an exception is raised.

## Possible Predecessors

`TrainClassKnn`,
`ReadClassKnn`

## Alternatives

`ClassifyImageClassSvm`,
`ClassifyImageClassMlp`,
`ClassifyImageClassGmm`,
`ClassifyImageClassLut`,
`ClassNdimNorm`,
`Class2dimSup`

## See also

`AddSamplesImageClassKnn`,
`CreateClassKnn`

## Module

Foundation
