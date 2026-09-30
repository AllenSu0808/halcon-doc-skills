# ClassifyImageClassSvm (Operator)

## Name

`ClassifyImageClassSvm` — Classify an image with a support vector machine.

## Signature

`static void HOperatorSet.ClassifyImageClassSvm(HObject image, out HObject classRegions, HTuple SVMHandle)`

`HRegion HImage.ClassifyImageClassSvm(HClassSvm SVMHandle)`

`HRegion HClassSvm.ClassifyImageClassSvm(HImage image)`

## Description

`ClassifyImageClassSvm` performs a pixel classification
with the support vector machine (SVM) *`SVMHandle`* on the
multichannel image *`image`*. Before calling
`ClassifyImageClassSvm` the SVM must be trained with
[`TrainClassSvm`](train_class_svm.md). *`image`* must have
`numFeatures` channels, as specified with
[`CreateClassSvm`](create_class_svm.md). On output, *`classRegions`* contains
`numClasses` regions as the result of the classification. Note
that the order of the regions that are returned in
*`classRegions`* corresponds to the order of the classes as
defined by the training regions in
[`AddSamplesImageClassSvm`](add_samples_image_class_svm.md).

To prevent that the SVM assigns pixels that lie outside the
convex hull of the training data in the feature space to one of the
classes, it is useful in many cases to explicitly train a rejection
class by adding samples for the rejection class with
[`AddSamplesImageClassSvm`](add_samples_image_class_svm.md) and by re-training the SVM with
[`TrainClassSvm`](train_class_svm.md).

An alternative for explicitly defining a rejection class is to use an SVM in
the mode *"novelty-detection"*. Please refer to the description in
[`CreateClassSvm`](create_class_svm.md) and [`AddSamplesImageClassSvm`](add_samples_image_class_svm.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`image`** (input_object)  (multichannel-)image `→` [HImage](HImage.md) (byte / cyclic / direction / int1 / int2 / uint2 / int4 / real)

Input image.

**`classRegions`** (output_object)  region-array `→` [HRegion](HRegion.md)

Segmented classes.

**`SVMHandle`** (input_control)  class_svm `→` [HClassSvm](HClassSvm.md), [HTuple](HTuple.md) (*IntPtr*)

SVM handle.

## Example (HDevelop)

```
read_image (Image, 'ic')
gen_rectangle1 (Board, 20, 270, 160, 420)
gen_rectangle1 (Capacitor, 359, 263, 371, 302)
gen_rectangle1 (Resistor, 200, 252, 290, 256)
gen_rectangle1 (IC, 180, 135, 216, 165)
concat_obj (Board, Capacitor, Classes)
concat_obj (Classes, Resistor, Classes)
concat_obj (Classes, IC, Classes)
create_class_svm (3, 'rbf', 0.01, 0.01, 4, 'one-versus-all', \
                  'normalization', 3, SVMHandle)
add_samples_image_class_svm (Image, Classes, SVMHandle)
train_class_svm (SVMHandle, 0.001, 'default')
reduce_class_svm (SVMHandle, 'bottom_up', 2, 0.01, SVMHandleReduced)
classify_image_class_svm (Image, ClassRegions, SVMHandleReduced)
dev_display (ClassRegions)
```

## Result

If the parameters are valid the operator
`ClassifyImageClassSvm` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`TrainClassSvm`,
`ReadClassSvm`,
`ReduceClassSvm`

## Alternatives

`ClassifyImageClassGmm`,
`ClassifyImageClassKnn`,
`ClassifyImageClassMlp`,
`ClassifyImageClassLut`,
`ClassNdimNorm`,
`Class2dimSup`

## See also

`AddSamplesImageClassSvm`,
`CreateClassSvm`

## Module

Foundation
