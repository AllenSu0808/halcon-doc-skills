# binocular_calibration (Operator)

## Name

`binocular_calibration` — Determine all camera parameters of a binocular stereo system.

## Signature

`binocular_calibration( : : NX, NY, NZ, NRow1, NCol1, NRow2, NCol2, StartCamParam1, StartCamParam2, NStartPose1, NStartPose2, EstimateParams : CamParam1, CamParam2, NFinalPose1, NFinalPose2, RelPose, Errors)`

## Description

In general, binocular calibration means the exact determination of
the parameters that model the 3D reconstruction of a 3D point from
the corresponding images of this point in a binocular stereo system.
This reconstruction is specified by the internal parameters
*`CamParam1`* of camera 1 and *`CamParam2`* of camera 2
describing the underlying camera model, and the external
parameters *`RelPose`* describing the relative pose of camera
system 2 in relation to camera system 1.

Thus, known 3D model points (with coordinates *`NX`*,
*`NY`*, *`NZ`*) are projected in the image planes of both
cameras (camera 1 and camera 2) and the sum of the squared distances
between these projections and the corresponding measured image
points (with coordinates *`NRow1`*, *`NCol1`* for camera 1
and *`NRow2`*, *`NCol2`* for camera 2) is minimized. It
should be noted that all these model points must be visible in both
images. The used camera model is described in
[Calibration](toc_calibration.md). The camera model is represented (for each
camera separately) by a tuple of 9 to 16 parameters that correspond
to perspective or telecentric area scan or telecentric line scan
cameras (see [Calibration](toc_calibration.md)). The projection uses the
initial values *`StartCamParam1`* and *`StartCamParam2`*
of the internal parameters of camera 1 and camera 2, which can be
obtained from the camera data sheets. In addition, the initial
guesses *`NStartPose1`* and *`NStartPose2`* of the poses
of the 3D calibration model in relative to the camera coordinate
systems (*ccs*) of camera 1 and camera 2 are needed as
well. These poses are expected in the form
$\mathrm{CCS} P_{\mathrm{wcs}}$ ![figure](../assets/4c18b1c4fb564c93.svg), where *wcs* denotes the
world coordinate system (see [Transformations / Poses](toc_transformations_poses.md) and
`“Solution Guide III-C - 3D Vision”`). They can be
determined by the operator [`find_marks_and_pose`](find_marks_and_pose.md). Since this
calibration algorithm simultaneously handles correspondences between
measured image and known model points from different image pairs,
poses (*`NStartPose1`*,*`NStartPose2`*), and measured
points (*`NRow1`*,*`NCol1`*,*`NRow2`*,
*`NCol2`*) must be passed concatenated in a corresponding
order.

The input parameter *`EstimateParams`* is used to select the
parameters to be estimated. Usually this parameter is set to
*'all'*, i.e., all external camera parameters (translation
and rotation) and all internal camera parameters are determined.
Otherwise, *`EstimateParams`* contains a tuple of strings
indicating the combination of parameters to estimate.
For instance, if the internal camera parameters already have been
determined (e.g., by previous calls to `binocular_calibration`), it is
often desired to only determine relative the pose of the two cameras
to each other (*`RelPose`*). In this case,
*`EstimateParams`* can be set to *'pose_rel'*.
The internal parameters can be subsumed
by the parameter values *'cam_param1'* and
*'cam_param2'* as well. Note that if the polynomial model is
used to model the lens distortions, the values *'k1_i'*,
*'k2_i'* and *'k3_i'* can be specified individually,
whereas *'p1'* and *'p2'* can only be specified in the
group *'poly_tan_2_i'* (with *'i'* indicating the index of
the camera). *'poly_i'* specifies the group *'k1_i'*,
*'k2_i'*, *'k3_i'* and *'poly_tan_2_i'*.

The following list contains all possible strings that can be passed to
the tuple:

|  |  |
| --- | --- |
| *Allowed strings for* *`EstimateParams`* | *Determined parameters* |
| *'all'* (default) | All internal camera parameters, as well as the relative pose of both cameras and the poses of the calibration objects. |
| *'pose'* | Relative pose between the two cameras and poses of the calibration objects. |
| *'pose_rel'* | Relative pose between the two cameras. |
| *'alpha_rel'*, *'beta_rel'*, *'gamma_rel'*, *'transx_rel'*, *'transy_rel'*, *'transz_rel'* | Rotation angles and translation parameters of the relative pose between the two cameras. |
| *'pose_caltabs'* | Poses of the calibration objects. |
| *'alpha_caltabs'*, *'beta_caltabs'*, *'gamma_caltabs'*, *'transx_caltabs'*, *'transy_caltabs'*, *'transz_caltabs'* | Rotation angles and translation parameters of the relative poses of the calibration objects. |
| *'cam_param1'*, *'cam_param2'* | All internal camera parameters of camera 1 and camera 2, respectively. |
| *'focus1'*, *'magnification1'*, *'kappa1'*, *'poly_1'*, *'k1_1'*, *'k2_1'*, *'k3_1'*, *'poly_tan_2_1'*, *'image_plane_dist1'*, *'tilt1'*, *'cx1'*, *'cy1'*, *'sx1'*, *'sy1'*, *'focus2'*, *'magnification2'*, *'kappa2'*, *'poly_2'*, *'k1_2'*, *'k2_2'*, *'k3_2'*, *'poly_tan_2_2'*, *'image_plane_dist2'*, *'tilt2'*, *'cx2'*, *'cy2'*, *'sx2'*, *'sy2'* | Individual internal camera parameters of camera 1 and camera 2, respectively. |
| *'common_motion_vector'* | Determines whether two line scan cameras have a common motion vector. This is the case if the two cameras are mounted rigidly and the object is moved linearly in front of the cameras or if the two rigidly mounted cameras are moved by the same linear actuator. This is assumed to be the default. Therefore, you only need to set '~common_motion_vector' if the cameras are moving independently in different directions. |

