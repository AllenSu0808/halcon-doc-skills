# OpenComputeDevice (Operator)

## Name

`OpenComputeDevice` — Open a compute device.

## Signature

`static void HOperatorSet.OpenComputeDevice(HTuple deviceIdentifier, out HTuple deviceHandle)`

`public HComputeDevice(int deviceIdentifier)`

`void HComputeDevice.OpenComputeDevice(int deviceIdentifier)`

## Description

`OpenComputeDevice` opens the compute device referenced by
*`deviceIdentifier`* and
returns *`deviceHandle`*. Enable computation on
*`deviceHandle`* via [`ActivateComputeDevice`](activate_compute_device.md).

*`deviceIdentifier`* must be obtained by
[`QueryAvailableComputeDevices`](query_available_compute_devices.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: local (may only be called from the same thread in which the window, model, or tool instance was created).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`deviceIdentifier`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Compute device Identifier.

**`deviceHandle`** (output_control)  compute_device `→` [HComputeDevice](HComputeDevice.md), [HTuple](HTuple.md) (*IntPtr*)

Compute device handle.

## Result

`OpenComputeDevice` returns the value
2 (
H_MSG_TRUE)
if *`deviceIdentifier`* is valid. Otherwise
an exception will be raised.

## Possible Predecessors

`QueryAvailableComputeDevices`

## Possible Successors

`ActivateComputeDevice`,
`InitComputeDevice`

## Module

Foundation
