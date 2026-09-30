# classify_image_class_mlp (Operator)

## Name

`classify_image_class_mlp` — Classify an image with a multilayer perceptron.

## Signature

`classify_image_class_mlp(Image : ClassRegions : MLPHandle, RejectionThreshold : )`

## Description

`classify_image_class_mlp` performs a pixel classification
with the multilayer perceptron (MLP) *`MLPHandle`* on the
multichannel image *`Image`*. Before calling
`classify_image_class_mlp` the MLP must be trained with
[`train_class_mlp`](train_class_mlp.md). *`Image`* must have `NumInput`
channels, as specified with [`create_class_mlp`](create_class_mlp.md). On output,
*`ClassRegions`* contains `NumOutput` regions as the
result of the classification. Note that the order of the regions that
are returned in *`ClassRegions`* corresponds to the order of the
classes as defined by the training regions in
[`add_samples_image_class_mlp`](add_samples_image_class_mlp.md). The parameter
*`RejectionThreshold`* can be used to reject pixels that have
an uncertain classification. *`RejectionThreshold`* represents
a threshold on the probability measure returned by the
classification (see [`classify_class_mlp`](classify_class_mlp.md) and
[`evaluate_class_mlp`](evaluate_class_mlp.md)). All pixels having a probability below
*`RejectionThreshold`* are not assigned to any class. Because
an MLP typically assigns pixels that lie outside the convex hull of
the training data in the feature space to one of the classes with
high probability (confidence), it is useful in many cases to
explicitly train a rejection class, even if
*`RejectionThreshold`* is used, by adding samples for the
rejection class with [`add_samples_image_class_mlp`](add_samples_image_class_mlp.md) and by
re-training the MLP with [`train_class_mlp`](train_class_mlp.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`Image`** (input_object)  (multichannel-)image `→` object (byte / cyclic / direction / int1 / int2 / uint2 / int4 / real)

Input image.

**`ClassRegions`** (output_object)  region-array `→` object

Segmented classes.

**`MLPHandle`** (input_control)  class_mlp `→`  (handle)

MLP handle.

**`RejectionThreshold`** (input_control)  real `→`  (real)

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
create_class_mlp (3, 3, 4, 'softmax', 'principal_components', 3, 42, \
                  MLPHandle)
add_samples_image_class_mlp (Image, Classes, MLPHandle)
get_sample_num_class_mlp (MLPHandle, NumSamples)
train_class_mlp (MLPHandle, 200, 1, 0.01, Error, ErrorLog)
classify_image_class_mlp (Image, ClassRegions, MLPHandle, 0.5)
dev_display (ClassRegions)
```

## Result

If the parameters are valid, the operator
`classify_image_class_mlp` returns the value 2 (
H_MSG_TRUE)
. If
necessary an exception is raised.

## Possible Predecessors

`train_class_mlp`,
`read_class_mlp`

## Alternatives

`classify_image_class_gmm`,
`classify_image_class_knn`,
`classify_image_class_svm`,
`classify_image_class_lut`,
`class_ndim_norm`,
`class_2dim_sup`

## See also

`add_samples_image_class_mlp`,
`create_class_mlp`

## Module

Foundation
