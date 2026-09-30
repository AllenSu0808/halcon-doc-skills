# GetSerialParam (Operator)

## Name

`GetSerialParam` — Get the parameters of a serial device.

## Signature

`static void HOperatorSet.GetSerialParam(HTuple serialHandle, out HTuple baudRate, out HTuple dataBits, out HTuple flowControl, out HTuple parity, out HTuple stopBits, out HTuple totalTimeOut, out HTuple interCharTimeOut)`

`int HSerial.GetSerialParam(out int dataBits, out string flowControl, out string parity, out int stopBits, out int totalTimeOut, out int interCharTimeOut)`

## Description

`GetSerialParam` returns the current parameter settings of
the serial device passed in *`serialHandle`*. For a
description of the parameters of a serial device, see
[`SetSerialParam`](set_serial_param.md).

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

**`baudRate`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Speed of the serial interface.

**`dataBits`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Number of data bits of the serial interface.

**`flowControl`** (output_control)  string `→` [HTuple](HTuple.md) (*string*)

Type of flow control of the serial interface.

**`parity`** (output_control)  string `→` [HTuple](HTuple.md) (*string*)

Parity of the serial interface.

**`stopBits`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Number of stop bits of the serial interface.

**`totalTimeOut`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Total timeout of the serial interface in ms.

**`interCharTimeOut`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Inter-character timeout of the serial interface
in ms.

## Result

If the parameters are correct and the parameters of the device could
be read, the operator `GetSerialParam` returns the value
2 (
H_MSG_TRUE)
. Otherwise an exception is raised.

## Possible Predecessors

`OpenSerial`

## Possible Successors

`ReadSerial`,
`WriteSerial`

## See also

`SetSerialParam`

## Module

Foundation
