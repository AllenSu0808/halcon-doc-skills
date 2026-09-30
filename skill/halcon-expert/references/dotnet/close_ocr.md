# CloseOcr (Operator)

## Name

`CloseOcr` — Deallocation of the memory of an OCR classifier.

## Warning

**`CloseOcr` is obsolete and is only provided for
reasons of backward compatibility. New applications should use the
MLP, SVM or CNN based operators instead.**

## Signature

`static void HOperatorSet.CloseOcr(HTuple ocrHandle)`

`void HOCRBox.CloseOcr()`

## Description

The operator `CloseOcr` deallocates the
memory of the classifier having the number *`ocrHandle`*.
Hereby all corresponding data will be deleted. However,
if necessary, they can be saved in advance using the
operator [`WriteOcr`](write_ocr.md).
The number *`ocrHandle`* will be invalid after the call;
but later the system can use it again for new classifiers.

## Attention

All data of the classifier will be deleted in main memory (not on the
hard disk).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- ocrHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`ocrHandle`** (input_control, state is modified)  ocr_box `→` [HOCRBox](HOCRBox.md), [HTuple](HTuple.md) (*IntPtr*)

ID of the OCR classifier to be deleted.

## Result

If the parameter *`ocrHandle`* is valid, the operator
`CloseOcr` returns the value 2 (
H_MSG_TRUE)
.
Otherwise an exception will be raised.

## Possible Predecessors

`WriteOcrTrainf`

## Possible Successors

`ReadOcr`

## Module

OCR/OCV
