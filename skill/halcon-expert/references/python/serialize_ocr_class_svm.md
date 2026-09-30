# serialize_ocr_class_svm (Operator)

## Name

`serialize_ocr_class_svm` — Serialize a SVM-based OCR classifier

## Signature

`def serialize_ocr_class_svm(ocrhandle: HHandle) -> HHandle`

## Description

`serialize_ocr_class_svm` serializes a SVM-based OCR classifier (see
[`fwrite_serialized_item`](fwrite_serialized_item.md) for an introduction of the basic
principle of serialization). The same data that is written in a
file by [`write_ocr_class_svm`](write_ocr_class_svm.md) is converted to a serialized item.
The OCR classifier is defined by the handle *`ocrhandle`*. The
serialized OCR classifier is returned by the handle
*`serialized_item_handle`* and can be deserialized by
[`deserialize_ocr_class_svm`](deserialize_ocr_class_svm.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`ocrhandle`** (input_control)  ocr_svm `→` HHandle

Handle of the OCR classifier.

**`serialized_item_handle`** (output_control)  serialized_item `→` HHandle

Handle of the serialized item.

## Result

If the parameters are valid, the operator
`serialize_ocr_class_svm` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`trainf_ocr_class_svm`

## Possible Successors

`clear_ocr_class_svm`,
`fwrite_serialized_item`,
`send_serialized_item`,
`deserialize_ocr_class_svm`

## See also

`create_ocr_class_svm`,
`read_ocr_class_svm`,
`write_class_svm`,
`read_class_svm`,
`deserialize_ocr_class_svm`

## Module

OCR/OCV
