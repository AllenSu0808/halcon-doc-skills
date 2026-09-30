# close_ocr (Operator)

## Name

`close_ocr` — Deallocation of the memory of an OCR classifier.

## Warning

**`close_ocr` is obsolete and is only provided for
reasons of backward compatibility. New applications should use the
MLP, SVM or CNN based operators instead.**

## Signature

`def close_ocr(ocr_handle: HHandle) -> None`

## Description

The operator `close_ocr` deallocates the
memory of the classifier having the number *`ocr_handle`*.
Hereby all corresponding data will be deleted. However,
if necessary, they can be saved in advance using the
operator [`write_ocr`](write_ocr.md).
The number *`ocr_handle`* will be invalid after the call;
but later the system can use it again for new classifiers.

## Attention

All data of the classifier will be deleted in main memory (not on the
hard disk).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- ocr_handle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`ocr_handle`** (input_control, state is modified)  ocr_box `→` HHandle

ID of the OCR classifier to be deleted.

## Result

If the parameter *`ocr_handle`* is valid, the operator
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
