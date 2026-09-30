# deactivate_compute_device (Operator)

## Name

`deactivate_compute_device` — Deactivate a compute device.

## Signature

`deactivate_compute_device( : : DeviceHandle : )`

## Description

`deactivate_compute_device` deactivates the compute device
*`DeviceHandle`* for the current HALCON thread. Use
[`activate_compute_device`](activate_compute_device.md) to reactivate the device.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: local (may only be called from the same thread in which the window, model, or tool instance was created).
- Processed without parallelization.

## Parameters

**`DeviceHandle`** (input_control)  compute_device `→`  (handle)

Compute device handle.

## Result

`deactivate_compute_device` returns the value
2 (
H_MSG_TRUE)
if *`DeviceHandle`* is valid. Otherwise
an exception will be raised.

## Possible Predecessors

`activate_compute_device`

## See also

`deactivate_all_compute_devices`

## Module

Foundation
