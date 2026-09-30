# serialize_class_mlp (Operator)

## Name

`serialize_class_mlp` — Serialize a multilayer perceptron (MLP).

## Signature

`def serialize_class_mlp(mlphandle: HHandle) -> HHandle`

## Description

`serialize_class_mlp` serializes a multilayer perceptron (MLP) and
its stored training samples (see [`fwrite_serialized_item`](fwrite_serialized_item.md) for an
introduction of the basic principle of serialization). The same data that
is written in a file by [`write_class_mlp`](write_class_mlp.md) and
[`write_samples_class_mlp`](write_samples_class_mlp.md) is converted to a serialized item.
The multilayer perceptron is defined by the handle *`mlphandle`*.
The serialized multilayer perceptron is returned by the handle
*`serialized_item_handle`* and can be deserialized by
[`deserialize_class_mlp`](deserialize_class_mlp.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`mlphandle`** (input_control)  class_mlp `→` HHandle

MLP handle.

**`serialized_item_handle`** (output_control)  serialized_item `→` HHandle

Handle of the serialized item.

## Result

If the parameters are valid, the operator
`serialize_class_mlp` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`train_class_mlp`

## Possible Successors

`clear_class_mlp`,
`fwrite_serialized_item`,
`send_serialized_item`,
`deserialize_class_mlp`

## See also

`create_class_mlp`,
`read_class_mlp`,
`write_samples_class_mlp`,
`deserialize_class_mlp`

## Module

Foundation
