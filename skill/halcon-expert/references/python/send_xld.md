# send_xld (Operator)

## Name

`send_xld` — Send an XLD object over a socket connection.

## Signature

`def send_xld(xld: HObject, socket: HHandle) -> None`

## Description

`send_xld` sends an XLD object over the socket connection
determined by *`socket`*. The receiving HALCON process must
call [`receive_xld`](receive_xld.md) to read the XLD object from the socket.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`xld`** (input_object)  xld(-array) `→` HObject

XLD object to be sent.

**`socket`** (input_control)  socket `→` HHandle

Socket number.

## Example (HDevelop)

```
* Process 1
dev_set_colored (12)
open_socket_accept (3000, [], [], AcceptingSocket)
socket_accept_connect (AcceptingSocket, 'true', Socket)
receive_image (Image, Socket)
edges_sub_pix (Image, Edges, 'canny', 1.5, 20, 40)
send_xld (Edges, Socket)
receive_xld (Polygons, Socket)
split_contours_xld (Polygons, Contours, 'polygon', 1, 5)
gen_parallels_xld (Polygons, Parallels, 10, 30, 0.15, 'true')
send_xld (Parallels, Socket)
receive_xld (ModParallels, Socket)
receive_xld (ExtParallels, Socket)
stop ()
close_socket (Socket)
close_socket (AcceptingSocket)

* Process 2
dev_set_colored (12)
open_socket_connect ('localhost', 3000, [], [], Socket)
read_image (Image, 'mreut')
send_image (Image, Socket)
receive_xld (Edges, Socket)
gen_polygons_xld (Edges, Polygons, 'ramer', 2)
send_xld (Polygons, Socket)
split_contours_xld (Polygons, Contours, 'polygon', 1, 5)
receive_xld (Parallels, Socket)
mod_parallels_xld (Parallels, Image, ModParallels, ExtParallels, \
                   0.4, 160, 220, 10)
send_xld (ModParallels, Socket)
send_xld (ExtParallels, Socket)
stop ()
close_socket (Socket)
```

## Possible Predecessors

`open_socket_connect`,
`socket_accept_connect`

## See also

`receive_xld`,
`send_image`,
`receive_image`,
`send_region`,
`receive_region`,
`send_tuple`,
`receive_tuple`,
`get_next_socket_data_type`

## Module

Foundation
