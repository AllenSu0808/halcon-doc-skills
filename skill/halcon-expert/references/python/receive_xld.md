# receive_xld (Operator)

## Name

`receive_xld` — Receive an XLD object over a socket connection.

## Signature

`def receive_xld(socket: HHandle) -> HObject`

## Description

`receive_xld` reads an XLD object that was sent over the
socket connection determined by *`socket`* by another HALCON
process using the operator [`send_xld`](send_xld.md). If no XLD object has
been sent, the HALCON process calling `receive_xld` blocks
until enough data arrives. For a detailed example, see
[`send_xld`](send_xld.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`xld`** (output_object)  xld(-array) `→` HObject

Received XLD object.

**`socket`** (input_control)  socket `→` HHandle

Socket number.

## Possible Predecessors

`open_socket_connect`,
`socket_accept_connect`,
`get_socket_param`,
`set_socket_param`

## See also

`send_xld`,
`send_image`,
`receive_image`,
`send_region`,
`receive_region`,
`send_tuple`,
`receive_tuple`,
`get_next_socket_data_type`

## Module

Foundation
