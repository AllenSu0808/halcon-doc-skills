# WriteCalibData (Operator)

## Name

`WriteCalibData` — Store a calibration data model into a file.

## Signature

`static void HOperatorSet.WriteCalibData(HTuple calibDataID, HTuple fileName)`

`void HCalibData.WriteCalibData(string fileName)`

## Description

The operator `WriteCalibData` stores a calibration data model
*`calibDataID`* into a file specified by its file name
*`fileName`*. The information stored in the file includes:

- initial camera parameters
- calibration object descriptions
- observation data
- model settings: generic and specific optimization
  parameters for both cameras and calibration object poses.

Note that no calibration results are stored in the file. You can
access them with the operator [`GetCalibData`](get_calib_data.md), either as
individual items or in form of a camera setup model and
store them separately.

The calibration data model can be later read with [`ReadCalibData`](read_calib_data.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- calibDataID

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`calibDataID`** (input_control, state is modified)  calib_data `→` [HCalibData](HCalibData.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of a calibration data model.

**`fileName`** (input_control)  filename.write `→` [HTuple](HTuple.md) (*string*)

The file name of the model to be saved.

File extension:
.`ccd`

## Module

Calibration
