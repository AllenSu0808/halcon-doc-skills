# SerializeTuple (Operator)

## Name

`SerializeTuple` — Serialize a tuple.

## Signature

`static void HOperatorSet.SerializeTuple(HTuple tuple, out HTuple serializedItemHandle)`

`HSerializedItem HTuple.SerializeTuple()`

## Description

`SerializeTuple` serializes the data of a tuple (see
[`FwriteSerializedItem`](fwrite_serialized_item.md) for an introduction of the basic
principle of serialization). The same data that is written in a
file by [`WriteTuple`](write_tuple.md) is converted to a serialized item.
The tuple is defined by the handle *`tuple`*. The
serialized data of a tuple is returned by the handle
*`serializedItemHandle`* and can be deserialized by
[`DeserializeTuple`](deserialize_tuple.md).

Note that not all handle types can be serialized.
If *`tuple`* contains a handle that can not be serialized or that
has been freed already, an exception is raised.
The operators [`TupleIsSerializable`](tuple_is_serializable.md) and
[`TupleIsSerializableElem`](tuple_is_serializable_elem.md) can be used to find out if a tuple or
its elements can be serialized.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`tuple`** (input_control)  tuple(-array) `→` [HTuple](HTuple.md) (*double* / int / long / string / HHandle)

Tuple.

**`serializedItemHandle`** (output_control)  serialized_item `→` [HSerializedItem](HSerializedItem.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the serialized item.

## Result

If the parameters are valid, the operator
`SerializeTuple` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Successors

`FwriteSerializedItem`,
`SendSerializedItem`,
`DeserializeTuple`

## Module

Foundation
