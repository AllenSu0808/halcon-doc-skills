# sim_caltab (Operator)

## Name

`sim_caltab` — Simulate an image with calibration plate.

## Signature

`sim_caltab( : SimImage : CalPlateDescr, CameraParam, CalPlatePose, GrayBackground, GrayPlate, GrayMarks, ScaleFac : )`

## Description

`sim_caltab` is used to generate a simulated calibration
image. The calibration plate description is read from the file
*`CalPlateDescr`* and will be projected into the image plane
using the given camera parameters, thus internal camera parameters
*`CameraParam`* and external camera parameters
*`CalPlatePose`* (see also [`project_3d_point`](project_3d_point.md)).
Thereby the pose is expected to be in the form
$\mathrm{CCS} P_{\mathrm{wcs}}$ ![figure](../assets/4c18b1c4fb564c93.svg), where
*ccs* denotes the camera coordinate system and
*wcs* the world coordinate system (see
[Transformations / Poses](toc_transformations_poses.md)
and `“Solution Guide III-C - 3D Vision”`).

In the simulated image only the calibration plate is shown. The
image background is set to the gray value *`GrayBackground`*,
the calibration plate background is set to *`GrayPlate`*, and
the calibration marks are set to the gray value *`GrayMarks`*.
The parameter *`ScaleFac`* influences the number of supporting
points to approximate the elliptic contours of the calibration
marks, see also [`disp_caltab`](disp_caltab.md). Increasing the number of
supporting points causes a more accurate determination of the mark
boundary, but increases the computation time, too. For each pixel
of the simulated image which touches a subpixel-boundary of this
kind, the gray value is set linearly between *`GrayMarks`* and
*`GrayPlate`* dependent on the proportion Inside/Outside.

By applying the operator `sim_caltab` you can generate
synthetic calibration images (with known camera parameters!) to test
the quality of the calibration algorithm (see
[Calibration](toc_calibration.md)).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`SimImage`** (output_object)  image `→` object (byte)

Simulated calibration image.

**`CalPlateDescr`** (input_control)  filename.read `→`  (string)

File name of the calibration plate description.

Default:
'calplate_320mm.cpd'

List of values:
'calplate_10mm.cpd', 'calplate_1200mm.cpd', 'calplate_160mm.cpd', 'calplate_20mm.cpd', 'calplate_20mm_dark_on_light.cpd', 'calplate_320mm.cpd', 'calplate_40mm.cpd', 'calplate_40mm_dark_on_light.cpd', 'calplate_5mm.cpd', 'calplate_640mm.cpd', 'calplate_80mm.cpd', 'calplate_80mm_dark_on_light.cpd', 'caltab_100mm.descr', 'caltab_10mm.descr', 'caltab_200mm.descr', 'caltab_2500um.descr', 'caltab_30mm.descr', 'caltab_650um.descr', 'caltab_6mm.descr', 'caltab_800mm.descr', 'caltab_big.descr', 'caltab_small.descr'

File extension:
.`cpd`, .`descr`

**`CameraParam`** (input_control)  campar `→`  (real / integer / string)

Internal camera parameters.

**`CalPlatePose`** (input_control)  pose `→`  (real / integer)

External camera parameters (3D pose of the calibration
plate in camera coordinates).

Number of elements:
7

**`GrayBackground`** (input_control)  integer `→`  (integer)

Gray value of image background.

Default:
128

Suggested values:
0, 32, 64, 96, 128, 160

Restriction:
`0 <= GrayBackground <= 255`

**`GrayPlate`** (input_control)  integer `→`  (integer)

Gray value of calibration plate.

Default:
80

Suggested values:
144, 160, 176, 192, 208, 224, 240

Restriction:
`0 <= GrayPlate <= 255`

**`GrayMarks`** (input_control)  integer `→`  (integer)

Gray value of calibration marks.

Default:
224

Suggested values:
16, 32, 48, 64, 80, 96, 112

Restriction:
`0 <= GrayMarks <= 255`

**`ScaleFac`** (input_control)  real `→`  (real)

Scaling factor to reduce oversampling.

Default:
1.0

Suggested values:
1.0, 0.5, 0.25, 0.125

Recommended increment:
0.05

Restriction:
`1.0 >= ScaleFac`

## Example (HDevelop)

```
* Read calibration image.
read_image(Image1, 'calib-01')
* Find calibration pattern.
CameraType := 'area_scan_division'
StartCamPar := [CameraType, Focus, Kappa, Sx, Sy, Cx, Cy, \
                ImageWidth, ImageHeight]
create_calib_data ('calibration_object', 1, 1, CalibDataID)
set_calib_data_cam_param (CalibDataID, 0, [], StartCamPar)
set_calib_data_calib_object (CalibDataID, 0, 'calplate.cpd')
find_caltab(Image1, CalPlate1, 'caltab.descr', 3, 112, 5)
* Find calibration marks and initial pose.
find_calib_object (Image1, CalibDataID, 0, 0, 0, [], [])
* Camera calibration.
calibrate_cameras (CalibDataID, Error)
* Simulate calibration image.
get_calib_data (CalibDataID, 'calib_obj_pose', [0, 0], 'pose', FinalPose)
get_calib_data (CalibDataID, 'camera', 0, 'params', CameraParam)
sim_caltab(Image1Sim, 'calplate.cpd', CameraParam, FinalPose, 128, \
           80, 224, 1)
```

## Result

`sim_caltab` returns 2 (
H_MSG_TRUE)
if all parameter values are
correct. If necessary, an exception is raised.

## Possible Predecessors

`camera_calibration`,
`find_marks_and_pose`,
`read_pose`,
`read_cam_par`,
`hom_mat3d_to_pose`

## Possible Successors

`find_caltab`

## See also

`find_caltab`,
`find_marks_and_pose`,
`camera_calibration`,
`disp_caltab`,
`create_pose`,
`hom_mat3d_to_pose`,
`project_3d_point`,
`gen_caltab`

## Module

Calibration
