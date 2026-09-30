# clear_bead_inspection_model (Operator)

## Name

`clear_bead_inspection_model` — Delete the bead inspection model and free the allocated memory.

## Signature

`def clear_bead_inspection_model(bead_inspection_model: HHandle) -> None`

## Description

The operator `clear_bead_inspection_model` deletes a bead inspection
model that was created by [`create_bead_inspection_model`](create_bead_inspection_model.md).
All memory used by the model is freed.
The handle of the model is passed in *`bead_inspection_model`*. It is
invalid after the operator call.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- bead_inspection_model

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`bead_inspection_model`** (input_control, state is modified)  bead_inspection_model `→` HHandle

Handle of the bead inspection model.

## Result

The operator `clear_bead_inspection_model` returns the value 2 (
H_MSG_TRUE)
if a valid handle is passed and the referred bead inspection model can
be freed correctly.
Otherwise, an exception will be raised.

## Possible Predecessors

`create_bead_inspection_model`

## See also

`create_bead_inspection_model`

## Module

2D Metrology
