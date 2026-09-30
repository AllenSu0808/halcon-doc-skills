# OcrChangeChar (Operator)

## Name

`OcrChangeChar` — Define a new conversion table for the characters.

## Warning

**`OcrChangeChar` is obsolete and is only provided for
reasons of backward compatibility. New applications should use the
MLP, SVM or CNN based operators instead.**

## Signature

`static void HOperatorSet.OcrChangeChar(HTuple ocrHandle, HTuple character)`

`void HOCRBox.OcrChangeChar(HTuple character)`

## Description

The operator `OcrChangeChar` establishes
a new look-up table for the characters. Hereby the
number of strings of *`character`* must be the same as
of the classifier *`ocrHandle`*.
In order to enlarge the font, the operator
`OcrChangeChar` may be used as follows:
More characters than actually needed will be indicated when
creating a network using ([`CreateOcrClassBox`](create_ocr_class_box.md)).
The last n characters will not be used so far.
If more characters are needed at a later stage, these unused
characters will be allocated and then trained with the help of the
operator `OcrChangeChar`.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- ocrHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`ocrHandle`** (input_control, state is modified)  ocr_box `→` [HOCRBox](HOCRBox.md), [HTuple](HTuple.md) (*IntPtr*)

ID of the OCR-network to be changed.

**`character`** (input_control)  string-array `→` [HTuple](HTuple.md) (*string*)

New assign of characters.

Default:
["a","b","c"]

## Result

If the number of characters in *`character`* is identical
with the number of the characters of the network, the operator
`OcrChangeChar` returns the value 2 (
H_MSG_TRUE)
.
Otherwise an exception will be raised.

## Possible Predecessors

`ReadOcr`

## Possible Successors

`DoOcrMultiClassMlp`,
`DoOcrSingleClassMlp`

## Module

OCR/OCV
