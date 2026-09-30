# write_class_svm (Operator)

## Name

`write_class_svm` — Write a support vector machine to a file.

## Signature

`write_class_svm( : : SVMHandle, FileName : )`

## Description

`write_class_svm` writes the support vector machine (SVM)
*`SVMHandle`* to the file given by *`FileName`*.
The default HALCON file extension for the SVM classifier is 'gsc'.
`write_class_svm` is typically called after the SVM has been
trained with [`train_class_svm`](train_class_svm.md). The SVM can be read with
[`read_class_svm`](read_class_svm.md). `write_class_svm` does *not*
write any training samples that possibly have been stored in the
SVM. For this purpose, [`write_samples_class_svm`](write_samples_class_svm.md) should be
used.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`SVMHandle`** (input_control)  class_svm `→`  (handle)

SVM handle.

**`FileName`** (input_control)  filename.write `→`  (string)

File name.

File extension:
.`gsc`

## Result

If the parameters are valid the operator `write_class_svm`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is
raised.

## Possible Predecessors

`train_class_svm`

## Possible Successors

`clear_class_svm`

## See also

`create_class_svm`,
`read_class_svm`,
`write_samples_class_svm`

## Module

Foundation
