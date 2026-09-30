# ReceiveTuple (Operator)

## Name

`ReceiveTuple` — Receive a tuple over a socket connection.

## Signature

`static void HOperatorSet.ReceiveTuple(HTuple socket, out HTuple tuple)`

`HTuple HSocket.ReceiveTuple()`

## Description

`ReceiveTuple` reads a *`tuple`* that was sent over the socket
connection determined by *`socket`* by another HALCON process
using the operator [`SendTuple`](send_tuple.md).
If no tuple has been sent, the HALCON process calling `ReceiveTuple`
blocks until enough data arrives.
For a detailed example, see [`OpenSocketAccept`](open_socket_accept.md).

## Attention

`ReceiveTuple` does not allow receiving tuples containing
HALCON handles.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`socket`** (input_control)  socket `→` [HSocket](HSocket.md), [HTuple](HTuple.md) (*IntPtr*)

Socket number.

**`tuple`** (output_control)  string `→` [HTuple](HTuple.md) (*string* / double / int / long)

Received tuple.

## Possible Predecessors

`OpenSocketConnect`,
`SocketAcceptConnect`,
`GetSocketParam`,
`SetSocketParam`

## See also

`SendTuple`,
`SendImage`,
`ReceiveImage`,
`SendRegion`,
`ReceiveRegion`,
`GetNextSocketDataType`

## Module

Foundation
