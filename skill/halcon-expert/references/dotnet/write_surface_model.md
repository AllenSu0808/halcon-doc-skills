# WriteSurfaceModel (Operator)

## Name

`WriteSurfaceModel` — Write a surface model to a file.

## Signature

`static void HOperatorSet.WriteSurfaceModel(HTuple surfaceModelID, HTuple fileName)`

`void HSurfaceModel.WriteSurfaceModel(string fileName)`

## Description

The operator `WriteSurfaceModel` writes a surface model to the file
*`fileName`*.
The file can be read again with [`ReadSurfaceModel`](read_surface_model.md).
The default HALCON file extension for the surface model (SFM) file is
'sfm'.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`surfaceModelID`** (input_control)  surface_model `→` [HSurfaceModel](HSurfaceModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the surface model.

**`fileName`** (input_control)  filename.write `→` [HTuple](HTuple.md) (*string*)

File name.

File extension:
.`sfm`

## Result

`WriteSurfaceModel` returns 2 (
H_MSG_TRUE)
if all parameters are
correct and the HALCON process has write permission to the file.
If necessary, an exception is raised.

## Possible Predecessors

`ReadSurfaceModel`,
`CreateSurfaceModel`,
`GetSurfaceModelParam`

## Possible Successors

`ClearSurfaceModel`

## See also

`CreateSurfaceModel`,
`ReadSurfaceModel`

## Module

3D Metrology
