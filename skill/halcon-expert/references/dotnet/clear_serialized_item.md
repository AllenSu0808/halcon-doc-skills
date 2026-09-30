# ClearSerializedItem (Operator)

## Name

`ClearSerializedItem` — Delete a serialized item.

## Signature

`static void HOperatorSet.ClearSerializedItem(HTuple serializedItemHandle)`

`static void HSerializedItem.ClearSerializedItem(HSerializedItem[] serializedItemHandle)`

`void HSerializedItem.ClearSerializedItem()`

## Description

`ClearSerializedItem` deletes a serialized item, which is
passed by the handle *`serializedItemHandle`*
(see [`FwriteSerializedItem`](fwrite_serialized_item.md) for an introduction of the
basics of serialization). If a serialized item is created only
by a data pointer, it will not be deleted. Such a data pointer, that
points to the beginning of serialized item can be created
by the operator [`GetSerializedItemPtr`](get_serialized_item_ptr.md). After calling
`ClearSerializedItem`, the handle of the serialized item
becomes invalid.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- serializedItemHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`serializedItemHandle`** (input_control, state is modified)  serialized_item(-array) `→` [HSerializedItem](HSerializedItem.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the serialized item.

## Result

If the parameters are valid, the operator
`ClearSerializedItem` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`FwriteSerializedItem`,
`ReceiveSerializedItem`

## Module

Foundation
