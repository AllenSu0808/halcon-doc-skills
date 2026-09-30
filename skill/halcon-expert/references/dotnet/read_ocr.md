# ReadOcr (Operator)

## Name

`ReadOcr` — Read an OCR classifier from a file.

## Warning

**`ReadOcr` is obsolete and is only provided for
reasons of backward compatibility. New applications should use the
MLP, SVM or CNN based operators instead.**

## Signature

`static void HOperatorSet.ReadOcr(HTuple fileName, out HTuple ocrHandle)`

`public HOCRBox(string fileName)`

`void HOCRBox.ReadOcr(string fileName)`

## Description

The operator `ReadOcr` reads an OCR classifier from
a file *`fileName`*. This file will hereby be searched in
the directory ($HALCONROOT/ocr/) as well as in the currently used
directory. If too many classifiers have been loaded, an error message
will be displayed.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`fileName`** (input_control)  filename.read `→` [HTuple](HTuple.md) (*string*)

Name of the OCR classifier file.

Default:
"testnet"

File extension:
.`obc`, .`fnt`

**`ocrHandle`** (output_control)  ocr_box `→` [HOCRBox](HOCRBox.md), [HTuple](HTuple.md) (*IntPtr*)

ID of the read OCR classifier.

## Result

If the indicated file is available and the format is correct,
the operator `ReadOcr` returns the value 2 (
H_MSG_TRUE)
.
Otherwise an exception will be raised.

## Possible Predecessors

`ResetObjDb`

## Possible Successors

`DoOcrMulti`,
`DoOcrSingle`,
`TraindOcrClassBox`,
`TrainfOcrClassBox`

## See also

`WriteOcr`,
`DoOcrMulti`,
`TraindOcrClassBox`,
`TrainfOcrClassBox`

## Module

OCR/OCV
