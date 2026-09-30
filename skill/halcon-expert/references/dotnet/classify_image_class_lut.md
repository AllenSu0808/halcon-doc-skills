# ClassifyImageClassLut (Operator)

## Name

`ClassifyImageClassLut` — Classify a byte image using a look-up table.

## Signature

`static void HOperatorSet.ClassifyImageClassLut(HObject image, out HObject classRegions, HTuple classLUTHandle)`

`HRegion HImage.ClassifyImageClassLut(HClassLUT classLUTHandle)`

`HRegion HClassLUT.ClassifyImageClassLut(HImage image)`

## Description

`ClassifyImageClassLut` performs a pixel classification on a
multi-channel byte *`image`* using a look-up table (LUT)
*`classLUTHandle`*. The operator can replace
[`ClassifyImageClassGmm`](classify_image_class_gmm.md), [`ClassifyImageClassKnn`](classify_image_class_knn.md),
[`ClassifyImageClassMlp`](classify_image_class_mlp.md) and [`ClassifyImageClassSvm`](classify_image_class_svm.md).
The classification gets a major speed-up,
because the estimation of the class in every image point is no longer
necessary since every possible response of the GMM, KNN, MLP or SVM,
respectively, is stored in the LUT. This LUT classifier must be created
with the trained classifier in [`CreateClassLutGmm`](create_class_lut_gmm.md),
[`CreateClassLutKnn`](create_class_lut_knn.md), [`CreateClassLutMlp`](create_class_lut_mlp.md) or
[`CreateClassLutSvm`](create_class_lut_svm.md), respectively, before
`ClassifyImageClassLut` can be used. For the classification the
parameters in [`CreateClassGmm`](create_class_gmm.md), [`CreateClassKnn`](create_class_knn.md),
[`CreateClassMlp`](create_class_mlp.md) and [`CreateClassSvm`](create_class_svm.md), respectively,
are important: The byte *`image`* must have the same number of channels
as specified by `numInput`, `numFeatures` or `numDim`,
respectively. As result of the pixel classification
`ClassifyImageClassLut` passes `numOutput` or
`numClasses` regions in *`classRegions`*, respectively

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`image`** (input_object)  (multichannel-)image `→` [HImage](HImage.md) (byte)

Input image.

**`classRegions`** (output_object)  region-array `→` [HRegion](HRegion.md)

Segmented classes.

**`classLUTHandle`** (input_control)  class_lut `→` [HClassLUT](HClassLUT.md), [HTuple](HTuple.md) (*IntPtr*)

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
`ClassifyImageClassLut` returns the value 2 (
H_MSG_TRUE)
. If
necessary an exception is raised.

## Possible Predecessors

`CreateClassLutGmm`,
`CreateClassLutKnn`,
`CreateClassLutMlp`,
`CreateClassLutSvm`

## Alternatives

`ClassifyImageClassGmm`,
`ClassifyImageClassKnn`,
`ClassifyImageClassMlp`,
`ClassifyImageClassSvm`

## See also

`CreateClassLutGmm`,
`CreateClassLutKnn`,
`CreateClassLutMlp`,
`CreateClassLutSvm`,
`CreateClassLutGmm`

## Module

Foundation
