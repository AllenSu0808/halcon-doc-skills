# write_shape_model_3d (Operator)

## Name

`write_shape_model_3d` — Write a 3D shape model to a file.

## Signature

`write_shape_model_3d( : : ShapeModel3DID, FileName : )`

## Description

The operator `write_shape_model_3d` writes a 3D shape model to
the file *`FileName`*. The model can be read again with
[`read_shape_model_3d`](read_shape_model_3d.md). The default HALCON file extension for the
3D shape model is 'sm3'.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`ShapeModel3DID`** (input_control)  shape_model_3d `→`  (handle)

Handle of the 3D shape model.

**`FileName`** (input_control)  filename.write `→`  (string)

File name.

File extension:
.`sm3`

## Result

If the file name is valid (write permission), the operator
`write_shape_model_3d` returns the value 2 (
H_MSG_TRUE)
. If necessary
an exception is raised.

## Possible Predecessors

`create_shape_model_3d`

## Module

3D Metrology
