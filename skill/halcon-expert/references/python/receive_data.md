# receive_data (Operator)

## Name

`receive_data` — Receive arbitrary data from external devices or applications using a
generic socket connection.

## Signature

`def receive_data(socket: HHandle, format: MaybeSequence[str]) -> Tuple[Sequence[HTupleElementType], Sequence[Union[int, str]]]`

`def receive_data_s(socket: HHandle, format: MaybeSequence[str]) -> Tuple[HTupleElementType, Sequence[Union[int, str]]]`

## Description

`receive_data` receives arbitrary data over a generic socket
connection. The received data is converted from a binary network
packet to a value (or a tuple of values) using the parameter *`format`*
as specification and is well-suited to communicate with external devices or
applications. This operator does not support the standard *"HALCON"*
protocol, but is intended for arbitrary data transfer.

The received data is converted to a value or tuple of values using the
parameter *`format`*. It is possible to specify multiple formats. In
this case the *`from`* parameter will contain a 3rd value which tells
you which format has been used to convert the data. To decide which format to
use the size of the necessary data for each format is calculated initially.
When data is received, the first format string with the matching size is used
to convert the data to values.

The parameter *`from`* contains the IP address or hostname and port of
the communication partner. For UDP connections it can be used in the
[`send_data`](send_data.md) operator to send a response.

Please see [`send_data`](send_data.md) for a detailed description of the format.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`socket`** (input_control)  socket `→` HHandle

Socket number.

**`format`** (input_control)  string(-array) `→` MaybeSequence[str]

Specification how to convert the data to tuples.

Default:
"z"

**`data`** (output_control)  string(-array) `→` Sequence[HTupleElementType]

Value (or tuple of values) holding the received and converted
data.

**`from`** (output_control)  string-array `→` Sequence[Union[int, str]]

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
