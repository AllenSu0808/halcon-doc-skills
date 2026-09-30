# ReadSamplesClassSvm (Operator)

## Name

`ReadSamplesClassSvm` — Read the training data of a support vector machine from a file.

## Signature

`static void HOperatorSet.ReadSamplesClassSvm(HTuple SVMHandle, HTuple fileName)`

`void HClassSvm.ReadSamplesClassSvm(string fileName)`

## Description

`ReadSamplesClassSvm` reads training samples from the file
given by *`fileName`* and adds them to the training samples
that have already been added to the support vector machine (SVM)
given by *`SVMHandle`*. The SVM must be created with
[`CreateClassSvm`](create_class_svm.md) before calling
`ReadSamplesClassSvm`. As described with
[`TrainClassSvm`](train_class_svm.md) and [`WriteSamplesClassSvm`](write_samples_class_svm.md), the
operators `ReadSamplesClassSvm`,
[`AddSampleClassSvm`](add_sample_class_svm.md), and [`WriteSamplesClassSvm`](write_samples_class_svm.md)
can be used to build up a extensive set of training samples, and
hence to improve the performance of the SVM by retraining the SVM
with extended data sets.

It should be noted that the training samples must have the correct
dimensionality. The feature vectors and target vectors stored in
*`fileName`* must have the lengths `numFeatures` and
`numClasses` that were specified with
[`CreateClassSvm`](create_class_svm.md). The target is stored in vector form for
compatibility reason with the MLP (see
[`ReadSamplesClassMlp`](read_samples_class_mlp.md)). If the dimensions are incorrect an
error message is returned.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- SVMHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`SVMHandle`** (input_control, state is modified)  class_svm `→` [HClassSvm](HClassSvm.md), [HTuple](HTuple.md) (*IntPtr*)

SVM handle.

**`fileName`** (input_control)  filename.read `→` [HTuple](HTuple.md) (*string*)

File name.

## Result

If the parameters are valid the operator
`ReadSamplesClassSvm` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`CreateClassSvm`

## Possible Successors

`TrainClassSvm`

## Alternatives

`AddSampleClassSvm`

## See also

`WriteSamplesClassSvm`,
`ClearSamplesClassSvm`

## Module

Foundation
