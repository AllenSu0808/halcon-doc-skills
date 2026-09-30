# clear_samples_class_svm (Operator)

## Name

`clear_samples_class_svm` — Clear the training data of a support vector machine.

## Signature

`clear_samples_class_svm( : : SVMHandle : )`

## Description

`clear_samples_class_svm` clears all training samples that
have been added to the support vector machine (SVM)
*`SVMHandle`* with [`add_sample_class_svm`](add_sample_class_svm.md) or
[`read_samples_class_svm`](read_samples_class_svm.md). `clear_samples_class_svm`
should only be used if the SVM is trained in the same process that
uses the SVM for classification with [`classify_class_svm`](classify_class_svm.md). In
this case, the memory required for the training samples can be freed
with `clear_samples_class_svm`, and hence memory can be saved.
In the normal usage, in which the SVM is trained offline and written
to a file with [`write_class_svm`](write_class_svm.md), it is typically unnecessary
to call `clear_samples_class_svm` because
[`write_class_svm`](write_class_svm.md) does not save the training samples, and
hence the online process, which reads the SVM with
[`read_class_svm`](read_class_svm.md), requires no memory for the training
samples.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- SVMHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`SVMHandle`** (input_control, state is modified)  class_svm(-array) `→`  (handle)

SVM handle.

## Result

If the parameters are valid the operator
`clear_samples_class_svm` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`train_class_svm`,
`write_samples_class_svm`

## See also

`create_class_svm`,
`clear_class_svm`,
`add_sample_class_svm`,
`read_samples_class_svm`

## Module

Foundation
