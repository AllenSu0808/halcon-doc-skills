# InitComputeDevice (Operator)

## Name

`InitComputeDevice` — Initialize a compute device.

## Signature

`static void HOperatorSet.InitComputeDevice(HTuple deviceHandle, HTuple operators)`

`void HComputeDevice.InitComputeDevice(HTuple operators)`

## Description

`InitComputeDevice` initializes a compute device and prepares a
list of operators given in *`operators`* for the execution on this
device. Further the device is activated for the current thread.
If `InitComputeDevice` is not called or operators other than
those in *`operators`* are used on the device, the initialization
is performed on demand.

Use [`GetOperatorInfo`](get_operator_info.md) to test if an operator qualifies for
execution on the compute device.

## Attention

Be aware that the execution time of `InitComputeDevice` depends
on the number of *`operators`* and may last up to several seconds.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: local (may only be called from the same thread in which the window, model, or tool instance was created).
- Processed without parallelization.

## Parameters

**`deviceHandle`** (input_control)  compute_device `→` [HComputeDevice](HComputeDevice.md), [HTuple](HTuple.md) (*IntPtr*)

Compute device handle.

**`operators`** (input_control)  string-array `→` [HTuple](HTuple.md) (*string*)

List of operators to prepare.

Default:
"all"

List of values:
"all", "derivate_gauss", "sobel_amp"

## Result

The operator `InitComputeDevice` returns the
value 2 (
H_MSG_TRUE)
if the initialization was successful. Otherwise
an exception will be raised.

## Possible Predecessors

`QueryAvailableComputeDevices`,
`OpenComputeDevice`

## Possible Successors

`ActivateComputeDevice`

## Module

Foundation
