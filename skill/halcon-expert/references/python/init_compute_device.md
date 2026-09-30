# init_compute_device (Operator)

## Name

`init_compute_device` — Initialize a compute device.

## Signature

`def init_compute_device(device_handle: HHandle, operators: Sequence[str]) -> None`

## Description

`init_compute_device` initializes a compute device and prepares a
list of operators given in *`operators`* for the execution on this
device. Further the device is activated for the current thread.
If `init_compute_device` is not called or operators other than
those in *`operators`* are used on the device, the initialization
is performed on demand.

Use [`get_operator_info`](get_operator_info.md) to test if an operator qualifies for
execution on the compute device.

## Attention

Be aware that the execution time of `init_compute_device` depends
on the number of *`operators`* and may last up to several seconds.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: local (may only be called from the same thread in which the window, model, or tool instance was created).
- Processed without parallelization.

## Parameters

**`device_handle`** (input_control)  compute_device `→` HHandle

Compute device handle.

**`operators`** (input_control)  string-array `→` Sequence[str]

List of operators to prepare.

Default:
"all"

List of values:
"all", "derivate_gauss", "sobel_amp"

## Result

The operator `init_compute_device` returns the
value 2 (
H_MSG_TRUE)
if the initialization was successful. Otherwise
an exception will be raised.

## Possible Predecessors

`query_available_compute_devices`,
`open_compute_device`

## Possible Successors

`activate_compute_device`

## Module

Foundation
