# ControlIoChannel (Operator)

## Name

`ControlIoChannel` — Perform an action on I/O channels.

## Signature

`static void HOperatorSet.ControlIoChannel(HTuple IOChannelHandle, HTuple action, HTuple argument, out HTuple result)`

`static HTuple HIOChannel.ControlIoChannel(HIOChannel[] IOChannelHandle, string action, HTuple argument)`

`HTuple HIOChannel.ControlIoChannel(string action, HTuple argument)`

## Description

`ControlIoChannel` performs an action on the specified I/O channels.
The supported parameters are interface-specific and listed in the
corresponding documentation of the used I/O interface that can be
found in the directory `doc/html/reference/io`.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`IOChannelHandle`** (input_control)  io_channel(-array) `→` [HIOChannel](HIOChannel.md), [HTuple](HTuple.md) (*IntPtr*)

Handles of the opened I/O channels.

**`action`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Name of the action to perform.

**`argument`** (input_control)  string-array `→` [HTuple](HTuple.md) (*string* / int / long / double)

List of arguments for the action.

Default:
[]

**`result`** (output_control)  string-array `→` [HTuple](HTuple.md) (*string* / int / long / double)

List of values returned by the action.

## Result

If the parameters are valid, the operator `ControlIoChannel`
returns the value 2 (
H_MSG_TRUE)
. If necessary an exception is raised. In this
case an extended error information may be set and can be queried with
the operator [`GetExtendedErrorInfo`](get_extended_error_info.md).

## Possible Predecessors

`OpenIoChannel`

## Module

Foundation
