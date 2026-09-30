# deserialize_ocr_class_knn (Operator)

## Name

`deserialize_ocr_class_knn` — Deserialize a serialized k-NN-based OCR classifier.

## Signature

`deserialize_ocr_class_knn( : : SerializedItemHandle : OCRHandle)`

## Description

`deserialize_ocr_class_knn` deserializes a k-NN-based OCR
classifier, that was serialized by [`serialize_ocr_class_knn`](serialize_ocr_class_knn.md) (see
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

**`OCRHandle`** (output_control)  ocr_knn `→`  (handle)

Handle of the OCR classifier.

## Result

If the parameters are valid, the operator
`deserialize_ocr_class_knn` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`fread_serialized_item`,
`receive_serialized_item`,
`serialize_ocr_class_knn`

## Possible Successors

`classify_class_knn`

## See also

`create_ocr_class_knn`,
`serialize_ocr_class_knn`

## References

Marius Muja, David G. Lowe: “Fast Approximate Nearest Neighbors with
Automatic Algorithm Configuration”;
International Conference on Computer Vision Theory
and Applications (VISAPP 09); 2009.

## Module

OCR/OCV
