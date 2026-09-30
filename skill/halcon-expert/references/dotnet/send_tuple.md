# SendTuple (Operator)

## Name

`SendTuple` — Send a tuple over a socket connection.

## Signature

`static void HOperatorSet.SendTuple(HTuple socket, HTuple tuple)`

`void HSocket.SendTuple(HTuple tuple)`

`void HSocket.SendTuple(string tuple)`

## Description

`SendTuple` sends a tuple *`tuple`* over the socket connection
determined by *`socket`*.
The receiving HALCON process must call [`ReceiveTuple`](receive_tuple.md) to read the
tuple from the socket.
For a detailed example, see [`OpenSocketAccept`](open_socket_accept.md).

## Attention

`SendTuple` does not allow sending tuples containing HALCON handles.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`socket`** (input_control)  socket `→` [HSocket](HSocket.md), [HTuple](HTuple.md) (*IntPtr*)

Socket number.

**`tuple`** (input_control)  string `→` [HTuple](HTuple.md) (*string* / double / int / long)

Tuple to be sent.

## Possible Predecessors

`OpenSocketConnect`,
`SocketAcceptConnect`

## See also

`ReceiveTuple`,
`SendImage`,
`ReceiveImage`,
`SendRegion`,
`ReceiveRegion`,
`GetNextSocketDataType`

## Module

Foundation
