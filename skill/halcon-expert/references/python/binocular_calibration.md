# binocular_calibration (Operator)

## Name

`binocular_calibration` — Determine all camera parameters of a binocular stereo system.

## Signature

`def binocular_calibration(nx: Sequence[Union[float, int]], ny: Sequence[Union[float, int]], nz: Sequence[Union[float, int]], nrow_1: Sequence[Union[float, int]], ncol_1: Sequence[Union[float, int]], nrow_2: Sequence[Union[float, int]], ncol_2: Sequence[Union[float, int]], start_cam_param_1: Sequence[Union[float, int, str]], start_cam_param_2: Sequence[Union[float, int, str]], nstart_pose_1: Sequence[Union[float, int]], nstart_pose_2: Sequence[Union[float, int]], estimate_params: Sequence[str]) -> Tuple[Sequence[Union[float, int, str]], Sequence[Union[float, int, str]], Sequence[Union[float, int]], Sequence[Union[float, int]], Sequence[Union[float, int]], Sequence[float]]`

`def binocular_calibration_s(nx: Sequence[Union[float, int]], ny: Sequence[Union[float, int]], nz: Sequence[Union[float, int]], nrow_1: Sequence[Union[float, int]], ncol_1: Sequence[Union[float, int]], nrow_2: Sequence[Union[float, int]], ncol_2: Sequence[Union[float, int]], start_cam_param_1: Sequence[Union[float, int, str]], start_cam_param_2: Sequence[Union[float, int, str]], nstart_pose_1: Sequence[Union[float, int]], nstart_pose_2: Sequence[Union[float, int]], estimate_params: Sequence[str]) -> Tuple[Sequence[Union[float, int, str]], Sequence[Union[float, int, str]], Sequence[Union[float, int]], Sequence[Union[float, int]], Sequence[Union[float, int]], float]`

## Description

In general, binocular calibration means the exact determination of
the parameters that model the 3D reconstruction of a 3D point from
the corresponding images of this point in a binocular stereo system.
This reconstruction is specified by the internal parameters
*`cam_param_1`* of camera 1 and *`cam_param_2`* of camera 2
describing the underlying camera model, and the external
parameters *`rel_pose`* describing the relative pose of camera
system 2 in relation to camera system 1.

Thus, known 3D model points (with coordinates *`nx`*,
*`ny`*, *`nz`*) are projected in the image planes of both
cameras (camera 1 and camera 2) and the sum of the squared distances
between these projections and the corresponding measured image
points (with coordinates *`nrow_1`*, *`ncol_1`* for camera 1
and *`nrow_2`*, *`ncol_2`* for camera 2) is minimized. It
should be noted that all these model points must be visible in both
images. The used camera model is described in
[Calibration](toc_calibration.md). The camera model is represented (for each
camera separately) by a tuple of 9 to 16 parameters that correspond
to perspective or telecentric area scan or telecentric line scan
cameras (see [Calibration](toc_calibration.md)). The projection uses the
initial values *`start_cam_param_1`* and *`start_cam_param_2`*
of the internal parameters of camera 1 and camera 2, which can be
obtained from the camera data sheets. In addition, the initial
guesses *`nstart_pose_1`* and *`nstart_pose_2`* of the poses
of the 3D calibration model in relative to the camera coordinate
systems (*ccs*) of camera 1 and camera 2 are needed as
well. These poses are expected in the form
$\mathrm{CCS} P_{\mathrm{wcs}}$ ![figure](../assets/4c18b1c4fb564c93.svg), where *wcs* denotes the
world coordinate system (see [Transformations / Poses](toc_transformations_poses.md) and
`“Solution Guide III-C - 3D Vision”`). They can be
determined by the operator [`find_marks_and_pose`](find_marks_and_pose.md). Since this
calibration algorithm simultaneously handles correspondences between
measured image and known model points from different image pairs,
poses (*`nstart_pose_1`*,*`nstart_pose_2`*), and measured
points (*`nrow_1`*,*`ncol_1`*,*`nrow_2`*,
*`ncol_2`*) must be passed concatenated in a corresponding
order.

The input parameter *`estimate_params`* is used to select the
parameters to be estimated. Usually this parameter is set to
*"all"*, i.e., all external camera parameters (translation
and rotation) and all internal camera parameters are determined.
Otherwise, *`estimate_params`* contains a tuple of strings
indicating the combination of parameters to estimate.
For instance, if the internal camera parameters already have been
determined (e.g., by previous calls to `binocular_calibration`), it is
often desired to only determine relative the pose of the two cameras
to each other (*`rel_pose`*). In this case,
*`estimate_params`* can be set to *"pose_rel"*.
The internal parameters can be subsumed
by the parameter values *"cam_param1"* and
*"cam_param2"* as well. Note that if the polynomial model is
used to model the lens distortions, the values *"k1_i"*,
*"k2_i"* and *"k3_i"* can be specified individually,
whereas *"p1"* and *"p2"* can only be specified in the
group *"poly_tan_2_i"* (with *"i"* indicating the index of
the camera). *"poly_i"* specifies the group *"k1_i"*,
*"k2_i"*, *"k3_i"* and *"poly_tan_2_i"*.

