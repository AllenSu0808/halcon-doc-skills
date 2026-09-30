# SendImage (Operator)

## Name

`SendImage` — Send an image over a socket connection.

## Signature

`static void HOperatorSet.SendImage(HObject image, HTuple socket)`

`void HSocket.SendImage(HImage image)`

`void HImage.SendImage(HSocket socket)`

## Description

`SendImage` sends an image object over the socket connection
determined by *`socket`*. The receiving HALCON process must
call [`ReceiveImage`](receive_image.md) to read the image from the socket.
For a detailed example, see [`OpenSocketAccept`](open_socket_accept.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`image`** (input_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Image to be sent.

**`socket`** (input_control)  socket `→` [HSocket](HSocket.md), [HTuple](HTuple.md) (*IntPtr*)

Socket number.

## Possible Predecessors

`OpenSocketConnect`,
`SocketAcceptConnect`

## See also

`ReceiveImage`,
`SendRegion`,
`ReceiveRegion`,
`SendTuple`,
`ReceiveTuple`,
`GetNextSocketDataType`

## Module

Foundation
