# read_ocr_class_svm (Operator)

## Name

`read_ocr_class_svm` — Read a SVM-based OCR classifier from a file.

## Signature

`read_ocr_class_svm( : : FileName : OCRHandle)`

## Description

`read_ocr_class_svm` reads an OCR classifier that has been
stored with [`write_ocr_class_svm`](write_ocr_class_svm.md). Since the training of an
OCR classifier can consume a relatively long time, the classifier is
typically trained in an offline process and written to a file with
[`write_ocr_class_svm`](write_ocr_class_svm.md). In the online process the classifier is
read with `read_ocr_class_svm` and subsequently used for
classification with [`do_ocr_single_class_svm`](do_ocr_single_class_svm.md) or
[`do_ocr_multi_class_svm`](do_ocr_multi_class_svm.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`FileName`** (input_control)  filename.read `→`  (string)

File name.

File extension:
.`osc`, .`fnt`

**`OCRHandle`** (output_control)  ocr_svm `→`  (handle)

Handle of the OCR classifier.

## Result

If the parameters are valid the operator `read_ocr_class_svm`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is
raised.

## Possible Successors

`do_ocr_single_class_svm`,
`do_ocr_multi_class_svm`

## See also

`create_ocr_class_svm`,
`write_ocr_class_svm`,
`read_class_svm`,
`write_class_svm`

## Module

OCR/OCV
