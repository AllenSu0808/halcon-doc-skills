# remove_calib_data_observ (Operator)

## Name

`remove_calib_data_observ` — Remove observation data from a calibration data model.

## Signature

`remove_calib_data_observ( : : CalibDataID, CameraIdx, CalibObjIdx, CalibObjPoseIdx : )`

## Description

The operator `remove_calib_data_observ` removes observations that were
set in a calibration data model *`CalibDataID`* using
[`find_calib_object`](find_calib_object.md), [`set_calib_data_observ_points`](set_calib_data_observ_points.md), or
[`set_calib_data_observ_pose`](set_calib_data_observ_pose.md). The parameters *`CameraIdx`*,
*`CalibObjIdx`*, and *`CalibObjPoseIdx`* should specify a valid
observation from the calibration model.
Note that if the calibration data model *`CalibDataID`* is used
in [`calibrate_hand_eye`](calibrate_hand_eye.md), the corresponding tool pose also has to
be deleted using [`remove_calib_data`](remove_calib_data.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- CalibDataID

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`CalibDataID`** (input_control, state is modified)  calib_data `→`  (handle)

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

## Possible Predecessors

`find_calib_object`,
`set_calib_data_observ_points`,
`set_calib_data_observ_pose`

## Possible Successors

`remove_calib_data`,
`calibrate_cameras`,
`calibrate_hand_eye`

## Module

Calibration
