# write_calib_data (Operator)

## Name

`write_calib_data` — Store a calibration data model into a file.

## Signature

`def write_calib_data(calib_data_id: HHandle, file_name: str) -> None`

## Description

The operator `write_calib_data` stores a calibration data model
*`calib_data_id`* into a file specified by its file name
*`file_name`*. The information stored in the file includes:

- initial camera parameters
- calibration object descriptions
- observation data
- model settings: generic and specific optimization
  parameters for both cameras and calibration object poses.

Note that no calibration results are stored in the file. You can
access them with the operator [`get_calib_data`](get_calib_data.md), either as
individual items or in form of a camera setup model and
store them separately.

The calibration data model can be later read with [`read_calib_data`](read_calib_data.md).

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

**`file_name`** (input_control)  filename.write `→` str

The file name of the model to be saved.

File extension:
.`ccd`

## Module

Calibration
