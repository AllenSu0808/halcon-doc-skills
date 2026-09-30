# SetComputeDeviceParam (Operator)

## Name

`SetComputeDeviceParam` — Set parameters of an compute device.

## Signature

`static void HOperatorSet.SetComputeDeviceParam(HTuple deviceHandle, HTuple genParamName, HTuple genParamValue)`

`void HComputeDevice.SetComputeDeviceParam(string genParamName, HTuple genParamValue)`

`void HComputeDevice.SetComputeDeviceParam(string genParamName, string genParamValue)`

## Description

`SetComputeDeviceParam` sets parameters of the
compute device *`deviceHandle`* for the current HALCON thread.

The following parameters can be set:

- ***"alloc_pinned"*** —

  If *"true"*, the output image matrices of all operators
  (executed on the compute device or not) called in the
  current HALCON thread are created in page locked
  (so called 'pinned') memory.
  This accelerates the transfer between host and device
  memory. However, too excessive usage of page locked memory
  may have a negative impact on overall system performance.
  You should activate page locked memory allocation if
  the output image of of the next operator call is to be
  transferred to the device.
  Page locked memory allocation should be deactivated for
  all operator calls whose output images are not required
  on the compute device (see example).

  List of values:
   *"true"*, *"false"*.

  Default:
   *"true"*.
- ***"asynchronous_execution"*** —

  If *"true"*, operators executed on the compute device
  do not wait for the device computations to finish but
  return after initiating the computations.
  All device computations are synchronized as soon as
  the output of a compute device operation is used on
  the CPU (e.g., by [`DispImage`](disp_image.md)).

  List of values:
   *"true"*, *"false"*.

  Default:
   *"true"*.
- ***"buffer_cache_capacity"*** —

  Maximum size (in bytes) of the compute device buffer
  cache.

  Default:
   1/3 of the available device memory
- ***"image_cache_capacity"*** —

  Maximum size (in bytes) of the compute device image
  cache.

  Default:
   1/3 of the available device memory
- ***"pinned_mem_cache_capacity"*** —

  Maximum size (in bytes) of the page locked (pinned) memory
  cache.

  Default:
   *32000000* (32MByte)

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: local (may only be called from the same thread in which the window, model, or tool instance was created).
- Processed without parallelization.

## Parameters

**`deviceHandle`** (input_control)  compute_device `→` [HComputeDevice](HComputeDevice.md), [HTuple](HTuple.md) (*IntPtr*)

Compute device handle.

**`genParamName`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Name of the parameter to set.

Default:
"buffer_cache_capacity"

List of values:
"alloc_pinned", "asynchronous_execution", "buffer_cache_capacity", "image_cache_capacity", "pinned_mem_cache_capacity"

**`genParamValue`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string* / int / long / double)

New parameter value.

## Example (HDevelop)

```
activate_compute_device (DeviceHandle)
read_image (Image, 'fuse')
set_compute_device_param (DeviceHandle, 'alloc_pinned', 'true')
* filter on compute device, output image is page locked
derivate_gauss (Image, DerivGauss, 3, 'gradient')
* filter result on the CPU, output image should not be page locked
set_compute_device_param (DeviceHandle, 'alloc_pinned', 'false')
median_image (DerivGauss, ImageMedian, 'circle', 1, 'mirrored')
```

## Result

The operator `SetComputeDeviceParam` returns the
value 2 (
H_MSG_TRUE)
if the parameters are correct. Otherwise
an exception will be raised.

## Possible Predecessors

`ActivateComputeDevice`

## See also

`GetComputeDeviceParam`

## Module

Foundation
