# serialize_class_knn (Operator)

## Name

`serialize_class_knn` — Serialize a k-NN classifier.

## Signature

`def serialize_class_knn(knnhandle: HHandle) -> HHandle`

## Description

`serialize_class_knn` serializes a k-NN classifier (k-NN) and
its stored training samples (see [`fwrite_serialized_item`](fwrite_serialized_item.md) for an
introduction of the basic principle of serialization). The same data that
is written in a file by [`write_class_knn`](write_class_knn.md) is converted to a
serialized item. The k-NN classifier is defined by the handle
*`knnhandle`*. The serialized k-NN classifier is returned by the
handle *`serialized_item_handle`* and can be deserialized by
[`deserialize_class_knn`](deserialize_class_knn.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`knnhandle`** (input_control)  class_knn `→` HHandle

Handle of the k-NN classifier.

**`serialized_item_handle`** (output_control)  serialized_item `→` HHandle

Handle of the serialized item.

## Result

If the parameters are valid, the operator
`serialize_class_knn` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`train_class_knn`,
`read_class_knn`

## Possible Successors

`fwrite_serialized_item`,
`send_serialized_item`,
`deserialize_class_knn`

## See also

`create_class_knn`,
`read_class_knn`,
`deserialize_class_knn`

## References

Marius Muja, David G. Lowe: “Fast Approximate Nearest Neighbors with
Automatic Algorithm Configuration”;
International Conference on Computer Vision Theory
and Applications (VISAPP 09); 2009.

## Module

Foundation
