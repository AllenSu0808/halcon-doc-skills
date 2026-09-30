# open_socket_connect (Operator)

## Name

`open_socket_connect` — Open a socket and connect it to an accepting socket.

## Signature

`def open_socket_connect(host_name: str, port: int, gen_param_name: MaybeSequence[str], gen_param_value: MaybeSequence[Union[float, int, str]]) -> HHandle`

## Description

`open_socket_connect` opens a connecting socket to an accepting
socket on the computer *`host_name`*, which listens on port
*`port`*.

The following parameters can be set for *`gen_param_name`*.

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
  for *`host_name`* determines the address family to be used.
  Both communication partners must use the same protocol.
  To exchange data using generic sockets use [`send_data`](send_data.md) and
  [`receive_data`](receive_data.md) only.

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
  strings with this socket. It is used for [`send_tuple`](send_tuple.md) and
  [`receive_tuple`](receive_tuple.md) as well as [`send_data`](send_data.md) and [`receive_data`](receive_data.md).
  When the protocol *"HALCON"* is used, the setting only has effect
  on connections to HALCON versions prior to 18.11. If the connection
  partner is detected to have HALCON version 18.11 or newer, UTF-8 is
  used to encode tuples.

For the *"HALCON"* protocol the listening socket must have been
created earlier with the operator [`open_socket_accept`](open_socket_accept.md) in another
HALCON process. To establish the connection, the HALCON process, in which the
accepting socket resides, must call [`socket_accept_connect`](socket_accept_connect.md). For a
detailed example, see [`open_socket_accept`](open_socket_accept.md).

For generic sockets the socket to connect to can be any socket from the
same protocol type.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`host_name`** (input_control)  string `→` str

Hostname of the computer to connect to.

Default:
"localhost"

**`port`** (input_control)  number `→` int

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

**`gen_param_name`** (input_control)  attribute.name(-array) `→` MaybeSequence[str]

Names of the generic parameters that can be
adjusted for the socket.

Default:
[]

List of values:
"protocol", "string_encoding", "timeout", "tls_certificate", "tls_enable", "tls_sni"

**`gen_param_value`** (input_control)  attribute.value(-array) `→` MaybeSequence[Union[float, int, str]]

Values of the generic parameters that can be
adjusted for the socket.

Default:
[]

Suggested values:
0, 3.0, "infinite", "HALCON", "UDP", "TCP", "HALCON4", "UDP4", "TCP4", "HALCON6", "UDP6", "TCP6", "utf8", "locale", "ignore", "true", "false"

**`socket`** (output_control)  socket `→` HHandle

Socket number.

## Possible Successors

`send_image`,
`receive_image`,
`send_region`,
`receive_region`,
`send_tuple`,
`receive_tuple`,
`send_data`,
`receive_data`

## See also

`open_socket_accept`,
`socket_accept_connect`,
`get_socket_param`,
`set_socket_param`,
`close_socket`

## Module

Foundation
