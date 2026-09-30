# query_io_device (Operator)

## Name

`query_io_device` — Query information about channels of the specified I/O device.

## Signature

`def query_io_device(iodevice_handle: HHandle, iochannel_name: MaybeSequence[str], query: Sequence[str]) -> Sequence[Union[int, float, str]]`

## Description

The operator `query_io_device` returns information about
transmission channels of a specified I/O device. The handle to the
I/O device is passed to in *`iodevice_handle`*, whereas the
channels are addressed by *`iochannel_name`*. The desired
information about the I/O channels is specified via *`query`*.
A list of all supported channel names is usually returned when passing
*"io_channel_name"* to *`query`* while the input
parameter *`iochannel_name`* is ignored.

Please check the directory `doc/html/reference/io`
for documentation about your specific I/O device interface, where
all supported channel-specific parameters are listed.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`iodevice_handle`** (input_control)  io_device `→` HHandle

Handle of the opened I/O device.

**`iochannel_name`** (input_control)  string(-array) `→` MaybeSequence[str]

Channel names to query.

**`query`** (input_control)  string-array `→` Sequence[str]

Name of the query.

Default:
"param_name"

List of values:
"io_channel_names", "param_name"

**`result`** (output_control)  string-array `→` Sequence[Union[int, float, str]]

List of values (according to *`query`*).

## Example (HDevelop)

```
* Select a suitable i/o device interface of name IOInterfaceName
query_io_interface (IOInterfaceName, 'io_device_names', DeviceNames)
open_io_device (IOInterfaceName, DeviceNames[0], [], [], IODeviceHandle)
query_io_device (IODeviceHandle, [], 'io_channel_names.digital_input', \
                 ChannelInputNames)
open_io_channel (IODeviceHandle, ChannelInputNames[0], [], [], \
                 IOChannelHandle)
read_io_channel (IOChannelHandle, Value, Status)
```

## Result

If the parameters are valid, the operator
`query_io_device` returns the value 2 (
H_MSG_TRUE)
. If necessary an
exception is raised. In this case, an extended error information may be
set and can be queried with the operator [`get_extended_error_info`](get_extended_error_info.md).

## Possible Successors

`open_io_device`

## Module

Foundation
