# FwriteSerializedItem (Operator)

## Name

`FwriteSerializedItem` — Write a serialized item to a file.

## Signature

`static void HOperatorSet.FwriteSerializedItem(HTuple fileHandle, HTuple serializedItemHandle)`

`void HSerializedItem.FwriteSerializedItem(HFile fileHandle)`

## Description

`FwriteSerializedItem` writes a serialized item to the
output file with the handle *`fileHandle`*. The serialized
item is defined by the handle *`serializedItemHandle`*. The
file can be opened by the operator [`OpenFile`](open_file.md). Note that the
file must be open in binary format. For writing more than one item in
one file, the operator `FwriteSerializedItem` must be called
several times. A serialized item can be read with
[`FreadSerializedItem`](fread_serialized_item.md).

**Basics of the serialization and deserialization**

For writing or sending iconic objects, data, or models to a file or
to another HALCON process over a socket connection, first, the iconic
objects, data, or models must be converted to serialized items. For
this purpose, a lot of operators are available. E.g., the
operator [`SerializeShapeModel`](serialize_shape_model.md) performs the serialization
for the shape model . After this, a serialized item can be written
by `FwriteSerializedItem` in a file or can be transferred
by [`SendSerializedItem`](send_serialized_item.md) to another HALCON process over a
socket connection.

To deserialize a serialized item, first a serialized item is read
from a file (see [`FreadSerializedItem`](fread_serialized_item.md)) or is received over
the socket connection from another HALCON process (see
[`ReceiveSerializedItem`](receive_serialized_item.md)). There are also operators to convert
the serialized item to the original format, i.e., to the iconic object,
the data, or the model. These operators deserialize the iconic
object, the data, or the model. E.g., the operator
[`DeserializeShapeModel`](deserialize_shape_model.md) deserializes the item for a serialized
shape model .

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`fileHandle`** (input_control)  file `→` [HFile](HFile.md), [HTuple](HTuple.md) (*IntPtr*)

File handle.

**`serializedItemHandle`** (input_control)  serialized_item `→` [HSerializedItem](HSerializedItem.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the serialized item.

## Result

If the parameters are valid, the operator
`FwriteSerializedItem` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`OpenFile`,
`SerializeShapeModel`,
`SerializeNccModel`

## Possible Successors

`CloseFile`,
`FreadSerializedItem`

## Module

Foundation
