# GetComputeDeviceParam (Operator)

## Name

`GetComputeDeviceParam` — Query compute device parameters.

## Signature

`static void HOperatorSet.GetComputeDeviceParam(HTuple deviceHandle, HTuple genParamName, out HTuple genParamValue)`

`HTuple HComputeDevice.GetComputeDeviceParam(string genParamName)`

## Description

`GetComputeDeviceParam` returns parameters of the
compute device *`deviceHandle`* for the current HALCON thread
in *`genParamValue`*.

The following parameters can be queried (for more information
see [`SetComputeDeviceParam`](set_compute_device_param.md)) by setting them for
*`genParamName`*:

- ***"alloc_pinned"*** —

  If *"true"*, the output image matrices of all operators
  are created in page locked (so called 'pinned') memory.
- ***"asynchronous_execution"*** —

  If *"true"*, operators executed on the compute device
  do not wait for the device computations to finish but
  return after initiation the computations.
- ***"buffer_cache_capacity"*** —

  Maximum size (in bytes) of the compute device buffer cache.
- ***"buffer_cache_used"*** —

  Current size (in bytes) of the compute device buffer cache.
- ***"image_cache_capacity"*** —

  Maximum size (in bytes) of the compute device image cache.
- ***"image_cache_used"*** —

  Current size (in bytes) of the compute device image cache.
- ***"pinned_mem_cache_capacity"*** —

  Maximum size (in bytes) of the page locked (pinned) memory
  cache.
- ***"pinned_mem_cache_used"*** —

  Current size (in bytes) of the page locked (pinned) memory
  cache.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: local (may only be called from the same thread in which the window, model, or tool instance was created).
- Processed without parallelization.

## Parameters

**`deviceHandle`** (input_control)  compute_device `→` [HComputeDevice](HComputeDevice.md), [HTuple](HTuple.md) (*IntPtr*)

Compute device handle.

**`genParamName`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Name of the parameter to query.

Default:
"buffer_cache_capacity"

List of values:
"alloc_pinned", "asynchronous_execution", "buffer_cache_capacity", "buffer_cache_used", "image_cache_capacity", "image_cache_used", "pinned_mem_cache_capacity", "pinned_mem_cache_used"

**`genParamValue`** (output_control)  string(-array) `→` [HTuple](HTuple.md) (*string* / int / long / double)

Value of the parameter.

## Result

The operator `GetComputeDeviceParam` returns the
value 2 (
H_MSG_TRUE)
if the parameters are correct. Otherwise
an exception will be raised.

## Possible Predecessors

`ActivateComputeDevice`

## See also

`SetComputeDeviceParam`,
`GetComputeDeviceInfo`

## Module

Foundation
