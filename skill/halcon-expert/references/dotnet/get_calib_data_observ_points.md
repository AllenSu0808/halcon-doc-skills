# GetCalibDataObservPoints (Operator)

## Name

`GetCalibDataObservPoints` — Get point-based observation data from a calibration data model.

## Signature

`static void HOperatorSet.GetCalibDataObservPoints(HTuple calibDataID, HTuple cameraIdx, HTuple calibObjIdx, HTuple calibObjPoseIdx, out HTuple row, out HTuple column, out HTuple index, out HTuple pose)`

`void HCalibData.GetCalibDataObservPoints(int cameraIdx, int calibObjIdx, int calibObjPoseIdx, out HTuple row, out HTuple column, out HTuple index, out HTuple pose)`

## Description

The operator `GetCalibDataObservPoints` reads point-based
observation data from a calibration data model *`calibDataID`*. This
operator reads back observation data stored by
[`SetCalibDataObservPoints`](set_calib_data_observ_points.md) or [`FindCalibObject`](find_calib_object.md). See
[`SetCalibDataObservPoints`](set_calib_data_observ_points.md) for a detailed description of the
arguments.

Please note that if [`SetCalibDataObservPoints`](set_calib_data_observ_points.md) is used for
the calibration, the returned values of *`row`* and
*`column`* are the original values that have been set with
[`SetCalibDataObservPoints`](set_calib_data_observ_points.md). Similarly, if
[`FindCalibObject`](find_calib_object.md) is used for the extraction, the values of
*`row`* and *`column`* returned by
`GetCalibDataObservPoints` coincide with the coordinates
of the detected points computed by [`FindCalibObject`](find_calib_object.md).

Note that `GetCalibDataObservPoints` returns the pose of
an uncalibrated model. To get the pose of a calibrated model, use
[`GetCalibData`](get_calib_data.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`calibDataID`** (input_control)  calib_data `→` [HCalibData](HCalibData.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of a calibration data model.

**`cameraIdx`** (input_control)  number `→` [HTuple](HTuple.md) (*int* / long)

Index of the observing camera.

Default:
0

**`calibObjIdx`** (input_control)  number `→` [HTuple](HTuple.md) (*int* / long)

Index of the observed calibration object.

Default:
0

**`calibObjPoseIdx`** (input_control)  number `→` [HTuple](HTuple.md) (*int* / long)

Index of the observed calibration object pose.

Default:
0

**`row`** (output_control)  number-array `→` [HTuple](HTuple.md) (*double* / int / long)

Row coordinates of the detected points.

**`column`** (output_control)  number-array `→` [HTuple](HTuple.md) (*double* / int / long)

Column coordinates of the detected points.

**`index`** (output_control)  number-array `→` [HTuple](HTuple.md) (*int* / long / double)

Correspondence of the detected points to the
points of the observed calibration object.

**`pose`** (output_control)  number-array `→` [HTuple](HTuple.md) (*double* / int / long)

Roughly estimated pose of the observed calibration
object relative to the observing camera.

Number of elements:
7

## Module

Calibration
