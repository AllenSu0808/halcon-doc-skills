# get_socket_descriptor (Operator)

## Name

`get_socket_descriptor` — Get the socket descriptor of a socket used by the operating system.

## Signature

`def get_socket_descriptor(socket: HHandle) -> int`

## Description

`get_socket_descriptor` returns the socket descriptor used by
the operating system for the socket connection that is passed in
*`socket`*. The socket descriptor can be used in operating
system calls such as `select`, `read`, `write`,
`recv`, or `send`.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`socket`** (input_control)  socket `→` HHandle

Socket number.

**`socket_descriptor`** (output_control)  integer `→` int

Socket descriptor used by the operating system.

## Possible Predecessors

`open_socket_accept`,
`open_socket_connect`,
`socket_accept_connect`

## See also

`set_socket_param`

## Module

Foundation
