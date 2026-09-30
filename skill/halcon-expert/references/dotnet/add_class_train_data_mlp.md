# AddClassTrainDataMlp (Operator)

## Name

`AddClassTrainDataMlp` — Add training data to a multilayer perceptron (MLP).

## Signature

`static void HOperatorSet.AddClassTrainDataMlp(HTuple MLPHandle, HTuple classTrainDataHandle)`

`void HClassMlp.AddClassTrainDataMlp(HClassTrainData classTrainDataHandle)`

`void HClassTrainData.AddClassTrainDataMlp(HClassMlp MLPHandle)`

## Description

`AddClassTrainDataMlp` adds the training data specified by
*`classTrainDataHandle`* to a multilayer perceptron (MLP) specified by
*`MLPHandle`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- MLPHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`MLPHandle`** (input_control, state is modified)  class_mlp `→` [HClassMlp](HClassMlp.md), [HTuple](HTuple.md) (*IntPtr*)

MLP handle which receives the training data.

**`classTrainDataHandle`** (input_control)  class_train_data `→` [HClassTrainData](HClassTrainData.md), [HTuple](HTuple.md) (*IntPtr*)

Training data for a classifier.

## Result

If the parameters are valid, the operator
`AddClassTrainDataMlp`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`CreateClassMlp`,
`CreateClassTrainData`

## Possible Successors

`GetSampleClassMlp`

## Alternatives

`AddSampleClassMlp`

## See also

`CreateClassMlp`

## Module

Foundation
