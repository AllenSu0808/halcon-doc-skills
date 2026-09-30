# CloseIoDevice (Operator)

## Name

`CloseIoDevice` — Close the specified I/O device.

## Signature

`static void HOperatorSet.CloseIoDevice(HTuple IODeviceHandle)`

`void HIODevice.CloseIoDevice()`

## Description

The operator `CloseIoDevice` closes the I/O device specified
by *`IODeviceHandle`*. In particular, all associated channels
are closed (i.e., [`CloseIoChannel`](close_io_channel.md) is called implicitly on
all channels that had been opened for this device) and allocated
memory for data buffers is released.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- IODeviceHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`IODeviceHandle`** (input_control, state is modified)  io_device `→` [HIODevice](HIODevice.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the opened I/O device.

## Result

If the parameters are valid, the operator
`CloseIoDevice` returns the value 2 (
H_MSG_TRUE)
. If necessary an
exception is raised. In this case, an extended error information may be
set and can be queried with the operator [`GetExtendedErrorInfo`](get_extended_error_info.md).

## Possible Predecessors

`OpenIoDevice`

## Module

Foundation
