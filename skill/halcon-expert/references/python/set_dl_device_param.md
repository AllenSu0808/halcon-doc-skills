# set_dl_device_param (Operator)

## Name

`set_dl_device_param` — Set the parameters of a deep-learning-capable hardware device.

## Signature

`def set_dl_device_param(dldevice_handle: HHandle, gen_param_name: MaybeSequence[str], gen_param_value: HTupleType) -> None`

## Description

`set_dl_device_param` sets the parameter values
*`gen_param_value`* for *`gen_param_name`* for the
deep-learning-capable hardware device (hereafter referred to as device)
*`dldevice_handle`*.
See [`query_available_dl_devices`](query_available_dl_devices.md) for details about deep-learning-capable
hardware devices.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`dldevice_handle`** (input_control)  dl_device `→` HHandle

Handle of the deep-learning-capable hardware device.

**`gen_param_name`** (input_control)  attribute.name(-array) `→` MaybeSequence[str]

Name of the generic parameter.

Default:
[]

List of values:
"settable_device_params"

**`gen_param_value`** (input_control)  attribute.name(-array) `→` HTupleType

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
