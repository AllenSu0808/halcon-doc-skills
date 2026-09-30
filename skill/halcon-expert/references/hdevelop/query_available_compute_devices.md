# query_available_compute_devices (Operator)

## Name

`query_available_compute_devices` — Get the list of available compute devices.

## Signature

`query_available_compute_devices( : : : DeviceIdentifier)`

## Description

Returns the list of available compute devices. Use
[`get_compute_device_info`](get_compute_device_info.md) to query information on a specific device.
Use [`open_compute_device`](open_compute_device.md) to open a device in HALCON.

At present, HALCON only supports OpenCL compatible GPUs supporting the
OpenCL extension cl_khr_byte_addressable_store and image objects. If you
are not sure whether a certain device is supported, please
refer to the manufacturer.

Be aware that currently it is not possible to use OpenCL via the
Windows Remote Desktop, because Windows Remote Desktop does not allow
access to the graphics driver.
You may use a VNC solution to use OpenCL on a remote computer. Of course
you can use OpenCL via ssh on a Linux machine.

It is recommended to install the latest graphics drivers available for
your GPU. To access the GPU on a Linux system you should be member of the
'video' group.

## Execution Information

- Multithreading type: mutually exclusive (runs in parallel with other non-exclusive operators, but not with itself).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`DeviceIdentifier`** (output_control)  integer-array `→`  (integer)

List of available compute devices.

## Example (HDevelop)

```
query_available_compute_devices (DeviceIdentifiers)
for Index := 0 to |DeviceIdentifiers|-1 by 1
  get_compute_device_info (DeviceIdentifiers[Index], 'name', DeviceName)
  get_compute_device_info (DeviceIdentifiers[Index], 'vendor', DeviceVendor)
  if (DeviceVendor == 'NVIDIA Corporation' and \
    DeviceName == 'GeForce 8800 Ultra')
    open_compute_device (DeviceIdentifiers[Index], DeviceHandle)
    break
  endif
endfor
*
init_compute_device (DeviceHandle, 'derivate_gauss')
read_image (Image, 'rings_and_nuts')
*
* Gaussian convolution on a compute device
activate_compute_device (DeviceHandle)
derivate_gauss (Image, DerivGauss, 5, 'none')
*
* Gaussian convolution on the CPU
deactivate_compute_device (DeviceHandle)
derivate_gauss (Image, DerivGauss, 5, 'none')
```

## Result

`query_available_compute_devices` returns the value 2 (
H_MSG_TRUE)
.

## Possible Successors

`get_compute_device_info`,
`open_compute_device`

## Module

Foundation
