# SetCalibDataObservPose (Operator)

## Name

`SetCalibDataObservPose` — Set observed calibration object poses in a calibration data model.

## Signature

`static void HOperatorSet.SetCalibDataObservPose(HTuple calibDataID, HTuple cameraIdx, HTuple calibObjIdx, HTuple calibObjPoseIdx, HTuple objInCameraPose)`

`void HCalibData.SetCalibDataObservPose(int cameraIdx, int calibObjIdx, int calibObjPoseIdx, HPose objInCameraPose)`

## Description

For a calibration data model of type
`calibSetup`=*"hand_eye_moving_cam"*,
*"hand_eye_stationary_cam"*, *"hand_eye_scara_moving_cam"*, or
*"hand_eye_scara_stationary_cam"* with no calibration object (see
[`CreateCalibData`](create_calib_data.md)), the hand-eye calibration is based on so-called
observations of an arbitrary object in the camera coordinate system.
In the following this object will be called calibration object.
Additionally, the corresponding poses of the robot tool in the robot base
coordinate system must be known.
With `SetCalibDataObservPose`, you store an
observation of the calibration object pose in the calibration data model
*`calibDataID`*. An observation of the calibration object pose
consists of the following data:

- ***`cameraIdx`*:** —

  Index of the observing camera
- ***`calibObjIdx`*:** —

  Index of the observed calibration object
- ***`calibObjPoseIdx`*:** —

  Index of the observed pose of the
  calibration object. You can choose it freely, without following a strict
  order. If you specify an index that already exists for the calibration
  object *`calibObjIdx`*, the corresponding observation data is
  replaced by the new one.
- ***`objInCameraPose`*:** —

  Pose of the observed calibration
  object relative to observing camera.

Note that, since the model *`calibDataID`* uses a general
sensor and no calibration object (i.e., the model was created by
[`CreateCalibData`](create_calib_data.md) with `numCameras`=0 and
`numCalibObjects`=0), both *`cameraIdx`* and
*`calibObjIdx`* must be set to 0. If the model uses a camera
and an calibration object (i.e., `numCameras`=1 and
`numCalibObjects`=1), then [`FindCalibObject`](find_calib_object.md) or
[`SetCalibDataObservPoints`](set_calib_data_observ_points.md) must be used.

The observation pose data can be accessed later by calling
[`GetCalibDataObservPose`](get_calib_data_observ_pose.md) using the same values for the
arguments *`cameraIdx`*, *`calibObjIdx`*, and
*`calibObjPoseIdx`*.

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

**`cameraIdx`** (input_control)  number `→` [HTuple](HTuple.md) (*int* / long)

Index of the observing camera.

Default:
0

Suggested values:
0, 1, 2

**`calibObjIdx`** (input_control)  number `→` [HTuple](HTuple.md) (*int* / long)

Index of the calibration object.

Default:
0

Suggested values:
0, 1, 2

**`calibObjPoseIdx`** (input_control)  number `→` [HTuple](HTuple.md) (*int* / long)

Index of the observed calibration object.

Default:
0

Suggested values:
0, 1, 2

Restriction:
`CalibObjPoseIdx >= 0`

**`objInCameraPose`** (input_control)  pose `→` [HPose](HPose.md), [HTuple](HTuple.md) (*double* / int / long)

Pose of the observed calibration
object relative to the observing camera.

Number of elements:
7

## Possible Predecessors

`FindMarksAndPose`,
`SetCalibDataCamParam`,
`SetCalibDataCalibObject`

## Possible Successors

`SetCalibData`,
`CalibrateCameras`

## Alternatives

`FindCalibObject`

## Module

Calibration
