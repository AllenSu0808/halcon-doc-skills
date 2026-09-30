# SerializeOcr (Operator)

## Name

`SerializeOcr` — Serialize an OCR classifier.

## Warning

**`SerializeOcr` is obsolete and is only provided for
reasons of backward compatibility. New applications should use the
MLP, SVM or CNN based operators instead.**

## Signature

`static void HOperatorSet.SerializeOcr(HTuple ocrHandle, out HTuple serializedItemHandle)`

`HSerializedItem HOCRBox.SerializeOcr()`

## Description

`SerializeOcr` serializes an OCR classifier (see
[`FwriteSerializedItem`](fwrite_serialized_item.md) for an introduction of the basic
principle of serialization). The same data that is written in a
file by [`WriteOcr`](write_ocr.md) is converted to a serialized item.
The OCR classifier is defined by the handle *`ocrHandle`*. The
serialized OCR classifier is returned by the handle
*`serializedItemHandle`* and can be deserialized by
[`DeserializeOcr`](deserialize_ocr.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`ocrHandle`** (input_control)  ocr_box `→` [HOCRBox](HOCRBox.md), [HTuple](HTuple.md) (*IntPtr*)

ID of the OCR classifier.

**`serializedItemHandle`** (output_control)  serialized_item `→` [HSerializedItem](HSerializedItem.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the serialized item.

## Result

If the parameters are valid, the operator
`SerializeOcr` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`TraindOcrClassBox`,
`TrainfOcrClassBox`

## Possible Successors

`DoOcrMulti`,
`DoOcrSingle`,
`FwriteSerializedItem`,
`SendSerializedItem`,
`DeserializeOcr`

## See also

`DeserializeOcr`,
`DoOcrMulti`,
`TraindOcrClassBox`,
`TrainfOcrClassBox`

## Module

OCR/OCV
