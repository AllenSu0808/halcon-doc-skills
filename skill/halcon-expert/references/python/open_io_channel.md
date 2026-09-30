# open_io_channel (Operator)

## Name

`open_io_channel` — Open and configure I/O channels.

## Signature

`def open_io_channel(iodevice_handle: HHandle, iochannel_name: MaybeSequence[str], gen_param_name: Sequence[str], gen_param_value: Sequence[Union[int, float, str]]) -> Sequence[HHandle]`

`def open_io_channel_s(iodevice_handle: HHandle, iochannel_name: MaybeSequence[str], gen_param_name: Sequence[str], gen_param_value: Sequence[Union[int, float, str]]) -> HHandle`

## Description

The operator `open_io_channel` opens and configures
transmission channels of an opened I/O device instance. The device
instance must have been opened by [`open_io_device`](open_io_device.md) before and
is passed to *`iodevice_handle`*. The transmission channels
themselves are addressed by their names passed to
*`iochannel_name`*. Available names can be queried using
[`query_io_device`](query_io_device.md) with query parameter
*"io_channel_name"*. The channels can be configured by the
parameters *`gen_param_name`* and *`gen_param_value`*. A
reference to each transmission channel is returned in
*`iochannel_handle`*. If the instance of the channel is not
needed any more, it should be released and closed via the operator
[`close_io_channel`](close_io_channel.md). Besides, it will be closed automatically
when closing the associated device instance by
[`close_io_device`](close_io_device.md).

Having opened a transmission channel, values can be read and written
by the operators [`read_io_channel`](read_io_channel.md) and
[`write_io_channel`](write_io_channel.md) on the channel.

An opened channel can be reconfigured by using the operators
[`set_io_channel_param`](set_io_channel_param.md) and [`get_io_channel_param`](get_io_channel_param.md).

Please check the directory `doc/html/reference/io` for
documentation about your specific I/O device interface, where all
supported device specific parameters are listed.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`iodevice_handle`** (input_control)  io_device `→` HHandle

Handle of the opened I/O device.

**`iochannel_name`** (input_control)  string(-array) `→` MaybeSequence[str]

HALCON I/O channel names of the specified device.

**`gen_param_name`** (input_control)  string-array `→` Sequence[str]

Parameter names.

Default:
[]

**`gen_param_value`** (input_control)  string-array `→` Sequence[Union[int, float, str]]

Parameter values.

Default:
[]

**`iochannel_handle`** (output_control)  io_channel(-array) `→` Sequence[HHandle]

Handles of the opened I/O channel.

## Example (HDevelop)

```
query_io_device (IODeviceHandle, [], 'io_channel_names.digital_output', \
                 ChannelOutputNames)
open_io_channel (IODeviceHandle, ChannelOutputNames[0], [], [], \
                 IOChannelHandle)
write_io_channel (IOChannelHandle, 1, Status)
```

## Result

If the parameters are valid, the operator
`open_io_channel` returns the value 2 (
H_MSG_TRUE)
. If necessary an
exception is raised. In this case, an extended error information may be
set and can be queried with the operator [`get_extended_error_info`](get_extended_error_info.md).

## Possible Predecessors

`open_io_device`,
`query_io_device`

## Possible Successors

`set_io_channel_param`,
`read_io_channel`,
`write_io_channel`

## Module

Foundation
