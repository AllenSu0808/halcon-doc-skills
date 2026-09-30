# ActivateComputeDevice (Operator)

## Name

`ActivateComputeDevice` — Activate a compute device.

## Signature

`static void HOperatorSet.ActivateComputeDevice(HTuple deviceHandle)`

`void HComputeDevice.ActivateComputeDevice()`

## Description

`ActivateComputeDevice` activates the compute device
*`deviceHandle`* for the current HALCON thread.
All subsequent HALCON operators called in this thread are executed on
*`deviceHandle`* if they provide an implementation
(see [`GetOperatorInfo`](get_operator_info.md)) for this device.
Use [`DeactivateComputeDevice`](deactivate_compute_device.md) to deactivate
*`deviceHandle`*.

Currently, only one compute device can be active for a HALCON thread.
If a different device is active before `ActivateComputeDevice`
is called, this device is deactivated automatically.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: local (may only be called from the same thread in which the window, model, or tool instance was created).
- Processed without parallelization.

## Parameters

**`deviceHandle`** (input_control)  compute_device `→` [HComputeDevice](HComputeDevice.md), [HTuple](HTuple.md) (*IntPtr*)

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

`ActivateComputeDevice` returns the value
2 (
H_MSG_TRUE)
if *`deviceHandle`* is valid. Otherwise
an exception will be raised.

## Possible Predecessors

`OpenComputeDevice`

## See also

`DeactivateComputeDevice`,
`DeactivateAllComputeDevices`

## Module

Foundation
