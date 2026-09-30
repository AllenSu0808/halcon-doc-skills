# AddClassTrainDataSvm (Operator)

## Name

`AddClassTrainDataSvm` — Add training data to a support vector machine (SVM).

## Signature

`static void HOperatorSet.AddClassTrainDataSvm(HTuple SVMHandle, HTuple classTrainDataHandle)`

`void HClassSvm.AddClassTrainDataSvm(HClassTrainData classTrainDataHandle)`

`void HClassTrainData.AddClassTrainDataSvm(HClassSvm SVMHandle)`

## Description

`AddClassTrainDataSvm` adds the training data specified by
*`classTrainDataHandle`* to a support vector machine (SVM) specified by
*`SVMHandle`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- SVMHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`SVMHandle`** (input_control, state is modified)  class_svm `→` [HClassSvm](HClassSvm.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of a SVM which receives the training data.

**`classTrainDataHandle`** (input_control)  class_train_data `→` [HClassTrainData](HClassTrainData.md), [HTuple](HTuple.md) (*IntPtr*)

Training data for a classifier.

## Result

If the parameters are valid, the operator
`AddClassTrainDataSvm`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`CreateClassSvm`,
`CreateClassTrainData`

## Possible Successors

`GetSampleClassSvm`

## Alternatives

`AddSampleClassSvm`

## See also

`CreateClassSvm`

## Module

Foundation
