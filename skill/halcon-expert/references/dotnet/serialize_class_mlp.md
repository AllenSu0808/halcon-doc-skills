# SerializeClassMlp (Operator)

## Name

`SerializeClassMlp` — Serialize a multilayer perceptron (MLP).

## Signature

`static void HOperatorSet.SerializeClassMlp(HTuple MLPHandle, out HTuple serializedItemHandle)`

`HSerializedItem HClassMlp.SerializeClassMlp()`

## Description

`SerializeClassMlp` serializes a multilayer perceptron (MLP) and
its stored training samples (see [`FwriteSerializedItem`](fwrite_serialized_item.md) for an
introduction of the basic principle of serialization). The same data that
is written in a file by [`WriteClassMlp`](write_class_mlp.md) and
[`WriteSamplesClassMlp`](write_samples_class_mlp.md) is converted to a serialized item.
The multilayer perceptron is defined by the handle *`MLPHandle`*.
The serialized multilayer perceptron is returned by the handle
*`serializedItemHandle`* and can be deserialized by
[`DeserializeClassMlp`](deserialize_class_mlp.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`MLPHandle`** (input_control)  class_mlp `→` [HClassMlp](HClassMlp.md), [HTuple](HTuple.md) (*IntPtr*)

MLP handle.

**`serializedItemHandle`** (output_control)  serialized_item `→` [HSerializedItem](HSerializedItem.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the serialized item.

## Result

If the parameters are valid, the operator
`SerializeClassMlp` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`TrainClassMlp`

## Possible Successors

`ClearClassMlp`,
`FwriteSerializedItem`,
`SendSerializedItem`,
`DeserializeClassMlp`

## See also

`CreateClassMlp`,
`ReadClassMlp`,
`WriteSamplesClassMlp`,
`DeserializeClassMlp`

## Module

Foundation
