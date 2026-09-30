# serialize_ocr_class_knn (Operator)

## Name

`serialize_ocr_class_knn` — Serialize a k-NN-based OCR classifier.

## Signature

`def serialize_ocr_class_knn(ocrhandle: HHandle) -> HHandle`

## Description

`serialize_ocr_class_knn` serializes a k-NN-based OCR classifier (see
[`fwrite_serialized_item`](fwrite_serialized_item.md) for an introduction of the basic
principle of serialization). The same data that is written in a
file by [`write_ocr_class_knn`](write_ocr_class_knn.md) is converted to a serialized item.
The OCR classifier is defined by the handle *`ocrhandle`*. The
serialized OCR classifier is returned by the handle
*`serialized_item_handle`* and can be deserialized by
[`deserialize_ocr_class_knn`](deserialize_ocr_class_knn.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`ocrhandle`** (input_control)  ocr_knn `→` HHandle

Handle of the OCR classifier.

**`serialized_item_handle`** (output_control)  serialized_item `→` HHandle

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
