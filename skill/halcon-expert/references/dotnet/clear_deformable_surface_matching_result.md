# ClearDeformableSurfaceMatchingResult (Operator)

## Name

`ClearDeformableSurfaceMatchingResult` — Free the memory of a deformable surface matching result.

## Signature

`static void HOperatorSet.ClearDeformableSurfaceMatchingResult(HTuple deformableSurfaceMatchingResult)`

`static void HDeformableSurfaceMatchingResult.ClearDeformableSurfaceMatchingResult(HDeformableSurfaceMatchingResult[] deformableSurfaceMatchingResult)`

`void HDeformableSurfaceMatchingResult.ClearDeformableSurfaceMatchingResult()`

## Description

The operator `ClearDeformableSurfaceMatchingResult` frees the memory of a
deformable surface matching result that was created with [`FindDeformableSurfaceModel`](find_deformable_surface_model.md) or
[`RefineDeformableSurfaceModel`](refine_deformable_surface_model.md).
After calling `ClearDeformableSurfaceMatchingResult`, the result can no longer
be used. The handle *`deformableSurfaceMatchingResult`* becomes invalid.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- deformableSurfaceMatchingResult

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`deformableSurfaceMatchingResult`** (input_control, state is modified)  deformable_surface_matching_result(-array) `→` [HDeformableSurfaceMatchingResult](HDeformableSurfaceMatchingResult.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the deformable surface matching result.

## Result

If the handle of the result is valid, the operator
`ClearDeformableSurfaceMatchingResult` returns the value 2 (
H_MSG_TRUE)
.
If necessary an exception is raised.

## Possible Predecessors

`FindDeformableSurfaceModel`,
`RefineDeformableSurfaceModel`

## See also

`FindDeformableSurfaceModel`,
`RefineDeformableSurfaceModel`

## Module

3D Metrology
