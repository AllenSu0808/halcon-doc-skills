# deserialize_class_mlp (Operator)

## Name

`deserialize_class_mlp` — Deserialize a serialized multilayer perceptron.

## Signature

`deserialize_class_mlp( : : SerializedItemHandle : MLPHandle)`

## Description

`deserialize_class_mlp` deserializes a multilayer perceptron (MLP)
(including its training samples), that was serialized
by [`serialize_class_mlp`](serialize_class_mlp.md) (see [`fwrite_serialized_item`](fwrite_serialized_item.md) for an
introduction of the basic principle of serialization). The
serialized multilayer perceptron is defined by the handle
*`SerializedItemHandle`*. The deserialized values are stored in an
automatically created multilayer perceptron with the handle
*`MLPHandle`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`SerializedItemHandle`** (input_control)  serialized_item `→`  (handle)

Handle of the serialized item.

**`MLPHandle`** (output_control)  class_mlp `→`  (handle)

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
