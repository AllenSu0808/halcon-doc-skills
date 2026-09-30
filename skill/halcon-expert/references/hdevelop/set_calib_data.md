# set_calib_data (Operator)

## Name

`set_calib_data` — Set data in a calibration data model.

## Signature

`set_calib_data( : : CalibDataID, ItemType, ItemIdx, DataName, DataValue : )`

## Description

With the operator `set_calib_data`, you can set data in the
calibration data model *`CalibDataID`*.

Note that an overview on how the calibration data model is filled
with data during the processes of camera calibration and hand-eye
calibration is provided by the description of
[`get_calib_data`](get_calib_data.md).

The calibration data model can contain various kinds of data. How to
set specific data in the calibration data model is described for
different categories of data:

- Model-related data (*`ItemType`* *'model'*)
- Camera-related data (*`ItemType`* *'camera'*)
- Data related to calibration object poses (*`ItemType`*
  *'calib_obj_pose'*)
- Hand-eye calibration related data (*`ItemType`*
  *'tool'*)

The parameter *`ItemIdx`* lets you select whether the new
value should be set for all items of a type or only for an
individual one. The parameters to set are passed in
*`DataName`*, their values in *`DataValue`*.

To get detailed information about the calibration process of
your camera setup see the chapter [Calibration](toc_calibration.md).

### Model-related data

- ***`ItemType`*=*'model'*:** —

  *`ItemIdx`* must be set to *'general'*.

  Depending on
  the selection in *`DataName`*, you can set the following
  model-related parameters to the value passed in *`DataValue`*:

  - ***'reference_camera'*:** —

    Set the reference camera for the calibration model to the passed
    camera index. All poses stored in the calibration data model
    are specified in the coordinate system of the reference camera
    (see [`get_calib_data`](get_calib_data.md)).
  - ***'common_motion_vector'*:** —

    For stereo setups with telecentric line scan cameras, a string
    with a Boolean value (i.e., *'true'* or *'false'*)
    that determines whether the cameras have a common motion vector.
  - ***'optimization_method'*:** —

    Set the optimization method to be used in the hand-eye
    calibration process. If *`DataValue`*=*'linear'* is
    set, a linear method is used for the hand-eye calibration. If
    *`DataValue`*=*'nonlinear'* is set, a nonlinear method
    is used for the hand-eye calibration. If
    *`DataValue`*=*'stochastic'* is set, a method is used
    which also takes the uncertainty of measured observations
    into account (see [`calibrate_hand_eye`](calibrate_hand_eye.md) for more details).

### Camera-related data

- ***`ItemType`*=*'camera'*:** —

  *`ItemIdx`* determines, if data is set for all cameras in
  general or for a specific camera. With
  *`ItemIdx`*=*'general'*, the new settings are applied
  to all cameras in the model. If you pass a valid camera index
  instead, i.e., a number between 0 and `NumCameras`-1
  (`NumCameras` is specified during model creation with
  [`create_calib_data`](create_calib_data.md)), only the specified camera is affected
  by the changes.

  By selecting the following parameters in *`DataName`*, you can
  **specify which camera parameters shall be optimized during
  the calibration** performed by [`calibrate_cameras`](calibrate_cameras.md):

  - ***'calib_settings'*:** —

    The camera parameters listed in *`DataValue`* are marked
    for optimization for the affected camera(s) (additionally to the
    camera parameters that were already marked for
    optimization). Note that by default, all parameters are marked
    for the optimization. That is, *'calib_settings'* is
    mainly suited to add previously excluded parameters again.
  - ***'excluded_settings'*:** —

    The camera parameters listed in *`DataValue`* are excluded
    from the optimization for the affected camera(s).

  The following camera parameters can be passed in *`DataValue`*.
  See [Calibration](toc_calibration.md) for affected camera types and further details
  about the parameters.

  *Internal camera parameters*

  - ***'focus'*:** —

    Focal length of the lens.
  - ***'magnification'*:** —

    Magnification of the lens.
  - ***'kappa'*:** —

    Divisional distortion coefficient kappa.
  - ***'k1'*,*'k2'*,*'k3'*:** —

    Polynomial radial distortion parameters.
  - ***'poly_tan_2'*:** —

    An alias parameter for all polynomial tangential distortion
    parameters, i.e., p1 and p2.
  - ***'poly'*:** —

    An alias parameter for all polynomial distortion
    parameters, i.e., k1, k2, k3, p1, and p2.
  - ***'image_plane_dist'*:** —

    The distance of the tilted image plane from the perspective
    projection center.
  - ***'tilt'*:** —

    Tilt and rotation of the tilt lens.
  - ***'cx'*,*'cy'*:** —

    Coordinates of the camera's principal point.
  - ***'principal_point'*:** —

    An alias parameter for *'cx'* and *'cy'*.
  - ***'sx'*,*'sy'*:** —

    Sensor element dimensions.
  - ***'params'*:** —

    All internal camera parameters.

  *External camera parameters*

  - ***'alpha'*,*'beta'*,*'gamma'*:** —

    Rotation part of the camera pose.
  - ***'transx'*,*'transy'*,*'transz'*:** —

    Translation part of the camera pose.
  - ***'pose'*:** —

    All external camera parameters.

  *Further camera parameters*

  - ***'vx'*,*'vy'*,*'vz'*:** —

    Motion vector parameters.
    Note that for stereo setups with telecentric line scan cameras with a
    common motion vector (i.e.,
    *'common_motion_vector'* = *'true'*),
    the motion vector optimization parameters
    of the reference camera determine which parameters of the common
    motion vector are optimized. For this kind of setup, it is
    recommended not to exclude any motion vector parameters from the
    optimization.
  - ***'all'*:** —

    All camera parameters.

  By default, all parameters are marked for calibration. As an
  exception, the camera pose is excluded from the optimization for
  calibration setups with only one camera
  (`NumCameras`=1). This setting makes the calibration process
  equivalent to the one performed by [`camera_calibration`](camera_calibration.md).

