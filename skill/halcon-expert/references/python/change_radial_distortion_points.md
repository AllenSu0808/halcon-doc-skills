# change_radial_distortion_points (Operator)

## Name

`change_radial_distortion_points` — Change the radial distortion of pixel coordinates.

## Signature

`def change_radial_distortion_points(row: Sequence[float], col: Sequence[float], cam_param_in: Sequence[Union[int, float, str]], cam_param_out: Sequence[Union[int, float, str]]) -> Tuple[Sequence[float], Sequence[float]]`

## Description

`change_radial_distortion_points` changes the radial
distortion of input image coordinates (*`row`*, *`col`*)
in accordance to the internal camera parameters *`cam_param_in`*
and *`cam_param_out`*. Each input pixel (*`row`*,
*`col`*) is transformed into the image plane using
*`cam_param_in`* and projected into another image using
*`cam_param_out`*.

Please note that `change_radial_distortion_points` does not
work for line scan cameras with perspective lenses.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`row`** (input_control)  real-array `→` Sequence[float]

Original row component of pixel coordinates.

**`col`** (input_control)  real-array `→` Sequence[float]

Original column component of pixel coordinates.

**`cam_param_in`** (input_control)  campar `→` Sequence[Union[int, float, str]]

The inner camera parameters of the camera used
to create the input pixel coordinates.

**`cam_param_out`** (input_control)  campar `→` Sequence[Union[int, float, str]]

The inner camera parameters of a camera.

**`row_changed`** (output_control)  real-array `→` Sequence[float]

Row component of pixel coordinates after
changing the radial distortion.

**`col_changed`** (output_control)  real-array `→` Sequence[float]

Column component of pixel coordinates after
changing the radial distortion.

## Result

`change_radial_distortion_points` returns 2 (
H_MSG_TRUE)
if all
parameter values are correct.

## See also

`change_radial_distortion_cam_par`,
`camera_calibration`,
`read_cam_par`,
`change_radial_distortion_contours_xld`,
`change_radial_distortion_image`

## Module

Calibration
