# read_deformable_model (Operator)

## Name

`read_deformable_model` — Read a deformable model from a file.

## Signature

`read_deformable_model( : : FileName : ModelID)`

## Description

The operator `read_deformable_model` reads a deformable model from the
file *`FileName`*, which has been written with
[`write_deformable_model`](write_deformable_model.md). The default HALCON file extension for the
deformable model is 'dfm'.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`FileName`** (input_control)  filename.read `→`  (string)

File name.

File extension:
.`dfm`

**`ModelID`** (output_control)  deformable_model `→`  (handle)

Handle of the model.

## Possible Successors

`find_planar_uncalib_deformable_model`,
`find_planar_calib_deformable_model`,
`find_local_deformable_model`

## See also

`create_planar_uncalib_deformable_model`,
`create_planar_calib_deformable_model`,
`create_local_deformable_model`

## Module

Matching
