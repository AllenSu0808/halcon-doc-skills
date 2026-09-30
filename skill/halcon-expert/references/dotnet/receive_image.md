# ReceiveImage (Operator)

## Name

`ReceiveImage` — Receive an image over a socket connection.

## Signature

`static void HOperatorSet.ReceiveImage(out HObject image, HTuple socket)`

`HImage HSocket.ReceiveImage()`

`void HImage.ReceiveImage(HSocket socket)`

## Description

`ReceiveImage` reads an image object that was sent over the
socket connection determined by *`socket`* by another HALCON
process using the operator [`SendImage`](send_image.md). If no image has been
sent, the HALCON process calling `ReceiveImage` blocks until
enough data arrives. For a detailed example, see
[`OpenSocketAccept`](open_socket_accept.md).

## Attention

'int8' images can be received by 64 bit systems only!

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`image`** (output_object)  image(-array) `→` [HImage](HImage.md) (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Received image.

**`socket`** (input_control)  socket `→` [HSocket](HSocket.md), [HTuple](HTuple.md) (*IntPtr*)

Socket number.

## Possible Predecessors

`OpenSocketConnect`,
`SocketAcceptConnect`,
`GetSocketParam`,
`SetSocketParam`

## See also

`SendImage`,
`SendRegion`,
`ReceiveRegion`,
`SendTuple`,
`ReceiveTuple`,
`GetNextSocketDataType`

## Module

Foundation
