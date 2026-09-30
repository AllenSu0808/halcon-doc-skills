# cam_mat_to_cam_par (Operator)

## Name

`cam_mat_to_cam_par` — Compute the internal camera parameters from a camera matrix.

## Signature

`cam_mat_to_cam_par( : : CameraMatrix, Kappa, ImageWidth, ImageHeight : CameraParam)`

## Description

`cam_mat_to_cam_par` computes internal camera parameters from
the camera matrix *`CameraMatrix`*, the radial distortion
coefficient *`Kappa`*, the image width *`ImageWidth`*, and
the image height *`ImageHeight`*. The camera parameters are
returned in *`CameraParam`*. The parameters *`CameraMatrix`*
and *`Kappa`* can be determined with
[`stationary_camera_self_calibration`](stationary_camera_self_calibration.md).
`cam_mat_to_cam_par` converts this representation of the
internal camera parameters into the representation used by
[`camera_calibration`](camera_calibration.md). The conversion can only be performed if
the skew of the image axes is set to 0 in
[`stationary_camera_self_calibration`](stationary_camera_self_calibration.md), i.e., if the parameter
*'skew'* is *not* being determined.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`CameraMatrix`** (input_control)  hom_mat2d `→`  (real)

3x3 projective camera matrix
that determines the internal camera parameters.

**`Kappa`** (input_control)  number `→`  (real)

Kappa.

**`ImageWidth`** (input_control)  extent.x `→`  (integer)

Width of the images that correspond to
*`CameraMatrix`*.

Restriction:
`ImageWidth > 0`

**`ImageHeight`** (input_control)  extent.y `→`  (integer)

Height of the images that correspond to
*`CameraMatrix`*.

Restriction:
`ImageHeight > 0`

**`CameraParam`** (output_control)  campar `→`  (real / integer / string)

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
`cam_mat_to_cam_par` returns the value 2 (
H_MSG_TRUE)
. If
necessary an exception is raised.

## Possible Predecessors

`stationary_camera_self_calibration`

## See also

`camera_calibration`,
`cam_par_to_cam_mat`

## Module

Calibration
