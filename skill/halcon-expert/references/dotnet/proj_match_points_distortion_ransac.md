# ProjMatchPointsDistortionRansac (Operator)

## Name

`ProjMatchPointsDistortionRansac` — Compute a projective transformation matrix between two images and
the radial distortion coefficient by automatically finding
correspondences between points.

## Signature

`static void HOperatorSet.ProjMatchPointsDistortionRansac(HObject image1, HObject image2, HTuple rows1, HTuple cols1, HTuple rows2, HTuple cols2, HTuple grayMatchMethod, HTuple maskSize, HTuple rowMove, HTuple colMove, HTuple rowTolerance, HTuple colTolerance, HTuple rotation, HTuple matchThreshold, HTuple estimationMethod, HTuple distanceThreshold, HTuple randSeed, out HTuple homMat2D, out HTuple kappa, out HTuple error, out HTuple points1, out HTuple points2)`

`HHomMat2D HImage.ProjMatchPointsDistortionRansac(HImage image2, HTuple rows1, HTuple cols1, HTuple rows2, HTuple cols2, string grayMatchMethod, int maskSize, int rowMove, int colMove, int rowTolerance, int colTolerance, HTuple rotation, HTuple matchThreshold, string estimationMethod, HTuple distanceThreshold, int randSeed, out double kappa, out double error, out HTuple points1, out HTuple points2)`

`HHomMat2D HImage.ProjMatchPointsDistortionRansac(HImage image2, HTuple rows1, HTuple cols1, HTuple rows2, HTuple cols2, string grayMatchMethod, int maskSize, int rowMove, int colMove, int rowTolerance, int colTolerance, double rotation, int matchThreshold, string estimationMethod, double distanceThreshold, int randSeed, out double kappa, out double error, out HTuple points1, out HTuple points2)`

`double HHomMat2D.ProjMatchPointsDistortionRansac(HImage image1, HImage image2, HTuple rows1, HTuple cols1, HTuple rows2, HTuple cols2, string grayMatchMethod, int maskSize, int rowMove, int colMove, int rowTolerance, int colTolerance, HTuple rotation, HTuple matchThreshold, string estimationMethod, HTuple distanceThreshold, int randSeed, out double error, out HTuple points1, out HTuple points2)`

`double HHomMat2D.ProjMatchPointsDistortionRansac(HImage image1, HImage image2, HTuple rows1, HTuple cols1, HTuple rows2, HTuple cols2, string grayMatchMethod, int maskSize, int rowMove, int colMove, int rowTolerance, int colTolerance, double rotation, int matchThreshold, string estimationMethod, double distanceThreshold, int randSeed, out double error, out HTuple points1, out HTuple points2)`

## Description

Given a set of coordinates of characteristic points
(*`rows1`*,*`cols1`*) and
(*`rows2`*,*`cols2`*) in both input images
*`image1`* and *`image2`*, which must be of identical
size, `ProjMatchPointsDistortionRansac` automatically
determines corresponding points, the homogeneous projective
transformation matrix *`homMat2D`*, and the radial distortion
coefficient *`kappa`*$(\kappa)$ that optimally fulfill the
following equation:
$$\left(\begin{array}{c} r_{2} \\ c_{2} \\ 1 \end{array}\right) = \mathrm{HomMat2D} \cdot \left(\begin{array}{c} r_{1} \\ c_{1} \\ 1 \end{array}\right) \.$$ ![figure](../assets/c7511ca06df7f92b.svg)
Here, $(r_{1},c_{1})$ and $(r_{2},c_{2})$
denote image points that are obtained by undistorting the input
image points with the division model (see
[Calibration](toc_calibration.md)):
$$r = \frac{\tilde{r}}{1 + \kappa(\tilde{r}^2 + \tilde{c}^2)} c = \frac{\tilde{c}}{1 + \kappa(\tilde{r}^2 + \tilde{c}^2)}$$ ![figure](../assets/6ff1b1bb1ed9db6b.svg)
Here,
$(\tilde{r}_1, \tilde{c}_1) = (Rows1 - 0.5(h - 1), Cols1 - 0.5(w - 1))$ ![figure](../assets/d2fcb4cda5ac5181.svg)
and
$(\tilde{r}_{2}, \tilde{c}_{2}) = (Rows2 - 0.5(h - 1), Cols2 - 0.5(w - 1))$ ![figure](../assets/6b550dd0ce20a38d.svg)
denote the distorted image points, specified relative to the image center,
and w and h denote the width and height of the input images.
Thus, `ProjMatchPointsDistortionRansac` assumes that the
principal point of the camera, i.e., the center of the radial
distortions, lies at the center of the image.

