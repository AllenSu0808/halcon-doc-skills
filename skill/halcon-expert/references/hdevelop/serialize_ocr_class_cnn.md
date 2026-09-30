# serialize_ocr_class_cnn (Operator)

## Name

`serialize_ocr_class_cnn` — Serialize a CNN-based OCR classifier

## Signature

`serialize_ocr_class_cnn( : : OCRHandle : SerializedItemHandle)`

## Description

`serialize_ocr_class_cnn` serializes a CNN-based OCR classifier (see
[`fwrite_serialized_item`](fwrite_serialized_item.md) for an introduction of the basic
principle of serialization). The OCR classifier is defined by the handle
*`OCRHandle`*. The serialized OCR classifier is returned by the handle
*`SerializedItemHandle`* and can be deserialized by
[`deserialize_ocr_class_cnn`](deserialize_ocr_class_cnn.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`OCRHandle`** (input_control)  ocr_cnn `→`  (handle)

Handle of the OCR classifier.

**`SerializedItemHandle`** (output_control)  serialized_item `→`  (handle)

Handle of the serialized item.

## Result

If the parameters are valid, the operator
`serialize_ocr_class_cnn` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Successors

`clear_ocr_class_cnn`,
`fwrite_serialized_item`,
`send_serialized_item`,
`deserialize_ocr_class_cnn`

## Module

OCR/OCV
