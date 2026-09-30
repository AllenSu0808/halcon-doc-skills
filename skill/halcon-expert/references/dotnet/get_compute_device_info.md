# GetComputeDeviceInfo (Operator)

## Name

`GetComputeDeviceInfo` — Get information on a compute device.

## Signature

`static void HOperatorSet.GetComputeDeviceInfo(HTuple deviceIdentifier, HTuple infoName, out HTuple info)`

`static HTuple HComputeDevice.GetComputeDeviceInfo(int deviceIdentifier, string infoName)`

## Description

The operator `GetComputeDeviceInfo` returns information on a
compute device. In contrast to [`GetComputeDeviceParam`](get_compute_device_param.md), only
static information is queried, so that the device does not have to
be opened (see [`OpenComputeDevice`](open_compute_device.md)) and activated
(see [`ActivateComputeDevice`](activate_compute_device.md)).

The following information can be queried:

- **'vendor'** —

  Vendor of the compute device.
- **'name'** —

  Name of the compute device.
- **'platform_version'** —

  Version of the compute device platform. E.g., OpenCL version
  in the case of OpenCL devices.
- **'driver_version'** —

  Version of the device driver.
- **'extensions'** —

  Supported OpenCL extensions.
- **'image_support'** —

  *"true"* if the device supports image objects.
- **'image2d_max_width'** —

  Maximum width of OpenCL image objects.
- **'image2d_max_height'** —

  Maximum height of OpenCL image objects.
- **'max_mem_alloc_size'** —

  Maximum size (in bytes) of an OpenCL memory block.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`deviceIdentifier`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Compute device handle.

**`infoName`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Name of Information to query.

Default:
"name"

List of values:
"driver_version", "extensions", "image2d_max_height", "image2d_max_width", "image_support", "max_mem_alloc_size", "name", "platform_version", "vendor"

**`info`** (output_control)  string(-array) `→` [HTuple](HTuple.md) (*string* / int / long / double)

Returned information.

## Result

The operator `GetComputeDeviceInfo` returns the
value 2 (
H_MSG_TRUE)
if the parameters are correct. Otherwise
an exception will be raised.

## Possible Predecessors

`QueryAvailableComputeDevices`

## Possible Successors

`ActivateComputeDevice`

## Module

Foundation