The returned *`kappa`* can be used to construct camera
parameters that can be used to rectify images or points (see
[`ChangeRadialDistortionCamPar`](change_radial_distortion_cam_par.md),
[`ChangeRadialDistortionImage`](change_radial_distortion_image.md), and
[`ChangeRadialDistortionPoints`](change_radial_distortion_points.md)):
$$CamPar = [\'area_scan_telecentric_division\', 1.0, Kappa, 1.0, 1.0, 0.5(w - 1), 0.5(h - 1), w, h]$$ ![figure](../assets/f088ed9af2ccc16d.svg)

The matching process is based on characteristic points, which can be
extracted with point operators like [`PointsFoerstner`](points_foerstner.md) or
[`PointsHarris`](points_harris.md). The matching itself is carried out in two
steps: first, gray value correlations of mask windows around the
input points in the first and the second image are determined and an
initial matching between them is generated using the similarity of
the windows in both images. Then, the RANSAC algorithm is applied
to find the projective transformation matrix and radial distortion
coefficient that maximizes the number of correspondences under the
above constraint.

The size of the mask windows used for the matching is
*`maskSize`* x
*`maskSize`*. Three metrics for the correlation can be
selected. If *`grayMatchMethod`* has the value *"ssd"*,
the sum of the squared gray value differences is used,
*"sad"* means the sum of absolute differences, and
*"ncc"* is the normalized cross correlation. For details
please refer to [`BinocularDisparity`](binocular_disparity.md). The metric is minimized
(*"ssd"*, *"sad"*) or maximized (*"ncc"*) over
all possible point pairs. A thus found matching is only accepted if
the value of the metric is below the value of
*`matchThreshold`* (*"ssd"*, *"sad"*) or above
that value (*"ncc"*).

To increase the algorithm's performance, the search area for the
match candidates can be limited to a rectangle by specifying its
size and offset. Only points within a window of $2\cdot\texttt{RowTolerance}\times2\cdot\texttt{ColTolerance}$ points are considered. The offset of the
center of the search window in the second image with respect to the
position of the current point in the first image is given by
*`rowMove`* and *`colMove`*.

If the transformation contains a rotation, i.e., if the first image
is rotated with respect to the second image, the parameter
*`rotation`* may contain an estimate for the rotation angle or
an angle interval in radians. A good guess will increase the
quality of the gray value matching. If the actual rotation differs
too much from the specified estimate, the matching will typically
fail. In this case, an angle interval should be specified and
*`rotation`* is a tuple with two elements. The larger the
given interval is the slower the operator is since the RANSAC
algorithm is run over all (automatically determined) angle
increments within the interval.

After the initial matching has been completed, a randomized search
algorithm (RANSAC) is used to determine the projective
transformation matrix *`homMat2D`* and the radial distortion
coefficient *`kappa`*. It tries to find the parameters that
are consistent with a maximum number of correspondences. For a
point to be accepted, the distance in pixels to its corresponding
transformed point must not exceed the threshold
*`distanceThreshold`*.

The parameter *`estimationMethod`* determines which algorithm
is used to compute the projective transformation matrix. A linear
algorithm is used if *`estimationMethod`* is set to
*"linear"*. This algorithm is very fast and returns accurate
results for small to moderate noise of the point coordinates and for
most distortions (except for small distortions). For
*`estimationMethod`* = *"gold_standard"*, a
mathematically optimal but slower optimization is used, which
minimizes the geometric reprojection error. In general, it is
preferable to use *`estimationMethod`* =
*"gold_standard"*.

The value *`error`* indicates the overall quality of the
estimation procedure and is the mean symmetric euclidean distance in
pixels between the points and their corresponding transformed
points.

Point pairs consistent with the above constraints are considered to
be corresponding points. *`points1`* contains the indices of
the matched input points from the first image and *`points2`*
contains the indices of the corresponding points in the second
image.

The parameter *`randSeed`* can be used to control the
randomized nature of the RANSAC algorithm, and hence to obtain
reproducible results. If *`randSeed`* is set to a positive
number, the operator returns the same result on every call with the
same parameters because the internally used random number generator
is initialized with *`randSeed`*. If *`randSeed`* =
*0*, the random number generator is initialized with the
current time. In this case the results may not be reproducible.
The value set for the HALCON system variable *"seed_rand"*
(see [`SetSystem`](set_system.md)) does not affect the results of
`ProjMatchPointsDistortionRansac`.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`image1`** (input_object)  singlechannelimage `→` [HImage](HImage.md) (byte / uint2)

Input image 1.

**`image2`** (input_object)  singlechannelimage `→` [HImage](HImage.md) (byte / uint2)

Input image 2.

**`rows1`** (input_control)  point.y-array `→` [HTuple](HTuple.md) (*double* / int / long)

Input points in image 1 (row coordinate).

Restriction:
`length(Rows1) >= 5`

**`cols1`** (input_control)  point.x-array `→` [HTuple](HTuple.md) (*double* / int / long)

Input points in image 1 (column coordinate).

Restriction:
`length(Cols1) == length(Rows1)`

**`rows2`** (input_control)  point.y-array `→` [HTuple](HTuple.md) (*double* / int / long)

Input points in image 2 (row coordinate).

Restriction:
`length(Rows2) >= 5`

**`cols2`** (input_control)  point.x-array `→` [HTuple](HTuple.md) (*double* / int / long)

Input points in image 2 (column coordinate).

Restriction:
`length(Cols2) == length(Rows2)`

**`grayMatchMethod`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Gray value match metric.

Default:
"ncc"

List of values:
"ncc", "sad", "ssd"

**`maskSize`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Size of gray value masks.

Default:
10

Suggested values:
3, 7, 15

Value range:
`1
≤
maskSize`

**`rowMove`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Average row coordinate offset of corresponding points.

Default:
0

**`colMove`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Average column coordinate offset of corresponding points.

Default:
0

**`rowTolerance`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Half height of matching search window.

Default:
200

Restriction:
`RowTolerance >= 1`

**`colTolerance`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Half width of matching search window.

Default:
200

Restriction:
`ColTolerance >= 1`

**`rotation`** (input_control)  angle.rad(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Estimate of the relative rotation of the second image
with respect to the first image.

Default:
0.0

Suggested values:
0.0, 0.1, -0.1, 0.7854, 1.571, 3.142

**`matchThreshold`** (input_control)  number `→` [HTuple](HTuple.md) (*int* / long / double)

Threshold for gray value matching.

Default:
0.7

Suggested values:
0.9, 0.7, 0.5, 10, 20, 50, 100

**`estimationMethod`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Algorithm for the computation of the projective
transformation matrix.

Default:
"gold_standard"

List of values:
"gold_standard", "linear"

**`distanceThreshold`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / int / long)

Threshold for the transformation consistency check.

Default:
1

Restriction:
`DistanceThreshold > 0`

**`randSeed`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Seed for the random number generator.

Default:
0

**`homMat2D`** (output_control)  hom_mat2d `→` [HHomMat2D](HHomMat2D.md), [HTuple](HTuple.md) (*double*)

Computed homogeneous projective transformation matrix.

**`kappa`** (output_control)  real `→` [HTuple](HTuple.md) (*double*)

Computed radial distortion coefficient.

**`error`** (output_control)  real `→` [HTuple](HTuple.md) (*double*)

Root-Mean-Square transformation error.

**`points1`** (output_control)  integer-array `→` [HTuple](HTuple.md) (*int* / long)

Indices of matched input points in image 1.

**`points2`** (output_control)  integer-array `→` [HTuple](HTuple.md) (*int* / long)

Indices of matched input points in image 2.

## Example (HDevelop)

```
points_foerstner (Image1, 1, 2, 3, 50, 0.1, 'gauss', 'true', \
                  Rows1, Cols1, _, _, _, _, _, _, _, _)
points_foerstner (Image2, 1, 2, 3, 50, 0.1, 'gauss', 'true', \
                  Rows2, Cols2, _, _, _, _, _, _, _, _)
get_image_size (Image1, Width, Height)
proj_match_points_distortion_ransac (Image1, Image2, Rows1, Cols1, \
                                     Rows2, Cols2, 'ncc', 10, 0, 0, \
                                     Height, Width, 0, 0.5, \
                                     'gold_standard', 1, 42, \
                                     HomMat2D, Kappa, Error, \
                                     Points1, Points2)
CamParDist := ['area_scan_division',0.0,Kappa,1.0,1.0, \
               0.5*(Width-1),0.5*(Height-1),Width,Height]
change_radial_distortion_cam_par ('fixed', CamParDist, 0, CamPar)
change_radial_distortion_image (Image1, Image1, Image1Rect, \
                                CamParDist, CamPar)
change_radial_distortion_image (Image2, Image2, Image2Rect, \
                                CamParDist, CamPar)
concat_obj (Image1Rect, Image2Rect, ImagesRect)
gen_projective_mosaic (ImagesRect, MosaicImage, 1, 1, 2, HomMat2D, \
                       'default', 'false', MosaicMatrices2D)
```

## Possible Predecessors

`PointsFoerstner`,
`PointsHarris`

## Possible Successors

`VectorToProjHomMat2dDistortion`,
`ChangeRadialDistortionCamPar`,
`ChangeRadialDistortionImage`,
`ChangeRadialDistortionPoints`,
`GenBinocularProjRectification`,
`ProjectiveTransImage`,
`ProjectiveTransImageSize`,
`ProjectiveTransRegion`,
`ProjectiveTransContourXld`,
`ProjectiveTransPoint2d`,
`ProjectiveTransPixel`

## Alternatives

`ProjMatchPointsDistortionRansacGuided`

## See also

`ProjMatchPointsRansac`,
`ProjMatchPointsRansacGuided`,
`HomVectorToProjHomMat2d`,
`VectorToProjHomMat2d`

## References

Richard Hartley, Andrew Zisserman: “Multiple View Geometry in
Computer Vision”; Cambridge University Press, Cambridge; 2003.
  
Olivier Faugeras, Quang-Tuan Luong: “The Geometry of Multiple
Images: The Laws That Govern the Formation of Multiple Images of a
Scene and Some of Their Applications”; MIT Press, Cambridge, MA;
2001.

## Module

Matching
