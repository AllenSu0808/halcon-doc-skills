# close_socket (Operator)

## Name

`close_socket` — Close a socket.

## Signature

`close_socket( : : Socket : )`

## Description

`close_socket` closes a socket that was previously opened with
[`open_socket_accept`](open_socket_accept.md), [`open_socket_connect`](open_socket_connect.md), or
[`socket_accept_connect`](socket_accept_connect.md). For a detailed example, see
[`open_socket_accept`](open_socket_accept.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- Socket

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`Socket`** (input_control, state is modified)  socket `→`  (handle)

Socket number.

## Possible Predecessors

`open_socket_accept`,
`open_socket_connect`,
`socket_accept_connect`

## Module

Foundation
