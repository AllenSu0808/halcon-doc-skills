# ClearOcrClassCnn (Operator)

## Name

`ClearOcrClassCnn` — Clear an CNN-based OCR classifier.

## Signature

`static void HOperatorSet.ClearOcrClassCnn(HTuple OCRHandle)`

`static void HOCRCnn.ClearOcrClassCnn(HOCRCnn[] OCRHandle)`

`void HOCRCnn.ClearOcrClassCnn()`

## Description

`ClearOcrClassCnn` clears the OCR classifier given by
*`OCRHandle`* that was read with [`ReadOcrClassCnn`](read_ocr_class_cnn.md) and frees
all memory required for the classifier. After calling
`ClearOcrClassCnn`, the classifier can no longer be used. The
handle *`OCRHandle`* becomes invalid.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- OCRHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`OCRHandle`** (input_control, state is modified)  ocr_cnn(-array) `→` [HOCRCnn](HOCRCnn.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the OCR classifier.

## Result

If *`OCRHandle`* is valid, the operator
`ClearOcrClassCnn` returns the value 2 (
H_MSG_TRUE)
. If necessary, an
exception is raised.

## Possible Predecessors

`DoOcrSingleClassCnn`,
`DoOcrMultiClassCnn`,
`DoOcrWordCnn`

## See also

`ReadOcrClassCnn`

## Module

OCR/OCV
