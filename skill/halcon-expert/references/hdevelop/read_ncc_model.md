# read_ncc_model (Operator)

## Name

`read_ncc_model` — Read an NCC model from a file.

## Signature

`read_ncc_model( : : FileName : ModelID)`

## Description

The operator `read_ncc_model` reads an NCC model, which has
been written with [`write_ncc_model`](write_ncc_model.md), from the file
*`FileName`*. The default HALCON file extension for
the NCC model is 'ncm'.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`FileName`** (input_control)  filename.read `→`  (string)

File name.

File extension:
.`ncm`

**`ModelID`** (output_control)  ncc_model `→`  (handle)

Handle of the model.

## Result

If the file name is valid, the operator `read_ncc_model`
returns the value 2 (
H_MSG_TRUE)
. If necessary an exception is raised.

## Possible Successors

`find_ncc_model`,
`find_ncc_models`

## See also

`create_ncc_model`,
`clear_ncc_model`

## Module

Matching
