# TupleIsSerializableElem (Operator)

## Name

`TupleIsSerializableElem` — Test if the elements of a tuple are serializable.

## Signature

`static void HOperatorSet.TupleIsSerializableElem(HTuple tuple, out HTuple isSerializableElem)`

`HTuple HTuple.TupleIsSerializableElem()`

## Description

[`TupleIsSerializable`](tuple_is_serializable.md) checks if the elements of *`tuple`* can
be serialized with [`SerializeTuple`](serialize_tuple.md).
The output *`isSerializableElem`* has the same length as the input
*`tuple`* and contains at each position either *0* if the
corresponding entry in *`tuple`* cannot be serialized, or
*1* if it can.

A tuple element can be serialized if it is an integer, a string, a real value
or a serializable handle.
Handles that are already freed cannot be serialized.
To check the complete tuple for serializability, use
[`TupleIsSerializable`](tuple_is_serializable.md).

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`tuple`** (input_control)  tuple(-array) `→` [HTuple](HTuple.md) (*HHandle* / int / long / double / string)

Tuple to check for serializability.

**`isSerializableElem`** (output_control)  number(-array) `→` [HTuple](HTuple.md) (*int* / long)

Boolean value indicating if the input elements can be serialized.

## Example (HDevelop)

```
* Serialize all serializable elements of a tuple
tuple_is_serializable_elem (Tuple, IsSerializableElem)
if (sum(IsSerializableElem[=]0)>0)
  Tuple[find(IsSerializableElem,0)] := HNULL
endif
serialize_tuple (Tuple, SerializedItem)
```

## Result

If the parameters are valid, the operator
[`TupleIsSerializable`](tuple_is_serializable.md) returns the value 2 (
H_MSG_TRUE)
.

## Possible Successors

`SerializeTuple`,
`WriteTuple`

## Alternatives

`TupleIsSerializable`

## See also

`TupleIsSerializable`,
`SerializeTuple`,
`SerializeHandle`,
`DeserializeTuple`,
`DeserializeHandle`,
`WriteTuple`

## Module

Foundation
