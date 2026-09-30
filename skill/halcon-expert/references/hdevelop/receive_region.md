# receive_region (Operator)

## Name

`receive_region` — Receive regions over a socket connection.

## Signature

`receive_region( : Region : Socket : )`

## Description

`receive_region` reads a region object that was sent over the
socket connection determined by *`Socket`* by another HALCON
process using the operator [`send_region`](send_region.md). If no regions have
been sent, the HALCON process calling `receive_region` blocks
until enough data arrives. For a detailed example, see
[`open_socket_accept`](open_socket_accept.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Region`** (output_object)  region(-array) `→` object

Received regions.

**`Socket`** (input_control)  socket `→`  (handle)

Socket number.

## Possible Predecessors

`open_socket_connect`,
`socket_accept_connect`,
`get_socket_param`,
`set_socket_param`

## See also

`send_region`,
`send_image`,
`receive_image`,
`send_tuple`,
`receive_tuple`,
`get_next_socket_data_type`

## Module

Foundation
