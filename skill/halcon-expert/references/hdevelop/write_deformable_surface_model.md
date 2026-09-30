# write_deformable_surface_model (Operator)

## Name

`write_deformable_surface_model` — Write a deformable surface model to a file.

## Signature

`write_deformable_surface_model( : : DeformableSurfaceModel, FileName : )`

## Description

The operator `write_deformable_surface_model` writes a deformable
surface model to the file *`FileName`*.
The file can be read again with [`read_deformable_surface_model`](read_deformable_surface_model.md).
The default HALCON file extension for the deformable surface model
file is 'dsfm'.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`DeformableSurfaceModel`** (input_control)  deformable_surface_model `→`  (handle)

Handle of the deformable surface model to write.

**`FileName`** (input_control)  filename.write `→`  (string)

File name to write to.

File extension:
.`dsfm`

## Result

`write_deformable_surface_model` returns 2 (
H_MSG_TRUE)
if all parameters are
correct and the HALCON process has write permission to the file.
If necessary, an exception is raised.

## Possible Predecessors

`read_deformable_surface_model`,
`create_deformable_surface_model`,
`get_deformable_surface_model_param`

## Possible Successors

`clear_deformable_surface_model`

## See also

`create_deformable_surface_model`,
`read_deformable_surface_model`

## Module

3D Metrology
