# WriteOcrClassMlp (Operator)

## Name

`WriteOcrClassMlp` — Write an OCR classifier to a file.

## Signature

`static void HOperatorSet.WriteOcrClassMlp(HTuple OCRHandle, HTuple fileName)`

`void HOCRMlp.WriteOcrClassMlp(string fileName)`

## Description

`WriteOcrClassMlp` writes the OCR classifier
*`OCRHandle`* to the file given by *`fileName`*. If a
file extension is not specified in *`fileName`* the default
extension `'.omc'` is appended to *`fileName`*.
`WriteOcrClassMlp` is typically called after the classifier
has been trained with [`TrainfOcrClassMlp`](trainf_ocr_class_mlp.md). The classifier
can be read with [`ReadOcrClassMlp`](read_ocr_class_mlp.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`OCRHandle`** (input_control)  ocr_mlp `→` [HOCRMlp](HOCRMlp.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the OCR classifier.

**`fileName`** (input_control)  filename.write `→` [HTuple](HTuple.md) (*string*)

File name.

File extension:
.`omc`

## Result

If the parameters are valid, the operator
`WriteOcrClassMlp` returns the value 2 (
H_MSG_TRUE)
. If necessary, an
exception is raised.

## Possible Predecessors

`TrainfOcrClassMlp`

## Possible Successors

`ClearOcrClassMlp`

## See also

`CreateOcrClassMlp`,
`ReadOcrClassMlp`,
`WriteClassMlp`,
`ReadClassMlp`

## Module

OCR/OCV
