# DeserializeOcrClassKnn (Operator)

## Name

`DeserializeOcrClassKnn` — Deserialize a serialized k-NN-based OCR classifier.

## Signature

`static void HOperatorSet.DeserializeOcrClassKnn(HTuple serializedItemHandle, out HTuple OCRHandle)`

`void HOCRKnn.DeserializeOcrClassKnn(HSerializedItem serializedItemHandle)`

## Description

`DeserializeOcrClassKnn` deserializes a k-NN-based OCR
classifier, that was serialized by [`SerializeOcrClassKnn`](serialize_ocr_class_knn.md) (see
[`FwriteSerializedItem`](fwrite_serialized_item.md) for an introduction of the basic principle
of serialization). The serialized OCR classifier is defined by the handle
*`serializedItemHandle`*. The deserialized values are stored in an
automatically created OCR classifier with the handle *`OCRHandle`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`serializedItemHandle`** (input_control)  serialized_item `→` [HSerializedItem](HSerializedItem.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the serialized item.

**`OCRHandle`** (output_control)  ocr_knn `→` [HOCRKnn](HOCRKnn.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the OCR classifier.

## Result

If the parameters are valid, the operator
`DeserializeOcrClassKnn` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`FreadSerializedItem`,
`ReceiveSerializedItem`,
`SerializeOcrClassKnn`

## Possible Successors

`ClassifyClassKnn`

## See also

`CreateOcrClassKnn`,
`SerializeOcrClassKnn`

## References

Marius Muja, David G. Lowe: “Fast Approximate Nearest Neighbors with
Automatic Algorithm Configuration”;
International Conference on Computer Vision Theory
and Applications (VISAPP 09); 2009.

## Module

OCR/OCV
