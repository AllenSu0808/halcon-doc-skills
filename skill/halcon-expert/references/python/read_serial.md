# read_serial (Operator)

## Name

`read_serial` — Read from a serial device.

## Signature

`def read_serial(serial_handle: HHandle, num_characters: int) -> Sequence[int]`

`def read_serial_s(serial_handle: HHandle, num_characters: int) -> int`

## Description

`read_serial` tries to read *`num_characters`* from the
serial device given in *`serial_handle`*. The read characters
are returned in *`data`* as a tuple of integers. This allows
to read NUL characters, which would otherwise be interpreted as the
end of a string. If the timeout of the serial device has been set
to a value greater than 0 with [`set_serial_param`](set_serial_param.md),
`read_serial` waits at most as long for the arrival of the
first character as indicated by the timeout. Otherwise, the
operator returns immediately. In any case, the number of characters
available at the time of return are passed back to the caller, i.e.,
fewer characters than requested can be returned. This can be
checked by the length of the tuple *`data`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`serial_handle`** (input_control)  serial `→` HHandle

Serial interface handle.

**`num_characters`** (input_control)  integer `→` int

Number of characters to read.

Default:
1

Suggested values:
1, 2, 3, 4, 5, 10, 20, 40, 100

**`data`** (output_control)  integer(-array) `→` Sequence[int]

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
