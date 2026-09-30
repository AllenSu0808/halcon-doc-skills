# set_serial_param (Operator)

## Name

`set_serial_param` — Set the parameters of a serial device.

## Signature

`def set_serial_param(serial_handle: HHandle, baud_rate: Union[int, str], data_bits: Union[int, str], flow_control: str, parity: str, stop_bits: Union[int, str], total_time_out: Union[int, str], inter_char_time_out: Union[int, str]) -> None`

## Description

`set_serial_param` can be used to set the parameters of a
serial device. The parameter *`baud_rate`* determines the input
and output speed of the device. It should be noted that not all
devices support all possible speeds. The number of sent and
received data bits is set with *`data_bits`*. The parameter
*`flow_control`* determines if and what kind of data flow
control should be used. Software control (*"xon_xoff"*)
and hardware control (*"cts_rts"* and *"dtr_dsr"*)
can be used. Multiple values can be set separated by a space
within one string (e.g., *"cts_rts dtr_dsr"*).
If and what
kind of parity check of the transmitted data should be performed can
be determined by *`parity`*. The number of stop bits sent is
set with *`stop_bits`*. Finally, two timeout for reading from
the serial device can be set. The parameter *`total_time_out`*
determines the maximum time, which may pass in [`read_serial`](read_serial.md)
until the first character arrives, independent of the actual number
of characters requested. The parameter *`inter_char_time_out`*
determines the time which may pass between the reading of individual
characters, if multiple characters are requested with
[`read_serial`](read_serial.md). If one of the timeouts is set to *-1*,
the system waits an arbitrary amount of time for the arrival of
characters. If both timeouts are set to *0* the system
doesn't wait and returns the available or none characters. Thus, on
Windows systems, a total timeout of *`total_time_out`* + n
*`inter_char_time_out`* results if n characters are to be read.
On Unix-like systems, only one of the two timeouts can be set. Thus, if
both timeouts are passed larger than -1, only the total timeout is
used. The unit of both timeouts is milliseconds. It should be
noted, however, that the timeout is specified in increments of one
tenths of a second on Unix-like systems, i.e., the minimum timeout
that has any effect is *100*. For each parameter, the
current values can be left in effect by passing
*"unchanged"*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- serial_handle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`serial_handle`** (input_control, state is modified)  serial `→` HHandle

Serial interface handle.

**`baud_rate`** (input_control)  integer `→` Union[int, str]

Speed of the serial interface.

Default:
"unchanged"

List of values:
50, 75, 110, 134, 150, 200, 300, 600, 1200, 1800, 2400, 4800, 9600, 19200, 38400, 57600, 76800, 115200, 153600, 230400, 307200, 460800, "unchanged"

**`data_bits`** (input_control)  integer `→` Union[int, str]

Number of data bits of the serial interface.

Default:
"unchanged"

List of values:
5, 6, 7, 8, "unchanged"

**`flow_control`** (input_control)  string `→` str

Type of flow control of the serial interface.

Default:
"unchanged"

List of values:
"cts_rts dtr_dsr xon_xoff", "cts_rts dtr_dsr", "cts_rts xon_xoff", "cts_rts", "dtr_dsr xon_xoff", "dtr_dsr", "none", "unchanged", "xon_xoff"

**`parity`** (input_control)  string `→` str

Parity of the serial interface.

Default:
"unchanged"

List of values:
"even", "none", "odd", "unchanged"

**`stop_bits`** (input_control)  integer `→` Union[int, str]

Number of stop bits of the serial interface.

Default:
"unchanged"

List of values:
1, 2, "unchanged"

**`total_time_out`** (input_control)  integer `→` Union[int, str]

Total timeout of the serial interface in ms.

Default:
"unchanged"

Suggested values:
-1, 0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, "unchanged"

**`inter_char_time_out`** (input_control)  integer `→` Union[int, str]

Inter-character timeout of the serial interface
in ms.

Default:
"unchanged"

Suggested values:
-1, 0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, "unchanged"

## Result

If the parameters are correct and the parameters of the device could
be set, the operator `set_serial_param` returns the value
2 (
H_MSG_TRUE)
. Otherwise an exception is raised.

## Possible Predecessors

`open_serial`,
`get_serial_param`

## Possible Successors

`read_serial`,
`write_serial`

## See also

`get_serial_param`

## Module

Foundation
