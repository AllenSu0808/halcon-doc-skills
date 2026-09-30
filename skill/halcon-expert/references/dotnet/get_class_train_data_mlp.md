# GetClassTrainDataMlp (Operator)

## Name

`GetClassTrainDataMlp` — Get the training data of a multilayer perceptron (MLP).

## Signature

`static void HOperatorSet.GetClassTrainDataMlp(HTuple MLPHandle, out HTuple classTrainDataHandle)`

`HClassTrainData HClassMlp.GetClassTrainDataMlp()`

`void HClassTrainData.GetClassTrainDataMlp(HClassMlp MLPHandle)`

## Description

`GetClassTrainDataMlp` gets the training data of a
multilayer perceptron (MLP) and returns it in
*`classTrainDataHandle`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`MLPHandle`** (input_control)  class_mlp `→` [HClassMlp](HClassMlp.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of a MLP that contains training data.

**`classTrainDataHandle`** (output_control)  class_train_data `→` [HClassTrainData](HClassTrainData.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the training data of the classifier.

## Result

If the parameters are valid, the operator
`GetClassTrainDataMlp`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`AddSampleClassMlp`,
`ReadSamplesClassMlp`

## Possible Successors

`AddClassTrainDataSvm`,
`AddClassTrainDataGmm`,
`AddClassTrainDataKnn`

## See also

`CreateClassTrainData`

## Module

Foundation
