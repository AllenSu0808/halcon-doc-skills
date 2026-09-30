# DeserializeTuple (Operator)

## Name

`DeserializeTuple` — Deserialize a serialized tuple.

## Signature

`static void HOperatorSet.DeserializeTuple(HTuple serializedItemHandle, out HTuple tuple)`

`static HTuple HTuple.DeserializeTuple(HSerializedItem serializedItemHandle)`

## Description

`DeserializeTuple` deserializes the data of a tuple, that was
serialized by [`SerializeTuple`](serialize_tuple.md) (see [`FwriteSerializedItem`](fwrite_serialized_item.md)
for an introduction of the basic principle of serialization). The
serialized data of the tuple is defined by the handle
*`serializedItemHandle`*.
The deserialized values are stored in an automatically created
tuple with the handle *`tuple`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`serializedItemHandle`** (input_control)  serialized_item `→` [HSerializedItem](HSerializedItem.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the serialized item.

**`tuple`** (output_control)  tuple(-array) `→` [HTuple](HTuple.md) (*double* / int / long / string / HHandle)

Tuple.

## Result

If the parameters are valid, the operator
`DeserializeTuple` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`FreadSerializedItem`,
`ReceiveSerializedItem`,
`SerializeTuple`

## Module

Foundation
