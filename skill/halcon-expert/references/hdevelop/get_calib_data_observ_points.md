# get_calib_data_observ_points (Operator)

## Name

`get_calib_data_observ_points` — Get point-based observation data from a calibration data model.

## Signature

`get_calib_data_observ_points( : : CalibDataID, CameraIdx, CalibObjIdx, CalibObjPoseIdx : Row, Column, Index, Pose)`

## Description

The operator `get_calib_data_observ_points` reads point-based
observation data from a calibration data model *`CalibDataID`*. This
operator reads back observation data stored by
[`set_calib_data_observ_points`](set_calib_data_observ_points.md) or [`find_calib_object`](find_calib_object.md). See
[`set_calib_data_observ_points`](set_calib_data_observ_points.md) for a detailed description of the
arguments.

Please note that if [`set_calib_data_observ_points`](set_calib_data_observ_points.md) is used for
the calibration, the returned values of *`Row`* and
*`Column`* are the original values that have been set with
[`set_calib_data_observ_points`](set_calib_data_observ_points.md). Similarly, if
[`find_calib_object`](find_calib_object.md) is used for the extraction, the values of
*`Row`* and *`Column`* returned by
`get_calib_data_observ_points` coincide with the coordinates
of the detected points computed by [`find_calib_object`](find_calib_object.md).

Note that `get_calib_data_observ_points` returns the pose of
an uncalibrated model. To get the pose of a calibrated model, use
[`get_calib_data`](get_calib_data.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`CalibDataID`** (input_control)  calib_data `→`  (handle)

Handle of a calibration data model.

**`CameraIdx`** (input_control)  number `→`  (integer)

Index of the observing camera.

Default:
0

**`CalibObjIdx`** (input_control)  number `→`  (integer)

Index of the observed calibration object.

Default:
0

**`CalibObjPoseIdx`** (input_control)  number `→`  (integer)

Index of the observed calibration object pose.

Default:
0

**`Row`** (output_control)  number-array `→`  (real / integer)

Row coordinates of the detected points.

**`Column`** (output_control)  number-array `→`  (real / integer)

Column coordinates of the detected points.

**`Index`** (output_control)  number-array `→`  (integer / real)

Correspondence of the detected points to the
points of the observed calibration object.

**`Pose`** (output_control)  number-array `→`  (real / integer)

Roughly estimated pose of the observed calibration
object relative to the observing camera.

Number of elements:
7

## Module

Calibration
