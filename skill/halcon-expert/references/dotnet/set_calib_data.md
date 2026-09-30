# SetCalibData (Operator)

## Name

`SetCalibData` — Set data in a calibration data model.

## Signature

`static void HOperatorSet.SetCalibData(HTuple calibDataID, HTuple itemType, HTuple itemIdx, HTuple dataName, HTuple dataValue)`

`void HCalibData.SetCalibData(string itemType, HTuple itemIdx, string dataName, HTuple dataValue)`

`void HCalibData.SetCalibData(string itemType, int itemIdx, string dataName, string dataValue)`

## Description

With the operator `SetCalibData`, you can set data in the
calibration data model *`calibDataID`*.

Note that an overview on how the calibration data model is filled
with data during the processes of camera calibration and hand-eye
calibration is provided by the description of
[`GetCalibData`](get_calib_data.md).

The calibration data model can contain various kinds of data. How to
set specific data in the calibration data model is described for
different categories of data:

- Model-related data (*`itemType`* *"model"*)
- Camera-related data (*`itemType`* *"camera"*)
- Data related to calibration object poses (*`itemType`*
  *"calib_obj_pose"*)
- Hand-eye calibration related data (*`itemType`*
  *"tool"*)

The parameter *`itemIdx`* lets you select whether the new
value should be set for all items of a type or only for an
individual one. The parameters to set are passed in
*`dataName`*, their values in *`dataValue`*.

To get detailed information about the calibration process of
your camera setup see the chapter [Calibration](toc_calibration.md).

### Model-related data

- ***`itemType`*=*"model"*:** —

  *`itemIdx`* must be set to *"general"*.

  Depending on
  the selection in *`dataName`*, you can set the following
  model-related parameters to the value passed in *`dataValue`*:

  - ***"reference_camera"*:** —

    Set the reference camera for the calibration model to the passed
    camera index. All poses stored in the calibration data model
    are specified in the coordinate system of the reference camera
    (see [`GetCalibData`](get_calib_data.md)).
  - ***"common_motion_vector"*:** —

    For stereo setups with telecentric line scan cameras, a string
    with a Boolean value (i.e., *"true"* or *"false"*)
    that determines whether the cameras have a common motion vector.
  - ***"optimization_method"*:** —

    Set the optimization method to be used in the hand-eye
    calibration process. If *`dataValue`*=*"linear"* is
    set, a linear method is used for the hand-eye calibration. If
    *`dataValue`*=*"nonlinear"* is set, a nonlinear method
    is used for the hand-eye calibration. If
    *`dataValue`*=*"stochastic"* is set, a method is used
    which also takes the uncertainty of measured observations
    into account (see [`CalibrateHandEye`](calibrate_hand_eye.md) for more details).

### Camera-related data

- ***`itemType`*=*"camera"*:** —

  *`itemIdx`* determines, if data is set for all cameras in
  general or for a specific camera. With
  *`itemIdx`*=*"general"*, the new settings are applied
  to all cameras in the model. If you pass a valid camera index
  instead, i.e., a number between 0 and `numCameras`-1
  (`numCameras` is specified during model creation with
  [`CreateCalibData`](create_calib_data.md)), only the specified camera is affected
  by the changes.

  By selecting the following parameters in *`dataName`*, you can
  **specify which camera parameters shall be optimized during
  the calibration** performed by [`CalibrateCameras`](calibrate_cameras.md):

  - ***"calib_settings"*:** —

    The camera parameters listed in *`dataValue`* are marked
    for optimization for the affected camera(s) (additionally to the
    camera parameters that were already marked for
    optimization). Note that by default, all parameters are marked
    for the optimization. That is, *"calib_settings"* is
    mainly suited to add previously excluded parameters again.
  - ***"excluded_settings"*:** —

    The camera parameters listed in *`dataValue`* are excluded
    from the optimization for the affected camera(s).

  The following camera parameters can be passed in *`dataValue`*.
  See [Calibration](toc_calibration.md) for affected camera types and further details
  about the parameters.

  *Internal camera parameters*

  - ***"focus"*:** —

    Focal length of the lens.
  - ***"magnification"*:** —

    Magnification of the lens.
  - ***"kappa"*:** —

    Divisional distortion coefficient kappa.
  - ***"k1"*,*"k2"*,*"k3"*:** —

    Polynomial radial distortion parameters.
  - ***"poly_tan_2"*:** —

    An alias parameter for all polynomial tangential distortion
    parameters, i.e., p1 and p2.
  - ***"poly"*:** —

    An alias parameter for all polynomial distortion
    parameters, i.e., k1, k2, k3, p1, and p2.
  - ***"image_plane_dist"*:** —

    The distance of the tilted image plane from the perspective
    projection center.
  - ***"tilt"*:** —

    Tilt and rotation of the tilt lens.
  - ***"cx"*,*"cy"*:** —

    Coordinates of the camera's principal point.
  - ***"principal_point"*:** —

    An alias parameter for *"cx"* and *"cy"*.
  - ***"sx"*,*"sy"*:** —

    Sensor element dimensions.
  - ***"params"*:** —

    All internal camera parameters.

  *External camera parameters*

  - ***"alpha"*,*"beta"*,*"gamma"*:** —

    Rotation part of the camera pose.
  - ***"transx"*,*"transy"*,*"transz"*:** —

    Translation part of the camera pose.
  - ***"pose"*:** —

    All external camera parameters.

  *Further camera parameters*

  - ***"vx"*,*"vy"*,*"vz"*:** —

    Motion vector parameters.
    Note that for stereo setups with telecentric line scan cameras with a
    common motion vector (i.e.,
    *"common_motion_vector"* = *"true"*),
    the motion vector optimization parameters
    of the reference camera determine which parameters of the common
    motion vector are optimized. For this kind of setup, it is
    recommended not to exclude any motion vector parameters from the
    optimization.
  - ***"all"*:** —

    All camera parameters.

  By default, all parameters are marked for calibration. As an
  exception, the camera pose is excluded from the optimization for
  calibration setups with only one camera
  (`numCameras`=1). This setting makes the calibration process
  equivalent to the one performed by [`CameraCalibration`](camera_calibration.md).

