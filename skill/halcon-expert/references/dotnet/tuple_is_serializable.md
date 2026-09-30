# TupleIsSerializable (Operator)

## Name

`TupleIsSerializable` — Test if a tuple is serializable.

## Signature

`static void HOperatorSet.TupleIsSerializable(HTuple tuple, out HTuple isSerializable)`

`HTuple HTuple.TupleIsSerializable()`

`int HHandle.TupleIsSerializable()`

## Description

`TupleIsSerializable` checks if *`tuple`* can be serialized with
[`SerializeTuple`](serialize_tuple.md).
If yes, *1* is returned in *`isSerializable`*.
Otherwise, *0* is returned.

A tuple can be serialized if it contains only integers, strings, reals, and
serializable handles.
Handles that are already freed cannot be serialized.
To check all elements of a tuple individually, use
[`TupleIsSerializableElem`](tuple_is_serializable_elem.md).

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`tuple`** (input_control)  tuple(-array) `→` [HTuple](HTuple.md) (*HHandle* / int / long / double / string)

Tuple to check for serializability.

**`isSerializable`** (output_control)  number `→` [HTuple](HTuple.md) (*int* / long)

Boolean value indicating if the input can be serialized.

## Result

If the parameters are valid, the operator
`TupleIsSerializable` returns the value 2 (
H_MSG_TRUE)
.

## Possible Successors

`SerializeTuple`,
`WriteTuple`

## Alternatives

`TupleIsSerializableElem`

## See also

`TupleIsSerializableElem`,
`SerializeTuple`,
`SerializeHandle`,
`DeserializeTuple`,
`DeserializeHandle`,
`WriteTuple`

## Module

Foundation
