# ReadClassSvm (Operator)

## Name

`ReadClassSvm` — Read a support vector machine from a file.

## Signature

`static void HOperatorSet.ReadClassSvm(HTuple fileName, out HTuple SVMHandle)`

`public HClassSvm(string fileName)`

`void HClassSvm.ReadClassSvm(string fileName)`

## Description

`ReadClassSvm` reads a support vector machine (SVM) that has
been stored with [`WriteClassSvm`](write_class_svm.md). Since the training of an
SVM can consume a relatively long time, the SVM is typically trained
in an offline process and written to a file with
[`WriteClassSvm`](write_class_svm.md). In the online process the SVM is read
with `ReadClassSvm` and subsequently used for classification
with [`ClassifyClassSvm`](classify_class_svm.md).
The default HALCON file extension for the SVM classifier is 'gsc'.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`fileName`** (input_control)  filename.read `→` [HTuple](HTuple.md) (*string*)

File name.

File extension:
.`gsc`

**`SVMHandle`** (output_control)  class_svm `→` [HClassSvm](HClassSvm.md), [HTuple](HTuple.md) (*IntPtr*)

SVM handle.

## Result

If the parameters are valid the operator `ReadClassSvm`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is
raised.

## Possible Successors

`ClassifyClassSvm`,
`CreateClassLutSvm`

## Alternatives

`ReadDlModel`

## See also

`CreateClassSvm`,
`WriteClassSvm`

## Module

Foundation
