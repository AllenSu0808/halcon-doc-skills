# get_variation_model (Operator)

## Name

`get_variation_model` — Return the images used for image comparison by a variation model.

## Signature

`get_variation_model( : Image, VarImage : ModelID : )`

## Description

`get_variation_model` returns the image of the ideal object
and the corresponding variation image of the variation model
*`ModelID`* in *`Image`* and *`VarImage`*,
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

**`Image`** (output_object)  image `→` object (byte / int2 / uint2)

Image of the trained object.

**`VarImage`** (output_object)  image `→` object (real)

Variation image of the trained object.

**`ModelID`** (input_control)  variation_model `→`  (handle)

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
