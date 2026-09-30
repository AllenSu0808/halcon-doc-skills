# GetClassTrainDataGmm (Operator)

## Name

`GetClassTrainDataGmm` — Get the training data of a Gaussian Mixture Model (GMM).

## Signature

`static void HOperatorSet.GetClassTrainDataGmm(HTuple GMMHandle, out HTuple classTrainDataHandle)`

`HClassTrainData HClassGmm.GetClassTrainDataGmm()`

`void HClassTrainData.GetClassTrainDataGmm(HClassGmm GMMHandle)`

## Description

`GetClassTrainDataGmm` gets the training data of a
Gaussian Mixture Model (GMM) and returns it in
*`classTrainDataHandle`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`GMMHandle`** (input_control)  class_gmm `→` [HClassGmm](HClassGmm.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of a GMM that contains training data.

**`classTrainDataHandle`** (output_control)  class_train_data `→` [HClassTrainData](HClassTrainData.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the training data of the classifier.

## Result

If the parameters are valid, the operator
`GetClassTrainDataGmm`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`AddSampleClassGmm`,
`ReadSamplesClassGmm`

## Possible Successors

`AddClassTrainDataSvm`,
`AddClassTrainDataSvm`,
`AddClassTrainDataKnn`

## See also

`CreateClassTrainData`

## Module

Foundation
