# read_class_svm (Operator)

## Name

`read_class_svm` — Read a support vector machine from a file.

## Signature

`def read_class_svm(file_name: str) -> HHandle`

## Description

`read_class_svm` reads a support vector machine (SVM) that has
been stored with [`write_class_svm`](write_class_svm.md). Since the training of an
SVM can consume a relatively long time, the SVM is typically trained
in an offline process and written to a file with
[`write_class_svm`](write_class_svm.md). In the online process the SVM is read
with `read_class_svm` and subsequently used for classification
with [`classify_class_svm`](classify_class_svm.md).
The default HALCON file extension for the SVM classifier is 'gsc'.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`file_name`** (input_control)  filename.read `→` str

File name.

File extension:
.`gsc`

**`svmhandle`** (output_control)  class_svm `→` HHandle

SVM handle.

## Result

If the parameters are valid the operator `read_class_svm`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is
raised.

## Possible Successors

`classify_class_svm`,
`create_class_lut_svm`

## Alternatives

`read_dl_model`

## See also

`create_class_svm`,
`write_class_svm`

## Module

Foundation
