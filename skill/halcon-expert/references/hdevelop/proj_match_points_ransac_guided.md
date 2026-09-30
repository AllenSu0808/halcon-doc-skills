# proj_match_points_ransac_guided (Operator)

## Name

`proj_match_points_ransac_guided` — Compute a projective transformation matrix between two images by
finding correspondences between points based on a known
approximation of the projective transformation matrix.

## Signature

`proj_match_points_ransac_guided(Image1, Image2 : : Rows1, Cols1, Rows2, Cols2, GrayMatchMethod, MaskSize, HomMat2DGuide, DistanceTolerance, MatchThreshold, EstimationMethod, DistanceThreshold, RandSeed : HomMat2D, Points1, Points2)`

## Description

Given a set of coordinates of characteristic points
(*`Cols1`*,*`Rows1`*) and
(*`Cols2`*,*`Rows2`*) in both input images
*`Image1`* and *`Image2`*, and given a known approximation
*`HomMat2DGuide`* for the transformation matrix between
*`Image1`* and *`Image2`*,
`proj_match_points_ransac_guided` automatically determines
corresponding points and the homogeneous projective transformation
matrix *`HomMat2D`* that best transforms the corresponding
points from the different images into each other. The
characteristic points can, for example, be extracted with
[`points_foerstner`](points_foerstner.md) or [`points_harris`](points_harris.md). The
approximation *`HomMat2DGuide`* can, for example, be calculated
with [`proj_match_points_ransac`](proj_match_points_ransac.md) on lower resolution versions
of *`Image1`* and *`Image2`*.

The transformation is determined in two steps: First, gray value
correlations of mask windows around the input points in the first
and the second image are determined and an initial matching between
them is generated using the similarity of the windows in both
images.

The size of the mask windows is *`MaskSize`* x *`MaskSize`*. Three
metrics for the correlation can be selected. If
*`GrayMatchMethod`* has the value *'ssd'*, the sum of
the squared gray value differences is used, *'sad'* means the
sum of absolute differences, and *'ncc'* is the normalized
cross correlation. For details please refer to
[`binocular_disparity`](binocular_disparity.md). The metric is minimized (*'ssd'*,
*'sad'*) or maximized (*'ncc'*) over all possible
point pairs. A thus found matching is only accepted if the value of
the metric is below the value of *`MatchThreshold`*
(*'ssd'*, *'sad'*) or above that value
(*'ncc'*).

To increase the algorithm's performance, the search area for the
matching operations is limited based on the approximate transformation
*`HomMat2DGuide`*. Only points within a distance of
*`DistanceTolerance`* around the transformed a point in
*`Image2`* of a point in *`Image1`* via
*`HomMat2DGuide`* are considered for the matching.

Once the initial matching is complete, a randomized search algorithm
(RANSAC) is used to determine the transformation matrix
*`HomMat2D`*. It tries to find the matrix that is consistent
with a maximum number of correspondences. For a point to be
accepted, its distance from the coordinates predicted by the
transformation must not exceed the threshold
*`DistanceThreshold`*.

Once a choice has been made, the matrix is further optimized using
all consistent points. For this optimization, the
*`EstimationMethod`* can be chosen to either be the slow but
mathematically optimal *'gold_standard'* method or the faster
*'normalized_dlt'*. Here, the algorithms of
[`vector_to_proj_hom_mat2d`](vector_to_proj_hom_mat2d.md) are used.

Point pairs that still violate the consistency condition for the
final transformation are dropped, the matched points are returned as
control values. *`Points1`* contains the indices of the
matched input points from the first image, *`Points2`* contains
the indices of the corresponding points in the second image.

The parameter *`RandSeed`* can be used to control the
randomized nature of the RANSAC algorithm, and hence to obtain
reproducible results. If *`RandSeed`* is set to a positive
number, the operator yields the same result on every call with the
same parameters because the internally used random number generator
is initialized with the seed value. If *`RandSeed`* =
*0*, the random number generator is initialized with the
current time. Hence, the results may not be reproducible in this
case. The value set for the HALCON system variable *'seed_rand'*
(see [`set_system`](set_system.md)) does not affect the results of
`proj_match_points_ransac_guided`.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Image1`** (input_object)  singlechannelimage `→` object (byte / uint2)

Input image 1.

**`Image2`** (input_object)  singlechannelimage `→` object (byte / uint2)

Input image 2.

**`Rows1`** (input_control)  point.x-array `→`  (real / integer)

Row coordinates of characteristic points
in image 1.

**`Cols1`** (input_control)  point.y-array `→`  (real / integer)

Column coordinates of characteristic points
in image 1.

**`Rows2`** (input_control)  point.x-array `→`  (real / integer)

Row coordinates of characteristic points
in image 2.

**`Cols2`** (input_control)  point.y-array `→`  (real / integer)

Column coordinates of characteristic points
in image 2.

**`GrayMatchMethod`** (input_control)  string `→`  (string)

Gray value comparison metric.

Default:
'ssd'

List of values:
'ncc', 'sad', 'ssd'

**`MaskSize`** (input_control)  integer `→`  (integer)

Size of gray value masks.

Default:
10

Value range:
`MaskSize
≤
90`

**`HomMat2DGuide`** (input_control)  hom_mat2d `→`  (real)

Approximation of the Homogeneous projective
transformation matrix between the two images.

**`DistanceTolerance`** (input_control)  real `→`  (real)

Tolerance for the matching search window.

Default:
20.0

Suggested values:
0.2, 0.5, 1.0, 2.0, 3.0, 5.0, 10.0, 20.0, 50.0

**`MatchThreshold`** (input_control)  number `→`  (integer / real)

Threshold for gray value matching.

Default:
10

Suggested values:
10, 20, 50, 100, 0.9, 0.7

**`EstimationMethod`** (input_control)  string `→`  (string)

Transformation matrix estimation algorithm.

Default:
'normalized_dlt'

List of values:
'gold_standard', 'normalized_dlt'

**`DistanceThreshold`** (input_control)  real `→`  (real)

Threshold for transformation consistency check.

Default:
0.2

**`RandSeed`** (input_control)  integer `→`  (integer)

Seed for the random number generator.

Default:
0

**`HomMat2D`** (output_control)  hom_mat2d `→`  (real)

Homogeneous projective transformation matrix.

**`Points1`** (output_control)  integer-array `→`  (integer)

Indices of matched input points in image 1.

**`Points2`** (output_control)  integer-array `→`  (integer)

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

`points_foerstner`,
`points_harris`

## Possible Successors

`projective_trans_image`,
`projective_trans_image_size`,
`projective_trans_region`,
`projective_trans_contour_xld`,
`projective_trans_point_2d`,
`projective_trans_pixel`

## Alternatives

`hom_vector_to_proj_hom_mat2d`,
`vector_to_proj_hom_mat2d`

## See also

`proj_match_points_ransac`

## References

Richard Hartley, Andrew Zisserman: “Multiple View Geometry in
Computer Vision”; Cambridge University Press, Cambridge; 2000.
  
Olivier Faugeras, Quang-Tuan Luong: “The Geometry of Multiple
Images: The Laws That Govern the Formation of Multiple Images of a
Scene and Some of Their Applications”; MIT Press, Cambridge, MA;
2001.

## Module

Matching
