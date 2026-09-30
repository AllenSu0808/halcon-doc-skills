# GetSocketParam (Operator)

## Name

`GetSocketParam` — Get the value of a socket parameter.

## Signature

`static void HOperatorSet.GetSocketParam(HTuple socket, HTuple genParamName, out HTuple genParamValue)`

`HTuple HSocket.GetSocketParam(HTuple genParamName)`

`HTuple HSocket.GetSocketParam(string genParamName)`

## Description

`GetSocketParam` reads the *`genParamValue`* of the
*`genParamName`* for the specified socket connection.
Available parameters are *"timeout"*, *"address_info"*,
*"SO_SNDBUF"*, *"SO_RCVBUF"*, *"SO_BROADCAST"*, and
*"TCP_NODELAY"*.

The parameter *"address_info"* returns the IP address and port of the
local and the remote side of the specified socket connection.

See [`SetSocketParam`](set_socket_param.md) for a description of the other values.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`socket`** (input_control)  socket `→` [HSocket](HSocket.md), [HTuple](HTuple.md) (*IntPtr*)

Socket number.

**`genParamName`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Name of the socket parameter.

List of values:
"SO_BROADCAST", "SO_RCVBUF", "SO_SNDBUF", "TCP_NODELAY", "address_info", "timeout"

**`genParamValue`** (output_control)  string `→` [HTuple](HTuple.md) (*string* / double / int / long)

Value of the socket parameter.

## Possible Predecessors

`OpenSocketConnect`,
`SocketAcceptConnect`

## Possible Successors

`SetSocketParam`

## See also

`SetSocketParam`

## Module

Foundation
