# add_sample_class_svm (Operator)

## Name

`add_sample_class_svm` — Add a training sample to the training data of a support vector
machine.

## Signature

`add_sample_class_svm( : : SVMHandle, Features, Class : )`

## Description

`add_sample_class_svm` adds a training sample to the support
vector machine (SVM) given by *`SVMHandle`*. The training
sample is given by *`Features`* and *`Class`*.
*`Features`* is the feature vector of the sample, and
consequently must be a real vector of length `NumFeatures`,
as specified in [`create_class_svm`](create_class_svm.md). *`Class`* is the
target of the sample, which must be in the range of 0 to
`NumClasses`-1 (see [`create_class_svm`](create_class_svm.md)). In the special
case of *'novelty-detection'* the class is to be set to *0* as
only one class is assumed.
Before the SVM can be trained with
[`train_class_svm`](train_class_svm.md), training samples must be added to the
SVM with `add_sample_class_svm`. The usage of support vectors
of an already trained SVM as training samples is described in
[`train_class_svm`](train_class_svm.md).

The number of currently stored training samples can be queried with
[`get_sample_num_class_svm`](get_sample_num_class_svm.md). Stored training samples can be
read out again with [`get_sample_class_svm`](get_sample_class_svm.md).

Normally, it is useful to save the training samples in a file with
[`write_samples_class_svm`](write_samples_class_svm.md) to facilitate reusing the samples
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

**`SVMHandle`** (input_control, state is modified)  class_svm `→`  (handle)

SVM handle.

**`Features`** (input_control)  real-array `→`  (real)

Feature vector of the training sample to be stored.

**`Class`** (input_control)  number `→`  (integer / real)

Class of the training sample to be stored.

## Result

If the parameters are valid the operator
`add_sample_class_svm` returns the value 2 (
H_MSG_TRUE)
. If necessary,
an exception is raised.

## Possible Predecessors

`create_class_svm`

## Possible Successors

`train_class_svm`,
`write_samples_class_svm`,
`get_sample_num_class_svm`,
`get_sample_class_svm`

## Alternatives

`read_samples_class_svm`

## See also

`clear_samples_class_svm`,
`get_support_vector_class_svm`

## Module

Foundation
