# ReleaseAllComputeDevices (Operator)

## Name

`ReleaseAllComputeDevices` — Close all compute devices.

## Warning

**`ReleaseAllComputeDevices` must not be used in HDevelop!**

## Signature

`static void HOperatorSet.ReleaseAllComputeDevices()`

`static void HComputeDevice.ReleaseAllComputeDevices()`

## Description

`ReleaseAllComputeDevices` closes all compute devices for the
current HALCON thread and frees all associated resources.
`ReleaseAllComputeDevices` is solely for the purpose of freeing
all device related resources before unloading the HALCON library, if the
library was loaded using a mechanism like LoadLibrary or dlopen. In all
other cases you must not use `ReleaseAllComputeDevices`.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Result

`ReleaseAllComputeDevices` returns the value 2 (
H_MSG_TRUE)
if all devices were closed successfully. Otherwise
an exception will be raised.

## See also

`ReleaseComputeDevice`,
`DeactivateComputeDevice`,
`DeactivateAllComputeDevices`

## Module

Foundation
