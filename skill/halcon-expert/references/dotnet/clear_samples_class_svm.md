# ClearSamplesClassSvm (Operator)

## Name

`ClearSamplesClassSvm` — Clear the training data of a support vector machine.

## Signature

`static void HOperatorSet.ClearSamplesClassSvm(HTuple SVMHandle)`

`static void HClassSvm.ClearSamplesClassSvm(HClassSvm[] SVMHandle)`

`void HClassSvm.ClearSamplesClassSvm()`

## Description

`ClearSamplesClassSvm` clears all training samples that
have been added to the support vector machine (SVM)
*`SVMHandle`* with [`AddSampleClassSvm`](add_sample_class_svm.md) or
[`ReadSamplesClassSvm`](read_samples_class_svm.md). `ClearSamplesClassSvm`
should only be used if the SVM is trained in the same process that
uses the SVM for classification with [`ClassifyClassSvm`](classify_class_svm.md). In
this case, the memory required for the training samples can be freed
with `ClearSamplesClassSvm`, and hence memory can be saved.
In the normal usage, in which the SVM is trained offline and written
to a file with [`WriteClassSvm`](write_class_svm.md), it is typically unnecessary
to call `ClearSamplesClassSvm` because
[`WriteClassSvm`](write_class_svm.md) does not save the training samples, and
hence the online process, which reads the SVM with
[`ReadClassSvm`](read_class_svm.md), requires no memory for the training
samples.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- SVMHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`SVMHandle`** (input_control, state is modified)  class_svm(-array) `→` [HClassSvm](HClassSvm.md), [HTuple](HTuple.md) (*IntPtr*)

SVM handle.

## Result

If the parameters are valid the operator
`ClearSamplesClassSvm` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`TrainClassSvm`,
`WriteSamplesClassSvm`

## See also

`CreateClassSvm`,
`ClearClassSvm`,
`AddSampleClassSvm`,
`ReadSamplesClassSvm`

## Module

Foundation
