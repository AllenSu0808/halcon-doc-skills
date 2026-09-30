# ClearTrainingComponents (Operator)

## Name

`ClearTrainingComponents` — Free the memory of a component training result.

## Warning

**`ClearTrainingComponents` is obsolete and is only provided for
reasons of backward compatibility.
The operator will be removed with HALCON 26.11.**

## Signature

`static void HOperatorSet.ClearTrainingComponents(HTuple componentTrainingID)`

`void HComponentTraining.ClearTrainingComponents()`

## Description

The operator `ClearTrainingComponents` frees the memory of a
training result that was created by [`TrainModelComponents`](train_model_components.md).
After calling `ClearTrainingComponents`, the training result
can no longer be used. The handle *`componentTrainingID`*
becomes invalid.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- componentTrainingID

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`componentTrainingID`** (input_control, state is modified)  component_training `→` [HComponentTraining](HComponentTraining.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the training result.

## Result

If the handle of the training result is valid, the operator
`ClearTrainingComponents` returns the value 2 (
H_MSG_TRUE)
.
If necessary, an exception is raised.

## Module

Matching
