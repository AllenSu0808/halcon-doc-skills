# open_compute_device (Operator)

## Name

`open_compute_device` — Open a compute device.

## Signature

`open_compute_device( : : DeviceIdentifier : DeviceHandle)`

## Description

`open_compute_device` opens the compute device referenced by
*`DeviceIdentifier`* and
returns *`DeviceHandle`*. Enable computation on
*`DeviceHandle`* via [`activate_compute_device`](activate_compute_device.md).

*`DeviceIdentifier`* must be obtained by
[`query_available_compute_devices`](query_available_compute_devices.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: local (may only be called from the same thread in which the window, model, or tool instance was created).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`DeviceIdentifier`** (input_control)  integer `→`  (integer)

Compute device Identifier.

**`DeviceHandle`** (output_control)  compute_device `→`  (handle)

Compute device handle.

## Result

`open_compute_device` returns the value
2 (
H_MSG_TRUE)
if *`DeviceIdentifier`* is valid. Otherwise
an exception will be raised.

## Possible Predecessors

`query_available_compute_devices`

## Possible Successors

`activate_compute_device`,
`init_compute_device`

## Module

Foundation
