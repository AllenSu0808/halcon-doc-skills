# serialize_ocr (Operator)

## Name

`serialize_ocr` — Serialize an OCR classifier.

## Warning

**`serialize_ocr` is obsolete and is only provided for
reasons of backward compatibility. New applications should use the
MLP, SVM or CNN based operators instead.**

## Signature

`def serialize_ocr(ocr_handle: HHandle) -> HHandle`

## Description

`serialize_ocr` serializes an OCR classifier (see
[`fwrite_serialized_item`](fwrite_serialized_item.md) for an introduction of the basic
principle of serialization). The same data that is written in a
file by [`write_ocr`](write_ocr.md) is converted to a serialized item.
The OCR classifier is defined by the handle *`ocr_handle`*. The
serialized OCR classifier is returned by the handle
*`serialized_item_handle`* and can be deserialized by
[`deserialize_ocr`](deserialize_ocr.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`ocr_handle`** (input_control)  ocr_box `→` HHandle

ID of the OCR classifier.

**`serialized_item_handle`** (output_control)  serialized_item `→` HHandle

Handle of the serialized item.

## Result

If the parameters are valid, the operator
`serialize_ocr` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`traind_ocr_class_box`,
`trainf_ocr_class_box`

## Possible Successors

`do_ocr_multi`,
`do_ocr_single`,
`fwrite_serialized_item`,
`send_serialized_item`,
`deserialize_ocr`

## See also

`deserialize_ocr`,
`do_ocr_multi`,
`traind_ocr_class_box`,
`trainf_ocr_class_box`

## Module

OCR/OCV
