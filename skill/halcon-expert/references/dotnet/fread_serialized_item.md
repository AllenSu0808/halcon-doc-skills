# FreadSerializedItem (Operator)

## Name

`FreadSerializedItem` — Read a serialized item from a file.

## Signature

`static void HOperatorSet.FreadSerializedItem(HTuple fileHandle, out HTuple serializedItemHandle)`

`void HSerializedItem.FreadSerializedItem(HFile fileHandle)`

## Description

`FreadSerializedItem` reads a serialized item, that was
written by [`FwriteSerializedItem`](fwrite_serialized_item.md) from the current input
file with the file handle *`fileHandle`* (see
[`FwriteSerializedItem`](fwrite_serialized_item.md) for an introduction of the basics
of serialization). For this, a serialized item is created and
the values read from file are stored in the serialized item. The
operator returns the handle of the serialized item in the parameter
*`serializedItemHandle`*. The file can be opened by the
operator [`OpenFile`](open_file.md). Note that the file must be open in
binary format. For reading more than on item from one file the
operator `FreadSerializedItem` must be called several
times.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`fileHandle`** (input_control)  file `→` [HFile](HFile.md), [HTuple](HTuple.md) (*IntPtr*)

File handle.

**`serializedItemHandle`** (output_control)  serialized_item `→` [HSerializedItem](HSerializedItem.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the serialized item.

## Result

If the parameters are valid, the operator
`FreadSerializedItem` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.
The error code 9581 indicates that the end of file is reached before
a serialized item could be read.

## Possible Predecessors

`OpenFile`,
`FwriteSerializedItem`

## Possible Successors

`CloseFile`,
`GetSerializedItemPtr`,
`DeserializeShapeModel`,
`DeserializeNccModel`

## Module

Foundation
