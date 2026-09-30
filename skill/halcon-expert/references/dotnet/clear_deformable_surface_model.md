# ClearDeformableSurfaceModel (Operator)

## Name

`ClearDeformableSurfaceModel` — Free the memory of a deformable surface model.

## Signature

`static void HOperatorSet.ClearDeformableSurfaceModel(HTuple deformableSurfaceModel)`

`static void HDeformableSurfaceModel.ClearDeformableSurfaceModel(HDeformableSurfaceModel[] deformableSurfaceModel)`

`void HDeformableSurfaceModel.ClearDeformableSurfaceModel()`

## Description

The operator `ClearDeformableSurfaceModel` frees the memory of a
deformable surface model that was created, for example, by
[`ReadDeformableSurfaceModel`](read_deformable_surface_model.md) or [`CreateDeformableSurfaceModel`](create_deformable_surface_model.md).
After calling `ClearDeformableSurfaceModel`, the model can no longer
be used. The handle *`deformableSurfaceModel`* becomes invalid.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- deformableSurfaceModel

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`deformableSurfaceModel`** (input_control, state is modified)  deformable_surface_model(-array) `→` [HDeformableSurfaceModel](HDeformableSurfaceModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the deformable surface model.

## Result

If the handle of the model is valid, the operator
`ClearDeformableSurfaceModel` returns the value 2 (
H_MSG_TRUE)
. If necessary an
exception is raised.

## Possible Predecessors

`ReadDeformableSurfaceModel`,
`CreateDeformableSurfaceModel`

## See also

`ReadDeformableSurfaceModel`,
`CreateDeformableSurfaceModel`

## Module

3D Metrology
