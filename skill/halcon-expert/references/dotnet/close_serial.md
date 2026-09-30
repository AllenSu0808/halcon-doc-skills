# CloseSerial (Operator)

## Name

`CloseSerial` — Close a serial device.

## Signature

`static void HOperatorSet.CloseSerial(HTuple serialHandle)`

`void HSerial.CloseSerial()`

## Description

`CloseSerial` closes a serial device that was opened with
[`OpenSerial`](open_serial.md).

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

## Result

If the parameters are correct and the device could be closed, the
operator `CloseSerial` returns the value 2 (
H_MSG_TRUE)
. Otherwise an
exception is raised.

## Possible Predecessors

`OpenSerial`

## See also

`OpenSerial`,
`CloseFile`

## Module

Foundation
