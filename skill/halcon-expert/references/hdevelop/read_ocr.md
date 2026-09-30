# read_ocr (Operator)

## Name

`read_ocr` — Read an OCR classifier from a file.

## Warning

**`read_ocr` is obsolete and is only provided for
reasons of backward compatibility. New applications should use the
MLP, SVM or CNN based operators instead.**

## Signature

`read_ocr( : : FileName : OcrHandle)`

## Description

The operator `read_ocr` reads an OCR classifier from
a file *`FileName`*. This file will hereby be searched in
the directory ($HALCONROOT/ocr/) as well as in the currently used
directory. If too many classifiers have been loaded, an error message
will be displayed.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`FileName`** (input_control)  filename.read `→`  (string)

Name of the OCR classifier file.

Default:
'testnet'

File extension:
.`obc`, .`fnt`

**`OcrHandle`** (output_control)  ocr_box `→`  (handle)

ID of the read OCR classifier.

## Result

If the indicated file is available and the format is correct,
the operator `read_ocr` returns the value 2 (
H_MSG_TRUE)
.
Otherwise an exception will be raised.

## Possible Predecessors

`reset_obj_db`

## Possible Successors

`do_ocr_multi`,
`do_ocr_single`,
`traind_ocr_class_box`,
`trainf_ocr_class_box`

## See also

`write_ocr`,
`do_ocr_multi`,
`traind_ocr_class_box`,
`trainf_ocr_class_box`

## Module

OCR/OCV
