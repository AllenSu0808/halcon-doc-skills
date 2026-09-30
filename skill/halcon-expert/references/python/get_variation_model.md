# get_variation_model (Operator)

## Name

`get_variation_model` — Return the images used for image comparison by a variation model.

## Signature

`def get_variation_model(model_id: HHandle) -> Tuple[HObject, HObject]`

## Description

`get_variation_model` returns the image of the ideal object
and the corresponding variation image of the variation model
*`model_id`* in *`image`* and *`var_image`*,
respectively. The returned images can be used to check whether an
image of a bad object has been trained with
[`train_variation_model`](train_variation_model.md). This can be seen from the variation
image. If an image of a bad object has been trained, the variation
image typically has large variations in areas that should exhibit no
variations.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`image`** (output_object)  image `→` HObject (byte / int2 / uint2)

Image of the trained object.

**`var_image`** (output_object)  image `→` HObject (real)

Variation image of the trained object.

**`model_id`** (input_control)  variation_model `→` HHandle

ID of the variation model.

## Result

`get_variation_model` returns 2 (
H_MSG_TRUE)
if all parameters are
correct.

## Possible Predecessors

`train_variation_model`

## See also

`prepare_variation_model`,
`compare_variation_model`,
`compare_ext_variation_model`

## Module

Matching
