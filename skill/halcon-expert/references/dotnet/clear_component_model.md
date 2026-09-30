# ClearComponentModel (Operator)

## Name

`ClearComponentModel` — Free the memory of a component model.

## Warning

**`ClearComponentModel` is obsolete and is only provided for
reasons of backward compatibility.
The operator will be removed with HALCON 26.11.**

## Signature

`static void HOperatorSet.ClearComponentModel(HTuple componentModelID)`

`void HComponentModel.ClearComponentModel()`

## Description

The operator `ClearComponentModel` frees the memory of a
component model that was created by [`CreateComponentModel`](create_component_model.md)
or [`CreateTrainedComponentModel`](create_trained_component_model.md). After calling
`ClearComponentModel`, the model can no longer be used. The
handle *`componentModelID`* becomes invalid.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- componentModelID

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`componentModelID`** (input_control, state is modified)  component_model `→` [HComponentModel](HComponentModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the component model.

## Result

If the handle of the model is valid, the operator
`ClearComponentModel` returns the value 2 (
H_MSG_TRUE)
.
If necessary, an exception is raised.

## Module

Matching
