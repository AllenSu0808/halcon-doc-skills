# write_ocr (Operator)

## Name

`write_ocr` — Writing an OCR classifier into a file.

## Warning

**`write_ocr` is obsolete and is only provided for
reasons of backward compatibility. New applications should use the
MLP, SVM or CNN based operators instead.**

## Signature

`def write_ocr(ocr_handle: HHandle, file_name: str) -> None`

## Description

The operator `write_ocr` writes the OCR classifier
*`ocr_handle`* into the file *`file_name`*. Since the data
of the classifier will be lost when the program is finished, they
have to be stored after the training if the user wants to
use them again at a later execution of the program. The data can
then be read with the help of the operator [`read_ocr`](read_ocr.md).
The extension will be added automatically to the parameter
*`file_name`*.

## Attention

The output file *`file_name`* must be given without extension.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`ocr_handle`** (input_control)  ocr_box `→` HHandle

ID of the OCR classifier.

**`file_name`** (input_control)  filename.write `→` str

Name of the file for the OCR classifier (without extension).

Default:
"my_ocr"

File extension:
.`obc`

## Result

If the parameter *`ocr_handle`* is valid and the
indicated file can be written, the operator
`write_ocr` returns the value 2 (
H_MSG_TRUE)
.
Otherwise an exception will be raised.

## Possible Predecessors

`traind_ocr_class_box`,
`trainf_ocr_class_box`

## Possible Successors

`do_ocr_multi`,
`do_ocr_single`

## See also

`read_ocr`,
`do_ocr_multi`,
`traind_ocr_class_box`,
`trainf_ocr_class_box`

## Module

OCR/OCV
