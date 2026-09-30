# ReleaseComputeDevice (Operator)

## Name

`ReleaseComputeDevice` — Close a compute_device.

## Warning

**`ReleaseComputeDevice` must not be used in HDevelop!**

## Signature

`static void HOperatorSet.ReleaseComputeDevice(HTuple deviceHandle)`

`void HComputeDevice.ReleaseComputeDevice()`

## Description

`ReleaseComputeDevice` closes a compute devices for the current
HALCON thread and frees all resources associated to *`deviceHandle`*.
`ReleaseComputeDevice` is solely for the purpose of freeing all
device related resources before unloading the HALCON library, if the
library was loaded using a mechanism like LoadLibrary or dlopen. In all
other cases you must not use `ReleaseComputeDevice`!

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: local (may only be called from the same thread in which the window, model, or tool instance was created).
- Processed without parallelization.

## Parameters

**`deviceHandle`** (input_control)  compute_device `→` [HComputeDevice](HComputeDevice.md), [HTuple](HTuple.md) (*IntPtr*)

Compute device handle.

## Result

`ReleaseComputeDevice` returns the value 2 (
H_MSG_TRUE)
if *`deviceHandle`* was closed successfully. Otherwise
an exception will be raised.

## See also

`ReleaseAllComputeDevices`,
`DeactivateComputeDevice`,
`DeactivateAllComputeDevices`

## Module

Foundation
