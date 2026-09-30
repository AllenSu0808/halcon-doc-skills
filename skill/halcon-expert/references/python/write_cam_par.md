# write_cam_par (Operator)

## Name

`write_cam_par` — Write internal camera parameters into a file.

## Signature

`def write_cam_par(camera_param: Sequence[Union[int, float, str]], cam_par_file: str) -> None`

## Description

`write_cam_par` stores the internal camera parameters
*`camera_param`* into a file specified by its file name
*`cam_par_file`*.

The number of values in *`camera_param`* depends on the
specified camera type. See the description of
[`set_calib_data_cam_param`](set_calib_data_cam_param.md) for a list of values and the chapter
[Calibration](toc_calibration.md) for details on camera types and camera
parameters.

The default HALCON file extension for the camera parameters is
'dat'.

The internal camera parameters can be later read with
[`read_cam_par`](read_cam_par.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`camera_param`** (input_control)  campar `→` Sequence[Union[int, float, str]]

Internal camera parameters.

**`cam_par_file`** (input_control)  filename.write `→` str

File name of internal camera parameters.

Default:
"campar.dat"

List of values:
"campar.dat", "campar.final", "campar.initial"

File extension:
.`dat`

## Example (HDevelop)

```
*
* Calibrate the camera.
*
StartCamPar := ['area_scan_division', 0.016, 0, 0.0000074, 0.0000074, \
                326, 247, 652, 494]
create_calib_data ('calibration_object', 1, 1, CalibDataID)
set_calib_data_cam_param (CalibDataID, 0, [], StartCamPar)
set_calib_data_calib_object (CalibDataID, 0, 'caltab_30mm.descr')
NumImages := 10
for I := 1 to NumImages by 1
  read_image (Image, '3d_machine_vision/calib/calib_' + I$'02d')
  find_calib_object (Image, CalibDataID, 0, 0, I, [], [])
  get_calib_data_observ_contours (Caltab, CalibDataID, 'caltab', 0, 0, I)
endfor
calibrate_cameras (CalibDataID, Error)
get_calib_data (CalibDataID, 'camera', 0, 'params', CamParam)
* Write the internal camera parameters to a file.
write_cam_par (CamParam, 'camera_parameters.dat')
```

## Result

`write_cam_par` returns 2 (
H_MSG_TRUE)
if all parameter values are
correct and the file has been written successfully. If necessary an
exception is raised.

## Possible Predecessors

`camera_calibration`

## See also

`find_caltab`,
`find_marks_and_pose`,
`camera_calibration`,
`disp_caltab`,
`sim_caltab`,
`read_cam_par`,
`write_pose`,
`read_pose`,
`project_3d_point`,
`get_line_of_sight`

## Module

Foundation
