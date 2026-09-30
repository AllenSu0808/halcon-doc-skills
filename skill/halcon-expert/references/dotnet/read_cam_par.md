# ReadCamPar (Operator)

## Name

`ReadCamPar` — Read internal camera parameters from a file.

## Signature

`static void HOperatorSet.ReadCamPar(HTuple camParFile, out HTuple cameraParam)`

`void HCamPar.ReadCamPar(string camParFile)`

## Description

`ReadCamPar` reads the internal camera parameters
*`cameraParam`* from a file with name *`camParFile`*. The
file must have been written by [`WriteCamPar`](write_cam_par.md).

The default HALCON file extension for the camera parameters is
'dat'.

The number of values in *`cameraParam`* depends on the
specified camera type. See the description of
[`SetCalibDataCamParam`](set_calib_data_cam_param.md) for a list of values and the chapter
[Calibration](toc_calibration.md) for details on camera types and camera
parameters.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`camParFile`** (input_control)  filename.read `→` [HTuple](HTuple.md) (*string*)

File name of internal camera parameters.

Default:
"campar.dat"

List of values:
"campar.dat", "campar.final", "campar.initial"

File extension:
.`dat`

**`cameraParam`** (output_control)  campar `→` [HCamPar](HCamPar.md), [HTuple](HTuple.md) (*double* / int / long / string)

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

`ReadCamPar` returns 2 (
H_MSG_TRUE)
if all parameter values are
correct and the file has been read successfully. If necessary an
exception is raised.

## Possible Successors

`FindMarksAndPose`,
`SimCaltab`,
`GenCaltab`,
`DispCaltab`,
`CameraCalibration`

## See also

`FindCaltab`,
`FindMarksAndPose`,
`CameraCalibration`,
`DispCaltab`,
`SimCaltab`,
`WriteCamPar`,
`WritePose`,
`ReadPose`,
`Project3dPoint`,
`GetLineOfSight`

## Module

Foundation
