# write_tuple (Operator)

## Name

`write_tuple` — Write a tuple to a file.

## Signature

`def write_tuple(tuple: MaybeSequence[Union[float, int, str]], file_name: str) -> None`

## Description

The operator `write_tuple` writes the contents of *`tuple`* to a
file. The data is written in an ASCII format. Therefore, the file can be
exchanged between different architectures (see also
[Tuple / String Operations](toc_tuple_stringoperations.md)). The default HALCON
file extension for the tuple is 'tup'.

### Exception: Handles

Note that `write_tuple` does not support handles, since binary data
is not supported by the underlying ASCII format.
Any handle contained in *`tuple`* is replaced by the integer *0*.
To write a tuple that contains handles, use [`serialize_tuple`](serialize_tuple.md) and
[`fwrite_serialized_item`](fwrite_serialized_item.md).

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`tuple`** (input_control)  tuple(-array) `→` MaybeSequence[Union[float, int, str]]

Tuple with any kind of data.

**`file_name`** (input_control)  filename.write `→` str

Name of the file to be written.

File extension:
.`tup`

## Result

If the parameters are correct the operator `write_tuple`
returns the value 2 (
H_MSG_TRUE)
. Otherwise an exception is raised.

## Alternatives

`fwrite_string`

## See also

`read_tuple`,
`write_image`,
`write_region`,
`open_file`

## Module

Foundation
