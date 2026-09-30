# WriteTuple (Operator)

## Name

`WriteTuple` — Write a tuple to a file.

## Signature

`static void HOperatorSet.WriteTuple(HTuple tuple, HTuple fileName)`

`static void HMisc.WriteTuple(HTuple tuple, string fileName)`

`void HTuple.WriteTuple(HTuple fileName)`

## Description

The operator `WriteTuple` writes the contents of *`tuple`* to a
file. The data is written in an ASCII format. Therefore, the file can be
exchanged between different architectures (see also
[Tuple / String Operations](toc_tuple_stringoperations.md)). The default HALCON
file extension for the tuple is 'tup'.

### Exception: Handles

Note that `WriteTuple` does not support handles, since binary data
is not supported by the underlying ASCII format.
Any handle contained in *`tuple`* is replaced by the integer *0*.
To write a tuple that contains handles, use [`SerializeTuple`](serialize_tuple.md) and
[`FwriteSerializedItem`](fwrite_serialized_item.md).

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`tuple`** (input_control)  tuple(-array) `→` [HTuple](HTuple.md) (*double* / int / long / string)

Tuple with any kind of data.

**`fileName`** (input_control)  filename.write `→` [HTuple](HTuple.md) (*string*)

Name of the file to be written.

File extension:
.`tup`

## Result

If the parameters are correct the operator `WriteTuple`
returns the value 2 (
H_MSG_TRUE)
. Otherwise an exception is raised.

## Alternatives

`FwriteString`

## See also

`ReadTuple`,
`WriteImage`,
`WriteRegion`,
`OpenFile`

## Module

Foundation
