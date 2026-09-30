# CamMatToCamPar (Operator)

## Name

`CamMatToCamPar` — Compute the internal camera parameters from a camera matrix.

## Signature

`static void HOperatorSet.CamMatToCamPar(HTuple cameraMatrix, HTuple kappa, HTuple imageWidth, HTuple imageHeight, out HTuple cameraParam)`

`void HCamPar.CamMatToCamPar(HHomMat2D cameraMatrix, double kappa, int imageWidth, int imageHeight)`

`HCamPar HHomMat2D.CamMatToCamPar(double kappa, int imageWidth, int imageHeight)`

## Description

`CamMatToCamPar` computes internal camera parameters from
the camera matrix *`cameraMatrix`*, the radial distortion
coefficient *`kappa`*, the image width *`imageWidth`*, and
the image height *`imageHeight`*. The camera parameters are
returned in *`cameraParam`*. The parameters *`cameraMatrix`*
and *`kappa`* can be determined with
[`StationaryCameraSelfCalibration`](stationary_camera_self_calibration.md).
`CamMatToCamPar` converts this representation of the
internal camera parameters into the representation used by
[`CameraCalibration`](camera_calibration.md). The conversion can only be performed if
the skew of the image axes is set to 0 in
[`StationaryCameraSelfCalibration`](stationary_camera_self_calibration.md), i.e., if the parameter
*"skew"* is *not* being determined.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`cameraMatrix`** (input_control)  hom_mat2d `→` [HHomMat2D](HHomMat2D.md), [HTuple](HTuple.md) (*double*)

3x3 projective camera matrix
that determines the internal camera parameters.

**`kappa`** (input_control)  number `→` [HTuple](HTuple.md) (*double*)

Kappa.

**`imageWidth`** (input_control)  extent.x `→` [HTuple](HTuple.md) (*int* / long)

Width of the images that correspond to
*`cameraMatrix`*.

Restriction:
`ImageWidth > 0`

**`imageHeight`** (input_control)  extent.y `→` [HTuple](HTuple.md) (*int* / long)

Height of the images that correspond to
*`cameraMatrix`*.

Restriction:
`ImageHeight > 0`

**`cameraParam`** (output_control)  campar `→` [HCamPar](HCamPar.md), [HTuple](HTuple.md) (*double* / int / long / string)

Internal camera parameters.

## Example (HDevelop)

```
* For the input data to stationary_camera_self_calibration, please
* refer to the example for stationary_camera_self_calibration.
stationary_camera_self_calibration (4, 640, 480, 1, From, To, \
                                    HomMatrices2D, Rows1, Cols1, \
                                    Rows2, Cols2, NumMatches, \
                                    'gold_standard', \
                                    ['focus','principal_point','kappa'], \
                                    'true', CameraMatrix, Kappa, \
                                    RotationMatrices, X, Y, Z, Error)
cam_mat_to_cam_par (CameraMatrix, Kappa, 640, 480, CameraParam)
```

## Result

If the parameters are valid, the operator
`CamMatToCamPar` returns the value 2 (
H_MSG_TRUE)
. If
necessary an exception is raised.

## Possible Predecessors

`StationaryCameraSelfCalibration`

## See also

`CameraCalibration`,
`CamParToCamMat`

## Module

Calibration
