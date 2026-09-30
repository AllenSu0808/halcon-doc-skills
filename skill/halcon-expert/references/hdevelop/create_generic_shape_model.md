# create_generic_shape_model (Operator)

## Name

`create_generic_shape_model` — Create a shape model.

## Signature

`create_generic_shape_model( : : : ModelID)`

## Description

The operator `create_generic_shape_model` creates a shape
model and returns its handle in *`ModelID`*.

The created model is not trained. See [`train_generic_shape_model`](train_generic_shape_model.md)
for information about training a model.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`ModelID`** (output_control)  shape_model `→`  (handle)

Handle of the shape model.

## Result

If successful the operator `create_generic_shape_model` returns the
value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Successors

`set_generic_shape_model_param`,
`train_generic_shape_model`,
`write_shape_model`,
`set_shape_model_origin`

## Module

Matching
