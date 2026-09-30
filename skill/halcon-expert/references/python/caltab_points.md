# caltab_points (Operator)

## Name

`caltab_points` — Read the mark center points from the calibration plate description file.

## Signature

`def caltab_points(cal_plate_descr: str) -> Tuple[Sequence[float], Sequence[float], Sequence[float]]`

## Description

`caltab_points` reads the mark center points from the calibration plate
description file *`cal_plate_descr`* (see [`gen_caltab`](gen_caltab.md) for
calibration plates with rectangularly arranged marks and [`create_caltab`](create_caltab.md)
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
operator [`camera_calibration`](camera_calibration.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`cal_plate_descr`** (input_control)  filename.read `→` str

File name of the calibration plate description.

Default:
"calplate_320mm.cpd"

List of values:
"calplate_10mm.cpd", "calplate_1200mm.cpd", "calplate_160mm.cpd", "calplate_20mm.cpd", "calplate_20mm_dark_on_light.cpd", "calplate_320mm.cpd", "calplate_40mm.cpd", "calplate_40mm_dark_on_light.cpd", "calplate_5mm.cpd", "calplate_640mm.cpd", "calplate_80mm.cpd", "calplate_80mm_dark_on_light.cpd", "caltab_100mm.descr", "caltab_10mm.descr", "caltab_200mm.descr", "caltab_2500um.descr", "caltab_30mm.descr", "caltab_650um.descr", "caltab_6mm.descr", "caltab_800mm.descr", "caltab_big.descr", "caltab_small.descr"

File extension:
.`cpd`, .`descr`

**`x`** (output_control)  real-array `→` Sequence[float]

X coordinates of the mark center points in the
coordinate system of the calibration plate.

**`y`** (output_control)  real-array `→` Sequence[float]

Y coordinates of the mark center points in the
coordinate system of the calibration plate.

**`z`** (output_control)  real-array `→` Sequence[float]

Z coordinates of the mark center points in the
coordinate system of the calibration plate.

## Result

`caltab_points` returns 2 (
H_MSG_TRUE)
if all parameter values are
correct and the file *`cal_plate_descr`* has been read
successfully. If necessary, an exception is raised.

## Possible Successors

`camera_calibration`

## See also

`find_caltab`,
`find_marks_and_pose`,
`camera_calibration`,
`disp_caltab`,
`sim_caltab`,
`project_3d_point`,
`get_line_of_sight`,
`gen_caltab`

## Module

Foundation
