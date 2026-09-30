# read_texture_inspection_model (Operator)

## Name

`read_texture_inspection_model` — Read a texture inspection model from a file.

## Signature

`def read_texture_inspection_model(file_name: str) -> HHandle`

## Description

`read_texture_inspection_model` reads a texture inspection model that
has been stored with [`write_texture_inspection_model`](write_texture_inspection_model.md). Since the
training of a texture inspection model can consume a relatively long time,
the texture inspection model is typically trained in an offline process and
written to a file with [`write_texture_inspection_model`](write_texture_inspection_model.md). In the online
process the texture inspection model is read with
`read_texture_inspection_model` and subsequently used for evaluation
with [`apply_texture_inspection_model`](apply_texture_inspection_model.md).
The default HALCON file extension for the texture inspection model is
'htim'.

After reading a trained texture inspection model, it is possible to
classify test images using [`apply_texture_inspection_model`](apply_texture_inspection_model.md). However,
retraining this model can only be done, if the read model has images.
Furthermore, modifying parameters of the model leads to an entire retraining.

For an explanation of the concept of the texture inspection
see the introduction of chapter [Inspection / Texture Inspection](toc_inspection_texture.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`file_name`** (input_control)  filename.read `→` str

File name.

File extension:
.`htim`

**`texture_inspection_model`** (output_control)  texture_inspection_model `→` HHandle

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
add_texture_inspection_model_image (TrainImage, TextureInspectionModel, \
                                    Indices)
* Train the model
train_texture_inspection_model (TextureInspectionModel)
* Write out texture inspection model
write_texture_inspection_model (TextureInspectionModel, \
                                'ExampleModel.htim')
* Read in Model
read_texture_inspection_model ('ExampleModel.htim', \
                               TextureInspectionModelRead)
* Read and apply a test image
read_image (TestImage, 'carpet/carpet_02')
apply_texture_inspection_model (TestImage, DefectCandidates, \
                                TextureInspectionModelRead, \
                                TextureInspectionResultID)
```

## Result

If the parameters are valid, the operator
`read_texture_inspection_model` returns the value 2 (
H_MSG_TRUE)
. If necessary
an exception is raised.

## Possible Predecessors

`write_texture_inspection_model`

## Possible Successors

`apply_texture_inspection_model`

## See also

`create_texture_inspection_model`,
`clear_texture_inspection_model`,
`set_texture_inspection_model_param`,
`get_texture_inspection_model_param`,
`add_texture_inspection_model_image`

## Module

Matching
