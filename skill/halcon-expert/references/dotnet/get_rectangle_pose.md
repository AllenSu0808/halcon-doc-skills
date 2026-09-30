# GetRectanglePose (Operator)

## Name

`GetRectanglePose` — Determine the 3D pose of a rectangle from its perspective 2D
projection

## Signature

`static void HOperatorSet.GetRectanglePose(HObject contour, HTuple cameraParam, HTuple width, HTuple height, HTuple weightingMode, HTuple clippingFactor, out HTuple pose, out HTuple covPose, out HTuple error)`

`HPose[] HXLD.GetRectanglePose(HCamPar cameraParam, HTuple width, HTuple height, string weightingMode, double clippingFactor, out HTuple covPose, out HTuple error)`

`HPose HXLD.GetRectanglePose(HCamPar cameraParam, double width, double height, string weightingMode, double clippingFactor, out HTuple covPose, out HTuple error)`

`HPose[] HCamPar.GetRectanglePose(HXLD contour, HTuple width, HTuple height, string weightingMode, double clippingFactor, out HTuple covPose, out HTuple error)`

`HPose HCamPar.GetRectanglePose(HXLD contour, double width, double height, string weightingMode, double clippingFactor, out HTuple covPose, out HTuple error)`

## Description

A rectangle in space is projected as a general quadrangle into the
image. `GetRectanglePose` determines the *`pose`* of
the rectangle from this projection (*`contour`*).

The algorithm works as follows: First, *`contour`* is segmented
into four line segments and their intersections are considered as
corners of the contour. The corners together with the internal
camera parameters (*`cameraParam`*) and the rectangle size in
meters (*`width`*, *`height`*) are used for an initial
estimation of the rectangle pose. Then, the final *`pose`* is
refined with a non-linear optimization by minimizing the geometrical
distance of the contour points from the back projection of the
rectangle in the image.

The operator supports only area scan pinhole (projective)
cameras. An error is returned if *`cameraParam`* specifies a
line scan or a telecentric camera (see also
[Calibration](toc_calibration.md)).

*`width`* and *`height`* specify the size of the rectangle
in x and y dimensions, respectively, in its coordinate
system. The origin of this coordinate system is in the center of the
rectangle. The z axis points away from the camera.

The arguments *`weightingMode`* and *`clippingFactor`* can
be used to damp the impact of outliers on the algorithm. If
*`weightingMode`* is set to *"tukey"* or *"huber"*,
the contour points are weighted based on the approach of Tukey or Huber
respectively. In such a case a robust error statistics is used to
estimate the standard deviation of the distances of the contour
points from the backprojected rectangle excluding outliers. The
parameter *`clippingFactor`* (a scaling factor for the standard
deviation) controls the amount of damping outliers: The smaller the
value chosen for *`clippingFactor`* the more outliers are
detected. See a discussion about the properties of the different
weighting modes in [`FitLineContourXld`](fit_line_contour_xld.md). Note that, unlike
by [`FitLineContourXld`](fit_line_contour_xld.md), for the rectangle pose estimation
the approach of Huber is recommended.

### Output

The resulting *`pose`* is of code 0 (see [`CreatePose`](create_pose.md))
and represents the pose of the center of the rectangle. You can
compute the pose of the corners of the rectangle as follows:

|  |
| --- |
| [`SetOriginPose(Pose, Width/2, -Height/2, 0, PoseCorner1)`](set_origin_pose.md) |
| [`SetOriginPose(Pose, Width/2, Height/2, 0, PoseCorner2)`](set_origin_pose.md) |
| [`SetOriginPose(Pose, -Width/2, Height/2, 0, PoseCorner3)`](set_origin_pose.md) |
| [`SetOriginPose(Pose, -Width/2, -Height/2, 0, PoseCorner4)`](set_origin_pose.md) |
|  |

A rectangle is symmetric with respect to its x, y, and z axis
and one and the same contour can represent a rectangle in 4
different poses. The angles in *`pose`* are normalized to be in
the range [-90; 90] degrees and the rest of the 4 possible poses
can be computed by combining flips around the corresponding axis:

|  |
| --- |
| `* NOTE: the following code works ONLY for pose of code 0` |
| `* as it is returned by get_rectangle_pose` |
| `*` |
| `* flip around z-axis` |
| `PoseFlippedZ := Pose` |
| `PoseFlippedZ[5] := PoseFlippedZ[5]+180` |
| `* flip around y-axis` |
| `PoseFlippedY := Pose` |
| `PoseFlippedY[4] := PoseFlippedY[4]+180` |
| `PoseFlippedY[5] := -PoseFlippedY[5]` |
| `* flip around x-axis` |
| `PoseFlippedX := Pose` |
| `PoseFlippedX[3] := PoseFlippedX[3]+180` |
| `PoseFlippedX[4] := -PoseFlippedX[4]` |
| `PoseFlippedX[5] := -PoseFlippedX[5]` |
|  |

Note that if the rectangle is a square (*`width`* ==
*`height`*) the number of alternative poses is 8.

If more than one contour are given in *`contour`*, a
corresponding tuple of values for both *`width`* and
*`height`* has to be provided as well. Yet, if only one value
is provided for each of these arguments, then this value is applied
for each processed contour. A pose is estimated for each processed
contour and all poses are concatenated in *`pose`* (see the
example below).

### Accuracy of the pose

The accuracy of the estimated pose depends on the following three
factors:

