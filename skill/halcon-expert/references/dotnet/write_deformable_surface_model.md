# WriteDeformableSurfaceModel (Operator)

## Name

`WriteDeformableSurfaceModel` — Write a deformable surface model to a file.

## Signature

`static void HOperatorSet.WriteDeformableSurfaceModel(HTuple deformableSurfaceModel, HTuple fileName)`

`void HDeformableSurfaceModel.WriteDeformableSurfaceModel(string fileName)`

## Description

The operator `WriteDeformableSurfaceModel` writes a deformable
surface model to the file *`fileName`*.
The file can be read again with [`ReadDeformableSurfaceModel`](read_deformable_surface_model.md).
The default HALCON file extension for the deformable surface model
file is 'dsfm'.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`deformableSurfaceModel`** (input_control)  deformable_surface_model `→` [HDeformableSurfaceModel](HDeformableSurfaceModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the deformable surface model to write.

**`fileName`** (input_control)  filename.write `→` [HTuple](HTuple.md) (*string*)

File name to write to.

File extension:
.`dsfm`

## Result

`WriteDeformableSurfaceModel` returns 2 (
H_MSG_TRUE)
if all parameters are
correct and the HALCON process has write permission to the file.
If necessary, an exception is raised.

## Possible Predecessors

`ReadDeformableSurfaceModel`,
`CreateDeformableSurfaceModel`,
`GetDeformableSurfaceModelParam`

## Possible Successors

`ClearDeformableSurfaceModel`

## See also

`CreateDeformableSurfaceModel`,
`ReadDeformableSurfaceModel`

## Module

3D Metrology
