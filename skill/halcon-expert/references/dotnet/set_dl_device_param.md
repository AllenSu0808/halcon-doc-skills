# SetDlDeviceParam (Operator)

## Name

`SetDlDeviceParam` — Set the parameters of a deep-learning-capable hardware device.

## Signature

`static void HOperatorSet.SetDlDeviceParam(HTuple DLDeviceHandle, HTuple genParamName, HTuple genParamValue)`

`void HDlDevice.SetDlDeviceParam(HTuple genParamName, HTuple genParamValue)`

`void HDlDevice.SetDlDeviceParam(string genParamName, string genParamValue)`

## Description

`SetDlDeviceParam` sets the parameter values
*`genParamValue`* for *`genParamName`* for the
deep-learning-capable hardware device (hereafter referred to as device)
*`DLDeviceHandle`*.
See [`QueryAvailableDlDevices`](query_available_dl_devices.md) for details about deep-learning-capable
hardware devices.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`DLDeviceHandle`** (input_control)  dl_device `→` [HDlDevice](HDlDevice.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the deep-learning-capable hardware device.

**`genParamName`** (input_control)  attribute.name(-array) `→` [HTuple](HTuple.md) (*string*)

Name of the generic parameter.

Default:
[]

List of values:
"settable_device_params"

**`genParamValue`** (input_control)  attribute.name(-array) `→` [HTuple](HTuple.md) (*string* / double / int / long / HHandle)

Value of the generic parameter.

## Result

If the parameters are valid, the operator `SetDlDeviceParam`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`QueryAvailableDlDevices`

## Possible Successors

`SetDlModelParam`

## See also

`GetDlDeviceParam`

## Module

Foundation
