# get_dl_device_param (Operator)

## Name

`get_dl_device_param` — Return the parameters of a deep-learning-capable hardware device.

## Signature

`get_dl_device_param( : : DLDeviceHandle, GenParamName : GenParamValue)`

## Description

`get_dl_device_param` returns the parameter values
*`GenParamValue`* of *`GenParamName`* for the
deep-learning-capable hardware device (hereafter referred to as device)
*`DLDeviceHandle`*.
See [`query_available_dl_devices`](query_available_dl_devices.md) for details about
deep-learning-capable hardware devices.

Supported values for *`GenParamName`* are:

- ***'calibration_precisions'*:** —

  Specifies the unit data types that can be used for a calibration
  of a deep learning model.

  List of values:
   *'int8'*.
- ***'cast_precisions'*:** —

  Specifies the unit data types that can be used for a cast of
  a deep learning model.

  When changing the data type the calibration does not require any images.

  List of values:
   *'bfloat16'*, *'float32'*, *'float16'*.
- ***'conversion_supported'*:** —

  Returns *'true'* if unit data types for either a calibration
  or a cast of a deep learning model are available. Returns
  *'false'* in any other case.
- ***'id'*:** —

  The ID of the device. Within each AI
  2-Interface, the
  IDs of its supported devices are unique. The same holds for devices
  supported through HALCON.
- ***'inference_only'*:** —

  Indicates if the device can only
  be used to infer deep learning models (*'true'*) or
  also supports training or gradient-based operations
  (*'false'*).
- ***'ai2'*:** —

  AI Accelerator Interface (AI
  2) on which this unit
  *`DLDeviceHandle`* is executed.
  In case the device is directly supported by HALCON,
  the value *'none'* is returned.

  List of values:
   *'tensorrt'*, *'openvino'*,
  *'none'*.
- ***'ai_accelerator_interface'*:** —

  warning

  *'ai_accelerator_interface'* is obsolete and is only provided for
  reasons of backward compatibility. New applications should use
  *'ai2'* instead.
- ***'info'*:** —

  Dictionary containing additional information
  on the device.

  Restriction:
   Only for devices that are supported via an
  AI2-interface.
- ***'name'*:** —

  Name of the device.
- ***'optimize_for_inference_params'*:** —

  Dictionary with default-defined conversion parameters for a
  calibration or cast operation of a deep learning model.
  The entries can be changed.

  In case no parameter applies to the set device, an empty dictionary is
  returned.

  Restriction:
   Only for devices that are supported via an
  AI2-interface.
- ***'precisions'*:** —

  Specifies the data types that the
  unit supports for the weights and/or activations of a
  deep-learning-based model.

  List of values:
   *'bfloat16'*, *'float32'*,
  *'float16'*, *'int8'*.
- ***'settable_device_params'*:** —

  Dictionary with settable device
  parameters.

  Restriction:
   Only for devices that are supported via an
  AI2-interface.
- ***'type'*:** —

  Type of the device.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`DLDeviceHandle`** (input_control)  dl_device `→`  (handle)

Handle of the deep-learning-capable hardware device.

**`GenParamName`** (input_control)  attribute.name `→`  (string)

Name of the generic parameter.

Default:
'type'

List of values:
'ai2', 'calibration_precisions', 'cast_precisions', 'conversion_supported', 'execution_provider', 'id', 'inference_only', 'info', 'name', 'optimize_for_inference_params', 'precisions', 'settable_device_params', 'type'

**`GenParamValue`** (output_control)  attribute.name(-array) `→`  (string / real / integer)

Value of the generic parameter.

## Result

If the parameters are valid, the operator `get_dl_device_param`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`query_available_dl_devices`

## Possible Successors

`set_dl_model_param`

## Module

Foundation
