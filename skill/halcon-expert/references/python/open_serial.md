# open_serial (Operator)

## Name

`open_serial` — Open a serial device.

## Signature

`def open_serial(port_name: str) -> HHandle`

## Description

`open_serial` opens a serial device. The name of the device
is determined by the parameter *`port_name`* and is operating
system specific. On Windows machines,
*"COM1"*-*"COM4"* is typically used, while on Unix-like
systems the serial devices usually are named *"/dev/tty*"*.
The parameters of the serial device, e.g., its speed or number of
data bits, are set to the system default values for the respective
device after the device has been opened. They can be set or
changed by calling [`set_serial_param`](set_serial_param.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`port_name`** (input_control)  filename `→` str

Name of the serial port.

Default:
"COM1"

Suggested values:
"COM1", "COM2", "COM3", "COM4", "/dev/ttya", "/dev/ttyb", "/dev/tty00", "/dev/tty01", "/dev/ttyd1", "/dev/ttyd2", "/dev/cua0", "/dev/cua1"

**`serial_handle`** (output_control)  serial `→` HHandle

Serial interface handle.

## Result

If the parameters are correct and the device could be opened, the
operator `open_serial` returns the value 2 (
H_MSG_TRUE)
. Otherwise an
exception is raised.

## Possible Successors

`set_serial_param`,
`read_serial`,
`write_serial`,
`close_serial`

## See also

`set_serial_param`,
`get_serial_param`,
`open_file`

## Module

Foundation
