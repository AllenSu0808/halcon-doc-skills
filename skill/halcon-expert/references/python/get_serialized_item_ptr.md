# get_serialized_item_ptr (Operator)

## Name

`get_serialized_item_ptr` — Access the data pointer of a serialized item.

## Warning

**It is not recommended to use the operator
`get_serialized_item_ptr` in HDevelop.**

## Signature

`def get_serialized_item_ptr(serialized_item_handle: HHandle) -> Tuple[int, int]`

## Description

`get_serialized_item_ptr` returns the data pointer to the
serialized item which is passed by the handle
*`serialized_item_handle`* (see [`fwrite_serialized_item`](fwrite_serialized_item.md)
for an introduction of the basics of serialization). The
data pointer, i.e., the beginning of the serialized item is returned
by the parameter *`pointer`*. The size of the serialized item
in bytes is passed by the parameter *`size`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`serialized_item_handle`** (input_control)  serialized_item `→` HHandle

Handle of the serialized item.

**`pointer`** (output_control)  pointer `→` int

Data pointer of the serialized item.

**`size`** (output_control)  integer `→` int

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
