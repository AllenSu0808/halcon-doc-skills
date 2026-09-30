# deserialize_class_knn (Operator)

## Name

`deserialize_class_knn` — Deserialize a serialized k-NN classifier.

## Signature

`def deserialize_class_knn(serialized_item_handle: HHandle) -> HHandle`

## Description

`deserialize_class_knn` deserializes a k-NN classifier (k-NN)
(including its training samples), that was serialized
by [`serialize_class_knn`](serialize_class_knn.md) (see [`fwrite_serialized_item`](fwrite_serialized_item.md) for an
introduction of the basic principle of serialization). The
serialized k-NN classifier is defined by the handle
*`serialized_item_handle`*. The deserialized values are stored in an
automatically created k-NN classifier with the handle
*`knnhandle`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`serialized_item_handle`** (input_control)  serialized_item `→` HHandle

Handle of the serialized item.

**`knnhandle`** (output_control)  class_knn `→` HHandle

Handle of the k-NN classifier.

## Result

If the parameters are valid, the operator
`deserialize_class_knn` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`fread_serialized_item`,
`receive_serialized_item`,
`serialize_class_knn`

## Possible Successors

`classify_class_knn`

## Alternatives

`serialize_class_knn`

## See also

`create_class_knn`

## References

Marius Muja, David G. Lowe: “Fast Approximate Nearest Neighbors with
Automatic Algorithm Configuration”;
International Conference on Computer Vision Theory
and Applications (VISAPP 09); 2009.

## Module

Foundation
