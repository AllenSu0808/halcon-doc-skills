# clear_deformable_model (Operator)

## Name

`clear_deformable_model` — Free the memory of a deformable model.

## Signature

`def clear_deformable_model(model_id: MaybeSequence[HHandle]) -> None`

## Description

The operator `clear_deformable_model` frees the memory of a deformable
model that was created by [`create_planar_uncalib_deformable_model`](create_planar_uncalib_deformable_model.md)
or [`create_planar_calib_deformable_model`](create_planar_calib_deformable_model.md).
After calling `clear_deformable_model`, the deformable model can no
longer be used. The handle *`model_id`* becomes invalid.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- model_id

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`model_id`** (input_control, state is modified)  deformable_model(-array) `→` MaybeSequence[HHandle]

Handle of the model.

## Result

If the parameters are valid, the operator
`clear_deformable_model` returns the value 2 (
H_MSG_TRUE)
. If
necessary an exception is raised.

## See also

`create_planar_uncalib_deformable_model`,
`create_planar_calib_deformable_model`,
`create_local_deformable_model`

## Module

Matching
