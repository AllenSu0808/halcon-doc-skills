# CaltabPoints (Operator)

## Name

`CaltabPoints` — Read the mark center points from the calibration plate description file.

## Signature

`static void HOperatorSet.CaltabPoints(HTuple calPlateDescr, out HTuple x, out HTuple y, out HTuple z)`

`static void HMisc.CaltabPoints(string calPlateDescr, out HTuple x, out HTuple y, out HTuple z)`

## Description

`CaltabPoints` reads the mark center points from the calibration plate
description file *`calPlateDescr`* (see [`GenCaltab`](gen_caltab.md) for
calibration plates with rectangularly arranged marks and [`CreateCaltab`](create_caltab.md)
for calibration plates with hexagonally arranged marks) and
returns their coordinates in *`x`*, *`y`* and *`z`*. The mark
center points are 3D coordinates in the calibration plate coordinate system
and describe the 3D model of the calibration plate. The calibration plate
coordinate system is located in the middle of the surface of the calibration
plate for calibration plates with rectangularly arranged marks and at the
center of the central mark of the first finder pattern for calibration plates
with hexagonally arranged marks. Its z-axis points into the calibration
plate, its x-axis to the right, and its y-axis downwards.

The mark center points are typically used as input parameters for the
operator [`CameraCalibration`](camera_calibration.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`calPlateDescr`** (input_control)  filename.read `→` [HTuple](HTuple.md) (*string*)

File name of the calibration plate description.

Default:
"calplate_320mm.cpd"

List of values:
"calplate_10mm.cpd", "calplate_1200mm.cpd", "calplate_160mm.cpd", "calplate_20mm.cpd", "calplate_20mm_dark_on_light.cpd", "calplate_320mm.cpd", "calplate_40mm.cpd", "calplate_40mm_dark_on_light.cpd", "calplate_5mm.cpd", "calplate_640mm.cpd", "calplate_80mm.cpd", "calplate_80mm_dark_on_light.cpd", "caltab_100mm.descr", "caltab_10mm.descr", "caltab_200mm.descr", "caltab_2500um.descr", "caltab_30mm.descr", "caltab_650um.descr", "caltab_6mm.descr", "caltab_800mm.descr", "caltab_big.descr", "caltab_small.descr"

File extension:
.`cpd`, .`descr`

**`x`** (output_control)  real-array `→` [HTuple](HTuple.md) (*double*)

X coordinates of the mark center points in the
coordinate system of the calibration plate.

**`y`** (output_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Y coordinates of the mark center points in the
coordinate system of the calibration plate.

**`z`** (output_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Z coordinates of the mark center points in the
coordinate system of the calibration plate.

## Example (HDevelop)

```
* Read calibration image.
read_image(Image, 'calib/calib-3d-coord-03')
CalTabDescr := 'caltab_100mm.descr'
* Find calibration pattern.
find_caltab(Image, CalPlate1, CalTabDescr, 3, 112, 5)
* Find calibration marks and start poses.
StartCamPar := ['area_scan_division', 0.008, 0.0, 0.000011, 0.000011, \
                384, 288, 768, 576]
find_marks_and_pose(Image,CalPlate1,CalTabDescr, StartCamPar, \
                    128, 10, 18, 0.9, 15.0, 100.0, RCoord1, CCoord1, \
                    StartPose1)
* Read 3D positions of calibration marks.
caltab_points(CalTabDescr, NX, NY, NZ)
*  Calibrate camera.
camera_calibration(NX, NY, NZ, RCoord1, CCoord1, StartCamPar, \
                   StartPose1, 'all', CameraParam, FinalPose, Errors)
*  Visualize calibration result.
dev_display(Image)
disp_caltab(WindowHandle, CalTabDescr, CameraParam, FinalPose, 1.0)
```

## Result

`CaltabPoints` returns 2 (
H_MSG_TRUE)
if all parameter values are
correct and the file *`calPlateDescr`* has been read
successfully. If necessary, an exception is raised.

## Possible Successors

`CameraCalibration`

## See also

`FindCaltab`,
`FindMarksAndPose`,
`CameraCalibration`,
`DispCaltab`,
`SimCaltab`,
`Project3dPoint`,
`GetLineOfSight`,
`GenCaltab`

## Module

Foundation
