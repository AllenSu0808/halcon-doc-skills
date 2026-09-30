# get_io_channel_param (Operator)

## Name

`get_io_channel_param` — Query specific parameters of I/O channels.

## Signature

`def get_io_channel_param(iochannel_handle: MaybeSequence[HHandle], gen_param_name: MaybeSequence[str]) -> Sequence[HTupleElementType]`

## Description

`get_io_channel_param` queries settings of specific I/O
transmission channels. The query parameters are passed in
*`gen_param_name`*, the corresponding configuration values are
returned in *`gen_param_value`*. *`iochannel_handle`* specifies
the channels returned in [`open_io_channel`](open_io_channel.md) for a specific
device instance.

Please check the directory `doc/html/reference/io` for
documentation about your specific I/O device interface, where all
supported channel-specific parameters are listed.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`iochannel_handle`** (input_control)  io_channel(-array) `→` MaybeSequence[HHandle]

Handles of the opened I/O channels.

**`gen_param_name`** (input_control)  string(-array) `→` MaybeSequence[str]

Parameter names.

Default:
"param_name"

Suggested values:
"io_channel_name", "param_name"

**`gen_param_value`** (output_control)  string-array `→` Sequence[HTupleElementType]

Parameter values.

## Result

If the parameters are valid, the operator
`get_io_channel_param` returns the value 2 (
H_MSG_TRUE)
. If necessary an
exception is raised. In this case, an extended error information may be
set and can be queried with the operator [`get_extended_error_info`](get_extended_error_info.md).

## Possible Predecessors

`open_io_channel`

## Possible Successors

`read_io_channel`,
`write_io_channel`

## See also

`open_io_channel`,
`query_io_device`,
`set_io_channel_param`

## Module

Foundation
