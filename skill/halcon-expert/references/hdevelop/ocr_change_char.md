# ocr_change_char (Operator)

## Name

`ocr_change_char` — Define a new conversion table for the characters.

## Warning

**`ocr_change_char` is obsolete and is only provided for
reasons of backward compatibility. New applications should use the
MLP, SVM or CNN based operators instead.**

## Signature

`ocr_change_char( : : OcrHandle, Character : )`

## Description

The operator `ocr_change_char` establishes
a new look-up table for the characters. Hereby the
number of strings of *`Character`* must be the same as
of the classifier *`OcrHandle`*.
In order to enlarge the font, the operator
`ocr_change_char` may be used as follows:
More characters than actually needed will be indicated when
creating a network using ([`create_ocr_class_box`](create_ocr_class_box.md)).
The last n characters will not be used so far.
If more characters are needed at a later stage, these unused
characters will be allocated and then trained with the help of the
operator `ocr_change_char`.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- OcrHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`OcrHandle`** (input_control, state is modified)  ocr_box `→`  (handle)

ID of the OCR-network to be changed.

**`Character`** (input_control)  string-array `→`  (string)

New assign of characters.

Default:
['a','b','c']

## Result

If the number of characters in *`Character`* is identical
with the number of the characters of the network, the operator
`ocr_change_char` returns the value 2 (
H_MSG_TRUE)
.
Otherwise an exception will be raised.

## Possible Predecessors

`read_ocr`

## Possible Successors

`do_ocr_multi_class_mlp`,
`do_ocr_single_class_mlp`

## Module

OCR/OCV
