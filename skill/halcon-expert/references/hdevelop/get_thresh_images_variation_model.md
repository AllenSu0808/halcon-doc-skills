# get_thresh_images_variation_model (Operator)

## Name

`get_thresh_images_variation_model` — Return the threshold images used for image comparison by a variation
model.

## Signature

`get_thresh_images_variation_model( : MinImage, MaxImage : ModelID : )`

## Description

`get_thresh_images_variation_model` returns the threshold
images of the variation model *`ModelID`* in *`MaxImage`*
and *`MinImage`*. The threshold images must be computed with
[`prepare_variation_model`](prepare_variation_model.md) or
[`prepare_direct_variation_model`](prepare_direct_variation_model.md) before they can be read out.
The formula used for calculating the threshold images is described
with [`prepare_variation_model`](prepare_variation_model.md) or
[`prepare_direct_variation_model`](prepare_direct_variation_model.md). The threshold images are
used in [`compare_variation_model`](compare_variation_model.md) and
[`compare_ext_variation_model`](compare_ext_variation_model.md) to detect too large deviations
of an image with respect to the model. As described with
[`compare_variation_model`](compare_variation_model.md) and
[`compare_ext_variation_model`](compare_ext_variation_model.md), gray values outside the
interval given by *`MinImage`* and *`MaxImage`* are
regarded as errors.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`MinImage`** (output_object)  image `→` object (byte / int2 / uint2)

Threshold image for the lower threshold.

**`MaxImage`** (output_object)  image `→` object (real)

Threshold image for the upper threshold.

**`ModelID`** (input_control)  variation_model `→`  (handle)

ID of the variation model.

## Result

`get_thresh_images_variation_model` returns 2 (
H_MSG_TRUE)
if all
parameters are correct.

## Possible Predecessors

`prepare_variation_model`,
`prepare_direct_variation_model`

## See also

`compare_variation_model`,
`compare_ext_variation_model`

## Module

Matching
