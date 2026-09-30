# ClearSurfaceMatchingResult (Operator)

## Name

`ClearSurfaceMatchingResult` — Free the memory of a surface matching result.

## Signature

`static void HOperatorSet.ClearSurfaceMatchingResult(HTuple surfaceMatchingResultID)`

`static void HSurfaceMatchingResult.ClearSurfaceMatchingResult(HSurfaceMatchingResult[] surfaceMatchingResultID)`

`void HSurfaceMatchingResult.ClearSurfaceMatchingResult()`

## Description

The operator `ClearSurfaceMatchingResult` frees the memory of a
surface matching result that was created by [`FindSurfaceModel`](find_surface_model.md) or
[`RefineSurfaceModelPose`](refine_surface_model_pose.md).
After calling `ClearSurfaceMatchingResult`, the result can no longer
be used. The handle *`surfaceMatchingResultID`* becomes invalid.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- surfaceMatchingResultID

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`surfaceMatchingResultID`** (input_control, state is modified)  surface_matching_result(-array) `→` [HSurfaceMatchingResult](HSurfaceMatchingResult.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the surface matching result.

## Result

If the handle of the result is valid, the operator
`ClearSurfaceMatchingResult` returns the value 2 (
H_MSG_TRUE)
.
If necessary an exception is raised.

## Possible Predecessors

`FindSurfaceModel`,
`RefineSurfaceModelPose`

## See also

`FindSurfaceModel`,
`RefineSurfaceModelPose`

## Module

3D Metrology
