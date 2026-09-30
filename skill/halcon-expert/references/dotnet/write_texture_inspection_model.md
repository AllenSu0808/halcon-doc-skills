# WriteTextureInspectionModel (Operator)

## Name

`WriteTextureInspectionModel` — Write a texture inspection model to a file.

## Signature

`static void HOperatorSet.WriteTextureInspectionModel(HTuple textureInspectionModel, HTuple fileName)`

`void HTextureInspectionModel.WriteTextureInspectionModel(string fileName)`

## Description

`WriteTextureInspectionModel` writes the texture inspection model
*`textureInspectionModel`* to the file given by *`fileName`*.
The default HALCON file extension for the texture inspection model is
'htim'. `WriteTextureInspectionModel` is typically called after
the texture inspection model has been trained with
[`TrainTextureInspectionModel`](train_texture_inspection_model.md). However, it can also be used to
save an untrained model.
The texture inspection model can be read with
[`ReadTextureInspectionModel`](read_texture_inspection_model.md).
It should be noted that `WriteTextureInspectionModel` does
*not* write any training samples that possibly have been stored in the
texture inspection model. Instead, only the currently set parameters of the
model, possibly added images and, if trained, the classifiers of the single
pyramid levels are written.

For an explanation of the concept of the texture inspection
see the introduction of chapter [Inspection / Texture Inspection](toc_inspection_texture.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`textureInspectionModel`** (input_control)  texture_inspection_model `→` [HTextureInspectionModel](HTextureInspectionModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the texture inspection model.

**`fileName`** (input_control)  filename.write `→` [HTuple](HTuple.md) (*string*)

File name.

File extension:
.`htim`

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
* Write out texture inspection model
write_texture_inspection_model (TextureInspectionModel, 'ExampleModel.htim')
```

## Result

If the parameters are valid, the operator
`WriteTextureInspectionModel` returns the value 2 (
H_MSG_TRUE)
. If necessary
an exception is raised.

## Possible Predecessors

`TrainTextureInspectionModel`

## Possible Successors

`ClearTextureInspectionModel`

## See also

`CreateTextureInspectionModel`,
`ClearTextureInspectionModel`,
`SetTextureInspectionModelParam`,
`GetTextureInspectionModelParam`,
`AddTextureInspectionModelImage`

## Module

Matching
