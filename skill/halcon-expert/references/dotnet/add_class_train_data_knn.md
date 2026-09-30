# AddClassTrainDataKnn (Operator)

## Name

`AddClassTrainDataKnn` — Add training data to a k-nearest neighbors (k-NN) classifier.

## Signature

`static void HOperatorSet.AddClassTrainDataKnn(HTuple KNNHandle, HTuple classTrainDataHandle)`

`void HClassKnn.AddClassTrainDataKnn(HClassTrainData classTrainDataHandle)`

`void HClassTrainData.AddClassTrainDataKnn(HClassKnn KNNHandle)`

## Description

`AddClassTrainDataKnn` adds the training data specified by
*`classTrainDataHandle`* to a k-nearest neighbors (k-NN) classifier
specified by *`KNNHandle`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- KNNHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`KNNHandle`** (input_control, state is modified)  class_knn `→` [HClassKnn](HClassKnn.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of a k-NN which receives the
training data.

**`classTrainDataHandle`** (input_control)  class_train_data `→` [HClassTrainData](HClassTrainData.md), [HTuple](HTuple.md) (*IntPtr*)

Training data for a classifier.

## Result

If the parameters are valid, the operator
`AddClassTrainDataKnn`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`CreateClassKnn`,
`CreateClassTrainData`

## Possible Successors

`GetSampleClassKnn`

## Alternatives

`AddSampleClassKnn`

## See also

`CreateClassKnn`

## Module

Foundation
