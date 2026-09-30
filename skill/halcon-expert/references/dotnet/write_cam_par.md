# WriteCamPar (Operator)

## Name

`WriteCamPar` — Write internal camera parameters into a file.

## Signature

`static void HOperatorSet.WriteCamPar(HTuple cameraParam, HTuple camParFile)`

`void HCamPar.WriteCamPar(string camParFile)`

## Description

`WriteCamPar` stores the internal camera parameters
*`cameraParam`* into a file specified by its file name
*`camParFile`*.

The number of values in *`cameraParam`* depends on the
specified camera type. See the description of
[`SetCalibDataCamParam`](set_calib_data_cam_param.md) for a list of values and the chapter
[Calibration](toc_calibration.md) for details on camera types and camera
parameters.

The default HALCON file extension for the camera parameters is
'dat'.

The internal camera parameters can be later read with
[`ReadCamPar`](read_cam_par.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`cameraParam`** (input_control)  campar `→` [HCamPar](HCamPar.md), [HTuple](HTuple.md) (*double* / int / long / string)

Internal camera parameters.

**`camParFile`** (input_control)  filename.write `→` [HTuple](HTuple.md) (*string*)

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

`WriteCamPar` returns 2 (
H_MSG_TRUE)
if all parameter values are
correct and the file has been written successfully. If necessary an
exception is raised.

## Possible Predecessors

`CameraCalibration`

## See also

`FindCaltab`,
`FindMarksAndPose`,
`CameraCalibration`,
`DispCaltab`,
`SimCaltab`,
`ReadCamPar`,
`WritePose`,
`ReadPose`,
`Project3dPoint`,
`GetLineOfSight`

## Module

Foundation
