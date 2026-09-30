# set_calib_data_observ_pose (Operator)

## Name

`set_calib_data_observ_pose` — Set observed calibration object poses in a calibration data model.

## Signature

`set_calib_data_observ_pose( : : CalibDataID, CameraIdx, CalibObjIdx, CalibObjPoseIdx, ObjInCameraPose : )`

## Description

For a calibration data model of type
`CalibSetup`=*'hand_eye_moving_cam'*,
*'hand_eye_stationary_cam'*, *'hand_eye_scara_moving_cam'*, or
*'hand_eye_scara_stationary_cam'* with no calibration object (see
[`create_calib_data`](create_calib_data.md)), the hand-eye calibration is based on so-called
observations of an arbitrary object in the camera coordinate system.
In the following this object will be called calibration object.
Additionally, the corresponding poses of the robot tool in the robot base
coordinate system must be known.
With `set_calib_data_observ_pose`, you store an
observation of the calibration object pose in the calibration data model
*`CalibDataID`*. An observation of the calibration object pose
consists of the following data:

- ***`CameraIdx`*:** —

  Index of the observing camera
- ***`CalibObjIdx`*:** —

  Index of the observed calibration object
- ***`CalibObjPoseIdx`*:** —

  Index of the observed pose of the
  calibration object. You can choose it freely, without following a strict
  order. If you specify an index that already exists for the calibration
  object *`CalibObjIdx`*, the corresponding observation data is
  replaced by the new one.
- ***`ObjInCameraPose`*:** —

  Pose of the observed calibration
  object relative to observing camera.

Note that, since the model *`CalibDataID`* uses a general
sensor and no calibration object (i.e., the model was created by
[`create_calib_data`](create_calib_data.md) with `NumCameras`=0 and
`NumCalibObjects`=0), both *`CameraIdx`* and
*`CalibObjIdx`* must be set to 0. If the model uses a camera
and an calibration object (i.e., `NumCameras`=1 and
`NumCalibObjects`=1), then [`find_calib_object`](find_calib_object.md) or
[`set_calib_data_observ_points`](set_calib_data_observ_points.md) must be used.

The observation pose data can be accessed later by calling
[`get_calib_data_observ_pose`](get_calib_data_observ_pose.md) using the same values for the
arguments *`CameraIdx`*, *`CalibObjIdx`*, and
*`CalibObjPoseIdx`*.

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

Suggested values:
0, 1, 2

**`CalibObjIdx`** (input_control)  number `→`  (integer)

Index of the calibration object.

Default:
0

Suggested values:
0, 1, 2

**`CalibObjPoseIdx`** (input_control)  number `→`  (integer)

Index of the observed calibration object.

Default:
0

Suggested values:
0, 1, 2

Restriction:
`CalibObjPoseIdx >= 0`

**`ObjInCameraPose`** (input_control)  pose `→`  (real / integer)

Pose of the observed calibration
object relative to the observing camera.

Number of elements:
7

## Possible Predecessors

`find_marks_and_pose`,
`set_calib_data_cam_param`,
`set_calib_data_calib_object`

## Possible Successors

`set_calib_data`,
`calibrate_cameras`

## Alternatives

`find_calib_object`

## Module

Calibration
