# find_marks_and_pose (Operator)

## Name

`find_marks_and_pose` — Extract rectangularly arranged 2D calibration marks from the image and
calculate initial values for the external camera parameters.

## Signature

`def find_marks_and_pose(image: HObject, cal_plate_region: HObject, cal_plate_descr: str, start_cam_param: Sequence[Union[int, float, str]], start_thresh: int, delta_thresh: int, min_thresh: int, alpha: float, min_cont_length: float, max_diam_marks: float) -> Tuple[Sequence[float], Sequence[float], Sequence[Union[float, int]]]`

## Description

`find_marks_and_pose` is used to determine the
input data for a subsequent camera calibration using a calibration plate
with rectangularly arranged marks (see
[Calibration](toc_calibration.md) or [`camera_calibration`](camera_calibration.md)):
First, the 2D center points
[*`rcoord`*,*`ccoord`*] of the calibration marks within
the region *`cal_plate_region`* of the input image *`image`*
are extracted and ordered. Secondly, a rough estimate for
the external camera parameters (*`start_pose`*) is computed,
i.e., the 3D pose (= position and orientation) of the calibration plate
relative to the camera coordinate system (see [`create_pose`](create_pose.md) for more
information about 3D poses).

In the input image *`image`* an edge detector is applied
(see [`edges_image`](edges_image.md), mode 'lanser2') to the region
*`cal_plate_region`*,
which can be found by applying the operator [`find_caltab`](find_caltab.md).
The filter parameter for this edge detection can be tuned via
*`alpha`*. Use a smaller value for *`alpha`* to achieve
a stronger smoothing effect.
In the edge image closed contours are searched for: The number of
closed contours must correspond to the number of calibration marks
as described in the calibration plate description file
*`cal_plate_descr`* and the contours have to be elliptically shaped.
Contours shorter than *`min_cont_length`* are discarded,
just as contours enclosing regions with a diameter larger than
*`max_diam_marks`* (e.g., the border of the calibration plate).

For the detection of contours a threshold operator is applied
on the resulting amplitudes of the edge detector.
All points with a high amplitude (i.e., borders of marks)
are selected.

First, the threshold value is set to
*`start_thresh`*. If the search for the closed contours or the
successive pose estimate fails, this threshold value is successively
decreased by *`delta_thresh`* down to a minimum value of
*`min_thresh`*.

Each of the found contours is refined with subpixel accuracy (see
[`edges_sub_pix`](edges_sub_pix.md)) and
subsequently approximated by an ellipse. The center points of these
ellipses represent a good approximation of the desired 2D image coordinates
[*`rcoord`*,*`ccoord`*] of the calibration mark center points.
The order of the values within these two tuples must correspond to
the order of the 3D coordinates of the calibration marks in the calibration
plate description file *`cal_plate_descr`*, since this fixes the
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
and known model marks are used. The estimate *`start_pose`*
describes the pose of the calibration plate in the camera coordinate
system as required by the operator [`camera_calibration`](camera_calibration.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`image`** (input_object)  singlechannelimage `→` HObject (byte / uint2)

Input image.

**`cal_plate_region`** (input_object)  region `→` HObject

Region of the calibration plate.

**`cal_plate_descr`** (input_control)  filename.read `→` str

File name of the calibration plate description.

Default:
"caltab_100.descr"

List of values:
"caltab_100mm.descr", "caltab_10mm.descr", "caltab_200mm.descr", "caltab_2500um.descr", "caltab_30mm.descr", "caltab_650um.descr", "caltab_6mm.descr", "caltab_800mm.descr", "caltab_big.descr", "caltab_small.descr"

File extension:
.`descr`

**`start_cam_param`** (input_control)  campar `→` Sequence[Union[int, float, str]]

Initial values for the internal camera parameters.

**`start_thresh`** (input_control)  number `→` int

Initial threshold value for contour detection.

Default:
128

Suggested values:
80, 96, 112, 128, 144, 160

Restriction:
`StartThresh > 0`

**`delta_thresh`** (input_control)  number `→` int

Loop value for successive reduction of
*`start_thresh`*.

Default:
10

Suggested values:
6, 8, 10, 12, 14, 16, 18, 20, 22

Restriction:
`DeltaThresh > 0`

**`min_thresh`** (input_control)  number `→` int

Minimum threshold for contour detection.

Default:
18

Suggested values:
8, 10, 12, 14, 16, 18, 20, 22

Restriction:
`MinThresh > 0`

**`alpha`** (input_control)  real `→` float

Filter parameter for contour detection, see
[`edges_image`](edges_image.md).

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

**`min_cont_length`** (input_control)  real `→` float

Minimum length of the contours of the marks.

Default:
15.0

Suggested values:
10.0, 15.0, 20.0, 30.0, 40.0, 100.0

Restriction:
`MinContLength > 0.0`

**`max_diam_marks`** (input_control)  real `→` float

Maximum expected diameter of the marks.

Default:
100.0

Suggested values:
50.0, 100.0, 150.0, 200.0, 300.0

Restriction:
`MaxDiamMarks > 0.0`

**`rcoord`** (output_control)  real-array `→` Sequence[float]

Tuple with row coordinates of the detected marks.

**`ccoord`** (output_control)  real-array `→` Sequence[float]

Tuple with column coordinates of the detected marks.

**`start_pose`** (output_control)  pose `→` Sequence[Union[float, int]]

Estimation for the external camera parameters.

Number of elements:
7

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
