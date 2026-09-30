# SetSocketParam (Operator)

## Name

`SetSocketParam` — Set a socket parameter.

## Signature

`static void HOperatorSet.SetSocketParam(HTuple socket, HTuple genParamName, HTuple genParamValue)`

`void HSocket.SetSocketParam(HTuple genParamName, HTuple genParamValue)`

`void HSocket.SetSocketParam(string genParamName, string genParamValue)`

## Description

`SetSocketParam` sets the *`genParamName`*
according to *`genParamValue`* for the specified socket connection.
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

**`socket`** (input_control)  socket `→` [HSocket](HSocket.md), [HTuple](HTuple.md) (*IntPtr*)

Socket number.

**`genParamName`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Name of the socket parameter.

List of values:
"SO_BROADCAST", "SO_RCVBUF", "SO_SNDBUF", "TCP_NODELAY", "timeout"

**`genParamValue`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string* / double / int / long)

Value of the socket parameter.

Default:
"on"

Suggested values:
"on", "off", 0, 1, 3.0, "infinite", 530, 1460

## Possible Predecessors

`OpenSocketConnect`,
`SocketAcceptConnect`

## Possible Successors

`SendData`,
`ReceiveData`

## See also

`GetSocketParam`

## Module

Foundation
