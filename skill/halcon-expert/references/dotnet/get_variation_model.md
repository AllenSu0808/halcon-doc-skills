# GetVariationModel (Operator)

## Name

`GetVariationModel` — Return the images used for image comparison by a variation model.

## Signature

`static void HOperatorSet.GetVariationModel(out HObject image, out HObject varImage, HTuple modelID)`

`HImage HVariationModel.GetVariationModel(out HImage varImage)`

## Description

`GetVariationModel` returns the image of the ideal object
and the corresponding variation image of the variation model
*`modelID`* in *`image`* and *`varImage`*,
respectively. The returned images can be used to check whether an
image of a bad object has been trained with
[`TrainVariationModel`](train_variation_model.md). This can be seen from the variation
image. If an image of a bad object has been trained, the variation
image typically has large variations in areas that should exhibit no
variations.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`image`** (output_object)  image `→` [HImage](HImage.md) (byte / int2 / uint2)

Image of the trained object.

**`varImage`** (output_object)  image `→` [HImage](HImage.md) (real)

Variation image of the trained object.

**`modelID`** (input_control)  variation_model `→` [HVariationModel](HVariationModel.md), [HTuple](HTuple.md) (*IntPtr*)

ID of the variation model.

## Result

`GetVariationModel` returns 2 (
H_MSG_TRUE)
if all parameters are
correct.

## Possible Predecessors

`TrainVariationModel`

## See also

`PrepareVariationModel`,
`CompareVariationModel`,
`CompareExtVariationModel`

## Module

Matching
