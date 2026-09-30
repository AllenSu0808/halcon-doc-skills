# control_io_channel (Operator)

## Name

`control_io_channel` — Perform an action on I/O channels.

## Signature

`control_io_channel( : : IOChannelHandle, Action, Argument : Result)`

## Description

`control_io_channel` performs an action on the specified I/O channels.
The supported parameters are interface-specific and listed in the
corresponding documentation of the used I/O interface that can be
found in the directory `doc/html/reference/io`.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`IOChannelHandle`** (input_control)  io_channel(-array) `→`  (handle)

Handles of the opened I/O channels.

**`Action`** (input_control)  string `→`  (string)

Name of the action to perform.

**`Argument`** (input_control)  string-array `→`  (string / integer / real)

List of arguments for the action.

Default:
[]

**`Result`** (output_control)  string-array `→`  (string / integer / real)

List of values returned by the action.

## Result

If the parameters are valid, the operator `control_io_channel`
returns the value 2 (
H_MSG_TRUE)
. If necessary an exception is raised. In this
case an extended error information may be set and can be queried with
the operator [`get_extended_error_info`](get_extended_error_info.md).

## Possible Predecessors

`open_io_channel`

## Module

Foundation
