# close_serial (Operator)

## Name

`close_serial` — Close a serial device.

## Signature

`def close_serial(serial_handle: HHandle) -> None`

## Description

`close_serial` closes a serial device that was opened with
[`open_serial`](open_serial.md).

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

## Result

If the parameters are correct and the device could be closed, the
operator `close_serial` returns the value 2 (
H_MSG_TRUE)
. Otherwise an
exception is raised.

## Possible Predecessors

`open_serial`

## See also

`open_serial`,
`close_file`

## Module

Foundation
