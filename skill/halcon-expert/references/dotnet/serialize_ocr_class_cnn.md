# SerializeOcrClassCnn (Operator)

## Name

`SerializeOcrClassCnn` — Serialize a CNN-based OCR classifier

## Signature

`static void HOperatorSet.SerializeOcrClassCnn(HTuple OCRHandle, out HTuple serializedItemHandle)`

`HSerializedItem HOCRCnn.SerializeOcrClassCnn()`

## Description

`SerializeOcrClassCnn` serializes a CNN-based OCR classifier (see
[`FwriteSerializedItem`](fwrite_serialized_item.md) for an introduction of the basic
principle of serialization). The OCR classifier is defined by the handle
*`OCRHandle`*. The serialized OCR classifier is returned by the handle
*`serializedItemHandle`* and can be deserialized by
[`DeserializeOcrClassCnn`](deserialize_ocr_class_cnn.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`OCRHandle`** (input_control)  ocr_cnn `→` [HOCRCnn](HOCRCnn.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the OCR classifier.

**`serializedItemHandle`** (output_control)  serialized_item `→` [HSerializedItem](HSerializedItem.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the serialized item.

## Result

If the parameters are valid, the operator
`SerializeOcrClassCnn` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Successors

`ClearOcrClassCnn`,
`FwriteSerializedItem`,
`SendSerializedItem`,
`DeserializeOcrClassCnn`

## Module

OCR/OCV
