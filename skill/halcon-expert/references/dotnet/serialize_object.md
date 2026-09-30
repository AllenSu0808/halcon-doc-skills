# SerializeObject (Operator)

## Name

`SerializeObject` — Serialize an iconic object.

## Signature

`static void HOperatorSet.SerializeObject(HObject objectVal, out HTuple serializedItemHandle)`

`HSerializedItem HObject.SerializeObject()`

## Description

`SerializeObject` serializes an iconic object (see
[`FwriteSerializedItem`](fwrite_serialized_item.md) for an introduction of the basic
principle of serialization). The iconic object is a tuple of image objects,
region objects, or XLD objects, and is defined by the parameter
*`objectVal`*. The serialized iconic object is returned by the handle
*`serializedItemHandle`* and can be deserialized by
[`DeserializeObject`](deserialize_object.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`objectVal`** (input_object)  object(-array) `→` [HObject](HObject.md)

Iconic object.

**`serializedItemHandle`** (output_control)  serialized_item `→` [HSerializedItem](HSerializedItem.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the serialized item.

## Result

If the parameters are valid, the operator
`SerializeObject` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Successors

`FwriteSerializedItem`,
`SendSerializedItem`,
`DeserializeObject`

## See also

`DeserializeObject`

## Module

Foundation
