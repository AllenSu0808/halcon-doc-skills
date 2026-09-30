# QueryAvailableDlDevices (Operator)

## Name

`QueryAvailableDlDevices` — Get list of deep-learning-capable hardware devices.

## Signature

`static void HOperatorSet.QueryAvailableDlDevices(HTuple genParamName, HTuple genParamValue, out HTuple DLDeviceHandles)`

`static HDlDevice[] HDlDevice.QueryAvailableDlDevices(HTuple genParamName, HTuple genParamValue)`

`void HDlDevice.QueryAvailableDlDevices(string genParamName, string genParamValue)`

## Description

`QueryAvailableDlDevices` returns a list of handles. Each
handle refers to a deep-learning-capable hardware device
(hereafter referred to as device) that can be
used for inference or training of a deep learning model. For each
returned device, every parameter mentioned in *`genParamName`*
must be equal to at least one of its corresponding values that appear
in *`genParamValue`*. A parameter can have more than one value
by duplicating its name in *`genParamName`* and adding different
corresponding value in *`genParamValue`*.

A deep-learning-capable device is either supported directly
through HALCON or through an AI
2-interface.

The devices that are supported directly through HALCON are equivalent
to those that can be set to a deep learning model via
[`SetDlModelParam`](set_dl_model_param.md) using *"runtime"* = *"cpu"* or
*"runtime"* = *"gpu"*. HALCON provides an internal
implementation for the inference or training of a deep learning model
for those devices. See [Deep Learning](toc_deeplearning.md) for more details.

Devices that are supported through the AI
2-interface
can also be set to a deep learning model using [`SetDlModelParam`](set_dl_model_param.md).
In this case the inference is not executed by HALCON but by the device
itself.

`QueryAvailableDlDevices` returns a handle for each
deep-learning-capable device supported through HALCON and through an
AI
2-interface.

If a device is supported through HALCON and one or several AI
2-interfaces
, `QueryAvailableDlDevices` returns a handle for HALCON and for
each AI
2-interface.

*`genParamName`* can be used to filter for the devices.
All *`genParamName`* that are gettable by [`GetDlDeviceParam`](get_dl_device_param.md)
and that do not return a handle-typed value for *`genParamValue`*
are supported for filtering. See the operator reference of
[`GetDlDeviceParam`](get_dl_device_param.md) for the list of gettable parameters.
In addition, the following values are supported:

- ***"runtime"*:** —

  The devices, which are directly supported by
  HALCON for this device type.

  List of values:
   *"cpu"*, *"gpu"*.

*`genParamName`* can have multiple entries for the same value.
In this case filter combines the entries with a logical *'or'*.
Please see the example code below for some examples how to use the
filter.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`genParamName`** (input_control)  attribute.name(-array) `→` [HTuple](HTuple.md) (*string*)

Name of the generic parameter.

Default:
[]

List of values:
"ai2", "calibration_precisions", "cast_precisions", "conversion_supported", "id", "inference_only", "name", "optimize_for_inference_params", "precisions", "runtime", "settable_device_params", "type"

**`genParamValue`** (input_control)  attribute.value(-array) `→` [HTuple](HTuple.md) (*string* / int / long / double)

Value of the generic parameter.

Default:
[]

Suggested values:

**`DLDeviceHandles`** (output_control)  dl_device(-array) `→` [HDlDevice](HDlDevice.md), [HTuple](HTuple.md) (*IntPtr*)

Tuple of DLDevice handles

## Example (HDevelop)

```
* Query all deep-learning-capable hardware devices
query_available_dl_devices ([], [], DLDeviceHandles)

* Query all GPUs with ID 0 or 2
query_available_dl_devices (['type', 'id', 'id'], ['gpu', 0, 2],\
                            DLDeviceHandles)

* Query the unique GPU with ID 1 supported by HALCON
query_available_dl_devices (['runtime', 'id'], ['gpu', 1], DLDeviceHandles)
```

## Result

If the parameters are valid, the operator
`QueryAvailableDlDevices` returns the value 2 (
H_MSG_TRUE)
.
If necessary, an exception is raised.

## Possible Successors

`GetDlDeviceParam`

## Module

Foundation
