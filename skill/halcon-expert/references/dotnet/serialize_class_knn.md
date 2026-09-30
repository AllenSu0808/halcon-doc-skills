# SerializeClassKnn (Operator)

## Name

`SerializeClassKnn` — Serialize a k-NN classifier.

## Signature

`static void HOperatorSet.SerializeClassKnn(HTuple KNNHandle, out HTuple serializedItemHandle)`

`HSerializedItem HClassKnn.SerializeClassKnn()`

## Description

`SerializeClassKnn` serializes a k-NN classifier (k-NN) and
its stored training samples (see [`FwriteSerializedItem`](fwrite_serialized_item.md) for an
introduction of the basic principle of serialization). The same data that
is written in a file by [`WriteClassKnn`](write_class_knn.md) is converted to a
serialized item. The k-NN classifier is defined by the handle
*`KNNHandle`*. The serialized k-NN classifier is returned by the
handle *`serializedItemHandle`* and can be deserialized by
[`DeserializeClassKnn`](deserialize_class_knn.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`KNNHandle`** (input_control)  class_knn `→` [HClassKnn](HClassKnn.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the k-NN classifier.

**`serializedItemHandle`** (output_control)  serialized_item `→` [HSerializedItem](HSerializedItem.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the serialized item.

## Result

If the parameters are valid, the operator
`SerializeClassKnn` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`TrainClassKnn`,
`ReadClassKnn`

## Possible Successors

`FwriteSerializedItem`,
`SendSerializedItem`,
`DeserializeClassKnn`

## See also

`CreateClassKnn`,
`ReadClassKnn`,
`DeserializeClassKnn`

## References

Marius Muja, David G. Lowe: “Fast Approximate Nearest Neighbors with
Automatic Algorithm Configuration”;
International Conference on Computer Vision Theory
and Applications (VISAPP 09); 2009.

## Module

Foundation
