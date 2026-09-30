# clear_variation_model (Operator)

## Name

`clear_variation_model` — Free the memory of a variation model.

## Signature

`clear_variation_model( : : ModelID : )`

## Description

`clear_variation_model` frees the memory of a variation model
that was created by [`create_variation_model`](create_variation_model.md). After calling
[`create_variation_model`](create_variation_model.md), the model can no longer be used.
The handle *`ModelID`* becomes invalid.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- ModelID

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`ModelID`** (input_control, state is modified)  variation_model `→`  (handle)

ID of the variation model.

## Result

`clear_variation_model` returns 2 (
H_MSG_TRUE)
if all parameters are
correct.

## Possible Predecessors

`create_variation_model`

## Module

Matching
