# fwrite_serialized_item (Operator)

## Name

`fwrite_serialized_item` — Write a serialized item to a file.

## Signature

`def fwrite_serialized_item(file_handle: HHandle, serialized_item_handle: HHandle) -> None`

## Description

`fwrite_serialized_item` writes a serialized item to the
output file with the handle *`file_handle`*. The serialized
item is defined by the handle *`serialized_item_handle`*. The
file can be opened by the operator [`open_file`](open_file.md). Note that the
file must be open in binary format. For writing more than one item in
one file, the operator `fwrite_serialized_item` must be called
several times. A serialized item can be read with
[`fread_serialized_item`](fread_serialized_item.md).

**Basics of the serialization and deserialization**

For writing or sending iconic objects, data, or models to a file or
to another HALCON process over a socket connection, first, the iconic
objects, data, or models must be converted to serialized items. For
this purpose, a lot of operators are available. E.g., the
operator [`serialize_shape_model`](serialize_shape_model.md) performs the serialization
for the shape model . After this, a serialized item can be written
by `fwrite_serialized_item` in a file or can be transferred
by [`send_serialized_item`](send_serialized_item.md) to another HALCON process over a
socket connection.

To deserialize a serialized item, first a serialized item is read
from a file (see [`fread_serialized_item`](fread_serialized_item.md)) or is received over
the socket connection from another HALCON process (see
[`receive_serialized_item`](receive_serialized_item.md)). There are also operators to convert
the serialized item to the original format, i.e., to the iconic object,
the data, or the model. These operators deserialize the iconic
object, the data, or the model. E.g., the operator
[`deserialize_shape_model`](deserialize_shape_model.md) deserializes the item for a serialized
shape model .

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`file_handle`** (input_control)  file `→` HHandle

File handle.

**`serialized_item_handle`** (input_control)  serialized_item `→` HHandle

Handle of the serialized item.

## Result

If the parameters are valid, the operator
`fwrite_serialized_item` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`open_file`,
`serialize_shape_model`,
`serialize_ncc_model`

## Possible Successors

`close_file`,
`fread_serialized_item`

## Module

Foundation
