# WriteSamplesClassSvm (Operator)

## Name

`WriteSamplesClassSvm` — Write the training data of a support vector machine to a file.

## Signature

`static void HOperatorSet.WriteSamplesClassSvm(HTuple SVMHandle, HTuple fileName)`

`void HClassSvm.WriteSamplesClassSvm(string fileName)`

## Description

`WriteSamplesClassSvm` writes the training samples
currently stored in the support vector machine (SVM)
*`SVMHandle`* to the file given by *`fileName`*.
`WriteSamplesClassSvm` can be used to build up a database
of training samples, and hence to improve the performance of the SVM
by training it with an extended data set (see
[`TrainClassSvm`](train_class_svm.md)). The file *`fileName`* is overwritten
by `WriteSamplesClassSvm`. Nevertheless, extending the
database of training samples is easy to do because
[`ReadSamplesClassSvm`](read_samples_class_svm.md) and [`AddSampleClassSvm`](add_sample_class_svm.md) add
the training samples to the training samples that are already stored
in memory with the SVM.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`SVMHandle`** (input_control)  class_svm `→` [HClassSvm](HClassSvm.md), [HTuple](HTuple.md) (*IntPtr*)

SVM handle.

**`fileName`** (input_control)  filename.write `→` [HTuple](HTuple.md) (*string*)

File name.

## Result

If the parameters are valid the operator
`WriteSamplesClassSvm` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`AddSampleClassSvm`

## Possible Successors

`ClearSamplesClassSvm`

## See also

`CreateClassSvm`,
`GetPrepInfoClassSvm`,
`ReadSamplesClassSvm`

## Module

Foundation
