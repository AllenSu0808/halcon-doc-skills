# WriteOcrClassSvm (Operator)

## Name

`WriteOcrClassSvm` — Write an OCR classifier to a file.

## Signature

`static void HOperatorSet.WriteOcrClassSvm(HTuple OCRHandle, HTuple fileName)`

`void HOCRSvm.WriteOcrClassSvm(string fileName)`

## Description

`WriteOcrClassSvm` writes the OCR classifier
*`OCRHandle`* to the file given by *`fileName`*. If a
file extension is not specified in *`fileName`*, the default
extension `'.osc'` is appended to *`fileName`*.
`WriteOcrClassSvm` is typically called after the classifier
has been trained with [`TrainfOcrClassSvm`](trainf_ocr_class_svm.md). The classifier
can be read with [`ReadOcrClassSvm`](read_ocr_class_svm.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`OCRHandle`** (input_control)  ocr_svm `→` [HOCRSvm](HOCRSvm.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the OCR classifier.

**`fileName`** (input_control)  filename.write `→` [HTuple](HTuple.md) (*string*)

File name.

File extension:
.`osc`

## Result

If the parameters are valid the operator `WriteOcrClassSvm`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is
raised.

## Possible Predecessors

`TrainfOcrClassSvm`

## Possible Successors

`ClearOcrClassSvm`

## See also

`CreateOcrClassSvm`,
`ReadOcrClassSvm`,
`WriteClassSvm`,
`ReadClassSvm`

## Module

OCR/OCV
