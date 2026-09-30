# get_compute_device_info (Operator)

## Name

`get_compute_device_info` — Get information on a compute device.

## Signature

`def get_compute_device_info(device_identifier: int, info_name: str) -> Sequence[Union[str, int, float]]`

`def get_compute_device_info_s(device_identifier: int, info_name: str) -> Union[str, int, float]`

## Description

The operator `get_compute_device_info` returns information on a
compute device. In contrast to [`get_compute_device_param`](get_compute_device_param.md), only
static information is queried, so that the device does not have to
be opened (see [`open_compute_device`](open_compute_device.md)) and activated
(see [`activate_compute_device`](activate_compute_device.md)).

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

**`device_identifier`** (input_control)  integer `→` int

Compute device handle.

**`info_name`** (input_control)  string `→` str

Name of Information to query.

Default:
"name"

List of values:
"driver_version", "extensions", "image2d_max_height", "image2d_max_width", "image_support", "max_mem_alloc_size", "name", "platform_version", "vendor"

**`info`** (output_control)  string(-array) `→` Sequence[Union[str, int, float]]

Returned information.

## Result

The operator `get_compute_device_info` returns the
value 2 (
H_MSG_TRUE)
if the parameters are correct. Otherwise
an exception will be raised.

## Possible Predecessors

`query_available_compute_devices`

## Possible Successors

`activate_compute_device`

## Module

Foundation
