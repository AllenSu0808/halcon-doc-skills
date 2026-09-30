# QueryIoInterface (Operator)

## Name

`QueryIoInterface` — Query information about the specified I/O device interface.

## Signature

`static void HOperatorSet.QueryIoInterface(HTuple IOInterfaceName, HTuple query, out HTuple result)`

`static HTuple HIODevice.QueryIoInterface(string IOInterfaceName, HTuple query)`

`static HTuple HIODevice.QueryIoInterface(string IOInterfaceName, string query)`

## Description

The operator `QueryIoInterface` returns information about
the I/O device interface *`IOInterfaceName`*. The desired
information is specified via *`query`*. If applicable,
*`result`* contains a list of supported values.

Generally, when passing the value *"interface_name"* for
*`query`*, all available I/O interfaces are returned. The value
of the parameter *`IOInterfaceName`* is ignored in this case.

Please check the directory `doc/html/reference/io`
for documentation about your specific I/O device interface, where
all supported interface specific parameters are listed.

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

## Parameters

**`IOInterfaceName`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

HALCON I/O interface name.

Default:
[]

Suggested values:
"ADLINK-DAQPilot", "ADLINK-EOS", "Advantech", "Contec", "Hilscher-cifX", "Interface", "Linux-GPIO", "NIDAQmx", "OPC_Classic", "OPC_UA"

**`query`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Parameter name of the query.

Default:
"io_device_names"

Suggested values:
"interface_name", "io_device_names", "param_name", "revision"

**`result`** (output_control)  string-array `→` [HTuple](HTuple.md) (*string* / int / long / double)

List of result values (according to *`query`*).

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
`QueryIoInterface` returns the value 2 (
H_MSG_TRUE)
. If necessary an
exception is raised. In this case, an extended error information may be
set and can be queried with the operator [`GetExtendedErrorInfo`](get_extended_error_info.md).

## Possible Successors

`OpenIoDevice`

## Module

Foundation
