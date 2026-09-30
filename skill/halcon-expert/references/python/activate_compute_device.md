# activate_compute_device (Operator)

## Name

`activate_compute_device` — Activate a compute device.

## Signature

`def activate_compute_device(device_handle: HHandle) -> None`

## Description

`activate_compute_device` activates the compute device
*`device_handle`* for the current HALCON thread.
All subsequent HALCON operators called in this thread are executed on
*`device_handle`* if they provide an implementation
(see [`get_operator_info`](get_operator_info.md)) for this device.
Use [`deactivate_compute_device`](deactivate_compute_device.md) to deactivate
*`device_handle`*.

Currently, only one compute device can be active for a HALCON thread.
If a different device is active before `activate_compute_device`
is called, this device is deactivated automatically.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: local (may only be called from the same thread in which the window, model, or tool instance was created).
- Processed without parallelization.

## Parameters

**`device_handle`** (input_control)  compute_device `→` HHandle

Compute device handle.

## Example (HDevelop)

```
open_compute_device (DeviceIdentifier, DeviceHandle)
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

`activate_compute_device` returns the value
2 (
H_MSG_TRUE)
if *`device_handle`* is valid. Otherwise
an exception will be raised.

## Possible Predecessors

`open_compute_device`

## See also

`deactivate_compute_device`,
`deactivate_all_compute_devices`

## Module

Foundation
