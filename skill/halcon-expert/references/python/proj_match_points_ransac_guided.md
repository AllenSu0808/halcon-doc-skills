# proj_match_points_ransac_guided (Operator)

## Name

`proj_match_points_ransac_guided` — Compute a projective transformation matrix between two images by
finding correspondences between points based on a known
approximation of the projective transformation matrix.

## Signature

`def proj_match_points_ransac_guided(image_1: HObject, image_2: HObject, rows_1: Sequence[Union[float, int]], cols_1: Sequence[Union[float, int]], rows_2: Sequence[Union[float, int]], cols_2: Sequence[Union[float, int]], gray_match_method: str, mask_size: int, hom_mat_2dguide: Sequence[float], distance_tolerance: float, match_threshold: Union[int, float], estimation_method: str, distance_threshold: float, rand_seed: int) -> Tuple[Sequence[float], Sequence[int], Sequence[int]]`

## Description

Given a set of coordinates of characteristic points
(*`cols_1`*,*`rows_1`*) and
(*`cols_2`*,*`rows_2`*) in both input images
*`image_1`* and *`image_2`*, and given a known approximation
*`hom_mat_2dguide`* for the transformation matrix between
*`image_1`* and *`image_2`*,
`proj_match_points_ransac_guided` automatically determines
corresponding points and the homogeneous projective transformation
matrix *`hom_mat_2d`* that best transforms the corresponding
points from the different images into each other. The
characteristic points can, for example, be extracted with
[`points_foerstner`](points_foerstner.md) or [`points_harris`](points_harris.md). The
approximation *`hom_mat_2dguide`* can, for example, be calculated
with [`proj_match_points_ransac`](proj_match_points_ransac.md) on lower resolution versions
of *`image_1`* and *`image_2`*.

The transformation is determined in two steps: First, gray value
correlations of mask windows around the input points in the first
and the second image are determined and an initial matching between
them is generated using the similarity of the windows in both
images.

The size of the mask windows is *`mask_size`* x *`mask_size`*. Three
metrics for the correlation can be selected. If
*`gray_match_method`* has the value *"ssd"*, the sum of
the squared gray value differences is used, *"sad"* means the
sum of absolute differences, and *"ncc"* is the normalized
cross correlation. For details please refer to
[`binocular_disparity`](binocular_disparity.md). The metric is minimized (*"ssd"*,
*"sad"*) or maximized (*"ncc"*) over all possible
point pairs. A thus found matching is only accepted if the value of
the metric is below the value of *`match_threshold`*
(*"ssd"*, *"sad"*) or above that value
(*"ncc"*).

To increase the algorithm's performance, the search area for the
matching operations is limited based on the approximate transformation
*`hom_mat_2dguide`*. Only points within a distance of
*`distance_tolerance`* around the transformed a point in
*`image_2`* of a point in *`image_1`* via
*`hom_mat_2dguide`* are considered for the matching.

Once the initial matching is complete, a randomized search algorithm
(RANSAC) is used to determine the transformation matrix
*`hom_mat_2d`*. It tries to find the matrix that is consistent
with a maximum number of correspondences. For a point to be
accepted, its distance from the coordinates predicted by the
transformation must not exceed the threshold
*`distance_threshold`*.

Once a choice has been made, the matrix is further optimized using
all consistent points. For this optimization, the
*`estimation_method`* can be chosen to either be the slow but
mathematically optimal *"gold_standard"* method or the faster
*"normalized_dlt"*. Here, the algorithms of
[`vector_to_proj_hom_mat2d`](vector_to_proj_hom_mat2d.md) are used.

Point pairs that still violate the consistency condition for the
final transformation are dropped, the matched points are returned as
control values. *`points_1`* contains the indices of the
matched input points from the first image, *`points_2`* contains
the indices of the corresponding points in the second image.

The parameter *`rand_seed`* can be used to control the
randomized nature of the RANSAC algorithm, and hence to obtain
reproducible results. If *`rand_seed`* is set to a positive
number, the operator yields the same result on every call with the
same parameters because the internally used random number generator
is initialized with the seed value. If *`rand_seed`* =
*0*, the random number generator is initialized with the
current time. Hence, the results may not be reproducible in this
case. The value set for the HALCON system variable *"seed_rand"*
(see [`set_system`](set_system.md)) does not affect the results of
`proj_match_points_ransac_guided`.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`image_1`** (input_object)  singlechannelimage `→` HObject (byte / uint2)

Input image 1.

**`image_2`** (input_object)  singlechannelimage `→` HObject (byte / uint2)

Input image 2.

**`rows_1`** (input_control)  point.x-array `→` Sequence[Union[float, int]]

Row coordinates of characteristic points
in image 1.

**`cols_1`** (input_control)  point.y-array `→` Sequence[Union[float, int]]

Column coordinates of characteristic points
in image 1.

**`rows_2`** (input_control)  point.x-array `→` Sequence[Union[float, int]]

Row coordinates of characteristic points
in image 2.

**`cols_2`** (input_control)  point.y-array `→` Sequence[Union[float, int]]

Column coordinates of characteristic points
in image 2.

**`gray_match_method`** (input_control)  string `→` str

Gray value comparison metric.

Default:
"ssd"

List of values:
"ncc", "sad", "ssd"

**`mask_size`** (input_control)  integer `→` int

Size of gray value masks.

Default:
10

Value range:
`mask_size
≤
90`

**`hom_mat_2dguide`** (input_control)  hom_mat2d `→` Sequence[float]

Approximation of the Homogeneous projective
transformation matrix between the two images.

**`distance_tolerance`** (input_control)  real `→` float

Tolerance for the matching search window.

Default:
20.0

Suggested values:
0.2, 0.5, 1.0, 2.0, 3.0, 5.0, 10.0, 20.0, 50.0

**`match_threshold`** (input_control)  number `→` Union[int, float]

Threshold for gray value matching.

Default:
10

Suggested values:
10, 20, 50, 100, 0.9, 0.7

**`estimation_method`** (input_control)  string `→` str

Transformation matrix estimation algorithm.

Default:
"normalized_dlt"

List of values:
"gold_standard", "normalized_dlt"

**`distance_threshold`** (input_control)  real `→` float

Threshold for transformation consistency check.

Default:
0.2

**`rand_seed`** (input_control)  integer `→` int

Seed for the random number generator.

Default:
0

**`hom_mat_2d`** (output_control)  hom_mat2d `→` Sequence[float]

Homogeneous projective transformation matrix.

**`points_1`** (output_control)  integer-array `→` Sequence[int]

Indices of matched input points in image 1.

**`points_2`** (output_control)  integer-array `→` Sequence[int]

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
