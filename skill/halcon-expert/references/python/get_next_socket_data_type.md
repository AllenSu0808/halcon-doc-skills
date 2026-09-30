# get_next_socket_data_type (Operator)

## Name

`get_next_socket_data_type` — Determine the HALCON data type of the next socket data.

## Signature

`def get_next_socket_data_type(socket: HHandle) -> str`

## Description

`get_next_socket_data_type` returns the data type of the next
data that are present on the socket *`socket`* and returns it
in *`data_type`*. The possible values for *`data_type`*
are:

- **'no_data':** —

  No data are present.
- **'no_halcon_data':** —

  Some data are present, but they are not HALCON data.
- **'tuple':** —

  The next data is a tuple.
- **'region':** —

  The next data is a region object.
- **'image':** —

  The next data is an image object.
- **'xld_cont':** —

  The next data is an XLD contour.
- **'xld_poly':** —

  The next data is an XLD polygon.
- **'xld_para':** —

  The next data is an XLD parallel.
- **'xld_mod_para':** —

  The next data is a modified XLD parallel.
- **'xld_ext_para':** —

  The next data is an extended XLD parallel.
- **'serialized_item':** —

  The next data is a serialized item.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`socket`** (input_control)  socket `→` HHandle

Socket number.

**`data_type`** (output_control)  string `→` str

Data type of next HALCON data.

## See also

`send_image`,
`receive_image`,
`send_region`,
`receive_region`,
`send_tuple`,
`receive_tuple`,
`send_serialized_item`,
`receive_serialized_item`

## Module

Foundation
