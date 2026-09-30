# GetThreshImagesVariationModel (Operator)

## Name

`GetThreshImagesVariationModel` — Return the threshold images used for image comparison by a variation
model.

## Signature

`static void HOperatorSet.GetThreshImagesVariationModel(out HObject minImage, out HObject maxImage, HTuple modelID)`

`HImage HVariationModel.GetThreshImagesVariationModel(out HImage maxImage)`

## Description

`GetThreshImagesVariationModel` returns the threshold
images of the variation model *`modelID`* in *`maxImage`*
and *`minImage`*. The threshold images must be computed with
[`PrepareVariationModel`](prepare_variation_model.md) or
[`PrepareDirectVariationModel`](prepare_direct_variation_model.md) before they can be read out.
The formula used for calculating the threshold images is described
with [`PrepareVariationModel`](prepare_variation_model.md) or
[`PrepareDirectVariationModel`](prepare_direct_variation_model.md). The threshold images are
used in [`CompareVariationModel`](compare_variation_model.md) and
[`CompareExtVariationModel`](compare_ext_variation_model.md) to detect too large deviations
of an image with respect to the model. As described with
[`CompareVariationModel`](compare_variation_model.md) and
[`CompareExtVariationModel`](compare_ext_variation_model.md), gray values outside the
interval given by *`minImage`* and *`maxImage`* are
regarded as errors.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`minImage`** (output_object)  image `→` [HImage](HImage.md) (byte / int2 / uint2)

Threshold image for the lower threshold.

**`maxImage`** (output_object)  image `→` [HImage](HImage.md) (real)

Threshold image for the upper threshold.

**`modelID`** (input_control)  variation_model `→` [HVariationModel](HVariationModel.md), [HTuple](HTuple.md) (*IntPtr*)

ID of the variation model.

## Result

`GetThreshImagesVariationModel` returns 2 (
H_MSG_TRUE)
if all
parameters are correct.

## Possible Predecessors

`PrepareVariationModel`,
`PrepareDirectVariationModel`

## See also

`CompareVariationModel`,
`CompareExtVariationModel`

## Module

Matching
