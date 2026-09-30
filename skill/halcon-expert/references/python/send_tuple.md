# send_tuple (Operator)

## Name

`send_tuple` — Send a tuple over a socket connection.

## Signature

`def send_tuple(socket: HHandle, tuple: Union[float, int, str]) -> None`

## Description

`send_tuple` sends a tuple *`tuple`* over the socket connection
determined by *`socket`*.
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

**`socket`** (input_control)  socket `→` HHandle

Socket number.

**`tuple`** (input_control)  string `→` Union[float, int, str]

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
