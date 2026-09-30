# write_texture_inspection_model (Operator)

## Name

`write_texture_inspection_model` — Write a texture inspection model to a file.

## Signature

`def write_texture_inspection_model(texture_inspection_model: HHandle, file_name: str) -> None`

## Description

`write_texture_inspection_model` writes the texture inspection model
*`texture_inspection_model`* to the file given by *`file_name`*.
The default HALCON file extension for the texture inspection model is
'htim'. `write_texture_inspection_model` is typically called after
the texture inspection model has been trained with
[`train_texture_inspection_model`](train_texture_inspection_model.md). However, it can also be used to
save an untrained model.
The texture inspection model can be read with
[`read_texture_inspection_model`](read_texture_inspection_model.md).
It should be noted that `write_texture_inspection_model` does
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

**`texture_inspection_model`** (input_control)  texture_inspection_model `→` HHandle

Handle of the texture inspection model.

**`file_name`** (input_control)  filename.write `→` str

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
`write_texture_inspection_model` returns the value 2 (
H_MSG_TRUE)
. If necessary
an exception is raised.

## Possible Predecessors

`train_texture_inspection_model`

## Possible Successors

`clear_texture_inspection_model`

## See also

`create_texture_inspection_model`,
`clear_texture_inspection_model`,
`set_texture_inspection_model_param`,
`get_texture_inspection_model_param`,
`add_texture_inspection_model_image`

## Module

Matching
