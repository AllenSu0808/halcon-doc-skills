# receive_tuple (Operator)

## Name

`receive_tuple` — Receive a tuple over a socket connection.

## Signature

`def receive_tuple(socket: HHandle) -> Union[float, int, str]`

## Description

`receive_tuple` reads a *`tuple`* that was sent over the socket
connection determined by *`socket`* by another HALCON process
using the operator [`send_tuple`](send_tuple.md).
If no tuple has been sent, the HALCON process calling `receive_tuple`
blocks until enough data arrives.
For a detailed example, see [`open_socket_accept`](open_socket_accept.md).

## Attention

`receive_tuple` does not allow receiving tuples containing
HALCON handles.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`socket`** (input_control)  socket `→` HHandle

Socket number.

**`tuple`** (output_control)  string `→` Union[float, int, str]

Received tuple.

## Possible Predecessors

`open_socket_connect`,
`socket_accept_connect`,
`get_socket_param`,
`set_socket_param`

## See also

`send_tuple`,
`send_image`,
`receive_image`,
`send_region`,
`receive_region`,
`get_next_socket_data_type`

## Module

Foundation
