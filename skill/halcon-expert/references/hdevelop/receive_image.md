# receive_image (Operator)

## Name

`receive_image` — Receive an image over a socket connection.

## Signature

`receive_image( : Image : Socket : )`

## Description

`receive_image` reads an image object that was sent over the
socket connection determined by *`Socket`* by another HALCON
process using the operator [`send_image`](send_image.md). If no image has been
sent, the HALCON process calling `receive_image` blocks until
enough data arrives. For a detailed example, see
[`open_socket_accept`](open_socket_accept.md).

## Attention

'int8' images can be received by 64 bit systems only!

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Image`** (output_object)  image(-array) `→` object (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Received image.

**`Socket`** (input_control)  socket `→`  (handle)

Socket number.

## Possible Predecessors

`open_socket_connect`,
`socket_accept_connect`,
`get_socket_param`,
`set_socket_param`

## See also

`send_image`,
`send_region`,
`receive_region`,
`send_tuple`,
`receive_tuple`,
`get_next_socket_data_type`

## Module

Foundation
