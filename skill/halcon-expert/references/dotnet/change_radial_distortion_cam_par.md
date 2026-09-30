# ChangeRadialDistortionCamPar (Operator)

## Name

`ChangeRadialDistortionCamPar` — Determine new camera parameters in accordance to the specified
radial distortion.

## Signature

`static void HOperatorSet.ChangeRadialDistortionCamPar(HTuple mode, HTuple camParamIn, HTuple distortionCoeffs, out HTuple camParamOut)`

`HCamPar HCamPar.ChangeRadialDistortionCamPar(string mode, HTuple distortionCoeffs)`

`HCamPar HCamPar.ChangeRadialDistortionCamPar(string mode, double distortionCoeffs)`

## Description

`ChangeRadialDistortionCamPar` modifies the internal
camera parameters in accordance to the specified radial distortion
coefficients *`distortionCoeffs`*. The operator can only be
used for area scan cameras (with any lens type) and for line scan
cameras with telecentric lenses. Line scan cameras with perspective
lenses are not supported.

With the parameter *`mode`*, one of the following modes can be
selected:

- ***"fixed"*:** —

  Only the distortion coefficients are modified, the other
  internal camera parameters remain unchanged. In general, this leads
  to a change of the visible part of the scene.
- ***"fullsize"*:** —

  For area scan cameras, the scale factors $S_{x}$
  and$S_{y}$ and the image center point
  $(C_{x},C_{y})^{T}$ are modified in order to preserve
  the visible part of the scene. For line scan cameras with
  telecentric lenses, the scale factor $S_{x}$, the
  image center point $(C_{x},C_{y})^{T}$, and
  the $V_{y}$ component of the motion vector are
  changed to achieve the this effect. Thus, all points
  visible in the original image are also visible in the
  modified (rectified) image. In general, this leads to
  undefined pixels in the modified image.
- ***"adaptive"*:** —

  A trade-off between the other modes: The visible part of the
  scene is slightly reduced to prevent undefined pixels in the
  modified image. The same parameters as for
  *"fullsize"* are modified.
- ***"preserve_resolution"*:** —

  As in the mode *"fullsize"*, all points visible in
  the original image are also visible in the modified
  (rectified) image. For area scan cameras, the scale factors
  $S_{x}$ and $S_{y}$ and the image center
  point $(C_{x},C_{y})^{T}$ are modified. For
  line scan cameras with telecentric lenses, the scale factor
  $S_{x}$, the image center point
  $(C_{x},C_{y})^{T}$, and potentially the
  $V_{y}$ component of the motion vector are changed
  to achieve the this effect. In general, this leads to
  undefined pixels in the modified image. In contrast to the
  mode *"fullsize"*, additionally the size of the
  modified image is increased such that the image resolution
  does not decrease in any part of the image.

In all modes, the distortion coefficients in *`camParamOut`*
are set to *`distortionCoeffs`*. For telecentric line scan
cameras, the motion vector also influences the perceived
distortion. For example, a nonzero $V_{x}$ component leads
to skewed pixels. Furthermore, if $Vy \neq Sx / Magnification$ ![figure](../assets/482ad512c43e208d.svg), the pixels appear to be
non-square. Therefore, for telecentric line scan cameras, up to
three more components can be passed in addition to
$\kappa$ or
$(K_{1},K_{2},K_{3},P_{1},P_{2})$,
respectively, in *`distortionCoeffs`*. These specify
the new $V_{x}$, $V_{y}$, and $V_{z}$
components of the motion vector.

The transformation of a pixel in the modified image into the image
plane using *`camParamOut`* results in the same point as the
transformation of a pixel in the original image via
*`camParamIn`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`mode`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Mode

Default:
"adaptive"

Suggested values:
"fullsize", "adaptive", "fixed", "preserve_resolution"

**`camParamIn`** (input_control)  campar `→` [HCamPar](HCamPar.md), [HTuple](HTuple.md) (*double* / int / long / string)

Internal camera parameters (original).

**`distortionCoeffs`** (input_control)  real(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Desired radial distortions.

Number of elements:
DistortionCoeffs == 1 || DistortionCoeffs == 5

Default:
0.0

**`camParamOut`** (output_control)  campar `→` [HCamPar](HCamPar.md), [HTuple](HTuple.md) (*double* / int / long / string)

Internal camera parameters (modified).

## Result

`ChangeRadialDistortionCamPar` returns 2 (
H_MSG_TRUE)
if all
parameter values are correct. If necessary, an exception is
raised.

## Possible Predecessors

`CameraCalibration`,
`ReadCamPar`

## Possible Successors

`ChangeRadialDistortionImage`,
`ChangeRadialDistortionContoursXld`,
`GenRadialDistortionMap`

## See also

`CameraCalibration`,
`ReadCamPar`,
`ChangeRadialDistortionImage`,
`ChangeRadialDistortionContoursXld`,
`ChangeRadialDistortionPoints`

## Module

Calibration
