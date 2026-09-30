# ReadSamplesClassMlp (Operator)

## Name

`ReadSamplesClassMlp` — Read the training data of a multilayer perceptron from a file.

## Signature

`static void HOperatorSet.ReadSamplesClassMlp(HTuple MLPHandle, HTuple fileName)`

`void HClassMlp.ReadSamplesClassMlp(string fileName)`

## Description

`ReadSamplesClassMlp` reads training samples from the file
given by *`fileName`* and adds them to the training samples
that have already been added to the multilayer perceptron (MLP)
given by *`MLPHandle`*. The MLP must be created with
[`CreateClassMlp`](create_class_mlp.md) before calling
`ReadSamplesClassMlp`. As described with
[`TrainClassMlp`](train_class_mlp.md) and [`WriteSamplesClassMlp`](write_samples_class_mlp.md), the
operators `ReadSamplesClassMlp`,
[`AddSampleClassMlp`](add_sample_class_mlp.md), and [`WriteSamplesClassMlp`](write_samples_class_mlp.md)
can be used to build up a extensive set of training samples, and
hence to improve the performance of the MLP by retraining the MLP
with extended data sets.

It should be noted that the training samples must have the correct
dimensionality. The feature vectors and target vectors stored in
*`fileName`* must have the lengths `numInput` and
`numOutput` that were specified with
[`CreateClassMlp`](create_class_mlp.md). If this is not the case an error message
is returned.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- MLPHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`MLPHandle`** (input_control, state is modified)  class_mlp `→` [HClassMlp](HClassMlp.md), [HTuple](HTuple.md) (*IntPtr*)

MLP handle.

**`fileName`** (input_control)  filename.read `→` [HTuple](HTuple.md) (*string*)

File name.

## Result

If the parameters are valid, the operator
`ReadSamplesClassMlp` returns the value 2 (
H_MSG_TRUE)
. If necessary,
an exception is raised.

## Possible Predecessors

`CreateClassMlp`

## Possible Successors

`TrainClassMlp`

## Alternatives

`AddSampleClassMlp`

## See also

`WriteSamplesClassMlp`,
`ClearSamplesClassMlp`

## Module

Foundation
