# get_socket_descriptor (Operator)

## Name

`get_socket_descriptor` — Get the socket descriptor of a socket used by the operating system.

## Signature

`get_socket_descriptor( : : Socket : SocketDescriptor)`

## Description

`get_socket_descriptor` returns the socket descriptor used by
the operating system for the socket connection that is passed in
*`Socket`*. The socket descriptor can be used in operating
system calls such as `select`, `read`, `write`,
`recv`, or `send`.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Socket`** (input_control)  socket `→`  (handle)

Socket number.

**`SocketDescriptor`** (output_control)  integer `→`  (integer)

Socket descriptor used by the operating system.

## Possible Predecessors

`open_socket_accept`,
`open_socket_connect`,
`socket_accept_connect`

## See also

`set_socket_param`

## Module

Foundation
