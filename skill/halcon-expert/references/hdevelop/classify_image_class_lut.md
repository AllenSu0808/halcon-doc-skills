# classify_image_class_lut (Operator)

## Name

`classify_image_class_lut` — Classify a byte image using a look-up table.

## Signature

`classify_image_class_lut(Image : ClassRegions : ClassLUTHandle : )`

## Description

`classify_image_class_lut` performs a pixel classification on a
multi-channel byte *`Image`* using a look-up table (LUT)
*`ClassLUTHandle`*. The operator can replace
[`classify_image_class_gmm`](classify_image_class_gmm.md), [`classify_image_class_knn`](classify_image_class_knn.md),
[`classify_image_class_mlp`](classify_image_class_mlp.md) and [`classify_image_class_svm`](classify_image_class_svm.md).
The classification gets a major speed-up,
because the estimation of the class in every image point is no longer
necessary since every possible response of the GMM, KNN, MLP or SVM,
respectively, is stored in the LUT. This LUT classifier must be created
with the trained classifier in [`create_class_lut_gmm`](create_class_lut_gmm.md),
[`create_class_lut_knn`](create_class_lut_knn.md), [`create_class_lut_mlp`](create_class_lut_mlp.md) or
[`create_class_lut_svm`](create_class_lut_svm.md), respectively, before
`classify_image_class_lut` can be used. For the classification the
parameters in [`create_class_gmm`](create_class_gmm.md), [`create_class_knn`](create_class_knn.md),
[`create_class_mlp`](create_class_mlp.md) and [`create_class_svm`](create_class_svm.md), respectively,
are important: The byte *`Image`* must have the same number of channels
as specified by `NumInput`, `NumFeatures` or `NumDim`,
respectively. As result of the pixel classification
`classify_image_class_lut` passes `NumOutput` or
`NumClasses` regions in *`ClassRegions`*, respectively

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`Image`** (input_object)  (multichannel-)image `→` object (byte)

Input image.

**`ClassRegions`** (output_object)  region-array `→` object

Segmented classes.

**`ClassLUTHandle`** (input_control)  class_lut `→`  (handle)

Handle of the LUT classifier.

## Example (HDevelop)

```
read_image (Image, 'patras')
gen_rectangle1 (Sea, 10, 10, 120, 270)
gen_rectangle2 (Deck, [170,400], [350,375], [-0.56192,-0.75139], \
                [64,104], [26,11])
union1 (Deck, Deck)
gen_rectangle1 (Walls, 355, 623, 420, 702)
gen_rectangle2 (Chimney, 286, 623, -0.56192, 64, 33)
concat_obj (Sea, Deck, Classes)
concat_obj (Classes, Walls, Classes)
concat_obj (Classes, Chimney, Classes)
*
* create MLP classifier and train it with sample classes
create_class_mlp (3, 3, 4, 'softmax', 'principal_components', 3, \
                  42, MLPHandle)
add_samples_image_class_mlp (Image, Classes, MLPHandle)
train_class_mlp (MLPHandle, 200, 1, 0.01, Error, ErrorLog)
*
* create the LUT classifier
create_class_lut_mlp (MLPHandle, [], [], ClassLUTHandle)
*
* classify the image with the LUT
classify_image_class_lut (Image, ClassRegions, ClassLUTHandle)
```

## Result

If the parameters are valid, the operator
`classify_image_class_lut` returns the value 2 (
H_MSG_TRUE)
. If
necessary an exception is raised.

## Possible Predecessors

`create_class_lut_gmm`,
`create_class_lut_knn`,
`create_class_lut_mlp`,
`create_class_lut_svm`

## Alternatives

`classify_image_class_gmm`,
`classify_image_class_knn`,
`classify_image_class_mlp`,
`classify_image_class_svm`

## See also

`create_class_lut_gmm`,
`create_class_lut_knn`,
`create_class_lut_mlp`,
`create_class_lut_svm`,
`create_class_lut_gmm`

## Module

Foundation
