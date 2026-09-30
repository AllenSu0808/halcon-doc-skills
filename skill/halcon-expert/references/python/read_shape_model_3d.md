# read_shape_model_3d (Operator)

## Name

`read_shape_model_3d` — Read a 3D shape model from a file.

## Signature

`def read_shape_model_3d(file_name: str) -> HHandle`

## Description

The operator `read_shape_model_3d` reads a 3D shape model, which
has been written with [`write_shape_model_3d`](write_shape_model_3d.md), from the file
*`file_name`*. The default HALCON file extension for the 3D
shape model is 'sm3'.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`file_name`** (input_control)  filename.read `→` str

File name.

File extension:
.`sm3`

**`shape_model_3did`** (output_control)  shape_model_3d `→` HHandle

Handle of the 3D shape model.

## Result

If the file name is valid, the operator `read_shape_model_3d`
returns the value 2 (
H_MSG_TRUE)
. If necessary an exception is raised.

## Possible Successors

`find_shape_model_3d`,
`get_shape_model_3d_params`

## See also

`create_shape_model_3d`,
`clear_shape_model_3d`

## Module

3D Metrology
