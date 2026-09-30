# GetCameraSetupParam (Operator)

## Name

`GetCameraSetupParam` — Get generic camera setup model parameters.

## Signature

`static void HOperatorSet.GetCameraSetupParam(HTuple cameraSetupModelID, HTuple cameraIdx, HTuple genParamName, out HTuple genParamValue)`

`HTuple HCameraSetupModel.GetCameraSetupParam(HTuple cameraIdx, string genParamName)`

`HTuple HCameraSetupModel.GetCameraSetupParam(int cameraIdx, string genParamName)`

## Description

The operator `GetCameraSetupParam` can be used to inspect diverse
generic parameters of the camera setup model *`cameraSetupModelID`*.
Two types of parameters can be queried with this operator:

**General parameters:**

By setting *`cameraIdx`* to *"general"* and *`genParamName`*
to one of the following values, general camera setup parameters are
returned in *`genParamValue`*:

- ***"num_cameras"*:** —

  Number of cameras described in the model. The number of cameras is fixed
  with the creation of the camera setup model and cannot be changed after
  that (see [`CreateCameraSetupModel`](create_camera_setup_model.md)).
- ***"camera_calib_error"*:** —

  The root mean square error (RMSE) of the back projection of the
  optimization of the camera system. This error
  is identical with the error returned by [`CalibrateCameras`](calibrate_cameras.md).
- ***"reference_camera"*:** —

  Returns the index of the camera that has been defined as reference
  camera within the system. If no reference camera has been specified
  using [`SetCameraSetupParam`](set_camera_setup_param.md), the index 0 is returned.
  If the coordinate system has been moved by setting a pose with the
  parameter *"coord_transf_pose"* in [`SetCameraSetupParam`](set_camera_setup_param.md),
  the origin of the coordinate system is not located in any of the
  available cameras. Therefore, the index -1 is returned.
- ***"coord_transf_pose"*:** —

  Returns the pose in which the coordinate system of the setup has been
  moved. Please note that after setting a reference camera with
  [`SetCameraSetupParam`](set_camera_setup_param.md), the pose of this camera is returned.
  Adjusting this coordinate system subsequently using the parameter
  *"coord_transf_pose"* in [`SetCameraSetupParam`](set_camera_setup_param.md) yields a
  pose that corresponds to the location and orientation of the desired
  coordinate system relative to the current one.

**Camera parameters:**

By setting *`cameraIdx`* to a valid setup camera index (a value between
0 and `numCameras`-1) and *`genParamName`*
to one of the following values, camera-specific parameters are returned
in *`genParamValue`*:

- ***"type"*:** —

  Camera type (see [`SetCameraSetupCamParam`](set_camera_setup_cam_param.md)).
- ***"params"*:** —

  A tuple with internal camera parameters. The length of the tuple
  depends on the camera type.
- ***"params_deviations"*:** —

  A tuple representing the standard deviations of the internal camera
  parameters. The length of the tuple depends on the camera type.
- ***"params_covariances"*:** —

  A tuple representing the covariance matrix if the internal camera
  parameters. The length of the tuple depends on the camera type.
- ***"pose"*:** —

  Camera pose relative to the setup's coordinate system (see
  [`CreateCameraSetupModel`](create_camera_setup_model.md) for more details).

Note that the camera needs to be set first by
[`SetCameraSetupCamParam`](set_camera_setup_cam_param.md), before any of its parameters can be
inspected by `GetCameraSetupParam`. If *`cameraIdx`* is an
index of an undefined camera, the operator returns an error.

For more information about the calibration process of your camera setup
see the chapter [Calibration](toc_calibration.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`cameraSetupModelID`** (input_control)  camera_setup_model `→` [HCameraSetupModel](HCameraSetupModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle to the camera setup model.

**`cameraIdx`** (input_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long / string)

Index of the camera in the setup.

Default:
0

Suggested values:
0, 1, 2, "general"

**`genParamName`** (input_control)  attribute.name `→` [HTuple](HTuple.md) (*string*)

Names of the generic parameters to be queried.

List of values:
"camera_calib_error", "coord_transf_pose", "num_cameras", "params", "params_covariances", "params_deviations", "pose", "reference_camera", "type"

**`genParamValue`** (output_control)  attribute.value(-array) `→` [HTuple](HTuple.md) (*double* / int / long / string)

Values of the generic parameters to be queried.

## Module

Calibration
