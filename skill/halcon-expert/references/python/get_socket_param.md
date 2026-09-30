# get_socket_param (Operator)

## Name

`get_socket_param` — Get the value of a socket parameter.

## Signature

`def get_socket_param(socket: HHandle, gen_param_name: MaybeSequence[str]) -> Union[float, int, str]`

## Description

`get_socket_param` reads the *`gen_param_value`* of the
*`gen_param_name`* for the specified socket connection.
Available parameters are *"timeout"*, *"address_info"*,
*"SO_SNDBUF"*, *"SO_RCVBUF"*, *"SO_BROADCAST"*, and
*"TCP_NODELAY"*.

The parameter *"address_info"* returns the IP address and port of the
local and the remote side of the specified socket connection.

See [`set_socket_param`](set_socket_param.md) for a description of the other values.

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
"SO_BROADCAST", "SO_RCVBUF", "SO_SNDBUF", "TCP_NODELAY", "address_info", "timeout"

**`gen_param_value`** (output_control)  string `→` Union[float, int, str]

Value of the socket parameter.

## Possible Predecessors

`open_socket_connect`,
`socket_accept_connect`

## Possible Successors

`set_socket_param`

## See also

`set_socket_param`

## Module

Foundation
