# read_calib_data (Operator)

## Name

`read_calib_data` — Restore a calibration data model from a file.

## Signature

`read_calib_data( : : FileName : CalibDataID)`

## Description

The operator `read_calib_data` restores a calibration data model from
a file specified by its *`FileName`* and returns a handle to the
restored model in *`CalibDataID`*. The model file must have been
created by [`write_calib_data`](write_calib_data.md).

Note that [`write_calib_data`](write_calib_data.md) does not store any calibration results
into the file. Yet, [`calibrate_cameras`](calibrate_cameras.md) can be called for a
fully configured calibration model immediately after the reading. All
calibration results are accessible afterwards.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`FileName`** (input_control)  filename.read `→`  (string)

The path and file name of the model file.

File extension:
.`ccd`

**`CalibDataID`** (output_control)  calib_data `→`  (handle)

Handle of a calibration data model.

## Module

Calibration
