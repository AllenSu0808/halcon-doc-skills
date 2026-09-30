# FindMarksAndPose (Operator)

## Name

`FindMarksAndPose` — Extract rectangularly arranged 2D calibration marks from the image and
calculate initial values for the external camera parameters.

## Signature

`static void HOperatorSet.FindMarksAndPose(HObject image, HObject calPlateRegion, HTuple calPlateDescr, HTuple startCamParam, HTuple startThresh, HTuple deltaThresh, HTuple minThresh, HTuple alpha, HTuple minContLength, HTuple maxDiamMarks, out HTuple RCoord, out HTuple CCoord, out HTuple startPose)`

`HTuple HImage.FindMarksAndPose(HRegion calPlateRegion, string calPlateDescr, HCamPar startCamParam, int startThresh, int deltaThresh, int minThresh, double alpha, double minContLength, double maxDiamMarks, out HTuple CCoord, out HPose startPose)`

`HTuple HCamPar.FindMarksAndPose(HImage image, HRegion calPlateRegion, string calPlateDescr, int startThresh, int deltaThresh, int minThresh, double alpha, double minContLength, double maxDiamMarks, out HTuple CCoord, out HPose startPose)`

`HTuple HPose.FindMarksAndPose(HImage image, HRegion calPlateRegion, string calPlateDescr, HCamPar startCamParam, int startThresh, int deltaThresh, int minThresh, double alpha, double minContLength, double maxDiamMarks, out HTuple CCoord)`

## Description

`FindMarksAndPose` is used to determine the
input data for a subsequent camera calibration using a calibration plate
with rectangularly arranged marks (see
[Calibration](toc_calibration.md) or [`CameraCalibration`](camera_calibration.md)):
First, the 2D center points
[*`RCoord`*,*`CCoord`*] of the calibration marks within
the region *`calPlateRegion`* of the input image *`image`*
are extracted and ordered. Secondly, a rough estimate for
the external camera parameters (*`startPose`*) is computed,
i.e., the 3D pose (= position and orientation) of the calibration plate
relative to the camera coordinate system (see [`CreatePose`](create_pose.md) for more
information about 3D poses).

In the input image *`image`* an edge detector is applied
(see [`EdgesImage`](edges_image.md), mode 'lanser2') to the region
*`calPlateRegion`*,
which can be found by applying the operator [`FindCaltab`](find_caltab.md).
The filter parameter for this edge detection can be tuned via
*`alpha`*. Use a smaller value for *`alpha`* to achieve
a stronger smoothing effect.
In the edge image closed contours are searched for: The number of
closed contours must correspond to the number of calibration marks
as described in the calibration plate description file
*`calPlateDescr`* and the contours have to be elliptically shaped.
Contours shorter than *`minContLength`* are discarded,
just as contours enclosing regions with a diameter larger than
*`maxDiamMarks`* (e.g., the border of the calibration plate).

For the detection of contours a threshold operator is applied
on the resulting amplitudes of the edge detector.
All points with a high amplitude (i.e., borders of marks)
are selected.

First, the threshold value is set to
*`startThresh`*. If the search for the closed contours or the
successive pose estimate fails, this threshold value is successively
decreased by *`deltaThresh`* down to a minimum value of
*`minThresh`*.

Each of the found contours is refined with subpixel accuracy (see
[`EdgesSubPix`](edges_sub_pix.md)) and
subsequently approximated by an ellipse. The center points of these
ellipses represent a good approximation of the desired 2D image coordinates
[*`RCoord`*,*`CCoord`*] of the calibration mark center points.
The order of the values within these two tuples must correspond to
the order of the 3D coordinates of the calibration marks in the calibration
plate description file *`calPlateDescr`*, since this fixes the
correspondences between extracted image marks and known model marks
(given by [`CaltabPoints`](caltab_points.md))! If a
triangular orientation mark is defined in a corner of the plate by the
plate description file (see [`GenCaltab`](gen_caltab.md)), the mark will be detected
and the point order is returned in row-major order beginning with the
corner mark in the (barycentric) negative quadrant with respect to the
defined coordinate system of the plate. Else, if no orientation mark is
defined, the order of the center points is in row-major order beginning at
the upper left corner mark in the image.

