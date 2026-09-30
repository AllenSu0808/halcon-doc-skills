# write_ncc_model (Operator)

## Name

`write_ncc_model` — Write an NCC model to a file.

## Signature

`write_ncc_model( : : ModelID, FileName : )`

## Description

The operator `write_ncc_model` writes an NCC model to the file
*`FileName`*. The model can be read again with
[`read_ncc_model`](read_ncc_model.md). The default HALCON file extension for
the NCC model is 'ncm'.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`ModelID`** (input_control)  ncc_model `→`  (handle)

Handle of the model.

**`FileName`** (input_control)  filename.write `→`  (string)

File name.

File extension:
.`ncm`

## Result

If the file name is valid (write permission), the operator
`write_ncc_model` returns the value 2 (
H_MSG_TRUE)
. If necessary an
exception is raised.

## Possible Predecessors

`create_ncc_model`

## Module

Matching
