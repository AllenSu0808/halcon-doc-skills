# change_radial_distortion_points (Operator)

## Name

`change_radial_distortion_points` — Change the radial distortion of pixel coordinates.

## Signature

`change_radial_distortion_points( : : Row, Col, CamParamIn, CamParamOut : RowChanged, ColChanged)`

## Description

`change_radial_distortion_points` changes the radial
distortion of input image coordinates (*`Row`*, *`Col`*)
in accordance to the internal camera parameters *`CamParamIn`*
and *`CamParamOut`*. Each input pixel (*`Row`*,
*`Col`*) is transformed into the image plane using
*`CamParamIn`* and projected into another image using
*`CamParamOut`*.

Please note that `change_radial_distortion_points` does not
work for line scan cameras with perspective lenses.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Row`** (input_control)  real-array `→`  (real)

Original row component of pixel coordinates.

**`Col`** (input_control)  real-array `→`  (real)

Original column component of pixel coordinates.

**`CamParamIn`** (input_control)  campar `→`  (real / integer / string)

The inner camera parameters of the camera used
to create the input pixel coordinates.

**`CamParamOut`** (input_control)  campar `→`  (real / integer / string)

The inner camera parameters of a camera.

**`RowChanged`** (output_control)  real-array `→`  (real)

Row component of pixel coordinates after
changing the radial distortion.

**`ColChanged`** (output_control)  real-array `→`  (real)

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
