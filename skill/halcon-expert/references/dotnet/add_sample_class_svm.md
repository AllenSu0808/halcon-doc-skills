# AddSampleClassSvm (Operator)

## Name

`AddSampleClassSvm` — Add a training sample to the training data of a support vector
machine.

## Signature

`static void HOperatorSet.AddSampleClassSvm(HTuple SVMHandle, HTuple features, HTuple classVal)`

`void HClassSvm.AddSampleClassSvm(HTuple features, HTuple classVal)`

`void HClassSvm.AddSampleClassSvm(HTuple features, int classVal)`

## Description

`AddSampleClassSvm` adds a training sample to the support
vector machine (SVM) given by *`SVMHandle`*. The training
sample is given by *`features`* and *`classVal`*.
*`features`* is the feature vector of the sample, and
consequently must be a real vector of length `numFeatures`,
as specified in [`CreateClassSvm`](create_class_svm.md). *`classVal`* is the
target of the sample, which must be in the range of 0 to
`numClasses`-1 (see [`CreateClassSvm`](create_class_svm.md)). In the special
case of *"novelty-detection"* the class is to be set to *0* as
only one class is assumed.
Before the SVM can be trained with
[`TrainClassSvm`](train_class_svm.md), training samples must be added to the
SVM with `AddSampleClassSvm`. The usage of support vectors
of an already trained SVM as training samples is described in
[`TrainClassSvm`](train_class_svm.md).

The number of currently stored training samples can be queried with
[`GetSampleNumClassSvm`](get_sample_num_class_svm.md). Stored training samples can be
read out again with [`GetSampleClassSvm`](get_sample_class_svm.md).

Normally, it is useful to save the training samples in a file with
[`WriteSamplesClassSvm`](write_samples_class_svm.md) to facilitate reusing the samples
and to facilitate that, if necessary, new training samples can be
added to the data set, and hence to facilitate that a *newly
created* SVM can be trained with the extended data set.

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

**`features`** (input_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Feature vector of the training sample to be stored.

**`classVal`** (input_control)  number `→` [HTuple](HTuple.md) (*int* / long / double)

Class of the training sample to be stored.

## Result

If the parameters are valid the operator
`AddSampleClassSvm` returns the value 2 (
H_MSG_TRUE)
. If necessary,
an exception is raised.

## Possible Predecessors

`CreateClassSvm`

## Possible Successors

`TrainClassSvm`,
`WriteSamplesClassSvm`,
`GetSampleNumClassSvm`,
`GetSampleClassSvm`

## Alternatives

`ReadSamplesClassSvm`

## See also

`ClearSamplesClassSvm`,
`GetSupportVectorClassSvm`

## Module

Foundation
