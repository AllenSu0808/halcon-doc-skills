# OpenSocketConnect (Operator)

## Name

`OpenSocketConnect` — Open a socket and connect it to an accepting socket.

## Signature

`static void HOperatorSet.OpenSocketConnect(HTuple hostName, HTuple port, HTuple genParamName, HTuple genParamValue, out HTuple socket)`

`public HSocket(string hostName, int port, HTuple genParamName, HTuple genParamValue)`

`public HSocket(string hostName, int port, string genParamName, string genParamValue)`

`void HSocket.OpenSocketConnect(string hostName, int port, HTuple genParamName, HTuple genParamValue)`

`void HSocket.OpenSocketConnect(string hostName, int port, string genParamName, string genParamValue)`

## Description

`OpenSocketConnect` opens a connecting socket to an accepting
socket on the computer *`hostName`*, which listens on port
*`port`*.

The following parameters can be set for *`genParamName`*.

- ***"protocol"*:** —

  Specifies the protocol to be used. The *"HALCON"* protocol without
  a specific address family, will use IPv4 or IPv6 automatically depending
  on the network configuration of the computer. To use a specific address
  family a '4' or '6' (for IPv4 or IPv6, respectively) must be appended to
  the name of the protocol. For example, *"HALCON4"* designates a
  HALCON connection over IPv4. Possible values for a generic socket
  communication are *"UDP"* and *"TCP"* which also support
  appended '4' and '6'. Alternatively, the usage of addresses for
  IPv4 (e.g., *"127.0.0.1"*) or IPv6 (e.g., *"::1"*)
  for *`hostName`* determines the address family to be used.
  Both communication partners must use the same protocol.
  To exchange data using generic sockets use [`SendData`](send_data.md) and
  [`ReceiveData`](receive_data.md) only.

  Default:
   *"HALCON"*
- ***"timeout"*:** —

  Sets a timeout for this operation. The timeout is given in seconds or
  as the string *"infinite"*.
- ***"tls_enable"*:** —

  Controls the use of Transport Layer Security (TLS) for the new socket
  connection. When *"tls_enable"* is set to *"true"*, a
  connection attempt using TLS is undertaken. This requires TLS support on
  the server side. The certificate to optionally check against is specified
  with the generic parameter *"tls_certificate"*. Without a
  certificate, the connection will still be encrypted, but the authenticity
  of the server can not be verified.

  Default:
   *"false"*
- ***"tls_certificate"*:** —

  Specify the path to a certificate to check the authenticity of the server
  of connection using Transport Layer Security (TLS). The certificate must
  be provided in PEM-format. This parameter is ignored if
  *"tls_enable"* is not set to *"true"*.
- ***"tsl_sni"*:** —

  Set the “server name indication” to use for the TLS connection. This
  tells the server for which domain the certificate should be valid, which
  is important if multiple domains are hosted on the same server. This
  parameter is ignored if *"tls_enable"* is not set to *"true"*.
- ***"string_encoding"*:** —

  Sets the string encoding that is expected when sending and receiving
  strings with this socket. It is used for [`SendTuple`](send_tuple.md) and
  [`ReceiveTuple`](receive_tuple.md) as well as [`SendData`](send_data.md) and [`ReceiveData`](receive_data.md).
  When the protocol *"HALCON"* is used, the setting only has effect
  on connections to HALCON versions prior to 18.11. If the connection
  partner is detected to have HALCON version 18.11 or newer, UTF-8 is
  used to encode tuples.

For the *"HALCON"* protocol the listening socket must have been
created earlier with the operator [`OpenSocketAccept`](open_socket_accept.md) in another
HALCON process. To establish the connection, the HALCON process, in which the
accepting socket resides, must call [`SocketAcceptConnect`](socket_accept_connect.md). For a
detailed example, see [`OpenSocketAccept`](open_socket_accept.md).

For generic sockets the socket to connect to can be any socket from the
same protocol type.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`hostName`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Hostname of the computer to connect to.

Default:
"localhost"

**`port`** (input_control)  number `→` [HTuple](HTuple.md) (*int* / long)

Port number.

Suggested values:
3000, 4570

Value range:
`1024
≤
port
≤
65535`

Minimum increment:
1

Recommended increment:
1

**`genParamName`** (input_control)  attribute.name(-array) `→` [HTuple](HTuple.md) (*string*)

Names of the generic parameters that can be
adjusted for the socket.

Default:
[]

List of values:
"protocol", "string_encoding", "timeout", "tls_certificate", "tls_enable", "tls_sni"

**`genParamValue`** (input_control)  attribute.value(-array) `→` [HTuple](HTuple.md) (*string* / double / int / long)

Values of the generic parameters that can be
adjusted for the socket.

Default:
[]

Suggested values:
0, 3.0, "infinite", "HALCON", "UDP", "TCP", "HALCON4", "UDP4", "TCP4", "HALCON6", "UDP6", "TCP6", "utf8", "locale", "ignore", "true", "false"

**`socket`** (output_control)  socket `→` [HSocket](HSocket.md), [HTuple](HTuple.md) (*IntPtr*)

Socket number.

## Possible Successors

`SendImage`,
`ReceiveImage`,
`SendRegion`,
`ReceiveRegion`,
`SendTuple`,
`ReceiveTuple`,
`SendData`,
`ReceiveData`

## See also

`OpenSocketAccept`,
`SocketAcceptConnect`,
`GetSocketParam`,
`SetSocketParam`,
`CloseSocket`

## Module

Foundation