### Data related to calibration object poses

- ***`ItemType`*=*'calib_obj_pose'*:** —

  *`ItemIdx`* determines, if data is set for all calibration
  object poses in general or for a specific calibration object
  pose. With *`ItemIdx`*=*'general'* the new settings
  are applied to all calibration object poses in the model. If you
  pass a valid calibration object pose index instead, i.e., a tuple
  containing a valid index pair `[CalibObjIdx,
  CalibObjPoseIdx]`, you specify a calibration object pose, which
  is affected by the changes.

  By selecting the following parameters in *`DataName`*, you can
  **specify which calibration object pose parameters shall be
  optimized during the calibration** performed by
  [`calibrate_cameras`](calibrate_cameras.md):

  - ***'calib_settings'*:** —

    The calibration object pose settings listed in
    *`DataValue`* are marked for optimization for the affected
    pose(s). Note that by default, all calibration pose parameters
    are marked for the optimization. That is,
    *'calib_settings'* is mainly suited to add previously
    excluded parameters again.
  - ***'excluded_settings'*:** —

    The calibration object pose settings listed in
    *`DataValue`* are excluded from the optimization for the
    affected pose(s).

  The following calibration pose parameters can be passed in
  *`DataValue`*:

  - ***'alpha'*,*'beta'*,*'gamma'*:** —

    Rotation part of the calibration object pose.
  - ***'transx'*,*'transy'*,*'transz'*:** —

    Translation part of the calibration object pose.
  - ***'pose'*:** —

    All calibration object pose parameters.
  - ***'all'*:** —

    All calibration objects optimization parameters,
    i.e., the same as *'pose'*.

  By default all parameters are marked for calibration.

  The current settings for any model item can be queried with the
  operator [`get_calib_data`](get_calib_data.md).

### Hand-eye calibration related data

- ***`ItemType`*=*'tool'*:** —

  *`ItemIdx`* must be set to a valid calibration object pose index.

  By selecting the following parameter in *`DataName`*, you can
  set the pose of the robot tool:

  - ***'tool_in_base_pose'*:** —

    Set the pose of the robot tool (in robot base coordinates),
    which was used to obtain the observation of the pose of the
    calibration object with the same index *`ItemIdx`*
    (corresponds to the parameter `CalibObjPoseIdx` of any of
    the operators [`find_calib_object`](find_calib_object.md),
    [`set_calib_data_observ_pose`](set_calib_data_observ_pose.md), or
    [`set_calib_data_observ_points`](set_calib_data_observ_points.md)).

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

**`ItemType`** (input_control)  string `→`  (string)

Type of calibration data item.

Default:
'model'

List of values:
'calib_obj_pose', 'camera', 'model', 'tool'

**`ItemIdx`** (input_control)  number(-array) `→`  (integer / string)

Index of the affected item
(depending on the selected *`ItemType`*).

Default:
'general'

Suggested values:
0, 1, 2, 'general'

**`DataName`** (input_control)  attribute.name `→`  (string)

Parameter(s) to set.

Default:
'reference_camera'

List of values:
'calib_settings', 'common_motion_vector', 'excluded_settings', 'optimization_method', 'reference_camera', 'tool_in_base_pose'

**`DataValue`** (input_control)  attribute.value(-array) `→`  (string / integer)

New value(s).

Default:
0

Suggested values:
0, 1, 2, 'all', 'pose', 'params', 'alpha', 'beta', 'gamma', 'transx', 'transy', 'transz', 'focus', 'magnification', 'kappa', 'poly', 'poly_tan_2', 'k1', 'k2', 'k3', 'image_plane_dist', 'tilt', 'principal_point', 'cx', 'cy', 'sx', 'sy', 'vx', 'vy', 'vz', 'true', 'false', 'linear', 'nonlinear', 'stochastic'

## Example (HDevelop)

```
* Here, the cell size is known exactly, thus it is excluded from
* the optimization.
set_calib_data (CalibDataID, 'camera', 'general', 'excluded_settings', \
                ['sx','sy'])
```

## Possible Predecessors

`set_calib_data_observ_points`,
`find_calib_object`

## Possible Successors

`calibrate_cameras`,
`calibrate_hand_eye`

## Module

Calibration
