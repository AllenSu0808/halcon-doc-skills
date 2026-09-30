# write_shape_model (Operator)

## Name

`write_shape_model` — Write a shape model to a file.

## Signature

`write_shape_model( : : ModelID, FileName : )`

## Description

The operator `write_shape_model` writes a shape model to the
file *`FileName`*. The model can be read again with
[`read_shape_model`](read_shape_model.md). The default HALCON file extension for
the shape model is 'shm'.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`ModelID`** (input_control)  shape_model `→`  (handle)

Handle of the model.

**`FileName`** (input_control)  filename.write `→`  (string)

File name.

File extension:
.`shm`

## Result

If the file name is valid (write permission), the operator
`write_shape_model` returns the value 2 (
H_MSG_TRUE)
. If necessary an
exception is raised.

## Possible Predecessors

`set_generic_shape_model_param`,
`set_generic_shape_model_object`

## Module

Matching
