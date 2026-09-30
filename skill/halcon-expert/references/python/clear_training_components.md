# clear_training_components (Operator)

## Name

`clear_training_components` — Free the memory of a component training result.

## Warning

**`clear_training_components` is obsolete and is only provided for
reasons of backward compatibility.
The operator will be removed with HALCON 26.11.**

## Signature

`def clear_training_components(component_training_id: HHandle) -> None`

## Description

The operator `clear_training_components` frees the memory of a
training result that was created by [`train_model_components`](train_model_components.md).
After calling `clear_training_components`, the training result
can no longer be used. The handle *`component_training_id`*
becomes invalid.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- component_training_id

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`component_training_id`** (input_control, state is modified)  component_training `→` HHandle

Handle of the training result.

## Result

If the handle of the training result is valid, the operator
`clear_training_components` returns the value 2 (
H_MSG_TRUE)
.
If necessary, an exception is raised.

## Module

Matching
