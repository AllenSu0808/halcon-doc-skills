# write_samples_class_svm (Operator)

## Name

`write_samples_class_svm` — Write the training data of a support vector machine to a file.

## Signature

`write_samples_class_svm( : : SVMHandle, FileName : )`

## Description

`write_samples_class_svm` writes the training samples
currently stored in the support vector machine (SVM)
*`SVMHandle`* to the file given by *`FileName`*.
`write_samples_class_svm` can be used to build up a database
of training samples, and hence to improve the performance of the SVM
by training it with an extended data set (see
[`train_class_svm`](train_class_svm.md)). The file *`FileName`* is overwritten
by `write_samples_class_svm`. Nevertheless, extending the
database of training samples is easy to do because
[`read_samples_class_svm`](read_samples_class_svm.md) and [`add_sample_class_svm`](add_sample_class_svm.md) add
the training samples to the training samples that are already stored
in memory with the SVM.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`SVMHandle`** (input_control)  class_svm `→`  (handle)

SVM handle.

**`FileName`** (input_control)  filename.write `→`  (string)

File name.

## Result

If the parameters are valid the operator
`write_samples_class_svm` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`add_sample_class_svm`

## Possible Successors

`clear_samples_class_svm`

## See also

`create_class_svm`,
`get_prep_info_class_svm`,
`read_samples_class_svm`

## Module

Foundation
