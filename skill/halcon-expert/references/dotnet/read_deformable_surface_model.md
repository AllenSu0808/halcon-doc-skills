# ReadDeformableSurfaceModel (Operator)

## Name

`ReadDeformableSurfaceModel` — Read a deformable surface model from a file.

## Signature

`static void HOperatorSet.ReadDeformableSurfaceModel(HTuple fileName, out HTuple deformableSurfaceModel)`

`public HDeformableSurfaceModel(string fileName)`

`void HDeformableSurfaceModel.ReadDeformableSurfaceModel(string fileName)`

## Description

The operator `ReadDeformableSurfaceModel` reads the deformable
surface model, which has been written with
[`WriteDeformableSurfaceModel`](write_deformable_surface_model.md), from the file *`fileName`*.
The handle of the deformable surface model is returned in
*`deformableSurfaceModel`*.
If no absolute path is given in *`fileName`*, the file is searched
in the current directory of the HALCON process.
The default HALCON file extension for the deformable surface model file is
'dsfm'.
If no file named *`fileName`* exists, the default file extension is
appended to *`fileName`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`fileName`** (input_control)  filename.read `→` [HTuple](HTuple.md) (*string*)

Name of the file to read.

File extension:
.`dsfm`

**`deformableSurfaceModel`** (output_control)  deformable_surface_model `→` [HDeformableSurfaceModel](HDeformableSurfaceModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the read deformable surface model.

## Result

`ReadDeformableSurfaceModel` returns 2 (
H_MSG_TRUE)
if all parameters are
correct and the file can be read.
If the file is not a deformable surface model file, the error 9506 is raised.
If the file has a version that can not be read by this version of HALCON,
the error 9507 is raised.
If necessary, an exception is raised.

## Possible Predecessors

`WriteDeformableSurfaceModel`

## Possible Successors

`FindDeformableSurfaceModel`,
`RefineDeformableSurfaceModel`,
`GetDeformableSurfaceModelParam`,
`ClearDeformableSurfaceModel`

## Alternatives

`CreateDeformableSurfaceModel`

## See also

`CreateDeformableSurfaceModel`,
`WriteDeformableSurfaceModel`

## Module

3D Metrology
