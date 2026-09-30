# set_io_channel_param (Operator)

## Name

`set_io_channel_param` — Set specific parameters of I/O channels.

## Signature

`set_io_channel_param( : : IOChannelHandle, GenParamName, GenParamValue : )`

## Description

`set_io_channel_param` (re)configures the given transmission
channels. The configuration parameters are passed in
*`GenParamName`*, the corresponding values are passed in
*`GenParamValue`*. *`IOChannelHandle`* specifies the
transmission channels returned in [`open_io_channel`](open_io_channel.md).

Please check the directory `doc/html/reference/io` for
documentation about your specific I/O device interface, where all
supported channel-specific parameters are listed.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`IOChannelHandle`** (input_control)  io_channel(-array) `→`  (handle)

Handles of the opened I/O channels.

**`GenParamName`** (input_control)  string-array `→`  (string)

Parameter names.

Default:
[]

**`GenParamValue`** (input_control)  string-array `→`  (string / integer / real / handle)

Parameter values to set.

Default:
[]

## Result

If the parameters are valid, the operator
`set_io_channel_param` returns the value 2 (
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
`get_io_channel_param`,
`read_io_channel`,
`write_io_channel`

## Module

Foundation
