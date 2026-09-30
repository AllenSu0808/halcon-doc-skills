# serialize_ocr_class_knn (Operator)

## Name

`serialize_ocr_class_knn` — Serialize a k-NN-based OCR classifier.

## Signature

`serialize_ocr_class_knn( : : OCRHandle : SerializedItemHandle)`

## Description

`serialize_ocr_class_knn` serializes a k-NN-based OCR classifier (see
[`fwrite_serialized_item`](fwrite_serialized_item.md) for an introduction of the basic
principle of serialization). The same data that is written in a
file by [`write_ocr_class_knn`](write_ocr_class_knn.md) is converted to a serialized item.
The OCR classifier is defined by the handle *`OCRHandle`*. The
serialized OCR classifier is returned by the handle
*`SerializedItemHandle`* and can be deserialized by
[`deserialize_ocr_class_knn`](deserialize_ocr_class_knn.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`OCRHandle`** (input_control)  ocr_knn `→`  (handle)

Handle of the OCR classifier.

**`SerializedItemHandle`** (output_control)  serialized_item `→`  (handle)

Handle of the serialized item.

## Result

If the parameters are valid, the operator
`serialize_ocr_class_knn` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`trainf_ocr_class_knn`,
`read_ocr_class_knn`

## Possible Successors

`fwrite_serialized_item`,
`send_serialized_item`,
`deserialize_ocr_class_knn`

## See also

`create_class_knn`,
`read_ocr_class_knn`,
`deserialize_ocr_class_knn`

## References

Marius Muja, David G. Lowe: “Fast Approximate Nearest Neighbors with
Automatic Algorithm Configuration”;
International Conference on Computer Vision Theory
and Applications (VISAPP 09); 2009.

## Module

OCR/OCV
