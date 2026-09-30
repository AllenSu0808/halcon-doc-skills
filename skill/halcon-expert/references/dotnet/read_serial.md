# ReadSerial (Operator)

## Name

`ReadSerial` — Read from a serial device.

## Signature

`static void HOperatorSet.ReadSerial(HTuple serialHandle, HTuple numCharacters, out HTuple data)`

`HTuple HSerial.ReadSerial(int numCharacters)`

## Description

`ReadSerial` tries to read *`numCharacters`* from the
serial device given in *`serialHandle`*. The read characters
are returned in *`data`* as a tuple of integers. This allows
to read NUL characters, which would otherwise be interpreted as the
end of a string. If the timeout of the serial device has been set
to a value greater than 0 with [`SetSerialParam`](set_serial_param.md),
`ReadSerial` waits at most as long for the arrival of the
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

**`serialHandle`** (input_control)  serial `→` [HSerial](HSerial.md), [HTuple](HTuple.md) (*IntPtr*)

Serial interface handle.

**`numCharacters`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Number of characters to read.

Default:
1

Suggested values:
1, 2, 3, 4, 5, 10, 20, 40, 100

**`data`** (output_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long)

Read characters (as tuple of integers).

## Result

If the parameters are correct and the read from the device was
successful, the operator `ReadSerial` returns the value 2 (
H_MSG_TRUE)
.
Otherwise an exception is raised.

## Possible Predecessors

`OpenSerial`

## See also

`WriteSerial`

## Module

Foundation
