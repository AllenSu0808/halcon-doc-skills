# set_socket_param (Operator)

## Name

`set_socket_param` — Set a socket parameter.

## Signature

`def set_socket_param(socket: HHandle, gen_param_name: MaybeSequence[str], gen_param_value: MaybeSequence[Union[float, int, str]]) -> None`

## Description

`set_socket_param` sets the *`gen_param_name`*
according to *`gen_param_value`* for the specified socket connection.
Available parameters are *"timeout"*, *"SO_SNDBUF"*,
*"SO_RCVBUF"*, *"SO_BROADCAST"*, and *"TCP_NODELAY"*.

The parameter *"timeout"* can be used to set a timeout
for this socket. The timeout is given in seconds as a floating point
number or as the string *"infinite"*.

The parameters starting with 'SO_' or 'TCP_' set the corresponding socket
options. *"SO_SNDBUF"* and *"SO_RCVBUF"* specify the
size of the send respectively receive buffer of the operating system
for this socket. Please be aware that this does not mean the size
of one network packet but the size of the buffers where all packets are
temporarily stored by your operating system.
*"SO_BROADCAST"* can only be used together with UDP connections
and enables broadcasting of network packets.
*"TCP_NODELAY"* controls the Nagle algorithm, which optimizes the
flow of small TCP packets and can only be used with TCP connections.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`socket`** (input_control)  socket `→` HHandle

Socket number.

**`gen_param_name`** (input_control)  string(-array) `→` MaybeSequence[str]

Name of the socket parameter.

List of values:
"SO_BROADCAST", "SO_RCVBUF", "SO_SNDBUF", "TCP_NODELAY", "timeout"

**`gen_param_value`** (input_control)  string(-array) `→` MaybeSequence[Union[float, int, str]]

Value of the socket parameter.

Default:
"on"

Suggested values:
"on", "off", 0, 1, 3.0, "infinite", 530, 1460

## Possible Predecessors

`open_socket_connect`,
`socket_accept_connect`

## Possible Successors

`send_data`,
`receive_data`

## See also

`get_socket_param`

## Module

Foundation
