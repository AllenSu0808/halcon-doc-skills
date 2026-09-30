# deserialize_ocr (Operator)

## Name

`deserialize_ocr` — Deserialize a serialized OCR classifier.

## Warning

**`deserialize_ocr` is obsolete and is only provided for
reasons of backward compatibility. New applications should use the
MLP, SVM or CNN based operators instead.**

## Signature

`deserialize_ocr( : : SerializedItemHandle : OcrHandle)`

## Description

`deserialize_ocr` deserializes an OCR classifier, that was serialized
by [`serialize_ocr`](serialize_ocr.md) (see [`fwrite_serialized_item`](fwrite_serialized_item.md) for an
introduction of the basic principle of serialization). The serialized
OCR classifier is defined by the handle *`SerializedItemHandle`*.
The deserialized values are stored in an automatically created
OCR classifier with the handle *`OcrHandle`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`SerializedItemHandle`** (input_control)  serialized_item `→`  (handle)

Handle of the serialized item.

**`OcrHandle`** (output_control)  ocr_box `→`  (handle)

ID of the OCR classifier.

## Result

If the parameters are valid, the operator
`deserialize_ocr` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`reset_obj_db`,
`fread_serialized_item`,
`receive_serialized_item`,
`serialize_ocr`

## Possible Successors

`do_ocr_multi`,
`do_ocr_single`,
`traind_ocr_class_box`,
`trainf_ocr_class_box`

## See also

`serialize_ocr`,
`do_ocr_multi`,
`traind_ocr_class_box`,
`trainf_ocr_class_box`

## Module

OCR/OCV
