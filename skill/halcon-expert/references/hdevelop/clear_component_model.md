# clear_component_model (Operator)

## Name

`clear_component_model` — Free the memory of a component model.

## Warning

**`clear_component_model` is obsolete and is only provided for
reasons of backward compatibility.
The operator will be removed with HALCON 26.11.**

## Signature

`clear_component_model( : : ComponentModelID : )`

## Description

The operator `clear_component_model` frees the memory of a
component model that was created by [`create_component_model`](create_component_model.md)
or [`create_trained_component_model`](create_trained_component_model.md). After calling
`clear_component_model`, the model can no longer be used. The
handle *`ComponentModelID`* becomes invalid.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- ComponentModelID

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`ComponentModelID`** (input_control, state is modified)  component_model `→`  (handle)

Handle of the component model.

## Result

If the handle of the model is valid, the operator
`clear_component_model` returns the value 2 (
H_MSG_TRUE)
.
If necessary, an exception is raised.

## Module

Matching
