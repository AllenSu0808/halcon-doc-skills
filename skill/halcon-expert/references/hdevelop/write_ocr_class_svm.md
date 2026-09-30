# write_ocr_class_svm (Operator)

## Name

`write_ocr_class_svm` — Write an OCR classifier to a file.

## Signature

`write_ocr_class_svm( : : OCRHandle, FileName : )`

## Description

`write_ocr_class_svm` writes the OCR classifier
*`OCRHandle`* to the file given by *`FileName`*. If a
file extension is not specified in *`FileName`*, the default
extension `'.osc'` is appended to *`FileName`*.
`write_ocr_class_svm` is typically called after the classifier
has been trained with [`trainf_ocr_class_svm`](trainf_ocr_class_svm.md). The classifier
can be read with [`read_ocr_class_svm`](read_ocr_class_svm.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`OCRHandle`** (input_control)  ocr_svm `→`  (handle)

Handle of the OCR classifier.

**`FileName`** (input_control)  filename.write `→`  (string)

File name.

File extension:
.`osc`

## Result

If the parameters are valid the operator `write_ocr_class_svm`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is
raised.

## Possible Predecessors

`trainf_ocr_class_svm`

## Possible Successors

`clear_ocr_class_svm`

## See also

`create_ocr_class_svm`,
`read_ocr_class_svm`,
`write_class_svm`,
`read_class_svm`

## Module

OCR/OCV
