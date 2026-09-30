# open_socket_accept (Operator)

## Name

`open_socket_accept` — Open a socket that accepts connection requests.

## Signature

`open_socket_accept( : : Port, GenParamName, GenParamValue : AcceptingSocket)`

## Description

`open_socket_accept` opens a socket that will accept incoming
connection requests. This operator is the
necessary first step in the establishment of a communication channel
between two HALCON processes. The socket listens for incoming
connection requests on the port number given by *`Port`*.

It is possible to specify a *`Port`* of 0, triggering
implementation-defined behavior.
On most operating systems, using a port number of 0 instructs the
operating system to choose a free port randomly.

The following parameters can be set for *`GenParamName`*.

- ***'protocol'*:** —

  Specifies the protocol to be used. The *'HALCON'* protocol without
  a specific address family, will use IPv4 or IPv6 automatically depending
  on the network configuration of the computer. To use a specific address
  family a '4' or '6' (for IPv4 or IPv6, respectively) must be appended to
  the name of the protocol. For example, *'HALCON4'*
  designates a HALCON connection over IPv4.
  Possible values for a generic socket communication are *'UDP'* and
  *'TCP'* which also support appended '4' and '6'.
  Both communication partners must use the same protocol.
  To exchange data using generic sockets use [`send_data`](send_data.md) and
  [`receive_data`](receive_data.md) only.

  Default:
   *'HALCON'*
- ***'address'*:** —

  Instructs the socket to accept only connection requests addressed to a
  specific address. This address is specified as either an IPv4 or IPv6
  address in numerical form, or a hostname. For example, *'localhost'*
  would instruct the socket to accept only connections addressed to the
  address *'localhost'*, which normally maps to the local loopback
  network interface *'127.0.0.1'*.
- ***'timeout'*:** —

  Sets a timeout for this socket. The timeout is given in seconds or as
  the string *'infinite'*. It is used especially as timeout and
  waiting mode in a following [`socket_accept_connect`](socket_accept_connect.md) call with
  the parameter `Wait` set to *'auto'*.
- ***'string_encoding'*:** —

  Sets the string encoding that is expected when sending and receiving
  strings with this socket. It is used for [`send_tuple`](send_tuple.md) and
  [`receive_tuple`](receive_tuple.md) as well as [`send_data`](send_data.md) and [`receive_data`](receive_data.md).
  When the protocol *'HALCON'* is used, the setting only has effect on
  connections to HALCON versions prior to 18.11. If the connection partner
  is detected to have HALCON version 18.11 or newer, UTF-8 is used to
  encode tuples.
- ***'reuseaddr'*:** —

  Controls the setting of the socket option `SO_REUSEADDR`.
  When *'reuseaddr'* is set to *'false'*,
  `SO_REUSEADDR` will not be set.
  On Windows Systems, conflicting access on a single port will only be
  detected, when *'reuseaddr'* is set to *'false'*.

  Default:
   *'true'*
- ***'tls_enable'*:** —

  Controls the use of Transport Layer Security (TLS) for the new Socket.
  When *'tls_enable'* is set to *'true'*, the created socket
  will accept TLS secured connections only. Furthermore, both generic
  parameters *'tls_private_key'* and *'tls_certificate'* must be
  set, each with a path to the private certificate key and the path to the
  public server certificate. Private key and server certificate must be
  provided in PEM-format.

  Default:
   *'false'*

The accepting socket is returned in *`AcceptingSocket`*.
`open_socket_accept` returns immediately without waiting for a request
from another process, which must be initiated by calling
[`open_socket_connect`](open_socket_connect.md). This allows multiple other processes to connect
to the particular HALCON process that calls `open_socket_accept`. To
accept an incoming *'HALCON'* or *'TCP'* connection request,
[`socket_accept_connect`](socket_accept_connect.md) must be called to obtain a socket for the final
communication.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`Port`** (input_control)  number `→`  (integer)

Port number.

Default:
3000

Suggested values:
3000, 4570

Value range:
`1024
≤
Port
≤
65535`

Minimum increment:
1

Recommended increment:
1

**`GenParamName`** (input_control)  attribute.name(-array) `→`  (string)

Names of the generic parameters that can be
adjusted for the socket.

Default:
[]

List of values:
'address', 'protocol', 'string_encoding', 'timeout', 'tls_certificate', 'tls_enable', 'tls_private_key'

**`GenParamValue`** (input_control)  attribute.value(-array) `→`  (string / real / integer)

Values of the generic parameters that can be
adjusted for the socket.

Default:
[]

Suggested values:
0, 3.0, 'infinite', 'HALCON', 'UDP', 'TCP', 'HALCON4', 'UDP4', 'TCP4', 'HALCON6', 'UDP6', 'TCP6', 'utf8', 'locale', 'ignore', 'true', 'false'

**`AcceptingSocket`** (output_control)  socket `→`  (handle)

Socket number.

## Example (HDevelop)

```
* Process 1
dev_set_colored (12)
open_socket_accept (3000, [], [], AcceptingSocket)
* Busy wait for an incoming connection
dev_error_var (Error, 1)
dev_set_check ('~give_error')
OpenStatus := 5
while (OpenStatus != 2)
    socket_accept_connect (AcceptingSocket, 'false', Socket)
    OpenStatus := Error
    wait_seconds (0.2)
endwhile
dev_set_check ('give_error')
* Connection established
receive_image (Image, Socket)
threshold (Image, Region, 0, 63)
send_region (Region, Socket)
receive_region (ConnectedRegions, Socket)
area_center (ConnectedRegions, Area, Row, Column)
send_tuple (Socket, Area)
send_tuple (Socket, Row)
send_tuple (Socket, Column)
close_socket (Socket)
close_socket (AcceptingSocket)

* Process 2
dev_set_colored (12)
open_socket_connect ('localhost', 3000, [], [], Socket)
read_image (Image, 'fabrik')
send_image (Image, Socket)
receive_region (Region, Socket)
connection (Region, ConnectedRegions)
send_region (ConnectedRegions, Socket)
receive_tuple (Socket, Area)
receive_tuple (Socket, Row)
receive_tuple (Socket, Column)
close_socket (Socket)
```

## Possible Successors

`socket_accept_connect`

## See also

`open_socket_connect`,
`close_socket`,
`get_socket_param`,
`set_socket_param`,
`send_image`,
`receive_image`,
`send_region`,
`receive_region`,
`send_tuple`,
`receive_tuple`,
`send_data`,
`receive_data`

## Module

Foundation
