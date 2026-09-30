# SerializeOcrClassKnn (Operator)

## Name

`SerializeOcrClassKnn` — Serialize a k-NN-based OCR classifier.

## Signature

`static void HOperatorSet.SerializeOcrClassKnn(HTuple OCRHandle, out HTuple serializedItemHandle)`

`HSerializedItem HOCRKnn.SerializeOcrClassKnn()`

## Description

`SerializeOcrClassKnn` serializes a k-NN-based OCR classifier (see
[`FwriteSerializedItem`](fwrite_serialized_item.md) for an introduction of the basic
principle of serialization). The same data that is written in a
file by [`WriteOcrClassKnn`](write_ocr_class_knn.md) is converted to a serialized item.
The OCR classifier is defined by the handle *`OCRHandle`*. The
serialized OCR classifier is returned by the handle
*`serializedItemHandle`* and can be deserialized by
[`DeserializeOcrClassKnn`](deserialize_ocr_class_knn.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`OCRHandle`** (input_control)  ocr_knn `→` [HOCRKnn](HOCRKnn.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the OCR classifier.

**`serializedItemHandle`** (output_control)  serialized_item `→` [HSerializedItem](HSerializedItem.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the serialized item.

## Result

If the parameters are valid, the operator
`SerializeOcrClassKnn` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`TrainfOcrClassKnn`,
`ReadOcrClassKnn`

## Possible Successors

`FwriteSerializedItem`,
`SendSerializedItem`,
`DeserializeOcrClassKnn`

## See also

`CreateClassKnn`,
`ReadOcrClassKnn`,
`DeserializeOcrClassKnn`

## References

Marius Muja, David G. Lowe: “Fast Approximate Nearest Neighbors with
Automatic Algorithm Configuration”;
International Conference on Computer Vision Theory
and Applications (VISAPP 09); 2009.

## Module

OCR/OCV
