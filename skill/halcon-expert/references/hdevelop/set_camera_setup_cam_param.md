# set_camera_setup_cam_param (Operator)

## Name

`set_camera_setup_cam_param` — Define type, parameters, and relative pose of a camera in a camera setup
model.

## Signature

`set_camera_setup_cam_param( : : CameraSetupModelID, CameraIdx, CameraType, CameraParam, CameraPose : )`

## Description

The operator `set_camera_setup_cam_param` defines the internal
parameters and the pose of the camera with *`CameraIdx`* in
the camera setup model *`CameraSetupModelID`*. The parameter
*`CameraIdx`* must be between 0 and `NumCameras`-1 (see
[`get_camera_setup_param`](get_camera_setup_param.md) with argument
*'num_cameras'*). If a camera with *`CameraIdx`* was
already defined, its parameters are overwritten by the current ones
(the camera is 'substituted').

The number of values in *`CameraParam`* depends on the camera
type. See the description of [`set_calib_data_cam_param`](set_calib_data_cam_param.md) for a
list of values and [Calibration](toc_calibration.md) for details on camera
types and camera parameters.

The parameter *`CameraType`* is only provided for backwards
compatibility.
The information about the camera type is contained in the first element
of *`CameraParam`*.
Therefore, *`CameraType`* should be set either to its default value
*[]* (the recommended option) or to the same value as the
first element of *`CameraParam`*. In any other case an error is raised.

The parameter *`CameraPose`* specifies the pose of the camera
relative to the setup's coordinate system (see
[`set_camera_setup_param`](set_camera_setup_param.md) for further explanations on the
setup's coordinate system).

All of the parameters set by `set_camera_setup_cam_param` can
be read back by [`get_camera_setup_param`](get_camera_setup_param.md). While the camera
type can be changed only with a new call to
`set_camera_setup_cam_param`, all other camera parameters can
be modified by [`set_camera_setup_param`](set_camera_setup_param.md). Furthermore,
[`set_camera_setup_param`](set_camera_setup_param.md) can set additional data to a camera:
standard deviations or covariances of the internal camera
parameters.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`CameraSetupModelID`** (input_control)  camera_setup_model `→`  (handle)

Handle to the camera setup model.

**`CameraIdx`** (input_control)  number-array `→`  (integer)

Index of the camera in the setup.

Suggested values:
0, 1, 2

**`CameraType`** (input_control)  string(-array) `→`  (string)

Type of the camera.

Default:
[]

List of values:
[]

**`CameraParam`** (input_control)  campar `→`  (real / integer / string)

Internal camera parameters.

**`CameraPose`** (input_control)  number-array `→`  (real / integer)

Pose of the camera relative to the setup's coordinate
system.

Number of elements:
7

## Module

Calibration
