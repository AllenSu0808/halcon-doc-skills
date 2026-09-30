# close_ocr (Operator)

## Name

`close_ocr` — Deallocation of the memory of an OCR classifier.

## Warning

**`close_ocr` is obsolete and is only provided for
reasons of backward compatibility. New applications should use the
MLP, SVM or CNN based operators instead.**

## Signature

`close_ocr( : : OcrHandle : )`

## Description

The operator `close_ocr` deallocates the
memory of the classifier having the number *`OcrHandle`*.
Hereby all corresponding data will be deleted. However,
if necessary, they can be saved in advance using the
operator [`write_ocr`](write_ocr.md).
The number *`OcrHandle`* will be invalid after the call;
but later the system can use it again for new classifiers.

## Attention

All data of the classifier will be deleted in main memory (not on the
hard disk).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- OcrHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`OcrHandle`** (input_control, state is modified)  ocr_box `→`  (handle)

ID of the OCR classifier to be deleted.

## Result

If the parameter *`OcrHandle`* is valid, the operator
`close_ocr` returns the value 2 (
H_MSG_TRUE)
.
Otherwise an exception will be raised.

## Possible Predecessors

`write_ocr_trainf`

## Possible Successors

`read_ocr`

## Module

OCR/OCV
