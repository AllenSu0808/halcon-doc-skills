# set_camera_setup_param (Operator)

## Name

`set_camera_setup_param` — Set generic camera setup model parameters.

## Signature

`def set_camera_setup_param(camera_setup_model_id: HHandle, camera_idx: MaybeSequence[Union[int, str]], gen_param_name: str, gen_param_value: MaybeSequence[Union[float, int, str]]) -> None`

## Description

The operator `set_camera_setup_param` can be used to set
diverse generic parameters or transformations for the camera setup
model *`camera_setup_model_id`*. Two types of parameters can be
set with this operator:

**Coordinate system of the setup and transformation of camera
poses:**

By setting *`camera_idx`* to *"general"* and
*`gen_param_name`* to one of the following values, you can perform
the following general pose transformation for all cameras:

- ***"reference_camera"*:** —

  When setting *`gen_param_value`* to a valid camera index, all
  camera poses are recomputed relative to the coordinate system of
  this camera.
- ***"coord_transf_pose"*:** —

  When passing a tuple in HALCON pose format in
  *`gen_param_value`*, the current coordinate system is moved into
  this pose. The pose in *`gen_param_value`* represents the
  location and orientation of the desired coordinate system
  relative to the current one. All camera poses are recomputed
  relative to the new coordinate system.

The recomputed camera poses can be inspected with the operator
[`get_camera_setup_param`](get_camera_setup_param.md).

**Camera parameters:**

By setting *`camera_idx`* to a valid setup camera index (a value
between 0 and `num_cameras`-1) and *`gen_param_name`*
to one of the following values, camera specific parameters can be
set with *`gen_param_value`*:

- ***"params"*:** —

  A tuple with internal camera parameters.
- ***"params_deviations"*:** —

  A tuple with the standard deviations of the internal camera
  parameters except for `CameraType`, `Width`, and
  `Height`, thus `|params_deviations|=|params|-3`.
  The internal camera parameters are camera-type dependent.
  See the description of [`set_calib_data_cam_param`](set_calib_data_cam_param.md)
  for a list of values and [`calibrate_cameras`](calibrate_cameras.md) for details on
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
`set_camera_setup_param`. If *`camera_idx`* is an index of
a undefined camera, the operator returns an error.

All parameters can be read back by [`get_camera_setup_param`](get_camera_setup_param.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`camera_setup_model_id`** (input_control)  camera_setup_model `→` HHandle

Handle to the camera setup model.

**`camera_idx`** (input_control)  integer(-array) `→` MaybeSequence[Union[int, str]]

Unique index of the camera in the setup.

Default:
0

Suggested values:
0, 1, 2, "general"

**`gen_param_name`** (input_control)  attribute.name `→` str

Names of the generic parameters to be set.

List of values:
"coord_transf_pose", "params", "params_covariances", "params_deviations", "pose", "reference_camera"

**`gen_param_value`** (input_control)  attribute.value(-array) `→` MaybeSequence[Union[float, int, str]]

Values of the generic parameters to be set.

## Possible Predecessors

`create_camera_setup_model`,
`read_camera_setup_model`

## Module

Calibration
