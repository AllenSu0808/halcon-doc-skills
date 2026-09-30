# deactivate_all_compute_devices (Operator)

## Name

`deactivate_all_compute_devices` — Deactivate all compute devices.

## Signature

`deactivate_all_compute_devices( : : : )`

## Description

`deactivate_all_compute_devices` deactivates all compute devices
for the current HALCON thread.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Result

`deactivate_all_compute_devices` returns the value
2 (
H_MSG_TRUE)
.

## See also

`activate_compute_device`,
`deactivate_compute_device`

## Module

Foundation
