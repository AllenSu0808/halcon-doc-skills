# clear_ncc_model (Operator)

## Name

`clear_ncc_model` — Free the memory of an NCC model.

## Signature

`clear_ncc_model( : : ModelID : )`

## Description

The operator `clear_ncc_model` frees the memory of an NCC
model that was created by [`create_ncc_model`](create_ncc_model.md). After calling
`clear_ncc_model`, the model can no longer be used. The
handle *`ModelID`* becomes invalid.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- ModelID

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`ModelID`** (input_control, state is modified)  ncc_model `→`  (handle)

Handle of the model.

## Result

If the handle of the model is valid, the operator
`clear_ncc_model` returns the value 2 (
H_MSG_TRUE)
. If necessary an
exception is raised.

## Possible Predecessors

`create_ncc_model`,
`read_ncc_model`,
`write_ncc_model`,
`find_ncc_model`,
`find_ncc_models`

## Module

Matching
