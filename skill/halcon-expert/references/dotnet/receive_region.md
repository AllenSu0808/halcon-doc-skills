# ReceiveRegion (Operator)

## Name

`ReceiveRegion` — Receive regions over a socket connection.

## Signature

`static void HOperatorSet.ReceiveRegion(out HObject region, HTuple socket)`

`HRegion HSocket.ReceiveRegion()`

`void HRegion.ReceiveRegion(HSocket socket)`

## Description

`ReceiveRegion` reads a region object that was sent over the
socket connection determined by *`socket`* by another HALCON
process using the operator [`SendRegion`](send_region.md). If no regions have
been sent, the HALCON process calling `ReceiveRegion` blocks
until enough data arrives. For a detailed example, see
[`OpenSocketAccept`](open_socket_accept.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`region`** (output_object)  region(-array) `→` [HRegion](HRegion.md)

Received regions.

**`socket`** (input_control)  socket `→` [HSocket](HSocket.md), [HTuple](HTuple.md) (*IntPtr*)

Socket number.

## Possible Predecessors

`OpenSocketConnect`,
`SocketAcceptConnect`,
`GetSocketParam`,
`SetSocketParam`

## See also

`SendRegion`,
`SendImage`,
`ReceiveImage`,
`SendTuple`,
`ReceiveTuple`,
`GetNextSocketDataType`

## Module

Foundation
