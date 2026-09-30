# SerializeOcrClassMlp (Operator)

## Name

`SerializeOcrClassMlp` — Serialize a MLP-based OCR classifier.

## Signature

`static void HOperatorSet.SerializeOcrClassMlp(HTuple OCRHandle, out HTuple serializedItemHandle)`

`HSerializedItem HOCRMlp.SerializeOcrClassMlp()`

## Description

`SerializeOcrClassMlp` serializes a MLP-based OCR classifier (see
[`FwriteSerializedItem`](fwrite_serialized_item.md) for an introduction of the basic
principle of serialization). The same data that is written in a
file by [`WriteOcrClassMlp`](write_ocr_class_mlp.md) is converted to a serialized item.
The OCR classifier is defined by the handle *`OCRHandle`*. The
serialized OCR classifier is returned by the handle
*`serializedItemHandle`* and can be deserialized by
[`DeserializeOcrClassMlp`](deserialize_ocr_class_mlp.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`OCRHandle`** (input_control)  ocr_mlp `→` [HOCRMlp](HOCRMlp.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the OCR classifier.

**`serializedItemHandle`** (output_control)  serialized_item `→` [HSerializedItem](HSerializedItem.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the serialized item.

## Result

If the parameters are valid, the operator
`SerializeOcrClassMlp` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`TrainfOcrClassMlp`

## Possible Successors

`ClearOcrClassMlp`,
`FwriteSerializedItem`,
`SendSerializedItem`,
`DeserializeOcrClassMlp`

## See also

`CreateOcrClassMlp`,
`ReadOcrClassMlp`,
`WriteClassMlp`,
`ReadClassMlp`,
`DeserializeOcrClassMlp`

## Module

OCR/OCV
