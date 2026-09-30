# read_samples_class_svm (Operator)

## Name

`read_samples_class_svm` — Read the training data of a support vector machine from a file.

## Signature

`read_samples_class_svm( : : SVMHandle, FileName : )`

## Description

`read_samples_class_svm` reads training samples from the file
given by *`FileName`* and adds them to the training samples
that have already been added to the support vector machine (SVM)
given by *`SVMHandle`*. The SVM must be created with
[`create_class_svm`](create_class_svm.md) before calling
`read_samples_class_svm`. As described with
[`train_class_svm`](train_class_svm.md) and [`write_samples_class_svm`](write_samples_class_svm.md), the
operators `read_samples_class_svm`,
[`add_sample_class_svm`](add_sample_class_svm.md), and [`write_samples_class_svm`](write_samples_class_svm.md)
can be used to build up a extensive set of training samples, and
hence to improve the performance of the SVM by retraining the SVM
with extended data sets.

It should be noted that the training samples must have the correct
dimensionality. The feature vectors and target vectors stored in
*`FileName`* must have the lengths `NumFeatures` and
`NumClasses` that were specified with
[`create_class_svm`](create_class_svm.md). The target is stored in vector form for
compatibility reason with the MLP (see
[`read_samples_class_mlp`](read_samples_class_mlp.md)). If the dimensions are incorrect an
error message is returned.

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

**`FileName`** (input_control)  filename.read `→`  (string)

File name.

## Result

If the parameters are valid the operator
`read_samples_class_svm` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`create_class_svm`

## Possible Successors

`train_class_svm`

## Alternatives

`add_sample_class_svm`

## See also

`write_samples_class_svm`,
`clear_samples_class_svm`

## Module

Foundation
