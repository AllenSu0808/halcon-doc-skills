# CloseSocket (Operator)

## Name

`CloseSocket` — Close a socket.

## Signature

`static void HOperatorSet.CloseSocket(HTuple socket)`

`void HSocket.CloseSocket()`

## Description

`CloseSocket` closes a socket that was previously opened with
[`OpenSocketAccept`](open_socket_accept.md), [`OpenSocketConnect`](open_socket_connect.md), or
[`SocketAcceptConnect`](socket_accept_connect.md). For a detailed example, see
[`OpenSocketAccept`](open_socket_accept.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- socket

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`socket`** (input_control, state is modified)  socket `→` [HSocket](HSocket.md), [HTuple](HTuple.md) (*IntPtr*)

Socket number.

## Possible Predecessors

`OpenSocketAccept`,
`OpenSocketConnect`,
`SocketAcceptConnect`

## Module

Foundation
