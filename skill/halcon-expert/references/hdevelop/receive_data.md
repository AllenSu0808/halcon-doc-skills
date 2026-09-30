# receive_data (Operator)

## Name

`receive_data` — Receive arbitrary data from external devices or applications using a
generic socket connection.

## Signature

`receive_data( : : Socket, Format : Data, From)`

## Description

`receive_data` receives arbitrary data over a generic socket
connection. The received data is converted from a binary network
packet to a value (or a tuple of values) using the parameter *`Format`*
as specification and is well-suited to communicate with external devices or
applications. This operator does not support the standard *'HALCON'*
protocol, but is intended for arbitrary data transfer.

The received data is converted to a value or tuple of values using the
parameter *`Format`*. It is possible to specify multiple formats. In
this case the *`From`* parameter will contain a 3rd value which tells
you which format has been used to convert the data. To decide which format to
use the size of the necessary data for each format is calculated initially.
When data is received, the first format string with the matching size is used
to convert the data to values.

The parameter *`From`* contains the IP address or hostname and port of
the communication partner. For UDP connections it can be used in the
[`send_data`](send_data.md) operator to send a response.

Please see [`send_data`](send_data.md) for a detailed description of the format.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Socket`** (input_control)  socket `→`  (handle)

Socket number.

**`Format`** (input_control)  string(-array) `→`  (string)

Specification how to convert the data to tuples.

Default:
'z'

**`Data`** (output_control)  string(-array) `→`  (string / real / integer / handle)

Value (or tuple of values) holding the received and converted
data.

**`From`** (output_control)  string-array `→`  (string / integer)

IP address or hostname and network port of the communication
partner.

## Possible Predecessors

`open_socket_connect`,
`socket_accept_connect`,
`get_socket_param`,
`set_socket_param`

## Possible Successors

`close_socket`

## See also

`send_data`

## Module

Foundation
