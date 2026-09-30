# send_image (Operator)

## Name

`send_image` — Send an image over a socket connection.

## Signature

`send_image(Image : : Socket : )`

## Description

`send_image` sends an image object over the socket connection
determined by *`Socket`*. The receiving HALCON process must
call [`receive_image`](receive_image.md) to read the image from the socket.
For a detailed example, see [`open_socket_accept`](open_socket_accept.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Image`** (input_object)  (multichannel-)image(-array) `→` object (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Image to be sent.

**`Socket`** (input_control)  socket `→`  (handle)

Socket number.

## Possible Predecessors

`open_socket_connect`,
`socket_accept_connect`

## See also

`receive_image`,
`send_region`,
`receive_region`,
`send_tuple`,
`receive_tuple`,
`get_next_socket_data_type`

## Module

Foundation
