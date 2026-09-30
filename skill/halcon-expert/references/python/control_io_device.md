# control_io_device (Operator)

## Name

`control_io_device` — Perform an action on the I/O device.

## Signature

`def control_io_device(iodevice_handle: HHandle, action: str, argument: MaybeSequence[Union[int, float, str]]) -> Sequence[Union[int, float, str]]`

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

**`iodevice_handle`** (input_control)  io_device `→` HHandle

Handle of the opened I/O device.

**`action`** (input_control)  string `→` str

Name of the action to perform.

**`argument`** (input_control)  string(-array) `→` MaybeSequence[Union[int, float, str]]

List of arguments for the action.

Default:
[]

**`result`** (output_control)  string-array `→` Sequence[Union[int, float, str]]

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
