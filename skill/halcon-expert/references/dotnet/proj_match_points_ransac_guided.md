# ProjMatchPointsRansacGuided (Operator)

## Name

`ProjMatchPointsRansacGuided` — Compute a projective transformation matrix between two images by
finding correspondences between points based on a known
approximation of the projective transformation matrix.

## Signature

`static void HOperatorSet.ProjMatchPointsRansacGuided(HObject image1, HObject image2, HTuple rows1, HTuple cols1, HTuple rows2, HTuple cols2, HTuple grayMatchMethod, HTuple maskSize, HTuple homMat2DGuide, HTuple distanceTolerance, HTuple matchThreshold, HTuple estimationMethod, HTuple distanceThreshold, HTuple randSeed, out HTuple homMat2D, out HTuple points1, out HTuple points2)`

`HHomMat2D HImage.ProjMatchPointsRansacGuided(HImage image2, HTuple rows1, HTuple cols1, HTuple rows2, HTuple cols2, string grayMatchMethod, int maskSize, HHomMat2D homMat2DGuide, double distanceTolerance, HTuple matchThreshold, string estimationMethod, double distanceThreshold, int randSeed, out HTuple points1, out HTuple points2)`

`HHomMat2D HImage.ProjMatchPointsRansacGuided(HImage image2, HTuple rows1, HTuple cols1, HTuple rows2, HTuple cols2, string grayMatchMethod, int maskSize, HHomMat2D homMat2DGuide, double distanceTolerance, int matchThreshold, string estimationMethod, double distanceThreshold, int randSeed, out HTuple points1, out HTuple points2)`

`HHomMat2D HHomMat2D.ProjMatchPointsRansacGuided(HImage image1, HImage image2, HTuple rows1, HTuple cols1, HTuple rows2, HTuple cols2, string grayMatchMethod, int maskSize, double distanceTolerance, HTuple matchThreshold, string estimationMethod, double distanceThreshold, int randSeed, out HTuple points1, out HTuple points2)`

`HHomMat2D HHomMat2D.ProjMatchPointsRansacGuided(HImage image1, HImage image2, HTuple rows1, HTuple cols1, HTuple rows2, HTuple cols2, string grayMatchMethod, int maskSize, double distanceTolerance, int matchThreshold, string estimationMethod, double distanceThreshold, int randSeed, out HTuple points1, out HTuple points2)`

## Description

Given a set of coordinates of characteristic points
(*`cols1`*,*`rows1`*) and
(*`cols2`*,*`rows2`*) in both input images
*`image1`* and *`image2`*, and given a known approximation
*`homMat2DGuide`* for the transformation matrix between
*`image1`* and *`image2`*,
`ProjMatchPointsRansacGuided` automatically determines
corresponding points and the homogeneous projective transformation
matrix *`homMat2D`* that best transforms the corresponding
points from the different images into each other. The
characteristic points can, for example, be extracted with
[`PointsFoerstner`](points_foerstner.md) or [`PointsHarris`](points_harris.md). The
approximation *`homMat2DGuide`* can, for example, be calculated
with [`ProjMatchPointsRansac`](proj_match_points_ransac.md) on lower resolution versions
of *`image1`* and *`image2`*.

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
matching operations is limited based on the approximate transformation
*`homMat2DGuide`*. Only points within a distance of
*`distanceTolerance`* around the transformed a point in
*`image2`* of a point in *`image1`* via
*`homMat2DGuide`* are considered for the matching.

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
`ProjMatchPointsRansacGuided`.

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

**`homMat2DGuide`** (input_control)  hom_mat2d `→` [HHomMat2D](HHomMat2D.md), [HTuple](HTuple.md) (*double*)

Approximation of the Homogeneous projective
transformation matrix between the two images.

**`distanceTolerance`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Tolerance for the matching search window.

Default:
20.0

Suggested values:
0.2, 0.5, 1.0, 2.0, 3.0, 5.0, 10.0, 20.0, 50.0

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

## Example (HDevelop)

```
zoom_image_factor (Image1, Image1Zoomed, 0.5, 0.5, 'constant')
zoom_image_factor (Image2, Image2Zoomed, 0.5, 0.5, 'constant')
points_foerstner (Image1Zoomed, 1, 2, 3, 200, 0.3, 'gauss', 'false', \
                  Rows1, Cols1, _, _, _, _, _, _, _, _)
points_foerstner (Image2Zoomed, 1, 2, 3, 200, 0.3, 'gauss', 'false', \
                  Rows2, Cols2, _, _, _, _, _, _, _, _)
get_image_pointer1 (Image1Zoomed, Pointer, Type, Width, Height)
proj_match_points_ransac (Image1Zoomed, Image2Zoomed, Rows1, Cols1, \
                          Rows2, Cols2, 'ncc', 10, 0, 0, \
                          Height, Width, 0, 0.5, 'gold_standard', \
                          5, 0, HomMat2D, Points1, Points2)
hom_mat2d_scale_local (HomMat2D, 0.5, 0.5, HomMat2DGuide)
hom_mat2d_scale (HomMat2DGuide, 2, 2, 0, 0, HomMat2DGuide)
points_foerstner (Image1, 1, 2, 3, 200, 0.3, 'gauss', 'false', \
                  Rows1, Cols1, _, _, _, _, _, _, _, _)
points_foerstner (Image2, 1, 2, 3, 200, 0.3, 'gauss', 'false', \
                  Rows2, Cols2, _, _, _, _, _, _, _, _)
proj_match_points_ransac_guided (Image1, Image2, Rows1, Cols1, \
                                 Rows2, Cols2, 'ncc', 10, \
                                 HomMat2DGuide, 40, 0.5, \
                                 'gold_standard', 10, 0, HomMat2D, \
                                 Points1, Points2)
```

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

`ProjMatchPointsRansac`

## References

Richard Hartley, Andrew Zisserman: “Multiple View Geometry in
Computer Vision”; Cambridge University Press, Cambridge; 2000.
  
Olivier Faugeras, Quang-Tuan Luong: “The Geometry of Multiple
Images: The Laws That Govern the Formation of Multiple Images of a
Scene and Some of Their Applications”; MIT Press, Cambridge, MA;
2001.

## Module

Matching
