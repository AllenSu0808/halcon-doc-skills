# get_texture_inspection_model_image (Operator)

## Name

`get_texture_inspection_model_image` — Get the training images contained in a texture inspection model.

## Signature

`get_texture_inspection_model_image( : ModelImages : TextureInspectionModel : )`

## Description

The operator `get_texture_inspection_model_image` returns all
training images contained in a texture inspection model
*`TextureInspectionModel`* that were added by
[`add_texture_inspection_model_image`](add_texture_inspection_model_image.md).

For an explanation of the concept of the texture inspection
see the introduction of chapter [Inspection / Texture Inspection](toc_inspection_texture.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`ModelImages`** (output_object)  (multichannel-)image-array `→` object (byte / uint2)

Training images contained in the texture inspection
model.

**`TextureInspectionModel`** (input_control)  texture_inspection_model `→`  (handle)

Handle of the texture inspection model.

## Example (HDevelop)

```
* Create texture inspection model
create_texture_inspection_model ('basic', TextureInspectionModel)
* Make this short example fast:
set_texture_inspection_model_param (TextureInspectionModel, \
                                    'gmm_em_max_iter', 1)
* Read and add training images
read_image (TrainImage, 'carpet/carpet_01')
add_texture_inspection_model_image (ModelImages, TextureInspectionModel, \
                                    Indices)
* Get added training images
get_texture_inspection_model_image (ModelImagesOut, TextureInspectionModel)
```

## Result

The operator `get_texture_inspection_model_image` returns the value
2 (
H_MSG_TRUE)
if the given parameters are valid and within acceptable range.
Otherwise, an exception will be raised.

## Possible Predecessors

`create_texture_inspection_model`,
`set_texture_inspection_model_param`,
`get_texture_inspection_model_param`,
`add_texture_inspection_model_image`

## Possible Successors

`train_texture_inspection_model`,
`clear_texture_inspection_model`,
`remove_texture_inspection_model_image`

## Module

Matching
