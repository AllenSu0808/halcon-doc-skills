# SetCameraSetupCamParam (Operator)

## Name

`SetCameraSetupCamParam` — Define type, parameters, and relative pose of a camera in a camera setup
model.

## Signature

`static void HOperatorSet.SetCameraSetupCamParam(HTuple cameraSetupModelID, HTuple cameraIdx, HTuple cameraType, HTuple cameraParam, HTuple cameraPose)`

`void HCameraSetupModel.SetCameraSetupCamParam(HTuple cameraIdx, HTuple cameraType, HCamPar cameraParam, HTuple cameraPose)`

`void HCameraSetupModel.SetCameraSetupCamParam(HTuple cameraIdx, string cameraType, HCamPar cameraParam, HTuple cameraPose)`

`void HCamPar.SetCameraSetupCamParam(HCameraSetupModel cameraSetupModelID, HTuple cameraIdx, HTuple cameraType, HTuple cameraPose)`

`void HCamPar.SetCameraSetupCamParam(HCameraSetupModel cameraSetupModelID, HTuple cameraIdx, string cameraType, HTuple cameraPose)`

`static void HPose.SetCameraSetupCamParam(HCameraSetupModel cameraSetupModelID, HTuple cameraIdx, HTuple cameraType, HCamPar cameraParam, HTuple cameraPose)`

`static void HPose.SetCameraSetupCamParam(HCameraSetupModel cameraSetupModelID, HTuple cameraIdx, string cameraType, HCamPar cameraParam, HTuple cameraPose)`

## Description

The operator `SetCameraSetupCamParam` defines the internal
parameters and the pose of the camera with *`cameraIdx`* in
the camera setup model *`cameraSetupModelID`*. The parameter
*`cameraIdx`* must be between 0 and `numCameras`-1 (see
[`GetCameraSetupParam`](get_camera_setup_param.md) with argument
*"num_cameras"*). If a camera with *`cameraIdx`* was
already defined, its parameters are overwritten by the current ones
(the camera is 'substituted').

The number of values in *`cameraParam`* depends on the camera
type. See the description of [`SetCalibDataCamParam`](set_calib_data_cam_param.md) for a
list of values and [Calibration](toc_calibration.md) for details on camera
types and camera parameters.

The parameter *`cameraType`* is only provided for backwards
compatibility.
The information about the camera type is contained in the first element
of *`cameraParam`*.
Therefore, *`cameraType`* should be set either to its default value
*[]* (the recommended option) or to the same value as the
first element of *`cameraParam`*. In any other case an error is raised.

The parameter *`cameraPose`* specifies the pose of the camera
relative to the setup's coordinate system (see
[`SetCameraSetupParam`](set_camera_setup_param.md) for further explanations on the
setup's coordinate system).

All of the parameters set by `SetCameraSetupCamParam` can
be read back by [`GetCameraSetupParam`](get_camera_setup_param.md). While the camera
type can be changed only with a new call to
`SetCameraSetupCamParam`, all other camera parameters can
be modified by [`SetCameraSetupParam`](set_camera_setup_param.md). Furthermore,
[`SetCameraSetupParam`](set_camera_setup_param.md) can set additional data to a camera:
standard deviations or covariances of the internal camera
parameters.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`cameraSetupModelID`** (input_control)  camera_setup_model `→` [HCameraSetupModel](HCameraSetupModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle to the camera setup model.

**`cameraIdx`** (input_control)  number-array `→` [HTuple](HTuple.md) (*int* / long)

Index of the camera in the setup.

Suggested values:
0, 1, 2

**`cameraType`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Type of the camera.

Default:
[]

List of values:
[]

**`cameraParam`** (input_control)  campar `→` [HCamPar](HCamPar.md), [HTuple](HTuple.md) (*double* / int / long / string)

Internal camera parameters.

**`cameraPose`** (input_control)  number-array `→` [HTuple](HTuple.md) (*double* / int / long)

Pose of the camera relative to the setup's coordinate
system.

Number of elements:
7

## Module

Calibration
