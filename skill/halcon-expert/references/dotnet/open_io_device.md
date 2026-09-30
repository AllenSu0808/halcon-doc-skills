# OpenIoDevice (Operator)

## Name

`OpenIoDevice` — Open and configure an I/O device.

## Signature

`static void HOperatorSet.OpenIoDevice(HTuple IOInterfaceName, HTuple IODeviceName, HTuple genParamName, HTuple genParamValue, out HTuple IODeviceHandle)`

`public HIODevice(string IOInterfaceName, HTuple IODeviceName, HTuple genParamName, HTuple genParamValue)`

`void HIODevice.OpenIoDevice(string IOInterfaceName, HTuple IODeviceName, HTuple genParamName, HTuple genParamValue)`

## Description

The operator `OpenIoDevice` opens and configures the chosen
I/O device interface for the specific device. The device interface
is specified by the base name of the underlying library and passed
to *`IOInterfaceName`*. The interface library will be loaded
dynamically when configuring the first specific device for this
device interface. The specific device itself is addressed by a name
passed to *`IODeviceName`*. Available names can be queried by
[`QueryIoInterface`](query_io_interface.md). The device can be configured by the
parameters *`genParamName`* and *`genParamValue`*. A
reference to the device instance is returned in
*`IODeviceHandle`*. If the instance of the device is not needed
any more, it should be released and closed via the operator
[`CloseIoDevice`](close_io_device.md).

Having opened a specific device, a transmission channel can be
opened by calling [`OpenIoChannel`](open_io_channel.md). Values on the I/O channel
can be read and written by the operators [`ReadIoChannel`](read_io_channel.md) and
[`WriteIoChannel`](write_io_channel.md) on an opened transmission channel,
afterwards.

An opened device instance can be reconfigured by using the operators
[`SetIoDeviceParam`](set_io_device_param.md) and [`GetIoDeviceParam`](get_io_device_param.md).

Please check the directory `doc/html/reference/io` for
documentation about your specific I/O device interface, where all
supported device specific parameters are listed.

## Attention

On Windows Systems, error dialog boxes from the operating system can occur
when dependency modules of the interface are not found, e.g., the according
SDK was not installed. The occurrence of the error boxes can be controlled by
setting Windows' Error Mode. Please refer to the description of SetErrorMode
within the Windows MSDN documentation.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`IOInterfaceName`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

HALCON I/O interface name.

Default:
[]

Suggested values:
"ADLINK-DAQPilot", "ADLINK-EOS", "Advantech", "Contec", "Hilscher-cifX", "Interface", "Linux-GPIO", "NIDAQmx", "OPC_Classic", "OPC_UA"

**`IODeviceName`** (input_control)  tuple `→` [HTuple](HTuple.md) (*string*)

I/O device name.

Default:
[]

**`genParamName`** (input_control)  string-array `→` [HTuple](HTuple.md) (*string*)

Dynamic parameter names.

Default:
[]

**`genParamValue`** (input_control)  string-array `→` [HTuple](HTuple.md) (*string* / int / long / double)

Dynamic parameter values.

Default:
[]

**`IODeviceHandle`** (output_control)  io_device `→` [HIODevice](HIODevice.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the opened I/O device.

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
`OpenIoDevice` returns the value 2 (
H_MSG_TRUE)
. If necessary an
exception is raised. In this case, an extended error information may be
set and can be queried with the operator [`GetExtendedErrorInfo`](get_extended_error_info.md).

## Possible Predecessors

`QueryIoInterface`

## Possible Successors

`SetIoDeviceParam`,
`GetIoDeviceParam`,
`OpenIoChannel`

## Module

Foundation
