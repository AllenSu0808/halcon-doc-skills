# classify_image_class_svm (Operator)

## Name

`classify_image_class_svm` — Classify an image with a support vector machine.

## Signature

`classify_image_class_svm(Image : ClassRegions : SVMHandle : )`

## Description

`classify_image_class_svm` performs a pixel classification
with the support vector machine (SVM) *`SVMHandle`* on the
multichannel image *`Image`*. Before calling
`classify_image_class_svm` the SVM must be trained with
[`train_class_svm`](train_class_svm.md). *`Image`* must have
`NumFeatures` channels, as specified with
[`create_class_svm`](create_class_svm.md). On output, *`ClassRegions`* contains
`NumClasses` regions as the result of the classification. Note
that the order of the regions that are returned in
*`ClassRegions`* corresponds to the order of the classes as
defined by the training regions in
[`add_samples_image_class_svm`](add_samples_image_class_svm.md).

To prevent that the SVM assigns pixels that lie outside the
convex hull of the training data in the feature space to one of the
classes, it is useful in many cases to explicitly train a rejection
class by adding samples for the rejection class with
[`add_samples_image_class_svm`](add_samples_image_class_svm.md) and by re-training the SVM with
[`train_class_svm`](train_class_svm.md).

An alternative for explicitly defining a rejection class is to use an SVM in
the mode *'novelty-detection'*. Please refer to the description in
[`create_class_svm`](create_class_svm.md) and [`add_samples_image_class_svm`](add_samples_image_class_svm.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`Image`** (input_object)  (multichannel-)image `→` object (byte / cyclic / direction / int1 / int2 / uint2 / int4 / real)

Input image.

**`ClassRegions`** (output_object)  region-array `→` object

Segmented classes.

**`SVMHandle`** (input_control)  class_svm `→`  (handle)

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
`classify_image_class_svm` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`train_class_svm`,
`read_class_svm`,
`reduce_class_svm`

## Alternatives

`classify_image_class_gmm`,
`classify_image_class_knn`,
`classify_image_class_mlp`,
`classify_image_class_lut`,
`class_ndim_norm`,
`class_2dim_sup`

## See also

`add_samples_image_class_svm`,
`create_class_svm`

## Module

Foundation
