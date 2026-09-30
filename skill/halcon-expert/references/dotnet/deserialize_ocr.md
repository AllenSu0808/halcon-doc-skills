# DeserializeOcr (Operator)

## Name

`DeserializeOcr` — Deserialize a serialized OCR classifier.

## Warning

**`DeserializeOcr` is obsolete and is only provided for
reasons of backward compatibility. New applications should use the
MLP, SVM or CNN based operators instead.**

## Signature

`static void HOperatorSet.DeserializeOcr(HTuple serializedItemHandle, out HTuple ocrHandle)`

`void HOCRBox.DeserializeOcr(HSerializedItem serializedItemHandle)`

## Description

`DeserializeOcr` deserializes an OCR classifier, that was serialized
by [`SerializeOcr`](serialize_ocr.md) (see [`FwriteSerializedItem`](fwrite_serialized_item.md) for an
introduction of the basic principle of serialization). The serialized
OCR classifier is defined by the handle *`serializedItemHandle`*.
The deserialized values are stored in an automatically created
OCR classifier with the handle *`ocrHandle`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`serializedItemHandle`** (input_control)  serialized_item `→` [HSerializedItem](HSerializedItem.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the serialized item.

**`ocrHandle`** (output_control)  ocr_box `→` [HOCRBox](HOCRBox.md), [HTuple](HTuple.md) (*IntPtr*)

ID of the OCR classifier.

## Result

If the parameters are valid, the operator
`DeserializeOcr` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`ResetObjDb`,
`FreadSerializedItem`,
`ReceiveSerializedItem`,
`SerializeOcr`

## Possible Successors

`DoOcrMulti`,
`DoOcrSingle`,
`TraindOcrClassBox`,
`TrainfOcrClassBox`

## See also

`SerializeOcr`,
`DoOcrMulti`,
`TraindOcrClassBox`,
`TrainfOcrClassBox`

## Module

OCR/OCV
