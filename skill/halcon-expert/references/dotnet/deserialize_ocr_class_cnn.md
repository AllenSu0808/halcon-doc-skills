# DeserializeOcrClassCnn (Operator)

## Name

`DeserializeOcrClassCnn` — Deserialize a serialized CNN-based OCR classifier.

## Signature

`static void HOperatorSet.DeserializeOcrClassCnn(HTuple serializedItemHandle, out HTuple OCRHandle)`

`void HOCRCnn.DeserializeOcrClassCnn(HSerializedItem serializedItemHandle)`

## Description

`DeserializeOcrClassCnn` deserializes a CNN-based OCR classifier,
that was serialized by [`SerializeOcrClassCnn`](serialize_ocr_class_cnn.md) (see
[`FwriteSerializedItem`](fwrite_serialized_item.md) for an introduction of the basic principle
of serialization). The serialized OCR classifier is defined by the handle
*`serializedItemHandle`*. The deserialized values are stored in an
automatically created OCR classifier with the handle *`OCRHandle`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`serializedItemHandle`** (input_control)  serialized_item `→` [HSerializedItem](HSerializedItem.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the serialized item.

**`OCRHandle`** (output_control)  ocr_cnn `→` [HOCRCnn](HOCRCnn.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the OCR classifier.

## Result

If the parameters are valid, the operator
`DeserializeOcrClassCnn` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`FreadSerializedItem`,
`ReceiveSerializedItem`,
`SerializeOcrClassCnn`

## Possible Successors

`DoOcrSingleClassCnn`,
`DoOcrMultiClassCnn`

## Module

OCR/OCV