The following list contains all possible strings that can be passed to
the tuple:

|  |  |
| --- | --- |
| *Allowed strings for* *`estimate_params`* | *Determined parameters* |
| *"all"* (default) | All internal camera parameters, as well as the relative pose of both cameras and the poses of the calibration objects. |
| *"pose"* | Relative pose between the two cameras and poses of the calibration objects. |
| *"pose_rel"* | Relative pose between the two cameras. |
| *"alpha_rel"*, *"beta_rel"*, *"gamma_rel"*, *"transx_rel"*, *"transy_rel"*, *"transz_rel"* | Rotation angles and translation parameters of the relative pose between the two cameras. |
| *"pose_caltabs"* | Poses of the calibration objects. |
| *"alpha_caltabs"*, *"beta_caltabs"*, *"gamma_caltabs"*, *"transx_caltabs"*, *"transy_caltabs"*, *"transz_caltabs"* | Rotation angles and translation parameters of the relative poses of the calibration objects. |
| *"cam_param1"*, *"cam_param2"* | All internal camera parameters of camera 1 and camera 2, respectively. |
| *"focus1"*, *"magnification1"*, *"kappa1"*, *"poly_1"*, *"k1_1"*, *"k2_1"*, *"k3_1"*, *"poly_tan_2_1"*, *"image_plane_dist1"*, *"tilt1"*, *"cx1"*, *"cy1"*, *"sx1"*, *"sy1"*, *"focus2"*, *"magnification2"*, *"kappa2"*, *"poly_2"*, *"k1_2"*, *"k2_2"*, *"k3_2"*, *"poly_tan_2_2"*, *"image_plane_dist2"*, *"tilt2"*, *"cx2"*, *"cy2"*, *"sx2"*, *"sy2"* | Individual internal camera parameters of camera 1 and camera 2, respectively. |
| *"common_motion_vector"* | Determines whether two line scan cameras have a common motion vector. This is the case if the two cameras are mounted rigidly and the object is moved linearly in front of the cameras or if the two rigidly mounted cameras are moved by the same linear actuator. This is assumed to be the default. Therefore, you only need to set '~common_motion_vector' if the cameras are moving independently in different directions. |

In addition, parameters can be excluded from estimation by using the
prefix '~'. For example, the values
*["pose_rel", "~transx_rel"]* have the same effect as
*["alpha_rel","beta_rel","gamma_rel","transy_rel","transz_rel"]*.
On the other hand,
*["all","~focus1"]*
determines all internal and external parameters except the focus of
camera 1, for instance. The prefix '~' can be used
with all parameter values except *"all"*.

The underlying camera model is explained in the chapter
[Calibration](toc_calibration.md). The calibrated internal camera
parameters are returned in *`cam_param_1`* for camera 1 and in
*`cam_param_2`* for camera 2.

The external parameters are returned
analogously to [`camera_calibration`](camera_calibration.md), the 3D transformation
poses of the calibration model to the respective camera coordinate system
(*ccs*) are returned in *`nfinal_pose_1`* and
*`nfinal_pose_2`*.
Thus, the poses are in the form $\mathrm{CCS} P_{\mathrm{wcs}}$ ![figure](../assets/4c18b1c4fb564c93.svg), where
*wcs* denotes the world coordinate system of the 3D calibration model
(see [Transformations / Poses](toc_transformations_poses.md)
and `“Solution Guide III-C - 3D Vision”`).
The relative pose $ccs^1 P ccs^2$ ![figure](../assets/70dc27b5ce6d279e.svg),
*`rel_pose`*, specifies the transformation of points in *ccs2*
into *ccs1*. Therewith, the final poses are related with each other
(neglecting differences due to the balancing effects of the multi image
calibration) by:
HomMat3D_NFinalPose2 = INV(HomMat3D_RelPose) * HomMat3D_NFinalPose1 ,
where HomMat3D_* denotes a homogeneous transformation matrix of the
respective poses and INV() inverts a homogeneous matrix.

The computed average errors returned in *`errors`* give an
impression of the accuracy of the calibration. Using the determined
camera parameters, they denote the average euclidean distance
between the projection of the mark centers to their extracted image
coordinates.

For cameras with telecentric lenses, additional conditions must be
fulfilled for the setup. They can be found in the chapter
[Calibration](toc_calibration.md).

## Attention

Stereo setups that contain cameras with and without hypercentric
lenses at the same time are not supported. Furthermore, stereo
setups that contain area scan and line scan cameras at the same time
are not supported.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`nx`** (input_control)  number-array `→` Sequence[Union[float, int]]

