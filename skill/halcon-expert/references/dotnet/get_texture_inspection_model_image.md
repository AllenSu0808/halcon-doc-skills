# GetTextureInspectionModelImage (Operator)

## Name

`GetTextureInspectionModelImage` — Get the training images contained in a texture inspection model.

## Signature

`static void HOperatorSet.GetTextureInspectionModelImage(out HObject modelImages, HTuple textureInspectionModel)`

`void HImage.GetTextureInspectionModelImage(HTextureInspectionModel textureInspectionModel)`

`HImage HTextureInspectionModel.GetTextureInspectionModelImage()`

`static HImage HTextureInspectionResult.GetTextureInspectionModelImage(HTextureInspectionModel textureInspectionModel)`

## Description

The operator `GetTextureInspectionModelImage` returns all
training images contained in a texture inspection model
*`textureInspectionModel`* that were added by
[`AddTextureInspectionModelImage`](add_texture_inspection_model_image.md).

For an explanation of the concept of the texture inspection
see the introduction of chapter [Inspection / Texture Inspection](toc_inspection_texture.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`modelImages`** (output_object)  (multichannel-)image-array `→` [HImage](HImage.md) (byte / uint2)

Training images contained in the texture inspection
model.

**`textureInspectionModel`** (input_control)  texture_inspection_model `→` [HTextureInspectionModel](HTextureInspectionModel.md), [HTuple](HTuple.md) (*IntPtr*)

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

The operator `GetTextureInspectionModelImage` returns the value
2 (
H_MSG_TRUE)
if the given parameters are valid and within acceptable range.
Otherwise, an exception will be raised.

## Possible Predecessors

`CreateTextureInspectionModel`,
`SetTextureInspectionModelParam`,
`GetTextureInspectionModelParam`,
`AddTextureInspectionModelImage`

## Possible Successors

`TrainTextureInspectionModel`,
`ClearTextureInspectionModel`,
`RemoveTextureInspectionModelImage`

## Module

Matching
