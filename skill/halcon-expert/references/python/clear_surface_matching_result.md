# clear_surface_matching_result (Operator)

## Name

`clear_surface_matching_result` — Free the memory of a surface matching result.

## Signature

`def clear_surface_matching_result(surface_matching_result_id: MaybeSequence[HHandle]) -> None`

## Description

The operator `clear_surface_matching_result` frees the memory of a
surface matching result that was created by [`find_surface_model`](find_surface_model.md) or
[`refine_surface_model_pose`](refine_surface_model_pose.md).
After calling `clear_surface_matching_result`, the result can no longer
be used. The handle *`surface_matching_result_id`* becomes invalid.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- surface_matching_result_id

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`surface_matching_result_id`** (input_control, state is modified)  surface_matching_result(-array) `→` MaybeSequence[HHandle]

Handle of the surface matching result.

## Result

If the handle of the result is valid, the operator
`clear_surface_matching_result` returns the value 2 (
H_MSG_TRUE)
.
If necessary an exception is raised.

## Possible Predecessors

`find_surface_model`,
`refine_surface_model_pose`

## See also

`find_surface_model`,
`refine_surface_model_pose`

## Module

3D Metrology
