# write_descriptor_model (Operator)

## Name

`write_descriptor_model` — Write a descriptor model to a file.

## Signature

`write_descriptor_model( : : ModelID, FileName : )`

## Description

The operator `write_descriptor_model` writes a descriptor model
to the file *`FileName`*. The model can be read again with
[`read_descriptor_model`](read_descriptor_model.md). The default HALCON file extension
for the descriptor model is 'dsm'.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`ModelID`** (input_control)  descriptor_model `→`  (handle)

Handle of a model to be saved.

**`FileName`** (input_control)  filename.write `→`  (string)

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
