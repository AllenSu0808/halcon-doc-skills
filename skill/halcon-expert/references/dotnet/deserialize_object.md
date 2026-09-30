# DeserializeObject (Operator)

## Name

`DeserializeObject` — Deserialize a serialized iconic object.

## Signature

`static void HOperatorSet.DeserializeObject(out HObject objectVal, HTuple serializedItemHandle)`

`void HObject.DeserializeObject(HSerializedItem serializedItemHandle)`

## Description

`DeserializeObject` deserializes an iconic object, that was
serialized by [`SerializeObject`](serialize_object.md) (see [`FwriteSerializedItem`](fwrite_serialized_item.md)
for an introduction of the basic principle of serialization). The
serialized iconic object is defined by the parameter
*`serializedItemHandle`*. The deserialized iconic object is
stored in the iconic object defined by the parameter *`objectVal`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`objectVal`** (output_object)  object(-array) `→` [HObject](HObject.md)

Iconic object.

**`serializedItemHandle`** (input_control)  serialized_item `→` [HSerializedItem](HSerializedItem.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the serialized item.

## Result

If the parameters are valid, the operator
`DeserializeObject` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`FreadSerializedItem`,
`ReceiveSerializedItem`,
`SerializeObject`

## See also

`SerializeObject`

## Module

Foundation
