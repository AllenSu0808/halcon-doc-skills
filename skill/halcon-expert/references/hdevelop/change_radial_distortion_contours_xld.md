# change_radial_distortion_contours_xld (Operator)

## Name

`change_radial_distortion_contours_xld` — Change the radial distortion of contours.

## Signature

`change_radial_distortion_contours_xld(Contours : ContoursRectified : CamParamIn, CamParamOut : )`

## Description

`change_radial_distortion_contours_xld` changes the radial
distortion of the input contours *`Contours`* in accordance to the
internal camera parameters *`CamParamIn`* and *`CamParamOut`*.
Each subpixel of an input contour is transformed into the image plane
using *`CamParamIn`* and subsequently projected into a subpixel
of the corresponding contour in *`ContoursRectified`* using
*`CamParamOut`*.

If *`CamParamOut`* was computed via
[`change_radial_distortion_cam_par`](change_radial_distortion_cam_par.md), the contours
*`ContoursRectified`*
are equivalent to *`Contours`* obtained with a lens with a modified
radial distortion $\kappa$. If $\kappa=0$ the contours
are rectified. A subsequent pose estimation (determination of the
external camera parameters) is not affected by this operation.

Please note that `change_radial_distortion_contours_xld` does
not work for line scan cameras with perspective lenses.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Contours`** (input_object)  xld_cont(-array) `→` object

Original contours.

**`ContoursRectified`** (output_object)  xld_cont(-array) `→` object

Resulting contours with modified radial distortion.

**`CamParamIn`** (input_control)  campar `→`  (real / integer / string)

Internal camera parameter for *`Contours`*.

**`CamParamOut`** (input_control)  campar `→`  (real / integer / string)

Internal camera parameter for
*`ContoursRectified`*.

## Possible Predecessors

`change_radial_distortion_cam_par`,
`gen_contours_skeleton_xld`,
`edges_sub_pix`,
`smooth_contours_xld`

## Possible Successors

`gen_polygons_xld`,
`smooth_contours_xld`

## See also

`change_radial_distortion_cam_par`,
`camera_calibration`,
`read_cam_par`,
`change_radial_distortion_image`,
`change_radial_distortion_points`

## Module

Calibration
