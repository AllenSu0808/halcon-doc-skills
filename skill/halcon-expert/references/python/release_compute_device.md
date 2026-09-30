# release_compute_device (Operator)

## Name

`release_compute_device` — Close a compute_device.

## Warning

**`release_compute_device` must not be used in HDevelop!**

## Signature

`def release_compute_device(device_handle: HHandle) -> None`

## Description

`release_compute_device` closes a compute devices for the current
HALCON thread and frees all resources associated to *`device_handle`*.
`release_compute_device` is solely for the purpose of freeing all
device related resources before unloading the HALCON library, if the
library was loaded using a mechanism like LoadLibrary or dlopen. In all
other cases you must not use `release_compute_device`!

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: local (may only be called from the same thread in which the window, model, or tool instance was created).
- Processed without parallelization.

## Parameters

**`device_handle`** (input_control)  compute_device `→` HHandle

Compute device handle.

## Result

`release_compute_device` returns the value 2 (
H_MSG_TRUE)
if *`device_handle`* was closed successfully. Otherwise
an exception will be raised.

## See also

`release_all_compute_devices`,
`deactivate_compute_device`,
`deactivate_all_compute_devices`

## Module

Foundation
