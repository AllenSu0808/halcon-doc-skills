# SendRegion (Operator)

## Name

`SendRegion` — Send regions over a socket connection.

## Signature

`static void HOperatorSet.SendRegion(HObject region, HTuple socket)`

`void HSocket.SendRegion(HRegion region)`

`void HRegion.SendRegion(HSocket socket)`

## Description

`SendRegion` sends a region object over the socket connection
determined by *`socket`*. The receiving HALCON process must
call [`ReceiveRegion`](receive_region.md) to read the regions from the socket.
For a detailed example, see [`OpenSocketAccept`](open_socket_accept.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`region`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Regions to be sent.

**`socket`** (input_control)  socket `→` [HSocket](HSocket.md), [HTuple](HTuple.md) (*IntPtr*)

Socket number.

## Possible Predecessors

`OpenSocketConnect`,
`SocketAcceptConnect`

## See also

`ReceiveRegion`,
`SendImage`,
`ReceiveImage`,
`SendTuple`,
`ReceiveTuple`,
`GetNextSocketDataType`

## Module

Foundation
