# deserialize_ocr_class_svm (Operator)

## Name

`deserialize_ocr_class_svm` — Deserialize a serialized SVM-based OCR classifier.

## Signature

`def deserialize_ocr_class_svm(serialized_item_handle: HHandle) -> HHandle`

## Description

`deserialize_ocr_class_svm` deserializes a SVM-based OCR classifier,
that was serialized by [`serialize_ocr_class_svm`](serialize_ocr_class_svm.md) (see
[`fwrite_serialized_item`](fwrite_serialized_item.md) for an introduction of the basic principle
of serialization). The serialized OCR classifier is defined by the handle
*`serialized_item_handle`*. The deserialized values are stored in an
automatically created OCR classifier with the handle *`ocrhandle`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`serialized_item_handle`** (input_control)  serialized_item `→` HHandle

Handle of the serialized item.

**`ocrhandle`** (output_control)  ocr_svm `→` HHandle

Handle of the OCR classifier.

## Result

If the parameters are valid, the operator
`deserialize_ocr_class_svm` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`fread_serialized_item`,
`receive_serialized_item`,
`serialize_ocr_class_svm`

## Possible Successors

`do_ocr_single_class_svm`,
`do_ocr_multi_class_svm`

## See also

`create_ocr_class_svm`,
`write_ocr_class_svm`,
`read_class_svm`,
`write_class_svm`,
`serialize_ocr_class_svm`

## Module

OCR/OCV
