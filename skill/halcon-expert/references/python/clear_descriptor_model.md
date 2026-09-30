# clear_descriptor_model (Operator)

## Name

`clear_descriptor_model` — Free the memory of a descriptor model.

## Signature

`def clear_descriptor_model(model_id: MaybeSequence[HHandle]) -> None`

## Description

The operator `clear_descriptor_model` frees the memory of a
descriptor model that was created by
[`create_calib_descriptor_model`](create_calib_descriptor_model.md)
or [`create_uncalib_descriptor_model`](create_uncalib_descriptor_model.md).
After calling `clear_descriptor_model`, the model can no longer be
used. The handle *`model_id`* becomes invalid.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- model_id

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`model_id`** (input_control, state is modified)  descriptor_model(-array) `→` MaybeSequence[HHandle]

Handle of the descriptor model.

## Result

If the handle of the model is valid, the operator
`clear_descriptor_model` returns the value 2 (
H_MSG_TRUE)
. If necessary
an exception is raised.

## See also

`create_uncalib_descriptor_model`,
`create_calib_descriptor_model`

## Module

Matching
