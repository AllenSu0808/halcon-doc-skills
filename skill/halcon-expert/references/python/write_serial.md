# write_serial (Operator)

## Name

`write_serial` — Write to a serial connection.

## Signature

`def write_serial(serial_handle: HHandle, data: MaybeSequence[int]) -> None`

## Description

`write_serial` writes the characters given in *`data`* to
the serial device given by *`serial_handle`*. The data to be
written is passed as a tuple of integers. This allows to write NUL
characters, which would otherwise be interpreted as the end of a
string. `write_serial` always waits until all data has been
transmitted, i.e., a timeout for writing cannot be set.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`serial_handle`** (input_control)  serial `→` HHandle

Serial interface handle.

**`data`** (input_control)  integer(-array) `→` MaybeSequence[int]

Characters to write (as tuple of integers).

## Result

If the parameters are correct and the write to the device was
successful, the operator `write_serial` returns the value 2 (
H_MSG_TRUE)
.
Otherwise an exception is raised.

## Possible Predecessors

`open_serial`

## See also

`read_serial`

## Module

Foundation
