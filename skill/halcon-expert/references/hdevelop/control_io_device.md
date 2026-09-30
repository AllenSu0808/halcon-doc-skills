# control_io_device (Operator)

## Name

`control_io_device` — Perform an action on the I/O device.

## Signature

`control_io_device( : : IODeviceHandle, Action, Argument : Result)`

## Description

`control_io_device` performs an action on the I/O device. The
supported parameters are interface-specific and listed in the
corresponding documentation of the used I/O interface that can be
found in the directory `doc/html/reference/io`.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`IODeviceHandle`** (input_control)  io_device `→`  (handle)

Handle of the opened I/O device.

**`Action`** (input_control)  string `→`  (string)

Name of the action to perform.

**`Argument`** (input_control)  string(-array) `→`  (string / integer / real)

List of arguments for the action.

Default:
[]

**`Result`** (output_control)  string-array `→`  (string / integer / real)

List of result values returned by the action.

## Result

If the parameters are valid, the operator `control_io_device`
returns the value 2 (
H_MSG_TRUE)
. If necessary an exception is raised. In this
case an extended error information may be set and can be queried with
the operator [`get_extended_error_info`](get_extended_error_info.md).

## Possible Predecessors

`open_io_device`

## Module

Foundation
