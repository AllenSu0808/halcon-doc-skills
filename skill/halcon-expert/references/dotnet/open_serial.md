# OpenSerial (Operator)

## Name

`OpenSerial` — Open a serial device.

## Signature

`static void HOperatorSet.OpenSerial(HTuple portName, out HTuple serialHandle)`

`public HSerial(string portName)`

`void HSerial.OpenSerial(string portName)`

## Description

`OpenSerial` opens a serial device. The name of the device
is determined by the parameter *`portName`* and is operating
system specific. On Windows machines,
*"COM1"*-*"COM4"* is typically used, while on Unix-like
systems the serial devices usually are named *"/dev/tty*"*.
The parameters of the serial device, e.g., its speed or number of
data bits, are set to the system default values for the respective
device after the device has been opened. They can be set or
changed by calling [`SetSerialParam`](set_serial_param.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`portName`** (input_control)  filename `→` [HTuple](HTuple.md) (*string*)

Name of the serial port.

Default:
"COM1"

Suggested values:
"COM1", "COM2", "COM3", "COM4", "/dev/ttya", "/dev/ttyb", "/dev/tty00", "/dev/tty01", "/dev/ttyd1", "/dev/ttyd2", "/dev/cua0", "/dev/cua1"

**`serialHandle`** (output_control)  serial `→` [HSerial](HSerial.md), [HTuple](HTuple.md) (*IntPtr*)

Serial interface handle.

## Result

If the parameters are correct and the device could be opened, the
operator `OpenSerial` returns the value 2 (
H_MSG_TRUE)
. Otherwise an
exception is raised.

## Possible Successors

`SetSerialParam`,
`ReadSerial`,
`WriteSerial`,
`CloseSerial`

## See also

`SetSerialParam`,
`GetSerialParam`,
`OpenFile`

## Module

Foundation
