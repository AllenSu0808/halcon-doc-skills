# ChangeRadialDistortionContoursXld (Operator)

## Name

`ChangeRadialDistortionContoursXld` — Change the radial distortion of contours.

## Signature

`static void HOperatorSet.ChangeRadialDistortionContoursXld(HObject contours, out HObject contoursRectified, HTuple camParamIn, HTuple camParamOut)`

`HXLDCont HXLDCont.ChangeRadialDistortionContoursXld(HCamPar camParamIn, HCamPar camParamOut)`

`HXLDCont HCamPar.ChangeRadialDistortionContoursXld(HXLDCont contours, HCamPar camParamOut)`

## Description

`ChangeRadialDistortionContoursXld` changes the radial
distortion of the input contours *`contours`* in accordance to the
internal camera parameters *`camParamIn`* and *`camParamOut`*.
Each subpixel of an input contour is transformed into the image plane
using *`camParamIn`* and subsequently projected into a subpixel
of the corresponding contour in *`contoursRectified`* using
*`camParamOut`*.

If *`camParamOut`* was computed via
[`ChangeRadialDistortionCamPar`](change_radial_distortion_cam_par.md), the contours
*`contoursRectified`*
are equivalent to *`contours`* obtained with a lens with a modified
radial distortion $\kappa$. If $\kappa=0$ the contours
are rectified. A subsequent pose estimation (determination of the
external camera parameters) is not affected by this operation.

Please note that `ChangeRadialDistortionContoursXld` does
not work for line scan cameras with perspective lenses.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`contours`** (input_object)  xld_cont(-array) `→` [HXLDCont](HXLDCont.md)

Original contours.

**`contoursRectified`** (output_object)  xld_cont(-array) `→` [HXLDCont](HXLDCont.md)

Resulting contours with modified radial distortion.

**`camParamIn`** (input_control)  campar `→` [HCamPar](HCamPar.md), [HTuple](HTuple.md) (*double* / int / long / string)

Internal camera parameter for *`contours`*.

**`camParamOut`** (input_control)  campar `→` [HCamPar](HCamPar.md), [HTuple](HTuple.md) (*double* / int / long / string)

Internal camera parameter for
*`contoursRectified`*.

## Possible Predecessors

`ChangeRadialDistortionCamPar`,
`GenContoursSkeletonXld`,
`EdgesSubPix`,
`SmoothContoursXld`

## Possible Successors

`GenPolygonsXld`,
`SmoothContoursXld`

## See also

`ChangeRadialDistortionCamPar`,
`CameraCalibration`,
`ReadCamPar`,
`ChangeRadialDistortionImage`,
`ChangeRadialDistortionPoints`

## Module

Calibration
