# AddClassTrainDataGmm (Operator)

## Name

`AddClassTrainDataGmm` — Add training data to a Gaussian Mixture Model (GMM).

## Signature

`static void HOperatorSet.AddClassTrainDataGmm(HTuple GMMHandle, HTuple classTrainDataHandle)`

`void HClassGmm.AddClassTrainDataGmm(HClassTrainData classTrainDataHandle)`

`void HClassTrainData.AddClassTrainDataGmm(HClassGmm GMMHandle)`

## Description

`AddClassTrainDataGmm` adds the training data specified by
*`classTrainDataHandle`* to a Gaussian Mixture Model (GMM)
specified by *`GMMHandle`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- GMMHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`GMMHandle`** (input_control, state is modified)  class_gmm `→` [HClassGmm](HClassGmm.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of a GMM which receives the training data.

**`classTrainDataHandle`** (input_control)  class_train_data `→` [HClassTrainData](HClassTrainData.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of training data for a classifier.

## Result

If the parameters are valid, the operator
`AddClassTrainDataGmm`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`CreateClassGmm`,
`CreateClassTrainData`

## Possible Successors

`GetSampleClassGmm`

## Alternatives

`AddSampleClassGmm`

## See also

`CreateClassGmm`

## Module

Foundation
