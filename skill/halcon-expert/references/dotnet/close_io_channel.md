# CloseIoChannel (Operator)

## Name

`CloseIoChannel` — Close I/O channels.

## Signature

`static void HOperatorSet.CloseIoChannel(HTuple IOChannelHandle)`

`static void HIOChannel.CloseIoChannel(HIOChannel[] IOChannelHandle)`

`void HIOChannel.CloseIoChannel()`

## Description

The operator `CloseIoChannel` closes transmission
channels opened by [`OpenIoChannel`](open_io_channel.md). The references to the
channels are passed in *`IOChannelHandle`*. In particular,
allocated memory and reserved device resources are released.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- IOChannelHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`IOChannelHandle`** (input_control, state is modified)  io_channel(-array) `→` [HIOChannel](HIOChannel.md), [HTuple](HTuple.md) (*IntPtr*)

Handles of the opened I/O channels.

## Result

If the parameters are valid, the operator
`CloseIoChannel` returns the value 2 (
H_MSG_TRUE)
. If necessary an
exception is raised. In this case, an extended error information may be
set and can be queried with the operator [`GetExtendedErrorInfo`](get_extended_error_info.md).

## Possible Predecessors

`OpenIoChannel`

## Possible Successors

`CloseIoDevice`

## Module

Foundation
