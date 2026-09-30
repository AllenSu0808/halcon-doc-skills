# SetIoDeviceParam (Operator)

## Name

`SetIoDeviceParam` — Configure a specific I/O device instance.

## Signature

`static void HOperatorSet.SetIoDeviceParam(HTuple IODeviceHandle, HTuple genParamName, HTuple genParamValue)`

`void HIODevice.SetIoDeviceParam(HTuple genParamName, HTuple genParamValue)`

`void HIODevice.SetIoDeviceParam(string genParamName, string genParamValue)`

## Description

`SetIoDeviceParam` (re)configures a specific device
instance. The configuration parameters are passed in
*`genParamName`*, the corresponding values are passed in
*`genParamValue`*. *`IODeviceHandle`* specifies the device
specified in [`OpenIoDevice`](open_io_device.md).

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
[]

**`genParamValue`** (input_control)  attribute.value(-array) `→` [HTuple](HTuple.md) (*string* / int / long / double / HHandle)

Parameter values to set.

Default:
[]

## Result

If the parameters are valid, the operator
`SetIoDeviceParam` returns the value 2 (
H_MSG_TRUE)
. If necessary an
exception is raised. In this case, an extended error information may be
set and can be queried with the operator [`GetExtendedErrorInfo`](get_extended_error_info.md).

## Possible Predecessors

`OpenIoDevice`

## Possible Successors

`OpenIoChannel`

## See also

`OpenIoDevice`,
`QueryIoInterface`,
`GetIoDeviceParam`

## Module

Foundation
