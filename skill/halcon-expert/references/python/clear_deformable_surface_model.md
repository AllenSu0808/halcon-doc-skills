# clear_deformable_surface_model (Operator)

## Name

`clear_deformable_surface_model` — Free the memory of a deformable surface model.

## Signature

`def clear_deformable_surface_model(deformable_surface_model: MaybeSequence[HHandle]) -> None`

## Description

The operator `clear_deformable_surface_model` frees the memory of a
deformable surface model that was created, for example, by
[`read_deformable_surface_model`](read_deformable_surface_model.md) or [`create_deformable_surface_model`](create_deformable_surface_model.md).
After calling `clear_deformable_surface_model`, the model can no longer
be used. The handle *`deformable_surface_model`* becomes invalid.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- deformable_surface_model

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`deformable_surface_model`** (input_control, state is modified)  deformable_surface_model(-array) `→` MaybeSequence[HHandle]

Handle of the deformable surface model.

## Result

If the handle of the model is valid, the operator
`clear_deformable_surface_model` returns the value 2 (
H_MSG_TRUE)
. If necessary an
exception is raised.

## Possible Predecessors

`read_deformable_surface_model`,
`create_deformable_surface_model`

## See also

`read_deformable_surface_model`,
`create_deformable_surface_model`

## Module

3D Metrology
