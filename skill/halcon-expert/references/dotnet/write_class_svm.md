# WriteClassSvm (Operator)

## Name

`WriteClassSvm` — Write a support vector machine to a file.

## Signature

`static void HOperatorSet.WriteClassSvm(HTuple SVMHandle, HTuple fileName)`

`void HClassSvm.WriteClassSvm(string fileName)`

## Description

`WriteClassSvm` writes the support vector machine (SVM)
*`SVMHandle`* to the file given by *`fileName`*.
The default HALCON file extension for the SVM classifier is 'gsc'.
`WriteClassSvm` is typically called after the SVM has been
trained with [`TrainClassSvm`](train_class_svm.md). The SVM can be read with
[`ReadClassSvm`](read_class_svm.md). `WriteClassSvm` does *not*
write any training samples that possibly have been stored in the
SVM. For this purpose, [`WriteSamplesClassSvm`](write_samples_class_svm.md) should be
used.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`SVMHandle`** (input_control)  class_svm `→` [HClassSvm](HClassSvm.md), [HTuple](HTuple.md) (*IntPtr*)

SVM handle.

**`fileName`** (input_control)  filename.write `→` [HTuple](HTuple.md) (*string*)

File name.

File extension:
.`gsc`

## Result

If the parameters are valid the operator `WriteClassSvm`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is
raised.

## Possible Predecessors

`TrainClassSvm`

## Possible Successors

`ClearClassSvm`

## See also

`CreateClassSvm`,
`ReadClassSvm`,
`WriteSamplesClassSvm`

## Module

Foundation
