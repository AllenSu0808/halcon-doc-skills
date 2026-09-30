# GetIoDeviceParam (Operator)

## Name

`GetIoDeviceParam` — Query settings of an I/O device instance.

## Signature

`static void HOperatorSet.GetIoDeviceParam(HTuple IODeviceHandle, HTuple genParamName, out HTuple genParamValue)`

`HTuple HIODevice.GetIoDeviceParam(HTuple genParamName)`

`HTuple HIODevice.GetIoDeviceParam(string genParamName)`

## Description

`GetIoDeviceParam` queries configuration settings of a
specific device instance. The query parameters are passed in
*`genParamName`*, the corresponding configuration values are
returned in *`genParamValue`*. *`IODeviceHandle`* specifies
the device returned in [`OpenIoDevice`](open_io_device.md).

Please check the directory `doc/html/reference/io` for
documentation about your specific I/O device interface, where all
supported device specific parameters are listed.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`IODeviceHandle`** (input_control)  io_device `→` [HIODevice](HIODevice.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the opened I/O device.

**`genParamName`** (input_control)  attribute.name(-array) `→` [HTuple](HTuple.md) (*string*)

Parameter names.

Default:
"param_name"

Suggested values:
"io_device_name", "param_name"

**`genParamValue`** (output_control)  attribute.value(-array) `→` [HTuple](HTuple.md) (*string* / int / long / double / HHandle)

Parameter values.

## Result

If the parameters are valid, the operator
`GetIoDeviceParam` returns the value 2 (
H_MSG_TRUE)
. If necessary an
exception is raised. In this case, an extended error information may be
set and can be queried with the operator [`GetExtendedErrorInfo`](get_extended_error_info.md).

## Possible Predecessors

`OpenIoDevice`,
`SetIoDeviceParam`

## Possible Successors

`OpenIoChannel`

## See also

`OpenIoDevice`,
`QueryIoInterface`,
`SetIoDeviceParam`

## Module

Foundation
