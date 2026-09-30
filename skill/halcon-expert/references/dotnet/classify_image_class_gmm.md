# ClassifyImageClassGmm (Operator)

## Name

`ClassifyImageClassGmm` — Classify an image with a Gaussian Mixture Model.

## Signature

`static void HOperatorSet.ClassifyImageClassGmm(HObject image, out HObject classRegions, HTuple GMMHandle, HTuple rejectionThreshold)`

`HRegion HImage.ClassifyImageClassGmm(HClassGmm GMMHandle, double rejectionThreshold)`

`HRegion HClassGmm.ClassifyImageClassGmm(HImage image, double rejectionThreshold)`

## Description

`ClassifyImageClassGmm` performs a pixel classification
with the Gaussian Mixture Model (GMM) *`GMMHandle`* on the
multichannel image *`image`*. Before calling
`ClassifyImageClassGmm` the GMM must be trained with
[`TrainClassGmm`](train_class_gmm.md). *`image`* must have `numDim`
channels, as specified with [`CreateClassGmm`](create_class_gmm.md). On output,
*`classRegions`* contains `numClasses` regions as the
result of the classification. Note
that the order of the regions that are returned in
*`classRegions`* corresponds to the order of the classes as
defined by the training regions in
[`AddSamplesImageClassGmm`](add_samples_image_class_gmm.md). The parameter
*`rejectionThreshold`* can be used to reject pixels that have
an uncertain classification. *`rejectionThreshold`* represents
a threshold on the K-sigma probability measure returned by the
classification (see [`ClassifyClassGmm`](classify_class_gmm.md) and
[`EvaluateClassGmm`](evaluate_class_gmm.md)). All pixels having a probability below
*`rejectionThreshold`* are not assigned to any class.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`image`** (input_object)  (multichannel-)image `→` [HImage](HImage.md) (byte / cyclic / direction / int1 / int2 / uint2 / int4 / real)

Input image.

**`classRegions`** (output_object)  region-array `→` [HRegion](HRegion.md)

Segmented classes.

**`GMMHandle`** (input_control)  class_gmm `→` [HClassGmm](HClassGmm.md), [HTuple](HTuple.md) (*IntPtr*)

GMM handle.

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
create_class_gmm (3, 4, [1,30], 'full', 'none',0, 42, GMMHandle)
add_samples_image_class_gmm (Image, Classes, GMMHandle, 1.5)
get_sample_num_class_gmm (GMMHandle, NumSamples)
train_class_gmm (GMMHandle, 150, 1e-4, 'training', 1e-4, Centers, Iter)
classify_image_class_gmm (Image, ClassRegions, GMMHandle, 0.0001)
```

## Result

If the parameters are valid, the operator
`ClassifyImageClassGmm` returns the value 2 (
H_MSG_TRUE)
. If
necessary an exception is raised.

## Possible Predecessors

`TrainClassGmm`,
`ReadClassGmm`

## Alternatives

`ClassifyImageClassKnn`,
`ClassifyImageClassMlp`,
`ClassifyImageClassSvm`,
`ClassifyImageClassLut`,
`ClassNdimNorm`,
`Class2dimSup`

## See also

`AddSamplesImageClassGmm`,
`CreateClassGmm`

## Module

Foundation
