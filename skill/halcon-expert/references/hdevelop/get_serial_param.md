# get_serial_param (Operator)

## Name

`get_serial_param` — Get the parameters of a serial device.

## Signature

`get_serial_param( : : SerialHandle : BaudRate, DataBits, FlowControl, Parity, StopBits, TotalTimeOut, InterCharTimeOut)`

## Description

`get_serial_param` returns the current parameter settings of
the serial device passed in *`SerialHandle`*. For a
description of the parameters of a serial device, see
[`set_serial_param`](set_serial_param.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- SerialHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`SerialHandle`** (input_control, state is modified)  serial `→`  (handle)

Serial interface handle.

**`BaudRate`** (output_control)  integer `→`  (integer)

Speed of the serial interface.

**`DataBits`** (output_control)  integer `→`  (integer)

Number of data bits of the serial interface.

**`FlowControl`** (output_control)  string `→`  (string)

Type of flow control of the serial interface.

**`Parity`** (output_control)  string `→`  (string)

Parity of the serial interface.

**`StopBits`** (output_control)  integer `→`  (integer)

Number of stop bits of the serial interface.

**`TotalTimeOut`** (output_control)  integer `→`  (integer)

Total timeout of the serial interface in ms.

**`InterCharTimeOut`** (output_control)  integer `→`  (integer)

Inter-character timeout of the serial interface
in ms.

## Result

If the parameters are correct and the parameters of the device could
be read, the operator `get_serial_param` returns the value
2 (
H_MSG_TRUE)
. Otherwise an exception is raised.

## Possible Predecessors

`open_serial`

## Possible Successors

`read_serial`,
`write_serial`

## See also

`set_serial_param`

## Module

Foundation
