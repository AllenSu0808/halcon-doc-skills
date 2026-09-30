# cam_par_to_cam_mat (Operator)

## Name

`cam_par_to_cam_mat` — Compute a camera matrix from internal camera parameters.

## Signature

`def cam_par_to_cam_mat(camera_param: Sequence[Union[int, float, str]]) -> Tuple[Sequence[float], int, int]`

## Description

`cam_par_to_cam_mat` computes the camera matrix
*`camera_matrix`* as well as the image width
*`image_width`*, and the image height *`image_height`* from
the internal camera parameters *`camera_param`*. The internal
camera parameters *`camera_param`* can be determined with
[`camera_calibration`](camera_calibration.md). `cam_par_to_cam_mat` converts
this representation of the internal camera parameters into the
representation used by [`stationary_camera_self_calibration`](stationary_camera_self_calibration.md).
The conversion can only be performed if the camera is an area scan
pinhole camera and the distortion coefficients in
*`camera_param`* are 0. If necessary,
[`change_radial_distortion_cam_par`](change_radial_distortion_cam_par.md) must be used to set the
distortion coefficients to 0.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`camera_param`** (input_control)  campar `→` Sequence[Union[int, float, str]]

Internal camera parameters.

**`camera_matrix`** (output_control)  hom_mat2d `→` Sequence[float]

3x3 projective camera matrix
that corresponds to *`camera_param`*.

**`image_width`** (output_control)  extent.x `→` int

Width of the images that correspond to
*`camera_matrix`*.

Assertion:
`ImageWidth > 0`

**`image_height`** (output_control)  extent.y `→` int

Height of the images that correspond to
*`camera_matrix`*.

Assertion:
`ImageHeight > 0`

## Example (HDevelop)

```
* For the input data to calibrate_cameras, please refer to the
* example for calibrate_cameras.
calibrate_cameras (CalibDataID, Error)
get_calib_data (CalibDataID, 'camera', 0, 'params', CameraParam)
cam_par_to_cam_mat (CameraParam, CameraMatrix, ImageWidth, ImageHeight)

* Alternatively, the following calls can be used.
change_radial_distortion_cam_par ('adaptive', CameraParam, 0, CamParamOut)
cam_par_to_cam_mat (CamParamOut, CameraMatrix, ImageWidth, ImageHeight)
```

## Result

If the parameters are valid, the operator
`cam_par_to_cam_mat` returns the value 2 (
H_MSG_TRUE)
. If
necessary an exception is raised.

## Possible Predecessors

`camera_calibration`

## See also

`stationary_camera_self_calibration`,
`cam_mat_to_cam_par`

## Module

Calibration
