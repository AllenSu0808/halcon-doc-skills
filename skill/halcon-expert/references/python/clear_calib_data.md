# clear_calib_data (Operator)

## Name

`clear_calib_data` — Free the memory of a calibration data model.

## Signature

`def clear_calib_data(calib_data_id: HHandle) -> None`

## Description

The operator `clear_calib_data` frees the memory of the
calibration data model *`calib_data_id`*. After calling
`clear_calib_data`, the model can no longer be used. The
handle *`calib_data_id`* becomes invalid.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- calib_data_id

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`calib_data_id`** (input_control, state is modified)  calib_data `→` HHandle

Handle of a calibration data model.

## Module

Calibration
