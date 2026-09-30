# send_serialized_item (Operator)

## Name

`send_serialized_item` — Send a serialized item over a socket connection.

## Signature

`send_serialized_item( : : Socket, SerializedItemHandle : )`

## Description

`send_serialized_item` sends a serialized item over a socket
connection determined by *`Socket`* (see
[`fwrite_serialized_item`](fwrite_serialized_item.md) for an introduction of the
basics of serialization). The receiving HALCON process must
call [`receive_serialized_item`](receive_serialized_item.md) to read the serialized item
from the socket. The serialized item is returned by the handle
*`SerializedItemHandle`*.
For a detailed example showing the use of a socket connection, see
[`open_socket_accept`](open_socket_accept.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Socket`** (input_control)  socket `→`  (handle)

Socket number.

**`SerializedItemHandle`** (input_control)  serialized_item `→`  (handle)

Handle of the serialized item.

## Result

If the parameters are valid, the operator
`send_serialized_item` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`create_serialized_item_ptr`,
`serialize_matrix`,
`serialize_metrology_model`

## Possible Successors

`receive_serialized_item`

## Module

Foundation