- ratio *`width`*/*`height`*
- length of the projected contour
- degree of perspective distortion of the contour

In order to achieve an accurate pose estimation, there are three
corresponding criteria that should be considered:

The **ratio** *`width`*/*`height`*
should fulfill
$$\frac{1}{3} < \frac{Width}{Height} < 3$$ ![figure](../assets/285636aa75819166.svg)
For a rectangular object deviating from this criterion, its longer
side dominates the determination of its pose. This causes
instability in the estimation of the angle around the longer
rectangle's axis. In the extreme case when one of the dimensions is
0, the rectangle is in fact a line segment, whose pose cannot be
estimated.

Secondly, the **lengths of each side of the contour** should be
at least 20 pixels. An error is returned if a side of the contour is
less than 5 pixels long.

Thirdly, the more the contour appears **projectively
distorted**, the more stable the algorithm works. Therefore, the pose
of a rectangle tilted with respect to the image plane can be estimated
accurately, whereas the pose of an rectangle parallel to the image
plane of the camera could be unstable. This is further discussed in
the next paragraph. Additionally, there is a rule of thumb that
ensures projective distortion: the rectangle should be placed in
space such that its size in x and y dimension in the camera
coordinate system should not be less than 1/10th of its distance
from the camera in z direction.

`GetRectanglePose` provides two measures for the accuracy of
the estimated *`pose`*. *`error`* is the average pixel
error between the contour points and the modeled rectangle
backprojected on the image. If *`error`* is exceeding 0.5, this
is an indication that the algorithm did not converge properly, and
the resulting *`pose`* should not be used. *`covPose`*
contains 36 entries representing the 6×6
covariance matrix of the first 6 entries of *`pose`*. The above
mentioned case of instability of the angle about the longer
rectangle's axis be detected by checking that the absolute values of
the variances and covariances of the rotations around the x and
y axis (*`covPose`*[21],*`covPose`*[28], and
*`covPose`*[22] == *`covPose`*[27]) do not exceed
0.05. Further, unusually increased values of any of the covariances
and especially of the variances (the 6 values on the diagonal of
*`covPose`* with indices 0, 7, 14, 21, 28 and 35, respectively)
indicate a poor quality of *`pose`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`contour`** (input_object)  xld(-array) `→` [HXLD](HXLD.md)

Contour(s) to be examined.

**`cameraParam`** (input_control)  campar `→` [HCamPar](HCamPar.md), [HTuple](HTuple.md) (*double* / int / long / string)

Internal camera parameters.

**`width`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*double*)

Width of the rectangle in meters.

Restriction:
`Width > 0`

**`height`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*double*)

Height of the rectangle in meters.

Restriction:
`Height > 0`

**`weightingMode`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Weighting mode for the optimization phase.

Default:
"nonweighted"

List of values:
"huber", "nonweighted", "tukey"

**`clippingFactor`** (input_control)  number `→` [HTuple](HTuple.md) (*double*)

Clipping factor for the elimination of outliers
(typical: *1.0* for *"huber"* and
*3.0* for *"tukey"*).

Default:
2.0

Suggested values:
1.0, 1.5, 2.0, 2.5, 3.0

Restriction:
`ClippingFactor > 0`

**`pose`** (output_control)  pose(-array) `→` [HPose](HPose.md), [HTuple](HTuple.md) (*double* / int / long)

3D pose of the rectangle.

Number of elements:
Pose == 7 * Contour

**`covPose`** (output_control)  number-array `→` [HTuple](HTuple.md) (*double*)

Covariances of the pose values.

Number of elements:
CovPose == 36 * Contour

**`error`** (output_control)  number-array `→` [HTuple](HTuple.md) (*double*)

Root-mean-square value of the final residual error.

Number of elements:
Error == Contour

## Example (HDevelop)

```
* Process an image with several rectangles of the same size appearing
* as light objects.
RectWidth := 0.04
RectHeight := 0.025
gen_cam_par_area_scan_division (0.014, 830, 4.58e-006, 4.65e-006, \
                                509, 488, 800, 800, CameraParam)
read_image (Image, 'barcode/ean13/tea_box_01')
* Find light objects in the image.
mean_image (Image, ImageMean, 201, 201)
dyn_threshold (Image, ImageMean, Region, 5, 'light')
* Fill gaps in the objects.
fill_up (Region, RegionFillUp)
* Extract rectangular contours.
connection (RegionFillUp, ConnectedRegions)
select_shape (ConnectedRegions, SelectedRegions, ['area','rectangularity'], \
              'and', [50000,0.9], [640000,1])
boundary (SelectedRegions, RegionBorder, 'inner')
dilation_circle (RegionBorder, RegionDilation, 3.5)
* NOTE: for a real application, this step might require some additional
*       pre- or postprocessing.
reduce_domain (Image, RegionDilation, ImageReduced)
edges_sub_pix (ImageReduced, Edges, 'canny', 1, 20, 40)
* Get the pose of all contours found.
get_rectangle_pose (Edges, CameraParam, RectWidth, RectHeight, 'huber', 2, \
                    Poses, CovPose, Error)
NumPoses := |Poses|/7
for I := 0 to NumPoses-1 by 1
  Pose := Poses[I*7:I*7+6]
  * Use the Pose here.
  * ...
endfor
```

## Result

`GetRectanglePose` returns 2 (
H_MSG_TRUE)
if all parameter values are
correct and the position of the rectangle has been determined
successfully. If the provided contour(s) cannot be segmented as a
quadrangle `GetRectanglePose` returns
H_ERR_FIT_QUADRANGLE. If further necessary, an exception is
raised.

## Possible Predecessors

`EdgesSubPix`

## See also

`GetCirclePose`,
`SetOriginPose`,
`CameraCalibration`

## References

G.Schweighofer and A.Pinz: “Robust Pose Estimation from a Planar
Target”; Transactions on Pattern Analysis and Machine Intelligence
(PAMI), 28(12):2024-2030, 2006

## Module

3D Metrology