Ordered Tuple with all X-coordinates
of the calibration marks (in meters).

**`ny`** (input_control)  number-array `→` Sequence[Union[float, int]]

Ordered Tuple with all Y-coordinates
of the calibration marks (in meters).

Number of elements:
NY == NX

**`nz`** (input_control)  number-array `→` Sequence[Union[float, int]]

Ordered Tuple with all Z-coordinates
of the calibration marks (in meters).

Number of elements:
NZ == NX

**`nrow_1`** (input_control)  number-array `→` Sequence[Union[float, int]]

Ordered Tuple with all row-coordinates
of the extracted calibration marks of camera 1
(in pixels).

**`ncol_1`** (input_control)  number-array `→` Sequence[Union[float, int]]

Ordered Tuple with all column-coordinates
of the extracted calibration marks of camera 1
(in pixels).

Number of elements:
NCol1 == NRow1

**`nrow_2`** (input_control)  number-array `→` Sequence[Union[float, int]]

Ordered Tuple with all row-coordinates
of the extracted calibration marks of camera 2
(in pixels).

Number of elements:
NRow2 == NRow1

**`ncol_2`** (input_control)  number-array `→` Sequence[Union[float, int]]

Ordered Tuple with all column-coordinates
of the extracted calibration marks of camera 2
(in pixels).

Number of elements:
NCol2 == NRow1

**`start_cam_param_1`** (input_control)  campar `→` Sequence[Union[float, int, str]]

Initial values for the internal parameters of camera 1.

**`start_cam_param_2`** (input_control)  campar `→` Sequence[Union[float, int, str]]

Initial values for the internal parameters of camera 2.

**`nstart_pose_1`** (input_control)  pose(-array) `→` Sequence[Union[float, int]]

Ordered tuple with all initial values for the
poses of the calibration model in relation to
camera 1.

Number of elements:
NStartPose1 == 7 * NRow1 / NX

**`nstart_pose_2`** (input_control)  pose(-array) `→` Sequence[Union[float, int]]

Ordered tuple with all initial values for the
poses of the calibration model in relation to
camera 2.

Number of elements:
NStartPose2 == 7 * NRow1 / NX

**`estimate_params`** (input_control)  string-array `→` Sequence[str]

Camera parameters to be estimated.

Default:
"all"

List of values:
"all", "alpha_caltabs", "alpha_rel", "beta_caltabs", "beta_rel", "cam_param1", "cam_param2", "common_motion_vector", "cx1", "cx2", "cy1", "cy2", "focus1", "focus2", "gamma_caltabs", "gamma_rel", "image_plane_dist1", "image_plane_dist2", "k1_1", "k1_2", "k2_1", "k2_2", "k3_1", "k3_2", "kappa1", "kappa2", "magnification1", "magnification2", "poly_1", "poly_2", "poly_tan_2_1", "poly_tan_2_2", "pose", "pose_caltabs", "pose_rel", "sx1", "sx2", "sy1", "sy2", "tilt1", "tilt2", "transx_caltabs", "transx_rel", "transy_caltabs", "transy_rel", "transz_caltabs", "transz_rel"

**`cam_param_1`** (output_control)  campar `→` Sequence[Union[float, int, str]]

Internal parameters of camera 1.

**`cam_param_2`** (output_control)  campar `→` Sequence[Union[float, int, str]]

Internal parameters of camera 2.

**`nfinal_pose_1`** (output_control)  pose(-array) `→` Sequence[Union[float, int]]

Ordered tuple with all poses of the calibration model
in relation to camera 1.

Number of elements:
NFinalPose1 == 7 * NRow1 / NX

**`nfinal_pose_2`** (output_control)  pose(-array) `→` Sequence[Union[float, int]]

Ordered tuple with all poses of the calibration model
in relation to camera 2.

Number of elements:
NFinalPose2 == 7 * NRow1 / NX

**`rel_pose`** (output_control)  pose `→` Sequence[Union[float, int]]

Pose of camera 2 in relation to camera 1.

**`errors`** (output_control)  real(-array) `→` Sequence[float]

Average error distances in pixels.

## Result

`binocular_calibration` returns 2 (
H_MSG_TRUE)
if all parameter values
are correct and the desired parameters have been determined by the
minimization algorithm. If necessary, an exception is raised.

## Possible Predecessors

`find_marks_and_pose`,
`caltab_points`,
`read_cam_par`

## Possible Successors

`write_pose`,
`write_cam_par`,
`pose_to_hom_mat3d`,
`disp_caltab`,
`gen_binocular_rectification_map`

## See also

`find_caltab`,
`sim_caltab`,
`read_cam_par`,
`create_pose`,
`convert_pose_type`,
`read_pose`,
`hom_mat3d_to_pose`,
`create_caltab`,
`binocular_disparity`,
`binocular_distance`

## Module

3D Metrology
