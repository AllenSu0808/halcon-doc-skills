# ReadCalibData (Operator)

## Name

`ReadCalibData` — Restore a calibration data model from a file.

## Signature

`static void HOperatorSet.ReadCalibData(HTuple fileName, out HTuple calibDataID)`

`public HCalibData(string fileName)`

`void HCalibData.ReadCalibData(string fileName)`

## Description

The operator `ReadCalibData` restores a calibration data model from
a file specified by its *`fileName`* and returns a handle to the
restored model in *`calibDataID`*. The model file must have been
created by [`WriteCalibData`](write_calib_data.md).

Note that [`WriteCalibData`](write_calib_data.md) does not store any calibration results
into the file. Yet, [`CalibrateCameras`](calibrate_cameras.md) can be called for a
fully configured calibration model immediately after the reading. All
calibration results are accessible afterwards.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`fileName`** (input_control)  filename.read `→` [HTuple](HTuple.md) (*string*)

The path and file name of the model file.

File extension:
.`ccd`

**`calibDataID`** (output_control)  calib_data `→` [HCalibData](HCalibData.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of a calibration data model.

## Module

Calibration
