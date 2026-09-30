# ProjMatchPointsRansac (Operator)

## Name

`ProjMatchPointsRansac` — Compute a projective transformation matrix between two images by
finding correspondences between points.

## Signature

`static void HOperatorSet.ProjMatchPointsRansac(HObject image1, HObject image2, HTuple rows1, HTuple cols1, HTuple rows2, HTuple cols2, HTuple grayMatchMethod, HTuple maskSize, HTuple rowMove, HTuple colMove, HTuple rowTolerance, HTuple colTolerance, HTuple rotation, HTuple matchThreshold, HTuple estimationMethod, HTuple distanceThreshold, HTuple randSeed, out HTuple homMat2D, out HTuple points1, out HTuple points2)`

`HHomMat2D HImage.ProjMatchPointsRansac(HImage image2, HTuple rows1, HTuple cols1, HTuple rows2, HTuple cols2, string grayMatchMethod, int maskSize, int rowMove, int colMove, int rowTolerance, int colTolerance, HTuple rotation, HTuple matchThreshold, string estimationMethod, double distanceThreshold, int randSeed, out HTuple points1, out HTuple points2)`

`HHomMat2D HImage.ProjMatchPointsRansac(HImage image2, HTuple rows1, HTuple cols1, HTuple rows2, HTuple cols2, string grayMatchMethod, int maskSize, int rowMove, int colMove, int rowTolerance, int colTolerance, double rotation, int matchThreshold, string estimationMethod, double distanceThreshold, int randSeed, out HTuple points1, out HTuple points2)`

`HTuple HHomMat2D.ProjMatchPointsRansac(HImage image1, HImage image2, HTuple rows1, HTuple cols1, HTuple rows2, HTuple cols2, string grayMatchMethod, int maskSize, int rowMove, int colMove, int rowTolerance, int colTolerance, HTuple rotation, HTuple matchThreshold, string estimationMethod, double distanceThreshold, int randSeed, out HTuple points2)`

`HTuple HHomMat2D.ProjMatchPointsRansac(HImage image1, HImage image2, HTuple rows1, HTuple cols1, HTuple rows2, HTuple cols2, string grayMatchMethod, int maskSize, int rowMove, int colMove, int rowTolerance, int colTolerance, double rotation, int matchThreshold, string estimationMethod, double distanceThreshold, int randSeed, out HTuple points2)`

## Description

Given a set of coordinates of characteristic points
(*`cols1`*,*`rows1`*) and
(*`cols2`*,*`rows2`*) in both input images
*`image1`* and *`image2`*,
`ProjMatchPointsRansac` automatically determines
corresponding points and the homogeneous projective transformation
matrix *`homMat2D`* that best transforms the corresponding
points from the different images into each other. The
characteristic points can, for example, be extracted with
[`PointsFoerstner`](points_foerstner.md) or [`PointsHarris`](points_harris.md).

The transformation is determined in two steps: First, gray value
correlations of mask windows around the input points in the first
and the second image are determined and an initial matching between
them is generated using the similarity of the windows in both
images.

The size of the mask windows is *`maskSize`* x *`maskSize`*. Three
metrics for the correlation can be selected. If
*`grayMatchMethod`* has the value *"ssd"*, the sum of
the squared gray value differences is used, *"sad"* means the
sum of absolute differences, and *"ncc"* is the normalized
cross correlation. For details please refer to
[`BinocularDisparity`](binocular_disparity.md). The metric is minimized (*"ssd"*,
*"sad"*) or maximized (*"ncc"*) over all possible
point pairs. A thus found matching is only accepted if the value of
the metric is below the value of *`matchThreshold`*
(*"ssd"*, *"sad"*) or above that value
(*"ncc"*).

To increase the algorithm's performance, the search area for the
matching operations can be limited. Only points within a window of $2\cdot\texttt{RowTolerance}\times2\cdot\texttt{ColTolerance}$ points are considered. The offset of the
center of the search window in the second image with respect to the
position of the current point in the first image is given by
*`rowMove`* and *`colMove`*.

If the transformation contains a rotation, i.e., if the first image
is rotated with respect to the second image, the parameter
*`rotation`* may contain an estimate for the rotation angle or
an angle interval in radians. A good guess will increase the quality
of the gray value matching. If the actual rotation differs too much
from the specified estimate the matching will typically fail. The
larger the given interval, the slower the operator is since the
entire algorithm is run for all relevant angles within the interval.

Once the initial matching is complete, a randomized search algorithm
(RANSAC) is used to determine the transformation matrix
*`homMat2D`*. It tries to find the matrix that is consistent
with a maximum number of correspondences. For a point to be
accepted, its distance from the coordinates predicted by the
transformation must not exceed the threshold
*`distanceThreshold`*.

