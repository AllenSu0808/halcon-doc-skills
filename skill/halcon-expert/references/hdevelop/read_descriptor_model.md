# read_descriptor_model (Operator)

## Name

`read_descriptor_model` — Read a descriptor model from a file.

## Signature

`read_descriptor_model( : : FileName : ModelID)`

## Description

The operator `read_descriptor_model` reads a descriptor
model, which has been written with [`write_descriptor_model`](write_descriptor_model.md),
from the file *`FileName`*. The default HALCON file extension
for the descriptor model is 'dsm'.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`FileName`** (input_control)  filename.read `→`  (string)

File name.

File extension:
.`dsm`

**`ModelID`** (output_control)  descriptor_model `→`  (handle)

Handle of the model.

## Possible Successors

`find_uncalib_descriptor_model`,
`find_calib_descriptor_model`

## See also

`create_calib_descriptor_model`,
`create_uncalib_descriptor_model`

## Module

Matching
