# close_io_device (Operator)

## Name

`close_io_device` — Close the specified I/O device.

## Signature

`def close_io_device(iodevice_handle: HHandle) -> None`

## Description

The operator `close_io_device` closes the I/O device specified
by *`iodevice_handle`*. In particular, all associated channels
are closed (i.e., [`close_io_channel`](close_io_channel.md) is called implicitly on
all channels that had been opened for this device) and allocated
memory for data buffers is released.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- iodevice_handle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`iodevice_handle`** (input_control, state is modified)  io_device `→` HHandle

Handle of the opened I/O device.

## Result

If the parameters are valid, the operator
`close_io_device` returns the value 2 (
H_MSG_TRUE)
. If necessary an
exception is raised. In this case, an extended error information may be
set and can be queried with the operator [`get_extended_error_info`](get_extended_error_info.md).

## Possible Predecessors

`open_io_device`

## Module

Foundation
