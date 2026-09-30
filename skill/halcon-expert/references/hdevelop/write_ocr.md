# write_ocr (Operator)

## Name

`write_ocr` — Writing an OCR classifier into a file.

## Warning

**`write_ocr` is obsolete and is only provided for
reasons of backward compatibility. New applications should use the
MLP, SVM or CNN based operators instead.**

## Signature

`write_ocr( : : OcrHandle, FileName : )`

## Description

The operator `write_ocr` writes the OCR classifier
*`OcrHandle`* into the file *`FileName`*. Since the data
of the classifier will be lost when the program is finished, they
have to be stored after the training if the user wants to
use them again at a later execution of the program. The data can
then be read with the help of the operator [`read_ocr`](read_ocr.md).
The extension will be added automatically to the parameter
*`FileName`*.

## Attention

The output file *`FileName`* must be given without extension.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`OcrHandle`** (input_control)  ocr_box `→`  (handle)

ID of the OCR classifier.

**`FileName`** (input_control)  filename.write `→`  (string)

Name of the file for the OCR classifier (without extension).

Default:
'my_ocr'

File extension:
.`obc`

## Result

If the parameter *`OcrHandle`* is valid and the
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
