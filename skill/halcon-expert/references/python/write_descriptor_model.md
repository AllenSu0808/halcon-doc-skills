# write_descriptor_model (Operator)

## Name

`write_descriptor_model` — Write a descriptor model to a file.

## Signature

`def write_descriptor_model(model_id: HHandle, file_name: str) -> None`

## Description

The operator `write_descriptor_model` writes a descriptor model
to the file *`file_name`*. The model can be read again with
[`read_descriptor_model`](read_descriptor_model.md). The default HALCON file extension
for the descriptor model is 'dsm'.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`model_id`** (input_control)  descriptor_model `→` HHandle

Handle of a model to be saved.

**`file_name`** (input_control)  filename.write `→` str

The path and filename of the model to be saved.

File extension:
.`dsm`

## Possible Predecessors

`points_lepetit`,
`create_uncalib_descriptor_model`,
`create_calib_descriptor_model`

## See also

`create_uncalib_descriptor_model`,
`create_calib_descriptor_model`

## Module

Matching
