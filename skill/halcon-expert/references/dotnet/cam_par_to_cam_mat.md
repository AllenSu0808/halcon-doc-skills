# CamParToCamMat (Operator)

## Name

`CamParToCamMat` — Compute a camera matrix from internal camera parameters.

## Signature

`static void HOperatorSet.CamParToCamMat(HTuple cameraParam, out HTuple cameraMatrix, out HTuple imageWidth, out HTuple imageHeight)`

`HHomMat2D HCamPar.CamParToCamMat(out int imageWidth, out int imageHeight)`

`void HHomMat2D.CamParToCamMat(HCamPar cameraParam, out int imageWidth, out int imageHeight)`

## Description

`CamParToCamMat` computes the camera matrix
*`cameraMatrix`* as well as the image width
*`imageWidth`*, and the image height *`imageHeight`* from
the internal camera parameters *`cameraParam`*. The internal
camera parameters *`cameraParam`* can be determined with
[`CameraCalibration`](camera_calibration.md). `CamParToCamMat` converts
this representation of the internal camera parameters into the
representation used by [`StationaryCameraSelfCalibration`](stationary_camera_self_calibration.md).
The conversion can only be performed if the camera is an area scan
pinhole camera and the distortion coefficients in
*`cameraParam`* are 0. If necessary,
[`ChangeRadialDistortionCamPar`](change_radial_distortion_cam_par.md) must be used to set the
distortion coefficients to 0.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`cameraParam`** (input_control)  campar `→` [HCamPar](HCamPar.md), [HTuple](HTuple.md) (*double* / int / long / string)

Internal camera parameters.

**`cameraMatrix`** (output_control)  hom_mat2d `→` [HHomMat2D](HHomMat2D.md), [HTuple](HTuple.md) (*double*)

3x3 projective camera matrix
that corresponds to *`cameraParam`*.

**`imageWidth`** (output_control)  extent.x `→` [HTuple](HTuple.md) (*int* / long)

Width of the images that correspond to
*`cameraMatrix`*.

Assertion:
`ImageWidth > 0`

**`imageHeight`** (output_control)  extent.y `→` [HTuple](HTuple.md) (*int* / long)

Height of the images that correspond to
*`cameraMatrix`*.

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
`CamParToCamMat` returns the value 2 (
H_MSG_TRUE)
. If
necessary an exception is raised.

## Possible Predecessors

`CameraCalibration`

## See also

`StationaryCameraSelfCalibration`,
`CamMatToCamPar`

## Module

Calibration
