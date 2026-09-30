# DeactivateAllComputeDevices (Operator)

## Name

`DeactivateAllComputeDevices` — Deactivate all compute devices.

## Signature

`static void HOperatorSet.DeactivateAllComputeDevices()`

`static void HComputeDevice.DeactivateAllComputeDevices()`

## Description

`DeactivateAllComputeDevices` deactivates all compute devices
for the current HALCON thread.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Result

`DeactivateAllComputeDevices` returns the value
2 (
H_MSG_TRUE)
.

## See also

`ActivateComputeDevice`,
`DeactivateComputeDevice`

## Module

Foundation
