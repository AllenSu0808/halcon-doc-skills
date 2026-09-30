# clear_serial (Operator)

## Name

`clear_serial` — Clear the buffer of a serial connection.

## Signature

`clear_serial( : : SerialHandle, Channel : )`

## Description

`clear_serial` discards data written to the serial device
referred to by *`SerialHandle`*, but not transmitted
(*`Channel`* = *'output'*), or data received, but not
read (*`Channel`* = *'input'*), or performs both these
operations at once (*`Channel`* = *'in_out'*).

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

**`Channel`** (input_control)  string `→`  (string)

Buffer to be cleared.

Default:
'input'

List of values:
'in_out', 'input', 'output'

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
