# disp_caltab (Operator)

## Name

`disp_caltab` — Project and visualize the 3D model of the calibration plate in the image.

## Signature

`def disp_caltab(window_handle: HHandle, cal_plate_descr: str, camera_param: Sequence[Union[int, float, str]], cal_plate_pose: Sequence[Union[int, float]], scale_fac: float) -> None`

## Description

`disp_caltab` is used to visualize the calibration marks and
the connecting lines between the marks of the used calibration plate
(*`cal_plate_descr`*) in the window specified by
*`window_handle`*. Additionally, the x- and y-axes of the
plate's coordinate system are printed on the plate's surface. For
this, the 3D model of the calibration plate is projected into the
image plane using the internal (*`camera_param`*) and external
camera parameters (*`cal_plate_pose`*). Thereby the pose is in the form
$\mathrm{CCS} P_{\mathrm{wcs}}$ ![figure](../assets/4c18b1c4fb564c93.svg), where
*ccs* denotes the camera coordinate system and
*wcs* the world coordinate system (see
[Transformations / Poses](toc_transformations_poses.md)
and `“Solution Guide III-C - 3D Vision”`), thus
the pose of the calibration plate in camera coordinates.
The underlying camera model is described in
[Calibration](toc_calibration.md).

Typically, `disp_caltab` is used to verify the result of the
camera calibration (see [Calibration](toc_calibration.md) or
[`camera_calibration`](camera_calibration.md)) by superimposing it onto the original
image. The current line width can be set by [`set_line_width`](set_line_width.md),
the current color can be set by [`set_color`](set_color.md). Additionally, the
font type of the labels of the coordinate axes can be set by
[`set_font`](set_font.md).

The parameter *`scale_fac`* influences the number of supporting
points to approximate the elliptic contours of the calibration
marks. You should increase the number of supporting points, if the
image part in the output window is displayed with magnification (see
[`set_part`](set_part.md)).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`window_handle`** (input_control)  window `→` HHandle

Window in which the calibration plate should be
visualized.

**`cal_plate_descr`** (input_control)  filename.read `→` str

File name of the calibration plate description.

Default:
"calplate_320.cpd"

List of values:
"calplate_10mm.cpd", "calplate_1200mm.cpd", "calplate_160mm.cpd", "calplate_20mm.cpd", "calplate_20mm_dark_on_light.cpd", "calplate_320mm.cpd", "calplate_40mm.cpd", "calplate_40mm_dark_on_light.cpd", "calplate_5mm.cpd", "calplate_640mm.cpd", "calplate_80mm.cpd", "calplate_80mm_dark_on_light.cpd", "caltab_100mm.descr", "caltab_10mm.descr", "caltab_200mm.descr", "caltab_2500um.descr", "caltab_30mm.descr", "caltab_650um.descr", "caltab_6mm.descr", "caltab_800mm.descr", "caltab_big.descr", "caltab_small.descr"

File extension:
.`cpd`, .`descr`

**`camera_param`** (input_control)  campar `→` Sequence[Union[int, float, str]]

Internal camera parameters.

**`cal_plate_pose`** (input_control)  pose `→` Sequence[Union[int, float]]

External camera parameters (3D pose of the calibration
plate in camera coordinates).

Number of elements:
7

**`scale_fac`** (input_control)  real `→` float

Scaling factor for the visualization.

Default:
1.0

Suggested values:
0.5, 1.0, 2.0, 3.0

Recommended increment:
0.05

Restriction:
`0.0 < ScaleFac`

## Example (HDevelop)

```
* Read image of calibration plate.
read_image (Image, 'calib/calib_single_camera_01')
get_image_size (Image, Width, Height)
* Create and setup the calibration model.
create_calib_data ('calibration_object', 1, 1, CalibDataID)
CalPlateDescr := 'calplate_80mm.cpd'
set_calib_data_calib_object (CalibDataID, 0, CalPlateDescr)
CamParam := ['area_scan_division', 0.008, -1500, 3.7e-6, 3.7e-6, \
             640, 470, 1292, 964]
set_calib_data_cam_param (CalibDataID, 0, [], CamParam)
* Localize calibration plate in the image.
find_calib_object (Image, CalibDataID, 0, 0, 0, [], [])
get_calib_data_observ_pose (CalibDataID, 0, 0, 0, StartPose)
* Display calibration plate.
disp_caltab (WindowHandle, CalPlateDescr, CamParam, StartPose, 1)
```

## Result

`disp_caltab` returns 2 (
H_MSG_TRUE)
if all parameter values are
correct. If necessary, an exception is raised.

## Possible Predecessors

`camera_calibration`,
`read_cam_par`,
`read_pose`

## See also

`find_marks_and_pose`,
`camera_calibration`,
`sim_caltab`,
`write_cam_par`,
`read_cam_par`,
`create_pose`,
`write_pose`,
`read_pose`,
`project_3d_point`,
`get_line_of_sight`

## Module

Foundation
