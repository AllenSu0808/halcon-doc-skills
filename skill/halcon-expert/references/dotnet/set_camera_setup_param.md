# SetCameraSetupParam (Operator)

## Name

`SetCameraSetupParam` — Set generic camera setup model parameters.

## Signature

`static void HOperatorSet.SetCameraSetupParam(HTuple cameraSetupModelID, HTuple cameraIdx, HTuple genParamName, HTuple genParamValue)`

`void HCameraSetupModel.SetCameraSetupParam(HTuple cameraIdx, string genParamName, HTuple genParamValue)`

`void HCameraSetupModel.SetCameraSetupParam(int cameraIdx, string genParamName, double genParamValue)`

## Description

The operator `SetCameraSetupParam` can be used to set
diverse generic parameters or transformations for the camera setup
model *`cameraSetupModelID`*. Two types of parameters can be
set with this operator:

**Coordinate system of the setup and transformation of camera
poses:**

By setting *`cameraIdx`* to *"general"* and
*`genParamName`* to one of the following values, you can perform
the following general pose transformation for all cameras:

- ***"reference_camera"*:** —

  When setting *`genParamValue`* to a valid camera index, all
  camera poses are recomputed relative to the coordinate system of
  this camera.
- ***"coord_transf_pose"*:** —

  When passing a tuple in HALCON pose format in
  *`genParamValue`*, the current coordinate system is moved into
  this pose. The pose in *`genParamValue`* represents the
  location and orientation of the desired coordinate system
  relative to the current one. All camera poses are recomputed
  relative to the new coordinate system.

The recomputed camera poses can be inspected with the operator
[`GetCameraSetupParam`](get_camera_setup_param.md).

**Camera parameters:**

By setting *`cameraIdx`* to a valid setup camera index (a value
between 0 and `numCameras`-1) and *`genParamName`*
to one of the following values, camera specific parameters can be
set with *`genParamValue`*:

- ***"params"*:** —

  A tuple with internal camera parameters.
- ***"params_deviations"*:** —

  A tuple with the standard deviations of the internal camera
  parameters except for `CameraType`, `Width`, and
  `Height`, thus `|params_deviations|=|params|-3`.
  The internal camera parameters are camera-type dependent.
  See the description of [`SetCalibDataCamParam`](set_calib_data_cam_param.md)
  for a list of values and [`CalibrateCameras`](calibrate_cameras.md) for details on
  camera types and camera parameters.
- ***"params_covariances"*:** —

  A tuple with the covariance matrix of the internal camera parameters.
  The tuple must represent a square matrix whose both dimensions are
  identical to the number of standard deviation values, thus
  `|params_covariances|=|params_deviations|²=(|params|-3)²`
  , see *"params_deviations"*.
- ***"pose"*:** —

  A tuple representing the pose of the camera in HALCON pose
  format, relative to camera setup's coordinate system. See the
  above section for further details.

Note that the camera must already be defined in the model, before
any of its parameters can be changed by
`SetCameraSetupParam`. If *`cameraIdx`* is an index of
a undefined camera, the operator returns an error.

All parameters can be read back by [`GetCameraSetupParam`](get_camera_setup_param.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`cameraSetupModelID`** (input_control)  camera_setup_model `→` [HCameraSetupModel](HCameraSetupModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle to the camera setup model.

**`cameraIdx`** (input_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long / string)

Unique index of the camera in the setup.

Default:
0

Suggested values:
0, 1, 2, "general"

**`genParamName`** (input_control)  attribute.name `→` [HTuple](HTuple.md) (*string*)

Names of the generic parameters to be set.

List of values:
"coord_transf_pose", "params", "params_covariances", "params_deviations", "pose", "reference_camera"

**`genParamValue`** (input_control)  attribute.value(-array) `→` [HTuple](HTuple.md) (*double* / int / long / string)

Values of the generic parameters to be set.

## Possible Predecessors

`CreateCameraSetupModel`,
`ReadCameraSetupModel`

## Module

Calibration
