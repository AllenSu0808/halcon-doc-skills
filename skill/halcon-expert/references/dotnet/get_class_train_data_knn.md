# GetClassTrainDataKnn (Operator)

## Name

`GetClassTrainDataKnn` — Get the training data of a k-nearest neighbors (k-NN) classifier.

## Signature

`static void HOperatorSet.GetClassTrainDataKnn(HTuple KNNHandle, out HTuple classTrainDataHandle)`

`HClassTrainData HClassKnn.GetClassTrainDataKnn()`

`void HClassTrainData.GetClassTrainDataKnn(HClassKnn KNNHandle)`

## Description

`GetClassTrainDataKnn` gets the training data of a
k-nearest neighbors (k-NN) classifier and returns it in
*`classTrainDataHandle`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`KNNHandle`** (input_control)  class_knn `→` [HClassKnn](HClassKnn.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the k-NN classifier
that contains training data.

**`classTrainDataHandle`** (output_control)  class_train_data `→` [HClassTrainData](HClassTrainData.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the training data of the classifier.

## Result

If the parameters are valid, the operator
`GetClassTrainDataKnn`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`AddSampleClassKnn`

## Possible Successors

`AddClassTrainDataSvm`,
`AddClassTrainDataGmm`,
`AddClassTrainDataKnn`

## See also

`CreateClassTrainData`

## Module

Foundation
