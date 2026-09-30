# OpenIoChannel (Operator)

## Name

`OpenIoChannel` — Open and configure I/O channels.

## Signature

`static void HOperatorSet.OpenIoChannel(HTuple IODeviceHandle, HTuple IOChannelName, HTuple genParamName, HTuple genParamValue, out HTuple IOChannelHandle)`

`HIOChannel[] HIODevice.OpenIoChannel(HTuple IOChannelName, HTuple genParamName, HTuple genParamValue)`

`HIOChannel HIODevice.OpenIoChannel(string IOChannelName, HTuple genParamName, HTuple genParamValue)`

`public HIOChannel(HIODevice IODeviceHandle, string IOChannelName, HTuple genParamName, HTuple genParamValue)`

`static HIOChannel[] HIOChannel.OpenIoChannel(HIODevice IODeviceHandle, HTuple IOChannelName, HTuple genParamName, HTuple genParamValue)`

`void HIOChannel.OpenIoChannel(HIODevice IODeviceHandle, string IOChannelName, HTuple genParamName, HTuple genParamValue)`

## Description

The operator `OpenIoChannel` opens and configures
transmission channels of an opened I/O device instance. The device
instance must have been opened by [`OpenIoDevice`](open_io_device.md) before and
is passed to *`IODeviceHandle`*. The transmission channels
themselves are addressed by their names passed to
*`IOChannelName`*. Available names can be queried using
[`QueryIoDevice`](query_io_device.md) with query parameter
*"io_channel_name"*. The channels can be configured by the
parameters *`genParamName`* and *`genParamValue`*. A
reference to each transmission channel is returned in
*`IOChannelHandle`*. If the instance of the channel is not
needed any more, it should be released and closed via the operator
[`CloseIoChannel`](close_io_channel.md). Besides, it will be closed automatically
when closing the associated device instance by
[`CloseIoDevice`](close_io_device.md).

Having opened a transmission channel, values can be read and written
by the operators [`ReadIoChannel`](read_io_channel.md) and
[`WriteIoChannel`](write_io_channel.md) on the channel.

An opened channel can be reconfigured by using the operators
[`SetIoChannelParam`](set_io_channel_param.md) and [`GetIoChannelParam`](get_io_channel_param.md).

Please check the directory `doc/html/reference/io` for
documentation about your specific I/O device interface, where all
supported device specific parameters are listed.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`IODeviceHandle`** (input_control)  io_device `→` [HIODevice](HIODevice.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the opened I/O device.

**`IOChannelName`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

HALCON I/O channel names of the specified device.

**`genParamName`** (input_control)  string-array `→` [HTuple](HTuple.md) (*string*)

Parameter names.

Default:
[]

**`genParamValue`** (input_control)  string-array `→` [HTuple](HTuple.md) (*string* / int / long / double)

Parameter values.

Default:
[]

**`IOChannelHandle`** (output_control)  io_channel(-array) `→` [HIOChannel](HIOChannel.md), [HTuple](HTuple.md) (*IntPtr*)

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
`OpenIoChannel` returns the value 2 (
H_MSG_TRUE)
. If necessary an
exception is raised. In this case, an extended error information may be
set and can be queried with the operator [`GetExtendedErrorInfo`](get_extended_error_info.md).

## Possible Predecessors

`OpenIoDevice`,
`QueryIoDevice`

## Possible Successors

`SetIoChannelParam`,
`ReadIoChannel`,
`WriteIoChannel`

## Module

Foundation
