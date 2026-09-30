# proj_match_points_distortion_ransac_guided (Operator)

## Name

`proj_match_points_distortion_ransac_guided` — Compute a projective transformation matrix and the radial distortion
coefficient between two images by finding correspondences between
points based on known approximations of the projective
transformation matrix and the radial distortion coefficient.

## Signature

`def proj_match_points_distortion_ransac_guided(image_1: HObject, image_2: HObject, rows_1: Sequence[Union[float, int]], cols_1: Sequence[Union[float, int]], rows_2: Sequence[Union[float, int]], cols_2: Sequence[Union[float, int]], gray_match_method: str, mask_size: int, hom_mat_2dguide: Sequence[float], kappa_guide: float, distance_tolerance: float, match_threshold: Union[int, float], estimation_method: str, distance_threshold: Union[float, int], rand_seed: int) -> Tuple[Sequence[float], float, float, Sequence[int], Sequence[int]]`

## Description

Given a set of coordinates of characteristic points
(*`rows_1`*,*`cols_1`*) and
(*`rows_2`**`cols_2`*) in both input images
*`image_1`* and *`image_2`*, which must have identical size,
and given known approximations *`hom_mat_2dguide`* and
*`kappa_guide`* for the transformation matrix and the radial
distortion coefficient between *`image_1`* and *`image_2`*,
`proj_match_points_distortion_ransac_guided` automatically
determines corresponding points, the homogeneous projective
transformation matrix *`hom_mat_2d`*, and the radial distortion
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
Thus, `proj_match_points_distortion_ransac_guided` assumes that the
principal point of the camera, i.e., the center of the radial
distortions, lies at the center of the image.

