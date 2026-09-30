# release_all_compute_devices (Operator)

## Name

`release_all_compute_devices` — Close all compute devices.

## Warning

**`release_all_compute_devices` must not be used in HDevelop!**

## Signature

`def release_all_compute_devices() -> None`

## Description

`release_all_compute_devices` closes all compute devices for the
current HALCON thread and frees all associated resources.
`release_all_compute_devices` is solely for the purpose of freeing
all device related resources before unloading the HALCON library, if the
library was loaded using a mechanism like LoadLibrary or dlopen. In all
other cases you must not use `release_all_compute_devices`.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Result

`release_all_compute_devices` returns the value 2 (
H_MSG_TRUE)
if all devices were closed successfully. Otherwise
an exception will be raised.

## See also

`release_compute_device`,
`deactivate_compute_device`,
`deactivate_all_compute_devices`

## Module

Foundation
