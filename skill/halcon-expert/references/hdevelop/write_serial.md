# write_serial (Operator)

## Name

`write_serial` — Write to a serial connection.

## Signature

`write_serial( : : SerialHandle, Data : )`

## Description

`write_serial` writes the characters given in *`Data`* to
the serial device given by *`SerialHandle`*. The data to be
written is passed as a tuple of integers. This allows to write NUL
characters, which would otherwise be interpreted as the end of a
string. `write_serial` always waits until all data has been
transmitted, i.e., a timeout for writing cannot be set.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`SerialHandle`** (input_control)  serial `→`  (handle)

Serial interface handle.

**`Data`** (input_control)  integer(-array) `→`  (integer)

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
