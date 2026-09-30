# clear_shape_model (Operator)

## Name

`clear_shape_model` — Free the memory of a shape model.

## Signature

`clear_shape_model( : : ModelID : )`

## Description

The operator `clear_shape_model` frees the memory of a shape
model that was created by [`create_shape_model`](create_shape_model.md),
[`create_scaled_shape_model`](create_scaled_shape_model.md), or
[`create_aniso_shape_model`](create_aniso_shape_model.md). After calling
`clear_shape_model`, the model can no longer be used. The
handle *`ModelID`* becomes invalid.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- ModelID

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`ModelID`** (input_control, state is modified)  shape_model `→`  (handle)

Handle of the model.

## Result

If the handle of the model is valid, the operator
`clear_shape_model` returns the value 2 (
H_MSG_TRUE)
. If necessary an
exception is raised.

## Possible Predecessors

`create_generic_shape_model`,
`write_shape_model`

## Module

Matching
