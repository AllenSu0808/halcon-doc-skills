# ReceiveData (Operator)

## Name

`ReceiveData` — Receive arbitrary data from external devices or applications using a
generic socket connection.

## Signature

`static void HOperatorSet.ReceiveData(HTuple socket, HTuple format, out HTuple data, out HTuple from)`

`HTuple HSocket.ReceiveData(HTuple format, out HTuple from)`

`HTuple HSocket.ReceiveData(string format, out HTuple from)`

## Description

`ReceiveData` receives arbitrary data over a generic socket
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
[`SendData`](send_data.md) operator to send a response.

Please see [`SendData`](send_data.md) for a detailed description of the format.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`socket`** (input_control)  socket `→` [HSocket](HSocket.md), [HTuple](HTuple.md) (*IntPtr*)

Socket number.

**`format`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Specification how to convert the data to tuples.

Default:
"z"

**`data`** (output_control)  string(-array) `→` [HTuple](HTuple.md) (*string* / double / int / long / HHandle)

Value (or tuple of values) holding the received and converted
data.

**`from`** (output_control)  string-array `→` [HTuple](HTuple.md) (*string* / int / long)

IP address or hostname and network port of the communication
partner.

## Possible Predecessors

`OpenSocketConnect`,
`SocketAcceptConnect`,
`GetSocketParam`,
`SetSocketParam`

## Possible Successors

`CloseSocket`

## See also

`SendData`

## Module

Foundation