### Data related to calibration object poses

- ***`itemType`*=*"calib_obj_pose"*:** —

  *`itemIdx`* determines, if data is set for all calibration
  object poses in general or for a specific calibration object
  pose. With *`itemIdx`*=*"general"* the new settings
  are applied to all calibration object poses in the model. If you
  pass a valid calibration object pose index instead, i.e., a tuple
  containing a valid index pair `[CalibObjIdx,
  CalibObjPoseIdx]`, you specify a calibration object pose, which
  is affected by the changes.

  By selecting the following parameters in *`dataName`*, you can
  **specify which calibration object pose parameters shall be
  optimized during the calibration** performed by
  [`CalibrateCameras`](calibrate_cameras.md):

  - ***"calib_settings"*:** —

    The calibration object pose settings listed in
    *`dataValue`* are marked for optimization for the affected
    pose(s). Note that by default, all calibration pose parameters
    are marked for the optimization. That is,
    *"calib_settings"* is mainly suited to add previously
    excluded parameters again.
  - ***"excluded_settings"*:** —

    The calibration object pose settings listed in
    *`dataValue`* are excluded from the optimization for the
    affected pose(s).

  The following calibration pose parameters can be passed in
  *`dataValue`*:

  - ***"alpha"*,*"beta"*,*"gamma"*:** —

    Rotation part of the calibration object pose.
  - ***"transx"*,*"transy"*,*"transz"*:** —

    Translation part of the calibration object pose.
  - ***"pose"*:** —

    All calibration object pose parameters.
  - ***"all"*:** —

    All calibration objects optimization parameters,
    i.e., the same as *"pose"*.

  By default all parameters are marked for calibration.

  The current settings for any model item can be queried with the
  operator [`GetCalibData`](get_calib_data.md).

### Hand-eye calibration related data

- ***`itemType`*=*"tool"*:** —

  *`itemIdx`* must be set to a valid calibration object pose index.

  By selecting the following parameter in *`dataName`*, you can
  set the pose of the robot tool:

  - ***"tool_in_base_pose"*:** —

    Set the pose of the robot tool (in robot base coordinates),
    which was used to obtain the observation of the pose of the
    calibration object with the same index *`itemIdx`*
    (corresponds to the parameter `CalibObjPoseIdx` of any of
    the operators [`FindCalibObject`](find_calib_object.md),
    [`SetCalibDataObservPose`](set_calib_data_observ_pose.md), or
    [`SetCalibDataObservPoints`](set_calib_data_observ_points.md)).

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

**`itemType`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Type of calibration data item.

Default:
"model"

List of values:
"calib_obj_pose", "camera", "model", "tool"

**`itemIdx`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*int* / long / string)

Index of the affected item
(depending on the selected *`itemType`*).

Default:
"general"

Suggested values:
0, 1, 2, "general"

**`dataName`** (input_control)  attribute.name `→` [HTuple](HTuple.md) (*string*)

Parameter(s) to set.

Default:
"reference_camera"

List of values:
"calib_settings", "common_motion_vector", "excluded_settings", "optimization_method", "reference_camera", "tool_in_base_pose"

**`dataValue`** (input_control)  attribute.value(-array) `→` [HTuple](HTuple.md) (*string* / int / long)

New value(s).

Default:
0

Suggested values:
0, 1, 2, "all", "pose", "params", "alpha", "beta", "gamma", "transx", "transy", "transz", "focus", "magnification", "kappa", "poly", "poly_tan_2", "k1", "k2", "k3", "image_plane_dist", "tilt", "principal_point", "cx", "cy", "sx", "sy", "vx", "vy", "vz", "true", "false", "linear", "nonlinear", "stochastic"

## Example (HDevelop)

```
* Here, the cell size is known exactly, thus it is excluded from
* the optimization.
set_calib_data (CalibDataID, 'camera', 'general', 'excluded_settings', \
                ['sx','sy'])
```

## Possible Predecessors

`SetCalibDataObservPoints`,
`FindCalibObject`

## Possible Successors

`CalibrateCameras`,
`CalibrateHandEye`

## Module

Calibration
