# CreateTextureInspectionModel (Operator)

## Name

`CreateTextureInspectionModel` — Create a texture inspection model.

## Signature

`static void HOperatorSet.CreateTextureInspectionModel(HTuple modelType, out HTuple textureInspectionModel)`

`public HTextureInspectionModel(string modelType)`

`void HTextureInspectionModel.CreateTextureInspectionModel(string modelType)`

## Description

`CreateTextureInspectionModel` creates a new texture inspection
model of type *`modelType`*. Currently, only the model type
*"basic"* is supported.

The parameters of the texture inspection can be queried with
[`GetTextureInspectionModelParam`](get_texture_inspection_model_param.md) and manipulated by calls to
[`SetTextureInspectionModelParam`](set_texture_inspection_model_param.md).

For an explanation of the concept of the texture inspection
see the introduction of chapter [Inspection / Texture Inspection](toc_inspection_texture.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`modelType`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

The type of the created texture inspection model.

Default:
"basic"

List of values:
"basic"

**`textureInspectionModel`** (output_control)  texture_inspection_model `→` [HTextureInspectionModel](HTextureInspectionModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle for using and accessing the texture
inspection model.

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
read_image (TestImage, 'carpet/carpet_02')
apply_texture_inspection_model (TestImage, DefectCandidates, \
                                TextureInspectionModel, \
                                TextureInspectionResultID)
```

## Result

The operator `CreateTextureInspectionModel` returns the value 2 (
H_MSG_TRUE)
in the texture inspection model can be allocated correctly. Otherwise, an
exception will be raised..

## Possible Successors

`SetTextureInspectionModelParam`,
`GetTextureInspectionModelParam`,
`AddTextureInspectionModelImage`

## Module

Matching
