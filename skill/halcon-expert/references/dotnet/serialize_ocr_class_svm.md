# SerializeOcrClassSvm (Operator)

## Name

`SerializeOcrClassSvm` — Serialize a SVM-based OCR classifier

## Signature

`static void HOperatorSet.SerializeOcrClassSvm(HTuple OCRHandle, out HTuple serializedItemHandle)`

`HSerializedItem HOCRSvm.SerializeOcrClassSvm()`

## Description

`SerializeOcrClassSvm` serializes a SVM-based OCR classifier (see
[`FwriteSerializedItem`](fwrite_serialized_item.md) for an introduction of the basic
principle of serialization). The same data that is written in a
file by [`WriteOcrClassSvm`](write_ocr_class_svm.md) is converted to a serialized item.
The OCR classifier is defined by the handle *`OCRHandle`*. The
serialized OCR classifier is returned by the handle
*`serializedItemHandle`* and can be deserialized by
[`DeserializeOcrClassSvm`](deserialize_ocr_class_svm.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`OCRHandle`** (input_control)  ocr_svm `→` [HOCRSvm](HOCRSvm.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the OCR classifier.

**`serializedItemHandle`** (output_control)  serialized_item `→` [HSerializedItem](HSerializedItem.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the serialized item.

## Result

If the parameters are valid, the operator
`SerializeOcrClassSvm` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`TrainfOcrClassSvm`

## Possible Successors

`ClearOcrClassSvm`,
`FwriteSerializedItem`,
`SendSerializedItem`,
`DeserializeOcrClassSvm`

## See also

`CreateOcrClassSvm`,
`ReadOcrClassSvm`,
`WriteClassSvm`,
`ReadClassSvm`,
`DeserializeOcrClassSvm`

## Module

OCR/OCV
