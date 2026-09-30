# clear_metrology_model (Operator)

## Name

`clear_metrology_model` — Delete a metrology model and free the allocated memory.

## Signature

`def clear_metrology_model(metrology_handle: HHandle) -> None`

## Description

`clear_metrology_model` deletes a metrology model that was
created by [`create_metrology_model`](create_metrology_model.md), [`copy_metrology_model`](copy_metrology_model.md),
[`read_metrology_model`](read_metrology_model.md), or [`deserialize_metrology_model`](deserialize_metrology_model.md).
Note that by deleting the model also the including
metrology objects are deleted. All memory used by the metrology
model and the metrology objects is freed. The handle of the model is
passed in *`metrology_handle`*. After the operator call, the
metrology model is invalid.

For an explanation of the concept of 2D metrology see the
introduction of chapter [2D Metrology](toc_2dmetrology.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- metrology_handle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`metrology_handle`** (input_control, state is modified)  metrology_model `→` HHandle

Handle of the metrology model.

## Result

The operator `clear_metrology_model` returns the value 2 (
H_MSG_TRUE)
if a valid handle was passed and the referred metrology model can
be freed correctly. Otherwise, an exception will be raised.

## Possible Predecessors

`get_metrology_object_result`,
`write_metrology_model`

## Module

2D Metrology
