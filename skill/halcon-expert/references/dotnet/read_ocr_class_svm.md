# ReadOcrClassSvm (Operator)

## Name

`ReadOcrClassSvm` — Read a SVM-based OCR classifier from a file.

## Signature

`static void HOperatorSet.ReadOcrClassSvm(HTuple fileName, out HTuple OCRHandle)`

`public HOCRSvm(string fileName)`

`void HOCRSvm.ReadOcrClassSvm(string fileName)`

## Description

`ReadOcrClassSvm` reads an OCR classifier that has been
stored with [`WriteOcrClassSvm`](write_ocr_class_svm.md). Since the training of an
OCR classifier can consume a relatively long time, the classifier is
typically trained in an offline process and written to a file with
[`WriteOcrClassSvm`](write_ocr_class_svm.md). In the online process the classifier is
read with `ReadOcrClassSvm` and subsequently used for
classification with [`DoOcrSingleClassSvm`](do_ocr_single_class_svm.md) or
[`DoOcrMultiClassSvm`](do_ocr_multi_class_svm.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`fileName`** (input_control)  filename.read `→` [HTuple](HTuple.md) (*string*)

File name.

File extension:
.`osc`, .`fnt`

**`OCRHandle`** (output_control)  ocr_svm `→` [HOCRSvm](HOCRSvm.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the OCR classifier.

## Result

If the parameters are valid the operator `ReadOcrClassSvm`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is
raised.

## Possible Successors

`DoOcrSingleClassSvm`,
`DoOcrMultiClassSvm`

## See also

`CreateOcrClassSvm`,
`WriteOcrClassSvm`,
`ReadClassSvm`,
`WriteClassSvm`

## Module

OCR/OCV