In addition, parameters can be excluded from estimation by using the
prefix '~'. For example, the values
*['pose_rel', '~transx_rel']* have the same effect as
*['alpha_rel','beta_rel','gamma_rel','transy_rel','transz_rel']*.
On the other hand,
*['all','~focus1']*
determines all internal and external parameters except the focus of
camera 1, for instance. The prefix '~' can be used
with all parameter values except *'all'*.

The underlying camera model is explained in the chapter
[Calibration](toc_calibration.md). The calibrated internal camera
parameters are returned in *`CamParam1`* for camera 1 and in
*`CamParam2`* for camera 2.

The external parameters are returned
analogously to [`camera_calibration`](camera_calibration.md), the 3D transformation
poses of the calibration model to the respective camera coordinate system
(*ccs*) are returned in *`NFinalPose1`* and
*`NFinalPose2`*.
Thus, the poses are in the form $\mathrm{CCS} P_{\mathrm{wcs}}$ ![figure](../assets/4c18b1c4fb564c93.svg), where
*wcs* denotes the world coordinate system of the 3D calibration model
(see [Transformations / Poses](toc_transformations_poses.md)
and `“Solution Guide III-C - 3D Vision”`).
The relative pose $ccs^1 P ccs^2$ ![figure](../assets/70dc27b5ce6d279e.svg),
*`RelPose`*, specifies the transformation of points in *ccs2*
into *ccs1*. Therewith, the final poses are related with each other
(neglecting differences due to the balancing effects of the multi image
calibration) by:
HomMat3D_NFinalPose2 = INV(HomMat3D_RelPose) * HomMat3D_NFinalPose1 ,
where HomMat3D_* denotes a homogeneous transformation matrix of the
respective poses and INV() inverts a homogeneous matrix.

The computed average errors returned in *`Errors`* give an
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

**`NX`** (input_control)  number-array `→`  (real / integer)

Ordered Tuple with all X-coordinates
of the calibration marks (in meters).

**`NY`** (input_control)  number-array `→`  (real / integer)

Ordered Tuple with all Y-coordinates
of the calibration marks (in meters).

Number of elements:
NY == NX

**`NZ`** (input_control)  number-array `→`  (real / integer)

Ordered Tuple with all Z-coordinates
of the calibration marks (in meters).

Number of elements:
NZ == NX

**`NRow1`** (input_control)  number-array `→`  (real / integer)

Ordered Tuple with all row-coordinates
of the extracted calibration marks of camera 1
(in pixels).

**`NCol1`** (input_control)  number-array `→`  (real / integer)

Ordered Tuple with all column-coordinates
of the extracted calibration marks of camera 1
(in pixels).

Number of elements:
NCol1 == NRow1

**`NRow2`** (input_control)  number-array `→`  (real / integer)

Ordered Tuple with all row-coordinates
of the extracted calibration marks of camera 2
(in pixels).

Number of elements:
NRow2 == NRow1

**`NCol2`** (input_control)  number-array `→`  (real / integer)

Ordered Tuple with all column-coordinates
of the extracted calibration marks of camera 2
(in pixels).

Number of elements:
NCol2 == NRow1

**`StartCamParam1`** (input_control)  campar `→`  (real / integer / string)

Initial values for the internal parameters of camera 1.

**`StartCamParam2`** (input_control)  campar `→`  (real / integer / string)

Initial values for the internal parameters of camera 2.

**`NStartPose1`** (input_control)  pose(-array) `→`  (real / integer)

Ordered tuple with all initial values for the
poses of the calibration model in relation to
camera 1.

Number of elements:
NStartPose1 == 7 * NRow1 / NX

**`NStartPose2`** (input_control)  pose(-array) `→`  (real / integer)

Ordered tuple with all initial values for the
poses of the calibration model in relation to
camera 2.

Number of elements:
NStartPose2 == 7 * NRow1 / NX

**`EstimateParams`** (input_control)  string-array `→`  (string)

