# ReadSurfaceModel (Operator)

## Name

`ReadSurfaceModel` — Read a surface model from a file.

## Signature

`static void HOperatorSet.ReadSurfaceModel(HTuple fileName, out HTuple surfaceModelID)`

`public HSurfaceModel(string fileName)`

`void HSurfaceModel.ReadSurfaceModel(string fileName)`

## Description

The operator `ReadSurfaceModel` reads the surface model, which has
been written with [`WriteSurfaceModel`](write_surface_model.md), from the file
*`fileName`*.
The handle of the surface model is returned in *`surfaceModelID`*.
If no absolute path is given in *`fileName`*, the file is searched
in the current directory of the HALCON process.
The default HALCON file extension for the surface model (SFM) file is
'sfm'.
If no file named *`fileName`* exists, the default file extension is
appended to *`fileName`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`fileName`** (input_control)  filename.read `→` [HTuple](HTuple.md) (*string*)

Name of the SFM file.

File extension:
.`sfm`

**`surfaceModelID`** (output_control)  surface_model `→` [HSurfaceModel](HSurfaceModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the read surface model.

## Result

`ReadSurfaceModel` returns 2 (
H_MSG_TRUE)
if all parameters are
correct and the file can be read.
If the file is not a surface model file, the error 9506 is raised.
If the file has a version that can not be read by this version of HALCON,
the error 9507 is raised.
If necessary, an exception is raised.

## Possible Predecessors

`ReadObjectModel3d`,
`XyzToObjectModel3d`

## Possible Successors

`FindSurfaceModel`,
`RefineSurfaceModelPose`,
`GetSurfaceModelParam`,
`ClearSurfaceModel`,
`FindSurfaceModelImage`,
`RefineSurfaceModelPoseImage`

## Alternatives

`CreateSurfaceModel`

## See also

`CreateSurfaceModel`,
`WriteSurfaceModel`

## Module

3D Metrology
