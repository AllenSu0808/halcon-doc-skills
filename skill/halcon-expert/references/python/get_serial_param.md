# get_serial_param (Operator)

## Name

`get_serial_param` — Get the parameters of a serial device.

## Signature

`def get_serial_param(serial_handle: HHandle) -> Tuple[int, int, str, str, int, int, int]`

## Description

`get_serial_param` returns the current parameter settings of
the serial device passed in *`serial_handle`*. For a
description of the parameters of a serial device, see
[`set_serial_param`](set_serial_param.md).

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

**`baud_rate`** (output_control)  integer `→` int

Speed of the serial interface.

**`data_bits`** (output_control)  integer `→` int

Number of data bits of the serial interface.

**`flow_control`** (output_control)  string `→` str

Type of flow control of the serial interface.

**`parity`** (output_control)  string `→` str

Parity of the serial interface.

**`stop_bits`** (output_control)  integer `→` int

Number of stop bits of the serial interface.

**`total_time_out`** (output_control)  integer `→` int

Total timeout of the serial interface in ms.

**`inter_char_time_out`** (output_control)  integer `→` int

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
