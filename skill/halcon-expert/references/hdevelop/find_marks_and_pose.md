# find_marks_and_pose (Operator)

## Name

`find_marks_and_pose` — Extract rectangularly arranged 2D calibration marks from the image and
calculate initial values for the external camera parameters.

## Signature

`find_marks_and_pose(Image, CalPlateRegion : : CalPlateDescr, StartCamParam, StartThresh, DeltaThresh, MinThresh, Alpha, MinContLength, MaxDiamMarks : RCoord, CCoord, StartPose)`

## Description

`find_marks_and_pose` is used to determine the
input data for a subsequent camera calibration using a calibration plate
with rectangularly arranged marks (see
[Calibration](toc_calibration.md) or [`camera_calibration`](camera_calibration.md)):
First, the 2D center points
[*`RCoord`*,*`CCoord`*] of the calibration marks within
the region *`CalPlateRegion`* of the input image *`Image`*
are extracted and ordered. Secondly, a rough estimate for
the external camera parameters (*`StartPose`*) is computed,
i.e., the 3D pose (= position and orientation) of the calibration plate
relative to the camera coordinate system (see [`create_pose`](create_pose.md) for more
information about 3D poses).

In the input image *`Image`* an edge detector is applied
(see [`edges_image`](edges_image.md), mode 'lanser2') to the region
*`CalPlateRegion`*,
which can be found by applying the operator [`find_caltab`](find_caltab.md).
The filter parameter for this edge detection can be tuned via
*`Alpha`*. Use a smaller value for *`Alpha`* to achieve
a stronger smoothing effect.
In the edge image closed contours are searched for: The number of
closed contours must correspond to the number of calibration marks
as described in the calibration plate description file
*`CalPlateDescr`* and the contours have to be elliptically shaped.
Contours shorter than *`MinContLength`* are discarded,
just as contours enclosing regions with a diameter larger than
*`MaxDiamMarks`* (e.g., the border of the calibration plate).

For the detection of contours a threshold operator is applied
on the resulting amplitudes of the edge detector.
All points with a high amplitude (i.e., borders of marks)
are selected.

First, the threshold value is set to
*`StartThresh`*. If the search for the closed contours or the
successive pose estimate fails, this threshold value is successively
decreased by *`DeltaThresh`* down to a minimum value of
*`MinThresh`*.

Each of the found contours is refined with subpixel accuracy (see
[`edges_sub_pix`](edges_sub_pix.md)) and
subsequently approximated by an ellipse. The center points of these
ellipses represent a good approximation of the desired 2D image coordinates
[*`RCoord`*,*`CCoord`*] of the calibration mark center points.
The order of the values within these two tuples must correspond to
the order of the 3D coordinates of the calibration marks in the calibration
plate description file *`CalPlateDescr`*, since this fixes the
correspondences between extracted image marks and known model marks
(given by [`caltab_points`](caltab_points.md))! If a
triangular orientation mark is defined in a corner of the plate by the
plate description file (see [`gen_caltab`](gen_caltab.md)), the mark will be detected
and the point order is returned in row-major order beginning with the
corner mark in the (barycentric) negative quadrant with respect to the
defined coordinate system of the plate. Else, if no orientation mark is
defined, the order of the center points is in row-major order beginning at
the upper left corner mark in the image.

Based on the ellipse parameters for each calibration mark, a rough
estimate for the external camera parameters is finally computed.
For this purpose the fixed correspondences between extracted image marks
and known model marks are used. The estimate *`StartPose`*
describes the pose of the calibration plate in the camera coordinate
system as required by the operator [`camera_calibration`](camera_calibration.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Image`** (input_object)  singlechannelimage `→` object (byte / uint2)

Input image.

**`CalPlateRegion`** (input_object)  region `→` object

Region of the calibration plate.

**`CalPlateDescr`** (input_control)  filename.read `→`  (string)

File name of the calibration plate description.

Default:
'caltab_100.descr'

List of values:
'caltab_100mm.descr', 'caltab_10mm.descr', 'caltab_200mm.descr', 'caltab_2500um.descr', 'caltab_30mm.descr', 'caltab_650um.descr', 'caltab_6mm.descr', 'caltab_800mm.descr', 'caltab_big.descr', 'caltab_small.descr'

File extension:
.`descr`

**`StartCamParam`** (input_control)  campar `→`  (real / integer / string)

Initial values for the internal camera parameters.

**`StartThresh`** (input_control)  number `→`  (integer)

Initial threshold value for contour detection.

Default:
128

Suggested values:
80, 96, 112, 128, 144, 160

Restriction:
`StartThresh > 0`

**`DeltaThresh`** (input_control)  number `→`  (integer)

Loop value for successive reduction of
*`StartThresh`*.

Default:
10

Suggested values:
6, 8, 10, 12, 14, 16, 18, 20, 22

Restriction:
`DeltaThresh > 0`

**`MinThresh`** (input_control)  number `→`  (integer)

Minimum threshold for contour detection.

Default:
18

Suggested values:
8, 10, 12, 14, 16, 18, 20, 22

Restriction:
`MinThresh > 0`

**`Alpha`** (input_control)  real `→`  (real)

Filter parameter for contour detection, see
[`edges_image`](edges_image.md).

Default:
0.9

Suggested values:
0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1

Value range:
`0.2
≤
Alpha
≤
2.0`

Restriction:
`Alpha > 0.0`

**`MinContLength`** (input_control)  real `→`  (real)

Minimum length of the contours of the marks.

Default:
15.0

Suggested values:
10.0, 15.0, 20.0, 30.0, 40.0, 100.0

Restriction:
`MinContLength > 0.0`

**`MaxDiamMarks`** (input_control)  real `→`  (real)

Maximum expected diameter of the marks.

Default:
100.0

Suggested values:
50.0, 100.0, 150.0, 200.0, 300.0

Restriction:
`MaxDiamMarks > 0.0`

**`RCoord`** (output_control)  real-array `→`  (real)

Tuple with row coordinates of the detected marks.

**`CCoord`** (output_control)  real-array `→`  (real)

Tuple with column coordinates of the detected marks.

**`StartPose`** (output_control)  pose `→`  (real / integer)

Estimation for the external camera parameters.

Number of elements:
7

## Example (HDevelop)

```
* Read calibration image.
read_image(Image, 'calib/calib_distorted_01')
* Find calibration pattern.
find_caltab(Image,CalPlate, 'caltab_100mm.descr', 3, 112, 5)
* Find calibration marks and start pose.
find_marks_and_pose(Image, CalPlate, 'caltab_100mm.descr' , \
                    ['area_scan_division', 0.008, 0.0, \
                     0.000011, 0.000011, 384, 288, 640, 512], \
                    128, 10, 18, 0.9, 15.0, 100.0, RCoord, CCoord, StartPose)
```

## Result

`find_marks_and_pose` returns 2 (
H_MSG_TRUE)
if all parameter values are
correct and an estimation for the external camera parameters has been
determined successfully. If necessary, an exception is raised.

## Possible Predecessors

`find_caltab`

## Possible Successors

`camera_calibration`

## See also

`find_caltab`,
`camera_calibration`,
`disp_caltab`,
`sim_caltab`,
`read_cam_par`,
`read_pose`,
`create_pose`,
`pose_to_hom_mat3d`,
`caltab_points`,
`gen_caltab`,
`edges_sub_pix`,
`edges_image`

## Module

Foundation
