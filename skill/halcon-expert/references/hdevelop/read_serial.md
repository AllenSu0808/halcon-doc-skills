# read_serial (Operator)

## Name

`read_serial` — Read from a serial device.

## Signature

`read_serial( : : SerialHandle, NumCharacters : Data)`

## Description

`read_serial` tries to read *`NumCharacters`* from the
serial device given in *`SerialHandle`*. The read characters
are returned in *`Data`* as a tuple of integers. This allows
to read NUL characters, which would otherwise be interpreted as the
end of a string. If the timeout of the serial device has been set
to a value greater than 0 with [`set_serial_param`](set_serial_param.md),
`read_serial` waits at most as long for the arrival of the
first character as indicated by the timeout. Otherwise, the
operator returns immediately. In any case, the number of characters
available at the time of return are passed back to the caller, i.e.,
fewer characters than requested can be returned. This can be
checked by the length of the tuple *`Data`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`SerialHandle`** (input_control)  serial `→`  (handle)

Serial interface handle.

**`NumCharacters`** (input_control)  integer `→`  (integer)

Number of characters to read.

Default:
1

Suggested values:
1, 2, 3, 4, 5, 10, 20, 40, 100

**`Data`** (output_control)  integer(-array) `→`  (integer)

Read characters (as tuple of integers).

## Result

If the parameters are correct and the read from the device was
successful, the operator `read_serial` returns the value 2 (
H_MSG_TRUE)
.
Otherwise an exception is raised.

## Possible Predecessors

`open_serial`

## See also

`write_serial`

## Module

Foundation
