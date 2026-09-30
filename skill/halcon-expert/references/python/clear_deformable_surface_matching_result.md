# clear_deformable_surface_matching_result (Operator)

## Name

`clear_deformable_surface_matching_result` — Free the memory of a deformable surface matching result.

## Signature

`def clear_deformable_surface_matching_result(deformable_surface_matching_result: MaybeSequence[HHandle]) -> None`

## Description

The operator `clear_deformable_surface_matching_result` frees the memory of a
deformable surface matching result that was created with [`find_deformable_surface_model`](find_deformable_surface_model.md) or
[`refine_deformable_surface_model`](refine_deformable_surface_model.md).
After calling `clear_deformable_surface_matching_result`, the result can no longer
be used. The handle *`deformable_surface_matching_result`* becomes invalid.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- deformable_surface_matching_result

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`deformable_surface_matching_result`** (input_control, state is modified)  deformable_surface_matching_result(-array) `→` MaybeSequence[HHandle]

Handle of the deformable surface matching result.

## Result

If the handle of the result is valid, the operator
`clear_deformable_surface_matching_result` returns the value 2 (
H_MSG_TRUE)
.
If necessary an exception is raised.

## Possible Predecessors

`find_deformable_surface_model`,
`refine_deformable_surface_model`

## See also

`find_deformable_surface_model`,
`refine_deformable_surface_model`

## Module

3D Metrology
