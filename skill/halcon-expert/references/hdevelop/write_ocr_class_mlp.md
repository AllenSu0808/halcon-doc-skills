# write_ocr_class_mlp (Operator)

## Name

`write_ocr_class_mlp` — Write an OCR classifier to a file.

## Signature

`write_ocr_class_mlp( : : OCRHandle, FileName : )`

## Description

`write_ocr_class_mlp` writes the OCR classifier
*`OCRHandle`* to the file given by *`FileName`*. If a
file extension is not specified in *`FileName`* the default
extension `'.omc'` is appended to *`FileName`*.
`write_ocr_class_mlp` is typically called after the classifier
has been trained with [`trainf_ocr_class_mlp`](trainf_ocr_class_mlp.md). The classifier
can be read with [`read_ocr_class_mlp`](read_ocr_class_mlp.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`OCRHandle`** (input_control)  ocr_mlp `→`  (handle)

Handle of the OCR classifier.

**`FileName`** (input_control)  filename.write `→`  (string)

File name.

File extension:
.`omc`

## Result

If the parameters are valid, the operator
`write_ocr_class_mlp` returns the value 2 (
H_MSG_TRUE)
. If necessary, an
exception is raised.

## Possible Predecessors

`trainf_ocr_class_mlp`

## Possible Successors

`clear_ocr_class_mlp`

## See also

`create_ocr_class_mlp`,
`read_ocr_class_mlp`,
`write_class_mlp`,
`read_class_mlp`

## Module

OCR/OCV
