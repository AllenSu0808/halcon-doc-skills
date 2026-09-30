# deserialize_class_mlp (Operator)

## Name

`deserialize_class_mlp` — Deserialize a serialized multilayer perceptron.

## Signature

`def deserialize_class_mlp(serialized_item_handle: HHandle) -> HHandle`

## Description

`deserialize_class_mlp` deserializes a multilayer perceptron (MLP)
(including its training samples), that was serialized
by [`serialize_class_mlp`](serialize_class_mlp.md) (see [`fwrite_serialized_item`](fwrite_serialized_item.md) for an
introduction of the basic principle of serialization). The
serialized multilayer perceptron is defined by the handle
*`serialized_item_handle`*. The deserialized values are stored in an
automatically created multilayer perceptron with the handle
*`mlphandle`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`serialized_item_handle`** (input_control)  serialized_item `→` HHandle

Handle of the serialized item.

**`mlphandle`** (output_control)  class_mlp `→` HHandle

MLP handle.

## Result

If the parameters are valid, the operator
`deserialize_class_mlp` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`fread_serialized_item`,
`receive_serialized_item`,
`serialize_class_mlp`

## Possible Successors

`classify_class_mlp`,
`evaluate_class_mlp`,
`create_class_lut_mlp`

## See also

`create_class_mlp`,
`write_class_mlp`,
`serialize_class_mlp`

## Module

Foundation
