# change_radial_distortion_contours_xld (Operator)

## Name

`change_radial_distortion_contours_xld` — Change the radial distortion of contours.

## Signature

`def change_radial_distortion_contours_xld(contours: HObject, cam_param_in: Sequence[Union[int, float, str]], cam_param_out: Sequence[Union[int, float, str]]) -> HObject`

## Description

`change_radial_distortion_contours_xld` changes the radial
distortion of the input contours *`contours`* in accordance to the
internal camera parameters *`cam_param_in`* and *`cam_param_out`*.
Each subpixel of an input contour is transformed into the image plane
using *`cam_param_in`* and subsequently projected into a subpixel
of the corresponding contour in *`contours_rectified`* using
*`cam_param_out`*.

If *`cam_param_out`* was computed via
[`change_radial_distortion_cam_par`](change_radial_distortion_cam_par.md), the contours
*`contours_rectified`*
are equivalent to *`contours`* obtained with a lens with a modified
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

**`contours`** (input_object)  xld_cont(-array) `→` HObject

Original contours.

**`contours_rectified`** (output_object)  xld_cont(-array) `→` HObject

Resulting contours with modified radial distortion.

**`cam_param_in`** (input_control)  campar `→` Sequence[Union[int, float, str]]

Internal camera parameter for *`contours`*.

**`cam_param_out`** (input_control)  campar `→` Sequence[Union[int, float, str]]

Internal camera parameter for
*`contours_rectified`*.

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
