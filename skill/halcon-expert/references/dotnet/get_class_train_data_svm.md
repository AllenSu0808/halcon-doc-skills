# GetClassTrainDataSvm (Operator)

## Name

`GetClassTrainDataSvm` — Get the training data of a support vector machine (SVM).

## Signature

`static void HOperatorSet.GetClassTrainDataSvm(HTuple SVMHandle, out HTuple classTrainDataHandle)`

`HClassTrainData HClassSvm.GetClassTrainDataSvm()`

`void HClassTrainData.GetClassTrainDataSvm(HClassSvm SVMHandle)`

## Description

`GetClassTrainDataSvm` gets the training data of a
support vector machine (SVM) and returns it in
*`classTrainDataHandle`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`SVMHandle`** (input_control)  class_svm `→` [HClassSvm](HClassSvm.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of a SVM that contains training data.

**`classTrainDataHandle`** (output_control)  class_train_data `→` [HClassTrainData](HClassTrainData.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the training data of the classifier.

## Result

If the parameters are valid, the operator
`GetClassTrainDataSvm`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`AddSampleClassSvm`,
`ReadSamplesClassSvm`

## Possible Successors

`AddClassTrainDataMlp`,
`AddClassTrainDataGmm`,
`AddClassTrainDataKnn`

## See also

`CreateClassTrainData`

## Module

Foundation
