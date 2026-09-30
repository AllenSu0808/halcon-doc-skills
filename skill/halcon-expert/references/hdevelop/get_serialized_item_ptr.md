# get_serialized_item_ptr (Operator)

## Name

`get_serialized_item_ptr` — Access the data pointer of a serialized item.

## Warning

**It is not recommended to use the operator
`get_serialized_item_ptr` in HDevelop.**

## Signature

`get_serialized_item_ptr( : : SerializedItemHandle : Pointer, Size)`

## Description

`get_serialized_item_ptr` returns the data pointer to the
serialized item which is passed by the handle
*`SerializedItemHandle`* (see [`fwrite_serialized_item`](fwrite_serialized_item.md)
for an introduction of the basics of serialization). The
data pointer, i.e., the beginning of the serialized item is returned
by the parameter *`Pointer`*. The size of the serialized item
in bytes is passed by the parameter *`Size`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`SerializedItemHandle`** (input_control)  serialized_item `→`  (handle)

Handle of the serialized item.

**`Pointer`** (output_control)  pointer `→`  (integer)

Data pointer of the serialized item.

**`Size`** (output_control)  integer `→`  (integer)

Size of the serialized item.

## Result

If the parameters are valid, the operator
`get_serialized_item_ptr` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`create_serialized_item_ptr`

## Module

Foundation
