# clear_texture_inspection_model (Operator)

## Name

`clear_texture_inspection_model` — Clear a texture inspection model and free the allocated memory.

## Signature

`clear_texture_inspection_model( : : TextureInspectionModel : )`

## Description

The operator `clear_texture_inspection_model` deletes a texture
inspection model that was created by [`create_texture_inspection_model`](create_texture_inspection_model.md).
All memory used by the model is freed.
The handle of the model is passed in *`TextureInspectionModel`*. It is
invalid after the operator call.

For an explanation of the concept of the texture inspection
see the introduction of chapter [Inspection / Texture Inspection](toc_inspection_texture.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- TextureInspectionModel

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`TextureInspectionModel`** (input_control, state is modified)  texture_inspection_model(-array) `→`  (handle)

Handle of the texture inspection model.

## Example (HDevelop)

```
* Create texture inspection model
create_texture_inspection_model ('basic', TextureInspectionModel)
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

The operator `clear_texture_inspection_model` returns the value 2 (
H_MSG_TRUE)
if a valid handle is passed and the referred texture inspection model can
be freed correctly. Otherwise, an exception will be raised.

## See also

`create_texture_inspection_model`

## Module

Matching