Camera parameters to be estimated.

Default:
'all'

List of values:
'all', 'alpha_caltabs', 'alpha_rel', 'beta_caltabs', 'beta_rel', 'cam_param1', 'cam_param2', 'common_motion_vector', 'cx1', 'cx2', 'cy1', 'cy2', 'focus1', 'focus2', 'gamma_caltabs', 'gamma_rel', 'image_plane_dist1', 'image_plane_dist2', 'k1_1', 'k1_2', 'k2_1', 'k2_2', 'k3_1', 'k3_2', 'kappa1', 'kappa2', 'magnification1', 'magnification2', 'poly_1', 'poly_2', 'poly_tan_2_1', 'poly_tan_2_2', 'pose', 'pose_caltabs', 'pose_rel', 'sx1', 'sx2', 'sy1', 'sy2', 'tilt1', 'tilt2', 'transx_caltabs', 'transx_rel', 'transy_caltabs', 'transy_rel', 'transz_caltabs', 'transz_rel'

**`CamParam1`** (output_control)  campar `→`  (real / integer / string)

Internal parameters of camera 1.

**`CamParam2`** (output_control)  campar `→`  (real / integer / string)

Internal parameters of camera 2.

**`NFinalPose1`** (output_control)  pose(-array) `→`  (real / integer)

Ordered tuple with all poses of the calibration model
in relation to camera 1.

Number of elements:
NFinalPose1 == 7 * NRow1 / NX

**`NFinalPose2`** (output_control)  pose(-array) `→`  (real / integer)

Ordered tuple with all poses of the calibration model
in relation to camera 2.

Number of elements:
NFinalPose2 == 7 * NRow1 / NX

**`RelPose`** (output_control)  pose `→`  (real / integer)

Pose of camera 2 in relation to camera 1.

**`Errors`** (output_control)  real(-array) `→`  (real)

Average error distances in pixels.

## Example (HDevelop)

```
* Open image source.
open_framegrabber ('File', 1, 1, 0, 0, 0, 0, 'default', -1, 'default', -1, \
                   'default', 'images_l.seq', 'default', 0, -1, AcqHandle1)
open_framegrabber ('File', 1, 1, 0, 0, 0, 0, 'default', -1, 'default', -1, \
                   'default', 'images_r.seq', 'default', 1, -1, AcqHandle2)

* Initialize the start parameters.
caltab_points ('caltab_30mm.descr', X, Y, Z)
StartCamParam1 := ['area_scan_division', 0.0125, 0, 7.4e-6, 7.4e-6, \
                   Width/2.0, Height/2.0, Width, Height]
StartCamParam2 := StartCamParam1
Rows1 := []
Cols1 := []
StartPoses1 := []
Rows2 := []
Cols2 := []
StartPoses2 := []

* Find calibration marks and startposes.
for i := 0 to 11 by 1
  grab_image_async (Image1, AcqHandle1, -1)
  grab_image_async (Image2, AcqHandle2, -1)
  find_caltab (Image1, CalPlate1, 'caltab_30mm.descr', 3, 120, 5)
  find_caltab (Image2, CalPlate2, 'caltab_30mm.descr', 3, 120, 5)
  find_marks_and_pose (Image1, CalPlate1, 'caltab_30mm.descr', \
                       StartCamParam1, 128, 10, 20, 0.7, 5, 100, \
                       RCoord1, CCoord1, StartPose1)
  Rows1 := [Rows1,RCoord1]
  Cols1 := [Cols1,CCoord1]
  StartPoses1 := [StartPoses1,StartPose1]
  find_marks_and_pose (Image2, CalPlate2, 'caltab_30mm.descr', \
                       StartCamParam2, 128, 10, 20, 0.7, 5, 100, \
                       RCoord2, CCoord2, StartPose2)
  Rows2 := [Rows2,RCoord2]
  Cols2 := [Cols2,CCoord2]
  StartPoses2 := [StartPoses2,StartPose2]
endfor

* Calibrate the stereo rig.
binocular_calibration (X, Y, Z, Rows1, Cols1, Rows2, Cols2, StartCamParam1, \
                       StartCamParam2, StartPoses1, StartPoses2, 'all', \
                       CamParam1, CamParam2, NFinalPose1, NFinalPose2, \
                       RelPose, Errors)
* Archive the results.
write_cam_par (CamParam1, 'cam_left-125.dat')
write_cam_par (CamParam2, 'cam_right-125.dat')
write_pose (RelPose, 'rel_pose.dat')

* Rectify the stereo images.
gen_binocular_rectification_map (Map1, Map2, CamParam1, CamParam2, \
                                 RelPose, 1, 'viewing_direction', 'bilinear', \
                                 CamParamRect1, CamParamRect2, \
                                 CamPoseRect1, CamPoseRect2, \
                                 RelPoseRect)
map_image (Image1, Map1, ImageMapped1)
map_image (Image2, Map2, ImageMapped2)
```

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
