# fread_serialized_item (Operator)

## Name

`fread_serialized_item` — Read a serialized item from a file.

## Signature

`fread_serialized_item( : : FileHandle : SerializedItemHandle)`

## Description

`fread_serialized_item` reads a serialized item, that was
written by [`fwrite_serialized_item`](fwrite_serialized_item.md) from the current input
file with the file handle *`FileHandle`* (see
[`fwrite_serialized_item`](fwrite_serialized_item.md) for an introduction of the basics
of serialization). For this, a serialized item is created and
the values read from file are stored in the serialized item. The
operator returns the handle of the serialized item in the parameter
*`SerializedItemHandle`*. The file can be opened by the
operator [`open_file`](open_file.md). Note that the file must be open in
binary format. For reading more than on item from one file the
operator `fread_serialized_item` must be called several
times.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`FileHandle`** (input_control)  file `→`  (handle)

File handle.

**`SerializedItemHandle`** (output_control)  serialized_item `→`  (handle)

Handle of the serialized item.

## Result

If the parameters are valid, the operator
`fread_serialized_item` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.
The error code 9581 indicates that the end of file is reached before
a serialized item could be read.

## Possible Predecessors

`open_file`,
`fwrite_serialized_item`

## Possible Successors

`close_file`,
`get_serialized_item_ptr`,
`deserialize_shape_model`,
`deserialize_ncc_model`

## Module

Foundation
