# set_calib_data_observ_pose (Operator)

## Name

`set_calib_data_observ_pose` — Set observed calibration object poses in a calibration data model.

## Signature

`def set_calib_data_observ_pose(calib_data_id: HHandle, camera_idx: int, calib_obj_idx: int, calib_obj_pose_idx: int, obj_in_camera_pose: Sequence[Union[float, int]]) -> None`

## Description

For a calibration data model of type
`calib_setup`=*"hand_eye_moving_cam"*,
*"hand_eye_stationary_cam"*, *"hand_eye_scara_moving_cam"*, or
*"hand_eye_scara_stationary_cam"* with no calibration object (see
[`create_calib_data`](create_calib_data.md)), the hand-eye calibration is based on so-called
observations of an arbitrary object in the camera coordinate system.
In the following this object will be called calibration object.
Additionally, the corresponding poses of the robot tool in the robot base
coordinate system must be known.
With `set_calib_data_observ_pose`, you store an
observation of the calibration object pose in the calibration data model
*`calib_data_id`*. An observation of the calibration object pose
consists of the following data:

- ***`camera_idx`*:** —

  Index of the observing camera
- ***`calib_obj_idx`*:** —

  Index of the observed calibration object
- ***`calib_obj_pose_idx`*:** —

  Index of the observed pose of the
  calibration object. You can choose it freely, without following a strict
  order. If you specify an index that already exists for the calibration
  object *`calib_obj_idx`*, the corresponding observation data is
  replaced by the new one.
- ***`obj_in_camera_pose`*:** —

  Pose of the observed calibration
  object relative to observing camera.

Note that, since the model *`calib_data_id`* uses a general
sensor and no calibration object (i.e., the model was created by
[`create_calib_data`](create_calib_data.md) with `num_cameras`=0 and
`num_calib_objects`=0), both *`camera_idx`* and
*`calib_obj_idx`* must be set to 0. If the model uses a camera
and an calibration object (i.e., `num_cameras`=1 and
`num_calib_objects`=1), then [`find_calib_object`](find_calib_object.md) or
[`set_calib_data_observ_points`](set_calib_data_observ_points.md) must be used.

The observation pose data can be accessed later by calling
[`get_calib_data_observ_pose`](get_calib_data_observ_pose.md) using the same values for the
arguments *`camera_idx`*, *`calib_obj_idx`*, and
*`calib_obj_pose_idx`*.

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

**`camera_idx`** (input_control)  number `→` int

Index of the observing camera.

Default:
0

Suggested values:
0, 1, 2

**`calib_obj_idx`** (input_control)  number `→` int

Index of the calibration object.

Default:
0

Suggested values:
0, 1, 2

**`calib_obj_pose_idx`** (input_control)  number `→` int

Index of the observed calibration object.

Default:
0

Suggested values:
0, 1, 2

Restriction:
`CalibObjPoseIdx >= 0`

**`obj_in_camera_pose`** (input_control)  pose `→` Sequence[Union[float, int]]

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
