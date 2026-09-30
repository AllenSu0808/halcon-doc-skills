# send_region (Operator)

## Name

`send_region` — Send regions over a socket connection.

## Signature

`send_region(Region : : Socket : )`

## Description

`send_region` sends a region object over the socket connection
determined by *`Socket`*. The receiving HALCON process must
call [`receive_region`](receive_region.md) to read the regions from the socket.
For a detailed example, see [`open_socket_accept`](open_socket_accept.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Region`** (input_object)  region(-array) `→` object

Regions to be sent.

**`Socket`** (input_control)  socket `→`  (handle)

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
