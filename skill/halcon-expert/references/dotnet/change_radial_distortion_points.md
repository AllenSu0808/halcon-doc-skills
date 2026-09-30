# ChangeRadialDistortionPoints (Operator)

## Name

`ChangeRadialDistortionPoints` — Change the radial distortion of pixel coordinates.

## Signature

`static void HOperatorSet.ChangeRadialDistortionPoints(HTuple row, HTuple col, HTuple camParamIn, HTuple camParamOut, out HTuple rowChanged, out HTuple colChanged)`

`void HCamPar.ChangeRadialDistortionPoints(HTuple row, HTuple col, HCamPar camParamOut, out HTuple rowChanged, out HTuple colChanged)`

## Description

`ChangeRadialDistortionPoints` changes the radial
distortion of input image coordinates (*`row`*, *`col`*)
in accordance to the internal camera parameters *`camParamIn`*
and *`camParamOut`*. Each input pixel (*`row`*,
*`col`*) is transformed into the image plane using
*`camParamIn`* and projected into another image using
*`camParamOut`*.

Please note that `ChangeRadialDistortionPoints` does not
work for line scan cameras with perspective lenses.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`row`** (input_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Original row component of pixel coordinates.

**`col`** (input_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Original column component of pixel coordinates.

**`camParamIn`** (input_control)  campar `→` [HCamPar](HCamPar.md), [HTuple](HTuple.md) (*double* / int / long / string)

The inner camera parameters of the camera used
to create the input pixel coordinates.

**`camParamOut`** (input_control)  campar `→` [HCamPar](HCamPar.md), [HTuple](HTuple.md) (*double* / int / long / string)

The inner camera parameters of a camera.

**`rowChanged`** (output_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Row component of pixel coordinates after
changing the radial distortion.

**`colChanged`** (output_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Column component of pixel coordinates after
changing the radial distortion.

## Result

`ChangeRadialDistortionPoints` returns 2 (
H_MSG_TRUE)
if all
parameter values are correct.

## See also

`ChangeRadialDistortionCamPar`,
`CameraCalibration`,
`ReadCamPar`,
`ChangeRadialDistortionContoursXld`,
`ChangeRadialDistortionImage`

## Module

Calibration
