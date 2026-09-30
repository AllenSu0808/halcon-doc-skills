# ClearOcrClassMlp (Operator)

## Name

`ClearOcrClassMlp` — Clear an OCR classifier.

## Signature

`static void HOperatorSet.ClearOcrClassMlp(HTuple OCRHandle)`

`static void HOCRMlp.ClearOcrClassMlp(HOCRMlp[] OCRHandle)`

`void HOCRMlp.ClearOcrClassMlp()`

## Description

`ClearOcrClassMlp` clears the OCR classifier given by
*`OCRHandle`* that was created with
[`CreateOcrClassMlp`](create_ocr_class_mlp.md) and frees all memory required for the
classifier. After calling `ClearOcrClassMlp`, the
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

**`OCRHandle`** (input_control, state is modified)  ocr_mlp(-array) `→` [HOCRMlp](HOCRMlp.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the OCR classifier.

## Result

If *`OCRHandle`* is valid, the operator
`ClearOcrClassMlp` returns the value 2 (
H_MSG_TRUE)
. If necessary, an
exception is raised.

## Possible Predecessors

`DoOcrSingleClassMlp`,
`DoOcrMultiClassMlp`

## See also

`CreateOcrClassMlp`,
`ReadOcrClassMlp`,
`WriteOcrClassMlp`,
`TrainfOcrClassMlp`

## Module

OCR/OCV
