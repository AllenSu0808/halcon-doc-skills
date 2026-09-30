# ReceiveXld (Operator)

## Name

`ReceiveXld` — Receive an XLD object over a socket connection.

## Signature

`static void HOperatorSet.ReceiveXld(out HObject XLD, HTuple socket)`

`HXLD HSocket.ReceiveXld()`

`void HXLD.ReceiveXld(HSocket socket)`

## Description

`ReceiveXld` reads an XLD object that was sent over the
socket connection determined by *`socket`* by another HALCON
process using the operator [`SendXld`](send_xld.md). If no XLD object has
been sent, the HALCON process calling `ReceiveXld` blocks
until enough data arrives. For a detailed example, see
[`SendXld`](send_xld.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`XLD`** (output_object)  xld(-array) `→` [HXLD](HXLD.md)

Received XLD object.

**`socket`** (input_control)  socket `→` [HSocket](HSocket.md), [HTuple](HTuple.md) (*IntPtr*)

Socket number.

## Possible Predecessors

`OpenSocketConnect`,
`SocketAcceptConnect`,
`GetSocketParam`,
`SetSocketParam`

## See also

`SendXld`,
`SendImage`,
`ReceiveImage`,
`SendRegion`,
`ReceiveRegion`,
`SendTuple`,
`ReceiveTuple`,
`GetNextSocketDataType`

## Module

Foundation
