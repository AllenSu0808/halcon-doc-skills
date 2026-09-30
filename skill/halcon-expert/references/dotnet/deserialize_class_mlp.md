# DeserializeClassMlp (Operator)

## Name

`DeserializeClassMlp` — Deserialize a serialized multilayer perceptron.

## Signature

`static void HOperatorSet.DeserializeClassMlp(HTuple serializedItemHandle, out HTuple MLPHandle)`

`void HClassMlp.DeserializeClassMlp(HSerializedItem serializedItemHandle)`

## Description

`DeserializeClassMlp` deserializes a multilayer perceptron (MLP)
(including its training samples), that was serialized
by [`SerializeClassMlp`](serialize_class_mlp.md) (see [`FwriteSerializedItem`](fwrite_serialized_item.md) for an
introduction of the basic principle of serialization). The
serialized multilayer perceptron is defined by the handle
*`serializedItemHandle`*. The deserialized values are stored in an
automatically created multilayer perceptron with the handle
*`MLPHandle`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`serializedItemHandle`** (input_control)  serialized_item `→` [HSerializedItem](HSerializedItem.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the serialized item.

**`MLPHandle`** (output_control)  class_mlp `→` [HClassMlp](HClassMlp.md), [HTuple](HTuple.md) (*IntPtr*)

MLP handle.

## Result

If the parameters are valid, the operator
`DeserializeClassMlp` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`FreadSerializedItem`,
`ReceiveSerializedItem`,
`SerializeClassMlp`

## Possible Successors

`ClassifyClassMlp`,
`EvaluateClassMlp`,
`CreateClassLutMlp`

## See also

`CreateClassMlp`,
`WriteClassMlp`,
`SerializeClassMlp`

## Module

Foundation
