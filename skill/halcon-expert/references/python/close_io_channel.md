# close_io_channel (Operator)

## Name

`close_io_channel` — Close I/O channels.

## Signature

`def close_io_channel(iochannel_handle: MaybeSequence[HHandle]) -> None`

## Description

The operator `close_io_channel` closes transmission
channels opened by [`open_io_channel`](open_io_channel.md). The references to the
channels are passed in *`iochannel_handle`*. In particular,
allocated memory and reserved device resources are released.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- iochannel_handle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`iochannel_handle`** (input_control, state is modified)  io_channel(-array) `→` MaybeSequence[HHandle]

Handles of the opened I/O channels.

## Result

If the parameters are valid, the operator
`close_io_channel` returns the value 2 (
H_MSG_TRUE)
. If necessary an
exception is raised. In this case, an extended error information may be
set and can be queried with the operator [`get_extended_error_info`](get_extended_error_info.md).

## Possible Predecessors

`open_io_channel`

## Possible Successors

`close_io_device`

## Module

Foundation
