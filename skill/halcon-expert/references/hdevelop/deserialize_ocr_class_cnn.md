# deserialize_ocr_class_cnn (Operator)

## Name

`deserialize_ocr_class_cnn` — Deserialize a serialized CNN-based OCR classifier.

## Signature

`deserialize_ocr_class_cnn( : : SerializedItemHandle : OCRHandle)`

## Description

`deserialize_ocr_class_cnn` deserializes a CNN-based OCR classifier,
that was serialized by [`serialize_ocr_class_cnn`](serialize_ocr_class_cnn.md) (see
[`fwrite_serialized_item`](fwrite_serialized_item.md) for an introduction of the basic principle
of serialization). The serialized OCR classifier is defined by the handle
*`SerializedItemHandle`*. The deserialized values are stored in an
automatically created OCR classifier with the handle *`OCRHandle`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`SerializedItemHandle`** (input_control)  serialized_item `→`  (handle)

Handle of the serialized item.

**`OCRHandle`** (output_control)  ocr_cnn `→`  (handle)

Handle of the OCR classifier.

## Result

If the parameters are valid, the operator
`deserialize_ocr_class_cnn` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`fread_serialized_item`,
`receive_serialized_item`,
`serialize_ocr_class_cnn`

## Possible Successors

`do_ocr_single_class_cnn`,
`do_ocr_multi_class_cnn`

## Module

OCR/OCV
