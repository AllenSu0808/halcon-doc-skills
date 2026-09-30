# send_region (Operator)

## Name

`send_region` — Send regions over a socket connection.

## Signature

`def send_region(region: HObject, socket: HHandle) -> None`

## Description

`send_region` sends a region object over the socket connection
determined by *`socket`*. The receiving HALCON process must
call [`receive_region`](receive_region.md) to read the regions from the socket.
For a detailed example, see [`open_socket_accept`](open_socket_accept.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`region`** (input_object)  region(-array) `→` HObject

Regions to be sent.

**`socket`** (input_control)  socket `→` HHandle

Socket number.

## Possible Predecessors

`open_socket_connect`,
`socket_accept_connect`

## See also

`receive_region`,
`send_image`,
`receive_image`,
`send_tuple`,
`receive_tuple`,
`get_next_socket_data_type`

## Module

Foundation
