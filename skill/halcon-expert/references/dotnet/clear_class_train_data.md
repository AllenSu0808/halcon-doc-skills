# ClearClassTrainData (Operator)

## Name

`ClearClassTrainData` — Clears training data for classifiers.

## Signature

`static void HOperatorSet.ClearClassTrainData(HTuple classTrainDataHandle)`

`void HClassTrainData.ClearClassTrainData()`

## Description

`ClearClassTrainData` clears the training data given in
*`classTrainDataHandle`*.
After calling `ClearClassTrainData`, *`classTrainDataHandle`*
becomes invalid.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- classTrainDataHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`classTrainDataHandle`** (input_control, state is modified)  class_train_data `→` [HClassTrainData](HClassTrainData.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of training data for a classifier.

## Result

If the parameters are valid, the operator `ClearClassTrainData`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`CreateClassTrainData`

## See also

`CreateClassTrainData`

## Module

Foundation