Based on the ellipse parameters for each calibration mark, a rough
estimate for the external camera parameters is finally computed.
For this purpose the fixed correspondences between extracted image marks
and known model marks are used. The estimate *`startPose`*
describes the pose of the calibration plate in the camera coordinate
system as required by the operator [`CameraCalibration`](camera_calibration.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`image`** (input_object)  singlechannelimage `→` [HImage](HImage.md) (byte / uint2)

Input image.

**`calPlateRegion`** (input_object)  region `→` [HRegion](HRegion.md)

Region of the calibration plate.

**`calPlateDescr`** (input_control)  filename.read `→` [HTuple](HTuple.md) (*string*)

File name of the calibration plate description.

Default:
"caltab_100.descr"

List of values:
"caltab_100mm.descr", "caltab_10mm.descr", "caltab_200mm.descr", "caltab_2500um.descr", "caltab_30mm.descr", "caltab_650um.descr", "caltab_6mm.descr", "caltab_800mm.descr", "caltab_big.descr", "caltab_small.descr"

File extension:
.`descr`

**`startCamParam`** (input_control)  campar `→` [HCamPar](HCamPar.md), [HTuple](HTuple.md) (*double* / int / long / string)

Initial values for the internal camera parameters.

**`startThresh`** (input_control)  number `→` [HTuple](HTuple.md) (*int* / long)

Initial threshold value for contour detection.

Default:
128

Suggested values:
80, 96, 112, 128, 144, 160

Restriction:
`StartThresh > 0`

**`deltaThresh`** (input_control)  number `→` [HTuple](HTuple.md) (*int* / long)

Loop value for successive reduction of
*`startThresh`*.

Default:
10

Suggested values:
6, 8, 10, 12, 14, 16, 18, 20, 22

Restriction:
`DeltaThresh > 0`

**`minThresh`** (input_control)  number `→` [HTuple](HTuple.md) (*int* / long)

Minimum threshold for contour detection.

Default:
18

Suggested values:
8, 10, 12, 14, 16, 18, 20, 22

Restriction:
`MinThresh > 0`

**`alpha`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Filter parameter for contour detection, see
[`EdgesImage`](edges_image.md).

Default:
0.9

Suggested values:
0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1

Value range:
`0.2
≤
alpha
≤
2.0`

Restriction:
`Alpha > 0.0`

**`minContLength`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Minimum length of the contours of the marks.

Default:
15.0

Suggested values:
10.0, 15.0, 20.0, 30.0, 40.0, 100.0

Restriction:
`MinContLength > 0.0`

**`maxDiamMarks`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Maximum expected diameter of the marks.

Default:
100.0

Suggested values:
50.0, 100.0, 150.0, 200.0, 300.0

Restriction:
`MaxDiamMarks > 0.0`

**`RCoord`** (output_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Tuple with row coordinates of the detected marks.

**`CCoord`** (output_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Tuple with column coordinates of the detected marks.

**`startPose`** (output_control)  pose `→` [HPose](HPose.md), [HTuple](HTuple.md) (*double* / int / long)

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

`FindMarksAndPose` returns 2 (
H_MSG_TRUE)
if all parameter values are
correct and an estimation for the external camera parameters has been
determined successfully. If necessary, an exception is raised.

## Possible Predecessors

`FindCaltab`

## Possible Successors

`CameraCalibration`

## See also

`FindCaltab`,
`CameraCalibration`,
`DispCaltab`,
`SimCaltab`,
`ReadCamPar`,
`ReadPose`,
`CreatePose`,
`PoseToHomMat3d`,
`CaltabPoints`,
`GenCaltab`,
`EdgesSubPix`,
`EdgesImage`

## Module

Foundation
