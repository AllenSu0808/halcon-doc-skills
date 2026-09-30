# clear_serial (Operator)

## Name

`clear_serial` — Clear the buffer of a serial connection.

## Signature

`def clear_serial(serial_handle: HHandle, channel: str) -> None`

## Description

`clear_serial` discards data written to the serial device
referred to by *`serial_handle`*, but not transmitted
(*`channel`* = *"output"*), or data received, but not
read (*`channel`* = *"input"*), or performs both these
operations at once (*`channel`* = *"in_out"*).

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

**`channel`** (input_control)  string `→` str

Buffer to be cleared.

Default:
"input"

List of values:
"in_out", "input", "output"

## Result

If the parameters are correct and the buffers of the serial device
could be cleared, the operator `clear_serial` returns the
value 2 (
H_MSG_TRUE)
. Otherwise an exception is raised.

## Possible Predecessors

`open_serial`

## Possible Successors

`read_serial`,
`write_serial`

## See also

`read_serial`

## Module

Foundation
