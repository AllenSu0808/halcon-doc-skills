# DeserializeClassKnn (Operator)

## Name

`DeserializeClassKnn` — Deserialize a serialized k-NN classifier.

## Signature

`static void HOperatorSet.DeserializeClassKnn(HTuple serializedItemHandle, out HTuple KNNHandle)`

`void HClassKnn.DeserializeClassKnn(HSerializedItem serializedItemHandle)`

## Description

`DeserializeClassKnn` deserializes a k-NN classifier (k-NN)
(including its training samples), that was serialized
by [`SerializeClassKnn`](serialize_class_knn.md) (see [`FwriteSerializedItem`](fwrite_serialized_item.md) for an
introduction of the basic principle of serialization). The
serialized k-NN classifier is defined by the handle
*`serializedItemHandle`*. The deserialized values are stored in an
automatically created k-NN classifier with the handle
*`KNNHandle`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`serializedItemHandle`** (input_control)  serialized_item `→` [HSerializedItem](HSerializedItem.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the serialized item.

**`KNNHandle`** (output_control)  class_knn `→` [HClassKnn](HClassKnn.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the k-NN classifier.

## Result

If the parameters are valid, the operator
`DeserializeClassKnn` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`FreadSerializedItem`,
`ReceiveSerializedItem`,
`SerializeClassKnn`

## Possible Successors

`ClassifyClassKnn`

## Alternatives

`SerializeClassKnn`

## See also

`CreateClassKnn`

## References

Marius Muja, David G. Lowe: “Fast Approximate Nearest Neighbors with
Automatic Algorithm Configuration”;
International Conference on Computer Vision Theory
and Applications (VISAPP 09); 2009.

## Module

Foundation