The returned *`kappa`* can be used to construct camera
parameters that can be used to rectify images or points (see
[`change_radial_distortion_cam_par`](change_radial_distortion_cam_par.md),
[`change_radial_distortion_image`](change_radial_distortion_image.md), and
[`change_radial_distortion_points`](change_radial_distortion_points.md)):
$$CamPar = [\'area_scan_telecentric_division\',1.0,Kappa,1.0,1.0,0.5(w - 1),0.5(h - 1),w,h]$$ ![figure](../assets/e33e0685dafb939c.svg)

The approximations *`hom_mat_2dguide`* and *`kappa_guide`*
can, for example, be calculated with
[`proj_match_points_distortion_ransac`](proj_match_points_distortion_ransac.md) on lower resolution
versions of *`image_1`* and *`image_2`*. See the example
below.

The matching process is based on characteristic points, which can be
extracted with point operators like [`points_foerstner`](points_foerstner.md) or
[`points_harris`](points_harris.md). The matching itself is carried out in two
steps: first, gray value correlations of mask windows around the
input points in the first and the second image are determined and an
initial matching between them is generated using the similarity of
the windows in both images. Then, the RANSAC algorithm is applied
to find the projective transformation matrix and radial distortion
coefficient that maximizes the number of correspondences under the
above constraint.

The size of the mask windows used for the matching is
*`mask_size`* x
*`mask_size`*. Three metrics for the correlation can be
selected. If *`gray_match_method`* has the value *"ssd"*,
the sum of the squared gray value differences is used,
*"sad"* means the sum of absolute differences, and
*"ncc"* is the normalized cross correlation. For details
please refer to [`binocular_disparity`](binocular_disparity.md). The metric is minimized
(*"ssd"*, *"sad"*) or maximized (*"ncc"*) over
all possible point pairs. A thus found matching is only accepted if
the value of the metric is below the value of
*`match_threshold`* (*"ssd"*, *"sad"*) or above
that value (*"ncc"*).

To increase the algorithm's performance, the search area for the
match candidates is limited based on the approximate transformation
specified by *`hom_mat_2dguide`* and *`kappa_guide`*. Only
points within a distance of *`distance_tolerance`* around the
point in *`image_2`* that is obtained when transforming a point
in *`image_1`* via *`hom_mat_2dguide`* and
*`kappa_guide`* are considered for the matching.

After the initial matching has been completed, a randomized search
algorithm (RANSAC) is used to determine the projective
transformation matrix *`hom_mat_2d`* and the radial distortion
coefficient *`kappa`*. It tries to find the parameters that
are consistent with a maximum number of correspondences. For a
point to be accepted, the distance to its corresponding transformed
point must not exceed the threshold *`distance_threshold`*.
Consequently, *`distance_threshold`* should be smaller than
*`distance_tolerance`*.

The parameter *`estimation_method`* determines which algorithm
is used to compute the projective transformation matrix. A linear
algorithm is used if *`estimation_method`* is set to
*"linear"*. This algorithm is very fast and returns accurate
results for small to moderate noise of the point coordinates and for
most distortions (except for small distortions). For
*`estimation_method`* = *"gold_standard"*, a
mathematically optimal but slower optimization is used, which
minimizes the geometric reprojection error. In general, it is
preferable to use *`estimation_method`* =
*"gold_standard"*.

The value *`error`* indicates the overall quality of the
estimation procedure and is the mean symmetric euclidean distance in
pixels between the points and their corresponding transformed
points.

Point pairs consistent with the above constraints are considered to
be corresponding points. *`points_1`* contains the indices of
the matched input points from the first image and *`points_2`*
contains the indices of the corresponding points in the second
image.

The parameter *`rand_seed`* can be used to control the
randomized nature of the RANSAC algorithm, and hence to obtain
reproducible results. If *`rand_seed`* is set to a positive
number, the operator returns the same result on every call with the
same parameters because the internally used random number generator
is initialized with *`rand_seed`*. If *`rand_seed`* =
*0*, the random number generator is initialized with the
current time. In this case the results may not be reproducible.
The value set for the HALCON system variable *"seed_rand"*
(see [`set_system`](set_system.md)) does not affect the results of
`proj_match_points_distortion_ransac_guided`.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`image_1`** (input_object)  singlechannelimage `→` HObject (byte / uint2)

Input image 1.

**`image_2`** (input_object)  singlechannelimage `→` HObject (byte / uint2)

Input image 2.

**`rows_1`** (input_control)  point.y-array `→` Sequence[Union[float, int]]

Input points in image 1 (row coordinate).

Restriction:
`length(Rows1) >= 5`

**`cols_1`** (input_control)  point.x-array `→` Sequence[Union[float, int]]

Input points in image 1 (column coordinate).

Restriction:
`length(Cols1) == length(Rows1)`

**`rows_2`** (input_control)  point.y-array `→` Sequence[Union[float, int]]

Input points in image 2 (row coordinate).

Restriction:
`length(Rows2) >= 5`

**`cols_2`** (input_control)  point.x-array `→` Sequence[Union[float, int]]

Input points in image 2 (column coordinate).

Restriction:
`length(Cols2) == length(Rows2)`

**`gray_match_method`** (input_control)  string `→` str

Gray value match metric.

Default:
"ncc"

List of values:
"ncc", "sad", "ssd"

**`mask_size`** (input_control)  integer `→` int

Size of gray value masks.

Default:
10

Suggested values:
3, 7, 15

Value range:
`1
≤
mask_size`

**`hom_mat_2dguide`** (input_control)  hom_mat2d `→` Sequence[float]

Approximation of the homogeneous projective
transformation matrix between the two images.

**`kappa_guide`** (input_control)  real `→` float

Approximation of the radial distortion coefficient
in the two images.

**`distance_tolerance`** (input_control)  real `→` float

Tolerance for the matching search window.

Default:
20.0

Suggested values:
0.2, 0.5, 1.0, 2.0, 3.0, 5.0, 10.0, 20.0, 50.0

Restriction:
`DistanceTolerance > 0`

**`match_threshold`** (input_control)  number `→` Union[int, float]

Threshold for gray value matching.

Default:
0.7

Suggested values:
0.9, 0.7, 0.5, 10, 20, 50, 100

**`estimation_method`** (input_control)  string `→` str

Algorithm for the computation of the projective
transformation matrix.

Default:
"gold_standard"

List of values:
"gold_standard", "linear"

**`distance_threshold`** (input_control)  number `→` Union[float, int]

Threshold for transformation consistency check.

Default:
1

Restriction:
`DistanceThreshold > 0`

**`rand_seed`** (input_control)  integer `→` int

Seed for the random number generator.

Default:
0

**`hom_mat_2d`** (output_control)  hom_mat2d `→` Sequence[float]

Computed homogeneous projective transformation matrix.

**`kappa`** (output_control)  real `→` float

Computed radial distortion coefficient.

**`error`** (output_control)  real `→` float

Root-Mean-Square transformation error.

**`points_1`** (output_control)  integer-array `→` Sequence[int]

Indices of matched input points in image 1.

**`points_2`** (output_control)  integer-array `→` Sequence[int]

Indices of matched input points in image 2.

## Example (HDevelop)

```
Factor := 0.5
zoom_image_factor (Image1, Image1Zoomed, Factor, Factor, 'constant')
zoom_image_factor (Image2, Image2Zoomed, Factor, Factor, 'constant')
points_foerstner (Image1Zoomed, 1, 2, 3, 200, 0.3, 'gauss', 'true', \
                  Rows1, Cols1, _, _, _, _, _, _, _, _)
points_foerstner (Image2Zoomed, 1, 2, 3, 200, 0.3, 'gauss', 'true', \
                  Rows2, Cols2, _, _, _, _, _, _, _, _)
get_image_size (Image1Zoomed, Width, Height)
proj_match_points_distortion_ransac (Image1Zoomed, Image2Zoomed, \
                                     Rows1, Cols1, Rows2, Cols2, \
                                     'ncc', 10, 0, 0, Height, Width, \
                                     0, 0.5, 'gold_standard', 2, 0, \
                                     HomMat2D, Kappa, Error, \
                                     Points1, Points2)
hom_mat2d_scale_local (HomMat2D, Factor, Factor, HomMat2DGuide)
hom_mat2d_scale (HomMat2DGuide, 1.0/Factor, 1.0/Factor, 0, 0, \
                 HomMat2DGuide)
KappaGuide := Kappa*Factor*Factor
points_foerstner (Image1, 1, 2, 3, 200, 0.3, 'gauss', 'true', \
                  Rows1, Cols1, _, _, _, _, _, _, _, _)
points_foerstner (Image2, 1, 2, 3, 200, 0.3, 'gauss', 'true', \
                  Rows2, Cols2, _, _, _, _, _, _, _, _)
proj_match_points_distortion_ransac_guided (Image1, Image2, \
                                            Rows1, Cols1, \
                                            Rows2, Cols2, \
                                            'ncc', 10, \
                                            HomMat2DGuide, \
                                            KappaGuide, 5, 0.5, \
                                            'gold_standard', 2, 0, \
                                            HomMat2D, Kappa, \
                                            Error, Points1, Points2)
get_image_size (Image1, Width, Height)
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

`points_foerstner`,
`points_harris`

## Possible Successors

`vector_to_proj_hom_mat2d_distortion`,
`change_radial_distortion_cam_par`,
`change_radial_distortion_image`,
`change_radial_distortion_points`,
`gen_binocular_proj_rectification`,
`projective_trans_image`,
`projective_trans_image_size`,
`projective_trans_region`,
`projective_trans_contour_xld`,
`projective_trans_point_2d`,
`projective_trans_pixel`

## Alternatives

`proj_match_points_distortion_ransac`

## See also

`proj_match_points_ransac`,
`proj_match_points_ransac_guided`,
`hom_vector_to_proj_hom_mat2d`,
`vector_to_proj_hom_mat2d`

## References

Richard Hartley, Andrew Zisserman: “Multiple View Geometry in
Computer Vision”; Cambridge University Press, Cambridge; 2003.
  
Olivier Faugeras, Quang-Tuan Luong: “The Geometry of Multiple
Images: The Laws That Govern the Formation of Multiple Images of a
Scene and Some of Their Applications”; MIT Press, Cambridge, MA;
2001.

## Module

Matching
