# cam_mat_to_cam_par (Operator)

## Name

`cam_mat_to_cam_par` — Compute the internal camera parameters from a camera matrix.

## Signature

`def cam_mat_to_cam_par(camera_matrix: Sequence[float], kappa: float, image_width: int, image_height: int) -> Sequence[Union[int, float, str]]`

## Description

`cam_mat_to_cam_par` computes internal camera parameters from
the camera matrix *`camera_matrix`*, the radial distortion
coefficient *`kappa`*, the image width *`image_width`*, and
the image height *`image_height`*. The camera parameters are
returned in *`camera_param`*. The parameters *`camera_matrix`*
and *`kappa`* can be determined with
[`stationary_camera_self_calibration`](stationary_camera_self_calibration.md).
`cam_mat_to_cam_par` converts this representation of the
internal camera parameters into the representation used by
[`camera_calibration`](camera_calibration.md). The conversion can only be performed if
the skew of the image axes is set to 0 in
[`stationary_camera_self_calibration`](stationary_camera_self_calibration.md), i.e., if the parameter
*"skew"* is *not* being determined.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`camera_matrix`** (input_control)  hom_mat2d `→` Sequence[float]

3x3 projective camera matrix
that determines the internal camera parameters.

**`kappa`** (input_control)  number `→` float

Kappa.

**`image_width`** (input_control)  extent.x `→` int

Width of the images that correspond to
*`camera_matrix`*.

Restriction:
`ImageWidth > 0`

**`image_height`** (input_control)  extent.y `→` int

Height of the images that correspond to
*`camera_matrix`*.

Restriction:
`ImageHeight > 0`

**`camera_param`** (output_control)  campar `→` Sequence[Union[int, float, str]]

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
