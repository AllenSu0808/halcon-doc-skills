# read_cam_par (Operator)

## Name

`read_cam_par` — Read internal camera parameters from a file.

## Signature

`read_cam_par( : : CamParFile : CameraParam)`

## Description

`read_cam_par` reads the internal camera parameters
*`CameraParam`* from a file with name *`CamParFile`*. The
file must have been written by [`write_cam_par`](write_cam_par.md).

The default HALCON file extension for the camera parameters is
'dat'.

The number of values in *`CameraParam`* depends on the
specified camera type. See the description of
[`set_calib_data_cam_param`](set_calib_data_cam_param.md) for a list of values and the chapter
[Calibration](toc_calibration.md) for details on camera types and camera
parameters.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`CamParFile`** (input_control)  filename.read `→`  (string)

File name of internal camera parameters.

Default:
'campar.dat'

List of values:
'campar.dat', 'campar.final', 'campar.initial'

File extension:
.`dat`

**`CameraParam`** (output_control)  campar `→`  (real / integer / string)

Internal camera parameters.

## Example (HDevelop)

```
* Create sample camera parameters and write them to file.
gen_cam_par_area_scan_division (0.01, -731, 5.2e-006, 5.2e-006, \
                                654, 519, 1280, 1024, CameraParamTmp)
write_cam_par (CameraParamTmp, 'campar_tmp.dat')
* Read internal camera parameters.
read_cam_par('campar_tmp.dat', CameraParam)
```

## Result

`read_cam_par` returns 2 (
H_MSG_TRUE)
if all parameter values are
correct and the file has been read successfully. If necessary an
exception is raised.

## Possible Successors

`find_marks_and_pose`,
`sim_caltab`,
`gen_caltab`,
`disp_caltab`,
`camera_calibration`

## See also

`find_caltab`,
`find_marks_and_pose`,
`camera_calibration`,
`disp_caltab`,
`sim_caltab`,
`write_cam_par`,
`write_pose`,
`read_pose`,
`project_3d_point`,
`get_line_of_sight`

## Module

Foundation
