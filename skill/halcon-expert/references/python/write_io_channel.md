# write_io_channel (Operator)

## Name

`write_io_channel` — Write a value to the specified I/O channels.

## Signature

`def write_io_channel(iochannel_handle: MaybeSequence[HHandle], value: Sequence[HTupleElementType]) -> Sequence[int]`

## Description

`write_io_channel` writes values to the specified transmission
channels. The channels are passed in *`iochannel_handle`* and
can be opened and configured by [`open_io_channel`](open_io_channel.md), the values
are passed to *`value`*. The parameter *`status`* returns
for each written value in *`value`* a quality message. The
value *0* indicates that the corresponding value of
*`value`* could be written. Any other status value depends on
the interface. Please refer to the interface-specific documentation
in the directory `doc/html/reference/io` for further
explanation.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`iochannel_handle`** (input_control)  io_channel(-array) `→` MaybeSequence[HHandle]

Handles of the opened I/O channels.

**`value`** (input_control)  tuple-array `→` Sequence[HTupleElementType]

Write values.

**`status`** (output_control)  integer-array `→` Sequence[int]

Status of written values.

## Result

If the parameters are valid, the operator
`write_io_channel` returns the value 2 (
H_MSG_TRUE)
. If necessary an
exception is raised. In this case, an extended error information may be
set and can be queried with the operator [`get_extended_error_info`](get_extended_error_info.md).

## Possible Predecessors

`open_io_channel`,
`set_io_channel_param`

## Possible Successors

`close_io_channel`

## See also

`read_io_channel`,
`open_io_channel`,
`query_io_device`,
`set_io_channel_param`

## Module

Foundation
