# create_texture_inspection_model (Operator)

## Name

`create_texture_inspection_model` — Create a texture inspection model.

## Signature

`def create_texture_inspection_model(model_type: str) -> HHandle`

## Description

`create_texture_inspection_model` creates a new texture inspection
model of type *`model_type`*. Currently, only the model type
*"basic"* is supported.

The parameters of the texture inspection can be queried with
[`get_texture_inspection_model_param`](get_texture_inspection_model_param.md) and manipulated by calls to
[`set_texture_inspection_model_param`](set_texture_inspection_model_param.md).

For an explanation of the concept of the texture inspection
see the introduction of chapter [Inspection / Texture Inspection](toc_inspection_texture.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`model_type`** (input_control)  string `→` str

The type of the created texture inspection model.

Default:
"basic"

List of values:
"basic"

**`texture_inspection_model`** (output_control)  texture_inspection_model `→` HHandle

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

The operator `create_texture_inspection_model` returns the value 2 (
H_MSG_TRUE)
in the texture inspection model can be allocated correctly. Otherwise, an
exception will be raised..

## Possible Successors

`set_texture_inspection_model_param`,
`get_texture_inspection_model_param`,
`add_texture_inspection_model_image`

## Module

Matching
