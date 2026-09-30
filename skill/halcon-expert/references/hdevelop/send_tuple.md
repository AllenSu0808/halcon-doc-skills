# send_tuple (Operator)

## Name

`send_tuple` — Send a tuple over a socket connection.

## Signature

`send_tuple( : : Socket, Tuple : )`

## Description

`send_tuple` sends a tuple *`Tuple`* over the socket connection
determined by *`Socket`*.
The receiving HALCON process must call [`receive_tuple`](receive_tuple.md) to read the
tuple from the socket.
For a detailed example, see [`open_socket_accept`](open_socket_accept.md).

## Attention

`send_tuple` does not allow sending tuples containing HALCON handles.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Socket`** (input_control)  socket `→`  (handle)

Socket number.

**`Tuple`** (input_control)  string `→`  (string / real / integer)

Tuple to be sent.

## Possible Predecessors

`open_socket_connect`,
`socket_accept_connect`

## See also

`receive_tuple`,
`send_image`,
`receive_image`,
`send_region`,
`receive_region`,
`get_next_socket_data_type`

## Module

Foundation
