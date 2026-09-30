# GetSocketDescriptor (Operator)

## Name

`GetSocketDescriptor` — Get the socket descriptor of a socket used by the operating system.

## Signature

`static void HOperatorSet.GetSocketDescriptor(HTuple socket, out HTuple socketDescriptor)`

`int HSocket.GetSocketDescriptor()`

## Description

`GetSocketDescriptor` returns the socket descriptor used by
the operating system for the socket connection that is passed in
*`socket`*. The socket descriptor can be used in operating
system calls such as `select`, `read`, `write`,
`recv`, or `send`.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`socket`** (input_control)  socket `→` [HSocket](HSocket.md), [HTuple](HTuple.md) (*IntPtr*)

Socket number.

**`socketDescriptor`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Socket descriptor used by the operating system.

## Possible Predecessors

`OpenSocketAccept`,
`OpenSocketConnect`,
`SocketAcceptConnect`

## See also

`SetSocketParam`

## Module

Foundation
