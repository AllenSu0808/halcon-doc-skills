# cam_par_to_cam_mat (Operator)

## Name

`cam_par_to_cam_mat` — Compute a camera matrix from internal camera parameters.

## Signature

`cam_par_to_cam_mat( : : CameraParam : CameraMatrix, ImageWidth, ImageHeight)`

## Description

`cam_par_to_cam_mat` computes the camera matrix
*`CameraMatrix`* as well as the image width
*`ImageWidth`*, and the image height *`ImageHeight`* from
the internal camera parameters *`CameraParam`*. The internal
camera parameters *`CameraParam`* can be determined with
[`camera_calibration`](camera_calibration.md). `cam_par_to_cam_mat` converts
this representation of the internal camera parameters into the
representation used by [`stationary_camera_self_calibration`](stationary_camera_self_calibration.md).
The conversion can only be performed if the camera is an area scan
pinhole camera and the distortion coefficients in
*`CameraParam`* are 0. If necessary,
[`change_radial_distortion_cam_par`](change_radial_distortion_cam_par.md) must be used to set the
distortion coefficients to 0.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`CameraParam`** (input_control)  campar `→`  (real / integer / string)

Internal camera parameters.

**`CameraMatrix`** (output_control)  hom_mat2d `→`  (real)

3x3 projective camera matrix
that corresponds to *`CameraParam`*.

**`ImageWidth`** (output_control)  extent.x `→`  (integer)

Width of the images that correspond to
*`CameraMatrix`*.

Assertion:
`ImageWidth > 0`

**`ImageHeight`** (output_control)  extent.y `→`  (integer)

Height of the images that correspond to
*`CameraMatrix`*.

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