Once a choice has been made, the matrix is further optimized using
all consistent points. For this optimization, the
*`estimationMethod`* can be chosen to either be the slow but
mathematically optimal *"gold_standard"* method or the faster
*"normalized_dlt"*. Here, the algorithms of
[`VectorToProjHomMat2d`](vector_to_proj_hom_mat2d.md) are used.

Point pairs that still violate the consistency condition for the
final transformation are dropped, the matched points are returned as
control values. *`points1`* contains the indices of the
matched input points from the first image, *`points2`* contains
the indices of the corresponding points in the second image.

The parameter *`randSeed`* can be used to control the
randomized nature of the RANSAC algorithm, and hence to obtain
reproducible results. If *`randSeed`* is set to a positive
number, the operator yields the same result on every call with the
same parameters because the internally used random number generator
is initialized with the seed value. If *`randSeed`* =
*0*, the random number generator is initialized with the
current time. Hence, the results may not be reproducible in this
case. The value set for the HALCON system variable *"seed_rand"*
(see [`SetSystem`](set_system.md)) does not affect the results of
`ProjMatchPointsRansac`.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`image1`** (input_object)  singlechannelimage `→` [HImage](HImage.md) (byte / uint2)

Input image 1.

**`image2`** (input_object)  singlechannelimage `→` [HImage](HImage.md) (byte / uint2)

Input image 2.

**`rows1`** (input_control)  point.x-array `→` [HTuple](HTuple.md) (*double* / int / long)

Row coordinates of characteristic points
in image 1.

**`cols1`** (input_control)  point.y-array `→` [HTuple](HTuple.md) (*double* / int / long)

Column coordinates of characteristic points
in image 1.

**`rows2`** (input_control)  point.x-array `→` [HTuple](HTuple.md) (*double* / int / long)

Row coordinates of characteristic points
in image 2.

**`cols2`** (input_control)  point.y-array `→` [HTuple](HTuple.md) (*double* / int / long)

Column coordinates of characteristic points
in image 2.

**`grayMatchMethod`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Gray value comparison metric.

Default:
"ssd"

List of values:
"ncc", "sad", "ssd"

**`maskSize`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Size of gray value masks.

Default:
10

Value range:
`maskSize
≤
90`

**`rowMove`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Average row coordinate shift.

Default:
0

**`colMove`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Average column coordinate shift.

Default:
0

**`rowTolerance`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Half height of matching search window.

Default:
256

**`colTolerance`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Half width of matching search window.

Default:
256

**`rotation`** (input_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Range of rotation angles.

Default:
0.0

Suggested values:
0.0, 0.7854, 1.571, 3.142

**`matchThreshold`** (input_control)  number `→` [HTuple](HTuple.md) (*int* / long / double)

Threshold for gray value matching.

Default:
10

Suggested values:
10, 20, 50, 100, 0.9, 0.7

**`estimationMethod`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Transformation matrix estimation algorithm.

Default:
"normalized_dlt"

List of values:
"gold_standard", "normalized_dlt"

**`distanceThreshold`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Threshold for transformation consistency check.

Default:
0.2

**`randSeed`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Seed for the random number generator.

Default:
0

**`homMat2D`** (output_control)  hom_mat2d `→` [HHomMat2D](HHomMat2D.md), [HTuple](HTuple.md) (*double*)

Homogeneous projective transformation matrix.

**`points1`** (output_control)  integer-array `→` [HTuple](HTuple.md) (*int* / long)

Indices of matched input points in image 1.

**`points2`** (output_control)  integer-array `→` [HTuple](HTuple.md) (*int* / long)

Indices of matched input points in image 2.

## Possible Predecessors

`PointsFoerstner`,
`PointsHarris`

## Possible Successors

`ProjectiveTransImage`,
`ProjectiveTransImageSize`,
`ProjectiveTransRegion`,
`ProjectiveTransContourXld`,
`ProjectiveTransPoint2d`,
`ProjectiveTransPixel`

## Alternatives

`HomVectorToProjHomMat2d`,
`VectorToProjHomMat2d`

## See also

`ProjMatchPointsRansacGuided`

## References

Richard Hartley, Andrew Zisserman: “Multiple View Geometry in
Computer Vision”; Cambridge University Press, Cambridge; 2000.
  
Olivier Faugeras, Quang-Tuan Luong: “The Geometry of Multiple
Images: The Laws That Govern the Formation of Multiple Images of a
Scene and Some of Their Applications”; MIT Press, Cambridge, MA;
2001.

## Module

Matching
