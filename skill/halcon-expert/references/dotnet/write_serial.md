# WriteSerial (Operator)

## Name

`WriteSerial` — Write to a serial connection.

## Signature

`static void HOperatorSet.WriteSerial(HTuple serialHandle, HTuple data)`

`void HSerial.WriteSerial(HTuple data)`

`void HSerial.WriteSerial(int data)`

## Description

`WriteSerial` writes the characters given in *`data`* to
the serial device given by *`serialHandle`*. The data to be
written is passed as a tuple of integers. This allows to write NUL
characters, which would otherwise be interpreted as the end of a
string. `WriteSerial` always waits until all data has been
transmitted, i.e., a timeout for writing cannot be set.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`serialHandle`** (input_control)  serial `→` [HSerial](HSerial.md), [HTuple](HTuple.md) (*IntPtr*)

Serial interface handle.

**`data`** (input_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long)

Characters to write (as tuple of integers).

## Result

If the parameters are correct and the write to the device was
successful, the operator `WriteSerial` returns the value 2 (
H_MSG_TRUE)
.
Otherwise an exception is raised.

## Possible Predecessors

`OpenSerial`

## See also

`ReadSerial`

## Module

Foundation
