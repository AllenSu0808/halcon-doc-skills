# write_surface_model (Operator)

## Name

`write_surface_model` — Write a surface model to a file.

## Signature

`write_surface_model( : : SurfaceModelID, FileName : )`

## Description

The operator `write_surface_model` writes a surface model to the file
*`FileName`*.
The file can be read again with [`read_surface_model`](read_surface_model.md).
The default HALCON file extension for the surface model (SFM) file is
'sfm'.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`SurfaceModelID`** (input_control)  surface_model `→`  (handle)

Handle of the surface model.

**`FileName`** (input_control)  filename.write `→`  (string)

File name.

File extension:
.`sfm`

## Result

`write_surface_model` returns 2 (
H_MSG_TRUE)
if all parameters are
correct and the HALCON process has write permission to the file.
If necessary, an exception is raised.

## Possible Predecessors

`read_surface_model`,
`create_surface_model`,
`get_surface_model_param`

## Possible Successors

`clear_surface_model`

## See also

`create_surface_model`,
`read_surface_model`

## Module

3D Metrology
