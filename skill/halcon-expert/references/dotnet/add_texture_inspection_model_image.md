# AddTextureInspectionModelImage (Operator)

## Name

`AddTextureInspectionModelImage` — Add training images to the texture inspection model.

## Signature

`static void HOperatorSet.AddTextureInspectionModelImage(HObject image, HTuple textureInspectionModel, out HTuple indices)`

`HTuple HImage.AddTextureInspectionModelImage(HTextureInspectionModel textureInspectionModel)`

`HTuple HTextureInspectionModel.AddTextureInspectionModelImage(HImage image)`

`static HTuple HTextureInspectionResult.AddTextureInspectionModelImage(HImage image, HTextureInspectionModel textureInspectionModel)`

## Description

`AddTextureInspectionModelImage` adds training images
to the texture inspection model (*`textureInspectionModel`*).
The domain of the training images is considered in all further calculations.
Since the feature extraction considers a certain
neighborhood of each pixel, no features can be extracted for pixels at the
border of the domain. The border size (*Border*) depends on the
*"patch_size"* ([`SetTextureInspectionModelParam`](set_texture_inspection_model_param.md))
and computes to
*Border*$=(^{\prime}\textit{p atch}\_\textit{size}^{\prime}-1)/2$.

All images which are added to the texture inspection model are used within
the training process (see [`TrainTextureInspectionModel`](train_texture_inspection_model.md) for more
information). Furthermore, it is possible to query all of the images passed
to the texture inspection model with
[`GetTextureInspectionModelImage`](get_texture_inspection_model_image.md).

Every added image receives an index (*`indices`*), which allows the user
to generate an assignment between the added images and his image data.
By calls of [`RemoveTextureInspectionModelImage`](remove_texture_inspection_model_image.md), the index can
further be used to delete images from the model that are not needed anymore.

It is possible to add either gray-scale images or multichannel images.
However, all of the passed images should have the same number of
channels.

For an explanation of the concept of the texture inspection
see the introduction of chapter [Inspection / Texture Inspection](toc_inspection_texture.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

This operator modifies the state of the following input parameter:

- textureInspectionModel

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`image`** (input_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / uint2 / real)

Image of flawless texture.

**`textureInspectionModel`** (input_control, state is modified)  texture_inspection_model `→` [HTextureInspectionModel](HTextureInspectionModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the texture inspection model.

**`indices`** (output_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long)

Indices of the images that have been added
to the texture inspection model.

## Example (HDevelop)

```
* Create texture inspection model
create_texture_inspection_model ('basic', TextureInspectionModel)
* Make this short example fast:
set_texture_inspection_model_param (TextureInspectionModel, \
                                    'gmm_em_max_iter', 1)
* Read and add training images
read_image (TrainImage, 'carpet/carpet_01')
add_texture_inspection_model_image (TrainImage, TextureInspectionModel, \
                                    Indices)
* Train the model
train_texture_inspection_model (TextureInspectionModel)
* Read and apply a test image
read_image (TrainImage, 'carpet/carpet_02')
apply_texture_inspection_model (TestImage, DefectCandidates, \
                                TextureInspectionModel, \
                                TextureInspectionResultID)
```

## Result

The operator `AddTextureInspectionModelImage` returns the value
2 (
H_MSG_TRUE)
if the given parameters are valid and within acceptable range.
Otherwise, an exception will be raised.

## Possible Predecessors

`CreateTextureInspectionModel`,
`SetTextureInspectionModelParam`,
`GetTextureInspectionModelParam`

## Possible Successors

`TrainTextureInspectionModel`,
`ClearTextureInspectionModel`,
`RemoveTextureInspectionModelImage`,
`GetTextureInspectionModelImage`

## Module

Matching
