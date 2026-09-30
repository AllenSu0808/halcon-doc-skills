# read_shape_model (Operator)

## Name

`read_shape_model` — Read a shape model from a file.

## Signature

`def read_shape_model(file_name: str) -> HHandle`

## Description

The operator `read_shape_model` reads a shape model, which has
been written with [`write_shape_model`](write_shape_model.md), from the file
*`file_name`*. The default HALCON file extension for
the shape model is 'shm'.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`file_name`** (input_control)  filename.read `→` str

File name.

File extension:
.`shm`

**`model_id`** (output_control)  shape_model `→` HHandle

Handle of the model.

## Result

If the file name is valid, the operator `read_shape_model`
returns the value 2 (
H_MSG_TRUE)
. If necessary an exception is raised.

## Possible Successors

`find_generic_shape_model`

## Module

Matching
