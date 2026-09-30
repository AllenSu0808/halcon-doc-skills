# read_cam_par (Operator)

## Name

`read_cam_par` — Read internal camera parameters from a file.

## Signature

`def read_cam_par(cam_par_file: str) -> Sequence[Union[int, float, str]]`

## Description

`read_cam_par` reads the internal camera parameters
*`camera_param`* from a file with name *`cam_par_file`*. The
file must have been written by [`write_cam_par`](write_cam_par.md).

The default HALCON file extension for the camera parameters is
'dat'.

The number of values in *`camera_param`* depends on the
specified camera type. See the description of
[`set_calib_data_cam_param`](set_calib_data_cam_param.md) for a list of values and the chapter
[Calibration](toc_calibration.md) for details on camera types and camera
parameters.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`cam_par_file`** (input_control)  filename.read `→` str

File name of internal camera parameters.

Default:
"campar.dat"

List of values:
"campar.dat", "campar.final", "campar.initial"

File extension:
.`dat`

**`camera_param`** (output_control)  campar `→` Sequence[Union[int, float, str]]

Internal camera parameters.

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
