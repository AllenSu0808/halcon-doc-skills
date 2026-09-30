# clear_shape_model_3d (Operator)

## Name

`clear_shape_model_3d` — Free the memory of a 3D shape model.

## Signature

`def clear_shape_model_3d(shape_model_3did: MaybeSequence[HHandle]) -> None`

## Description

The operator `clear_shape_model_3d` frees the memory of a 3D
shape model that was created by [`create_shape_model_3d`](create_shape_model_3d.md).
After calling `clear_shape_model_3d`, the model can no longer
be used. The handle *`shape_model_3did`* becomes invalid.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- shape_model_3did

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`shape_model_3did`** (input_control, state is modified)  shape_model_3d(-array) `→` MaybeSequence[HHandle]

Handle of the 3D shape model.

## Result

If the handle of the model is valid, the operator
`clear_shape_model_3d` returns the value 2 (
H_MSG_TRUE)
. If necessary an
exception is raised.

## Possible Predecessors

`create_shape_model_3d`,
`read_shape_model_3d`,
`write_shape_model_3d`

## Module

3D Metrology
