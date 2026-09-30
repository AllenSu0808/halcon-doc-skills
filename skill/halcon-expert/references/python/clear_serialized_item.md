# clear_serialized_item (Operator)

## Name

`clear_serialized_item` — Delete a serialized item.

## Signature

`def clear_serialized_item(serialized_item_handle: MaybeSequence[HHandle]) -> None`

## Description

`clear_serialized_item` deletes a serialized item, which is
passed by the handle *`serialized_item_handle`*
(see [`fwrite_serialized_item`](fwrite_serialized_item.md) for an introduction of the
basics of serialization). If a serialized item is created only
by a data pointer, it will not be deleted. Such a data pointer, that
points to the beginning of serialized item can be created
by the operator [`get_serialized_item_ptr`](get_serialized_item_ptr.md). After calling
`clear_serialized_item`, the handle of the serialized item
becomes invalid.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- serialized_item_handle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`serialized_item_handle`** (input_control, state is modified)  serialized_item(-array) `→` MaybeSequence[HHandle]

Handle of the serialized item.

## Result

If the parameters are valid, the operator
`clear_serialized_item` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`fwrite_serialized_item`,
`receive_serialized_item`

## Module

Foundation
