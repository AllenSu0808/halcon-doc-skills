# WriteOcr (Operator)

## Name

`WriteOcr` — Writing an OCR classifier into a file.

## Warning

**`WriteOcr` is obsolete and is only provided for
reasons of backward compatibility. New applications should use the
MLP, SVM or CNN based operators instead.**

## Signature

`static void HOperatorSet.WriteOcr(HTuple ocrHandle, HTuple fileName)`

`void HOCRBox.WriteOcr(string fileName)`

## Description

The operator `WriteOcr` writes the OCR classifier
*`ocrHandle`* into the file *`fileName`*. Since the data
of the classifier will be lost when the program is finished, they
have to be stored after the training if the user wants to
use them again at a later execution of the program. The data can
then be read with the help of the operator [`ReadOcr`](read_ocr.md).
The extension will be added automatically to the parameter
*`fileName`*.

## Attention

The output file *`fileName`* must be given without extension.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`ocrHandle`** (input_control)  ocr_box `→` [HOCRBox](HOCRBox.md), [HTuple](HTuple.md) (*IntPtr*)

ID of the OCR classifier.

**`fileName`** (input_control)  filename.write `→` [HTuple](HTuple.md) (*string*)

Name of the file for the OCR classifier (without extension).

Default:
"my_ocr"

File extension:
.`obc`

## Result

If the parameter *`ocrHandle`* is valid and the
indicated file can be written, the operator
`WriteOcr` returns the value 2 (
H_MSG_TRUE)
.
Otherwise an exception will be raised.

## Possible Predecessors

`TraindOcrClassBox`,
`TrainfOcrClassBox`

## Possible Successors

`DoOcrMulti`,
`DoOcrSingle`

## See also

`ReadOcr`,
`DoOcrMulti`,
`TraindOcrClassBox`,
`TrainfOcrClassBox`

## Module

OCR/OCV
