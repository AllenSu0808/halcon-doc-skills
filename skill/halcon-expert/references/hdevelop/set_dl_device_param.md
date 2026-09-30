# set_dl_device_param (Operator)

## Name

`set_dl_device_param` — Set the parameters of a deep-learning-capable hardware device.

## Signature

`set_dl_device_param( : : DLDeviceHandle, GenParamName, GenParamValue : )`

## Description

`set_dl_device_param` sets the parameter values
*`GenParamValue`* for *`GenParamName`* for the
deep-learning-capable hardware device (hereafter referred to as device)
*`DLDeviceHandle`*.
See [`query_available_dl_devices`](query_available_dl_devices.md) for details about deep-learning-capable
hardware devices.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`DLDeviceHandle`** (input_control)  dl_device `→`  (handle)

Handle of the deep-learning-capable hardware device.

**`GenParamName`** (input_control)  attribute.name(-array) `→`  (string)

Name of the generic parameter.

Default:
[]

List of values:
'settable_device_params'

**`GenParamValue`** (input_control)  attribute.name(-array) `→`  (string / real / integer / handle)

Value of the generic parameter.

## Result

If the parameters are valid, the operator `set_dl_device_param`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`query_available_dl_devices`

## Possible Successors

`set_dl_model_param`

## See also

`get_dl_device_param`

## Module

Foundation
