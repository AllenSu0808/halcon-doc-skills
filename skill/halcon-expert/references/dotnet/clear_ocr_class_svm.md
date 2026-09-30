# ClearOcrClassSvm (Operator)

## Name

`ClearOcrClassSvm` — Clear an SVM-based OCR classifier.

## Signature

`static void HOperatorSet.ClearOcrClassSvm(HTuple OCRHandle)`

`static void HOCRSvm.ClearOcrClassSvm(HOCRSvm[] OCRHandle)`

`void HOCRSvm.ClearOcrClassSvm()`

## Description

`ClearOcrClassSvm` clears the OCR classifier given by
*`OCRHandle`* and frees all memory required for the
classifier. After calling `ClearOcrClassSvm`, the
classifier can no longer be used. The handle *`OCRHandle`*
becomes invalid.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- OCRHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`OCRHandle`** (input_control, state is modified)  ocr_svm(-array) `→` [HOCRSvm](HOCRSvm.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the OCR classifier.

## Result

If *`OCRHandle`* is valid the operator
`ClearOcrClassSvm` returns the value 2 (
H_MSG_TRUE)
. If necessary,
an exception is raised.

## Possible Predecessors

`DoOcrSingleClassSvm`,
`DoOcrMultiClassSvm`

## See also

`CreateOcrClassSvm`,
`ReadOcrClassSvm`,
`WriteOcrClassSvm`,
`TrainfOcrClassSvm`

## Module

OCR/OCV
