# write_deformable_model (Operator)

## Name

`write_deformable_model` — Write a deformable model to a file.

## Signature

`write_deformable_model( : : ModelID, FileName : )`

## Description

The operator `write_deformable_model` writes a deformable model
to the file *`FileName`*. The model can be read again with
[`read_deformable_model`](read_deformable_model.md). The default HALCON file extension for
the deformable model is 'dfm'.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`ModelID`** (input_control)  deformable_model `→`  (handle)

Handle of a model to be saved.

**`FileName`** (input_control)  filename.write `→`  (string)

The path and filename of the model to be saved.

File extension:
.`dfm`

## Possible Predecessors

`create_planar_uncalib_deformable_model`,
`create_planar_calib_deformable_model`,
`create_local_deformable_model`

## Module

Matching
