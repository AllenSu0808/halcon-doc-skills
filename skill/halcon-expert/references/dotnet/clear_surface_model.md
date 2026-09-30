# ClearSurfaceModel (Operator)

## Name

`ClearSurfaceModel` — Free the memory of a surface model.

## Signature

`static void HOperatorSet.ClearSurfaceModel(HTuple surfaceModelID)`

`static void HSurfaceModel.ClearSurfaceModel(HSurfaceModel[] surfaceModelID)`

`void HSurfaceModel.ClearSurfaceModel()`

## Description

The operator `ClearSurfaceModel` frees the memory of a
surface model that was created by [`ReadSurfaceModel`](read_surface_model.md) or
[`CreateSurfaceModel`](create_surface_model.md).
After calling `ClearSurfaceModel`, the model can no longer
be used. The handle *`surfaceModelID`* becomes invalid.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- surfaceModelID

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`surfaceModelID`** (input_control, state is modified)  surface_model(-array) `→` [HSurfaceModel](HSurfaceModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the surface model.

## Result

If the handle of the model is valid, the operator
`ClearSurfaceModel` returns the value 2 (
H_MSG_TRUE)
. If necessary an
exception is raised.

## Possible Predecessors

`ReadSurfaceModel`,
`CreateSurfaceModel`

## See also

`ReadSurfaceModel`,
`CreateSurfaceModel`

## Module

3D Metrology
