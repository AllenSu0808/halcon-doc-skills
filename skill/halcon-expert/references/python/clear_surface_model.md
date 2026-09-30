# clear_surface_model (Operator)

## Name

`clear_surface_model` — Free the memory of a surface model.

## Signature

`def clear_surface_model(surface_model_id: MaybeSequence[HHandle]) -> None`

## Description

The operator `clear_surface_model` frees the memory of a
surface model that was created by [`read_surface_model`](read_surface_model.md) or
[`create_surface_model`](create_surface_model.md).
After calling `clear_surface_model`, the model can no longer
be used. The handle *`surface_model_id`* becomes invalid.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- surface_model_id

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`surface_model_id`** (input_control, state is modified)  surface_model(-array) `→` MaybeSequence[HHandle]

Handle of the surface model.

## Result

If the handle of the model is valid, the operator
`clear_surface_model` returns the value 2 (
H_MSG_TRUE)
. If necessary an
exception is raised.

## Possible Predecessors

`read_surface_model`,
`create_surface_model`

## See also

`read_surface_model`,
`create_surface_model`

## Module

3D Metrology
