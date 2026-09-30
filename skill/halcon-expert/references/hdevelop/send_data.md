# send_data (Operator)

## Name

`send_data` — Send arbitrary data to external devices or applications using a
generic socket communication.

## Signature

`send_data( : : Socket, Format, Data, To : )`

## Description

`send_data` sends arbitrary data over a socket connection. The sent
data is converted to a binary network packet from a value (or a tuple of
values) using the parameter *`Format`* as specification and is
well-suited to communicate with external devices or applications.
This operator does not support the standard *'HALCON'* protocol, but
is intended for arbitrary data transfer.

The parameter *`Format`* specifies how to convert the given tuples to
a binary packet. It uses one or multiple qualifier characters each followed
by an optional modifier and repeat count. Most qualifiers require a single
value in the *`Data`* parameter which will be converted.

The following characters are allowed in this format string:

Integer values:

- **'c':** —

  One byte = 8 bit, signed.
- **'C':** —

  Same as 'c' but unsigned.
- **'s':** —

  Two bytes = 16 bit, signed.
- **'S':** —

  Same as 's' but unsigned.
- **'i':** —

  Four bytes = 32 bit, signed.
- **'I':** —

  Same as 'i' but unsigned.
- **'q':** —

  Eight bytes = 64 bit, signed (only available on 64bit
  architectures).
- **'Q':** —

  Same as 'q' but unsigned.

Float values:

- **'f':** —

  Float, 4 bytes = 32 bit.
- **'d':** —

  Double, 8 bytes = 64 bit.

String values:

- **'A':** —

  String (default length 1024 bytes), padded with spaces.
- **'a':** —

  String with arbitrary binary data. When sending data,
  the whole memory block will be transmitted and the size
  will be determined automatically. When receiving, the
  length argument must always be provided explicitly.
- **'Z':** —

  String (default length 1024 bytes), padded with NULL-Bytes
  and will be NULL terminated when sending.
- **'z':** —

  String with variable length, the length modifier specifies
  the maximum length (default length 1024 bytes).

Special characters which do not require a value as *`Data`* parameter:

- **'-':** —

  A single byte is written as binary NULL or when reading,
  a NULL-Byte is skipped.
- **'_':** —

  A single byte is written as space (binary 0x20) or when
  reading, a space byte is skipped.
- **' ':** —

  Ignored, can be used to enhance readability of the format
  string.

Modifiers which can be used after one of the qualifiers above:

- **'n':** —

  Convert the integer or float value when writing to or when
  reading from network byte order (big endian) to host byte
  order.
- **'N':** —

  Convert the integer or float value when writing to
  or when reading from Intel byte order (little endian) to host
  byte order.
- **'0-n':** —

  Specify a repeat count for the
  preceding qualifier, e.g., 'c5' means the same as 'ccccc' (and
  requires therefore a tuple of 5 values) but 'A10' means a
  string with a size of 10 bytes (and requires only one value).

The modifiers 'n' and 'N' can also be used as first character in the
format string and set the default byte order. 'n', which means network byte
order, is the default byte order when nothing else is specified.

For UDP connections the binary data must be transferred in one network packet
so that the size of the binary data must not be bigger than one network packet.
Usually this means it should be smaller than the MTU (maximum transfer unit)
of the interface, which is usually about 1500 bytes, but only 576 bytes are
guaranteed (1280 bytes for IPv6).

The parameter *`To`* should be left empty for socket connections that
are already bound (all TCP connections and bound UDP connections), but in
case of an unbound UDP connection it must be used to specify the IP
address or host name and port number of the communication partner.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Socket`** (input_control)  socket `→`  (handle)

Socket number.

**`Format`** (input_control)  string `→`  (string)

Specification how to convert the data.

Default:
'z'

**`Data`** (input_control)  string(-array) `→`  (string / real / integer / handle)

Value (or tuple of values) holding the data to send.

**`To`** (input_control)  string(-array) `→`  (string / integer)

IP address or hostname and network port of the communication
partner.

Default:
[]

List of values:
[], ['localhost',3000]

## Possible Predecessors

`open_socket_connect`,
`socket_accept_connect`,
`get_socket_param`,
`set_socket_param`

## Possible Successors

`close_socket`

## See also

`receive_data`

## Module

Foundation
