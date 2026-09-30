# control_io_channel (Operator)

## Name

`control_io_channel` — Perform an action on I/O channels.

## Signature

`def control_io_channel(iochannel_handle: MaybeSequence[HHandle], action: str, argument: Sequence[Union[int, float, str]]) -> Sequence[Union[int, float, str]]`

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

**`iochannel_handle`** (input_control)  io_channel(-array) `→` MaybeSequence[HHandle]

Handles of the opened I/O channels.

**`action`** (input_control)  string `→` str

Name of the action to perform.

**`argument`** (input_control)  string-array `→` Sequence[Union[int, float, str]]

List of arguments for the action.

Default:
[]

**`result`** (output_control)  string-array `→` Sequence[Union[int, float, str]]

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
