# ClassifyImageClassMlp (Operator)

## Name

`ClassifyImageClassMlp` — Classify an image with a multilayer perceptron.

## Signature

`static void HOperatorSet.ClassifyImageClassMlp(HObject image, out HObject classRegions, HTuple MLPHandle, HTuple rejectionThreshold)`

`HRegion HImage.ClassifyImageClassMlp(HClassMlp MLPHandle, double rejectionThreshold)`

`HRegion HClassMlp.ClassifyImageClassMlp(HImage image, double rejectionThreshold)`

## Description

`ClassifyImageClassMlp` performs a pixel classification
with the multilayer perceptron (MLP) *`MLPHandle`* on the
multichannel image *`image`*. Before calling
`ClassifyImageClassMlp` the MLP must be trained with
[`TrainClassMlp`](train_class_mlp.md). *`image`* must have `numInput`
channels, as specified with [`CreateClassMlp`](create_class_mlp.md). On output,
*`classRegions`* contains `numOutput` regions as the
result of the classification. Note that the order of the regions that
are returned in *`classRegions`* corresponds to the order of the
classes as defined by the training regions in
[`AddSamplesImageClassMlp`](add_samples_image_class_mlp.md). The parameter
*`rejectionThreshold`* can be used to reject pixels that have
an uncertain classification. *`rejectionThreshold`* represents
a threshold on the probability measure returned by the
classification (see [`ClassifyClassMlp`](classify_class_mlp.md) and
[`EvaluateClassMlp`](evaluate_class_mlp.md)). All pixels having a probability below
*`rejectionThreshold`* are not assigned to any class. Because
an MLP typically assigns pixels that lie outside the convex hull of
the training data in the feature space to one of the classes with
high probability (confidence), it is useful in many cases to
explicitly train a rejection class, even if
*`rejectionThreshold`* is used, by adding samples for the
rejection class with [`AddSamplesImageClassMlp`](add_samples_image_class_mlp.md) and by
re-training the MLP with [`TrainClassMlp`](train_class_mlp.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`image`** (input_object)  (multichannel-)image `→` [HImage](HImage.md) (byte / cyclic / direction / int1 / int2 / uint2 / int4 / real)

Input image.

**`classRegions`** (output_object)  region-array `→` [HRegion](HRegion.md)

Segmented classes.

**`MLPHandle`** (input_control)  class_mlp `→` [HClassMlp](HClassMlp.md), [HTuple](HTuple.md) (*IntPtr*)

MLP handle.

**`rejectionThreshold`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

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
`ClassifyImageClassMlp` returns the value 2 (
H_MSG_TRUE)
. If
necessary an exception is raised.

## Possible Predecessors

`TrainClassMlp`,
`ReadClassMlp`

## Alternatives

`ClassifyImageClassGmm`,
`ClassifyImageClassKnn`,
`ClassifyImageClassSvm`,
`ClassifyImageClassLut`,
`ClassNdimNorm`,
`Class2dimSup`

## See also

`AddSamplesImageClassMlp`,
`CreateClassMlp`

## Module

Foundation
