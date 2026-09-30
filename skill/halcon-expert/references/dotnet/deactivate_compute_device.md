# DeactivateComputeDevice (Operator)

## Name

`DeactivateComputeDevice` — Deactivate a compute device.

## Signature

`static void HOperatorSet.DeactivateComputeDevice(HTuple deviceHandle)`

`void HComputeDevice.DeactivateComputeDevice()`

## Description

`DeactivateComputeDevice` deactivates the compute device
*`deviceHandle`* for the current HALCON thread. Use
[`ActivateComputeDevice`](activate_compute_device.md) to reactivate the device.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: local (may only be called from the same thread in which the window, model, or tool instance was created).
- Processed without parallelization.

## Parameters

**`deviceHandle`** (input_control)  compute_device `→` [HComputeDevice](HComputeDevice.md), [HTuple](HTuple.md) (*IntPtr*)

Compute device handle.

## Result

`DeactivateComputeDevice` returns the value
2 (
H_MSG_TRUE)
if *`deviceHandle`* is valid. Otherwise
an exception will be raised.

## Possible Predecessors

`ActivateComputeDevice`

## See also

`DeactivateAllComputeDevices`

## Module

Foundation
