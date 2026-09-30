# ClearSerial (Operator)

## Name

`ClearSerial` — Clear the buffer of a serial connection.

## Signature

`static void HOperatorSet.ClearSerial(HTuple serialHandle, HTuple channel)`

`void HSerial.ClearSerial(string channel)`

## Description

`ClearSerial` discards data written to the serial device
referred to by *`serialHandle`*, but not transmitted
(*`channel`* = *"output"*), or data received, but not
read (*`channel`* = *"input"*), or performs both these
operations at once (*`channel`* = *"in_out"*).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- serialHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`serialHandle`** (input_control, state is modified)  serial `→` [HSerial](HSerial.md), [HTuple](HTuple.md) (*IntPtr*)

Serial interface handle.

**`channel`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Buffer to be cleared.

Default:
"input"

List of values:
"in_out", "input", "output"

## Result

If the parameters are correct and the buffers of the serial device
could be cleared, the operator `ClearSerial` returns the
value 2 (
H_MSG_TRUE)
. Otherwise an exception is raised.

## Possible Predecessors

`OpenSerial`

## Possible Successors

`ReadSerial`,
`WriteSerial`

## See also

`ReadSerial`

## Module

Foundation
