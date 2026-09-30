# classify_image_class_gmm (Operator)

## Name

`classify_image_class_gmm` — Classify an image with a Gaussian Mixture Model.

## Signature

`def classify_image_class_gmm(image: HObject, gmmhandle: HHandle, rejection_threshold: float) -> HObject`

## Description

`classify_image_class_gmm` performs a pixel classification
with the Gaussian Mixture Model (GMM) *`gmmhandle`* on the
multichannel image *`image`*. Before calling
`classify_image_class_gmm` the GMM must be trained with
[`train_class_gmm`](train_class_gmm.md). *`image`* must have `num_dim`
channels, as specified with [`create_class_gmm`](create_class_gmm.md). On output,
*`class_regions`* contains `num_classes` regions as the
result of the classification. Note
that the order of the regions that are returned in
*`class_regions`* corresponds to the order of the classes as
defined by the training regions in
[`add_samples_image_class_gmm`](add_samples_image_class_gmm.md). The parameter
*`rejection_threshold`* can be used to reject pixels that have
an uncertain classification. *`rejection_threshold`* represents
a threshold on the K-sigma probability measure returned by the
classification (see [`classify_class_gmm`](classify_class_gmm.md) and
[`evaluate_class_gmm`](evaluate_class_gmm.md)). All pixels having a probability below
*`rejection_threshold`* are not assigned to any class.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`image`** (input_object)  (multichannel-)image `→` HObject (byte / cyclic / direction / int1 / int2 / uint2 / int4 / real)

Input image.

**`class_regions`** (output_object)  region-array `→` HObject

Segmented classes.

**`gmmhandle`** (input_control)  class_gmm `→` HHandle

GMM handle.

**`rejection_threshold`** (input_control)  real `→` float

Threshold for the rejection of the classification.

Default:
0.5

Suggested values:
0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0

Restriction:
`RejectionThreshold >= 0.0 && RejectionThreshold <= 1.0`

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
create_class_gmm (3, 4, [1,30], 'full', 'none',0, 42, GMMHandle)
add_samples_image_class_gmm (Image, Classes, GMMHandle, 1.5)
get_sample_num_class_gmm (GMMHandle, NumSamples)
train_class_gmm (GMMHandle, 150, 1e-4, 'training', 1e-4, Centers, Iter)
classify_image_class_gmm (Image, ClassRegions, GMMHandle, 0.0001)
```

## Result

If the parameters are valid, the operator
`classify_image_class_gmm` returns the value 2 (
H_MSG_TRUE)
. If
necessary an exception is raised.

## Possible Predecessors

`train_class_gmm`,
`read_class_gmm`

## Alternatives

`classify_image_class_knn`,
`classify_image_class_mlp`,
`classify_image_class_svm`,
`classify_image_class_lut`,
`class_ndim_norm`,
`class_2dim_sup`

## See also

`add_samples_image_class_gmm`,
`create_class_gmm`

## Module

Foundation
