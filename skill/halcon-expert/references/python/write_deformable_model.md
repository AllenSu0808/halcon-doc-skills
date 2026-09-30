# write_deformable_model (Operator)

## Name

`write_deformable_model` — Write a deformable model to a file.

## Signature

`def write_deformable_model(model_id: HHandle, file_name: str) -> None`

## Description

The operator `write_deformable_model` writes a deformable model
to the file *`file_name`*. The model can be read again with
[`read_deformable_model`](read_deformable_model.md). The default HALCON file extension for
the deformable model is 'dfm'.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`model_id`** (input_control)  deformable_model `→` HHandle

Handle of a model to be saved.

**`file_name`** (input_control)  filename.write `→` str

The path and filename of the model to be saved.

File extension:
.`dfm`

## Possible Predecessors

`create_planar_uncalib_deformable_model`,
`create_planar_calib_deformable_model`,
`create_local_deformable_model`

## Module

Matching
