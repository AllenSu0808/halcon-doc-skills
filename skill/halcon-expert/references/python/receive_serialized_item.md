# receive_serialized_item (Operator)

## Name

`receive_serialized_item` — Receive a serialized item over a socket connection.

## Signature

`def receive_serialized_item(socket: HHandle) -> HHandle`

## Description

`receive_serialized_item` receives a serialized item that was
sent over the socket connection determined by *`socket`* of
another HALCON process using the operator [`send_serialized_item`](send_serialized_item.md)
(see [`fwrite_serialized_item`](fwrite_serialized_item.md) for an introduction of the
basics of serialization). If no serialized item has been sent,
the HALCON process calling `receive_serialized_item` blocks
until enough data arrives. The data is stored in a new created
serialized item. The operator returns the handle of the serialized
item in parameter *`serialized_item_handle`*. For a detailed
example showing the use of a socket connection, see
[`open_socket_accept`](open_socket_accept.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`socket`** (input_control)  socket `→` HHandle

Socket number.

**`serialized_item_handle`** (output_control)  serialized_item `→` HHandle

Handle of the serialized item.

## Result

If the parameters are valid, the operator
`receive_serialized_item` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`send_serialized_item`

## Possible Successors

`get_serialized_item_ptr`,
`deserialize_matrix`,
`deserialize_metrology_model`

## Module

Foundation
