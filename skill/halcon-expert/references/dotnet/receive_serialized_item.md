# ReceiveSerializedItem (Operator)

## Name

`ReceiveSerializedItem` — Receive a serialized item over a socket connection.

## Signature

`static void HOperatorSet.ReceiveSerializedItem(HTuple socket, out HTuple serializedItemHandle)`

`HSerializedItem HSocket.ReceiveSerializedItem()`

`void HSerializedItem.ReceiveSerializedItem(HSocket socket)`

## Description

`ReceiveSerializedItem` receives a serialized item that was
sent over the socket connection determined by *`socket`* of
another HALCON process using the operator [`SendSerializedItem`](send_serialized_item.md)
(see [`FwriteSerializedItem`](fwrite_serialized_item.md) for an introduction of the
basics of serialization). If no serialized item has been sent,
the HALCON process calling `ReceiveSerializedItem` blocks
until enough data arrives. The data is stored in a new created
serialized item. The operator returns the handle of the serialized
item in parameter *`serializedItemHandle`*. For a detailed
example showing the use of a socket connection, see
[`OpenSocketAccept`](open_socket_accept.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`socket`** (input_control)  socket `→` [HSocket](HSocket.md), [HTuple](HTuple.md) (*IntPtr*)

Socket number.

**`serializedItemHandle`** (output_control)  serialized_item `→` [HSerializedItem](HSerializedItem.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the serialized item.

## Result

If the parameters are valid, the operator
`ReceiveSerializedItem` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`SendSerializedItem`

## Possible Successors

`GetSerializedItemPtr`,
`DeserializeMatrix`,
`DeserializeMetrologyModel`

## Module

Foundation
