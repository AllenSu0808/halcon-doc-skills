# gen_binocular_proj_rectification (Operator)

## Name

`gen_binocular_proj_rectification` — Compute the projective rectification of weakly calibrated binocular
stereo images.

## Signature

`def gen_binocular_proj_rectification(fmatrix: Sequence[Union[float, int]], cov_fmat: Sequence[Union[float, int]], width_1: int, height_1: int, width_2: int, height_2: int, sub_sampling: Union[int, float], mapping: str) -> Tuple[HObject, HObject, Sequence[float], Sequence[float], Sequence[float]]`

## Description

A binocular stereo setup is called weakly calibrated if the
fundamental matrix,
which describes the projective relation between the two images, is known.
Rectification is the process of finding a suitable set of transformations,
that transform both images such that all corresponding epipolar lines
become collinear and parallel to the horizontal axes.
The rectified images can be
thought of as acquired by a stereo configuration where the left and right
image plane are identical and the difference between both image centers is
a horizontal translation. Note that rectification can only be performed if
both of the epipoles are located outside the images.

Typically, the fundamental matrix is calculated beforehand with
[`match_fundamental_matrix_ransac`](match_fundamental_matrix_ransac.md) and *`fmatrix`* is the basis
for the computation of the two homographies *`h1`* and *`h2`*,
which describe the rectifications for the left image and the right image
respectively. Since a projective rectification is an underdetermined
problem,
additional constraints are defined: the algorithm chooses the set
of homographies that minimizes the projective distortion induced by the
homographies in both images. For the computation of this cost function the
dimensions of the images must be provided in *`width_1`*,
*`height_1`*, *`width_2`*, *`height_2`*. After rectification
the fundamental matrix is always of the canonical form
$$\begin{pmatrix}0 & 0 & 0\\ 0 & 0 & -1\\ 0 & 1 & 0\end{pmatrix}.$$ ![figure](../assets/0eb8a51b46a5e966.svg)

In the case of a known covariance matrix *`cov_fmat`* of the
fundamental matrix *`fmatrix`*, the covariance matrix
*`cov_fmat_rect`* of the
above rectified fundamental matrix is calculated. This can help for an
improved stereo matching process because the covariance matrix defines in
terms of probabilities the image domain where to find a corresponding match.

Similar to the operator [`gen_binocular_rectification_map`](gen_binocular_rectification_map.md) the
output images *`map_1`* and *`map_2`* describe the transformation,
also called mapping, of the original images to the rectified ones.
The parameter *`mapping`* specifies whether bilinear interpolation
(*"bilinear_map"*) should be applied between the pixels in the input
image or whether the gray value of the nearest neighboring pixel should be
taken (*"nn_map"*).
The size and resolution of the maps and of the transformed
images can be adjusted by the parameter *`sub_sampling`*, which applies
a sub-sampling factor to the original images. For example, a factor of two
will halve the image sizes. If just the two homographies are required
*`mapping`* can be set to *"no_map"* and no maps will be
returned.
For speed reasons, this option should be used if for a
specific stereo configuration the images must be rectified only once.
If the stereo setup is fixed, the maps should be generated only once
and both images should be rectified with [`map_image`](map_image.md);
this will result in the smallest computational cost for on-line
rectification.

When using the maps, the transformed images are of the same size as
their maps.
Each pixel in the map contains the description of how the new pixel at this
position is generated.
The images *`map_1`* and *`map_2`* are single channel images if
*`mapping`* is set to *"nn_map"* and five channel images if
it is set to *"bilinear_map"*. In the first channel, which is of type
int4, the pixels contain the linear coordinates of their reference pixels
in the original image. With *`mapping`* equal to *"no_map"*
this reference pixel is the nearest neighbor to the back-transformed pixel
coordinates of the map.
In the case of bilinear interpolation the reference pixel is the next upper
left pixel relative to the back-transformed coordinates.
The following scheme shows the ordering of the pixels in the original image
next to the back-transformed pixel coordinates, where the reference pixel
takes the number 2.

|  |  |
| --- | --- |
| 2 | 3 |
| 4 | 5 |

The channels 2 to 5, which are of type uint2, contain
the weights of the relevant pixels for the bilinear interpolation.

Based on the rectified images, the disparity be
computed using [`binocular_disparity`](binocular_disparity.md).
In contrast to stereo with fully calibrated cameras, using the operator
[`gen_binocular_rectification_map`](gen_binocular_rectification_map.md) and its successors, metric depth
information can not be derived for weakly calibrated cameras.
The disparity map gives just a qualitative depth ordering of the
scene.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`map_1`** (output_object)  image(-array) `→` HObject (int4 / uint2)

Image coding the rectification of the 1. image.

**`map_2`** (output_object)  image(-array) `→` HObject (int4 / uint2)

Image coding the rectification of the 2. image.

**`fmatrix`** (input_control)  hom_mat2d `→` Sequence[Union[float, int]]

Fundamental matrix.

**`cov_fmat`** (input_control)  number-array `→` Sequence[Union[float, int]]

9x9 covariance matrix of the
fundamental matrix.

Default:
[]

**`width_1`** (input_control)  integer `→` int

Width of the 1. image.

Default:
512

Suggested values:
128, 256, 512, 1024

Restriction:
`Width1 > 0`

**`height_1`** (input_control)  integer `→` int

Height of the 1. image.

Default:
512

Suggested values:
128, 256, 512, 1024

Restriction:
`Height1 > 0`

**`width_2`** (input_control)  integer `→` int

Width of the 2. image.

Default:
512

Suggested values:
128, 256, 512, 1024

Restriction:
`Width2 > 0`

**`height_2`** (input_control)  integer `→` int

Height of the 2. image.

Default:
512

Suggested values:
128, 256, 512, 1024

Restriction:
`Height2 > 0`

**`sub_sampling`** (input_control)  number `→` Union[int, float]

Subsampling factor.

Default:
1

List of values:
1, 2, 3, 1.5

**`mapping`** (input_control)  string `→` str

Type of mapping.

Default:
"no_map"

List of values:
"bilinear_map", "nn_map", "no_map"

**`cov_fmat_rect`** (output_control)  number-array `→` Sequence[float]

9x9 covariance matrix of the rectified
fundamental matrix.

**`h1`** (output_control)  hom_mat2d `→` Sequence[float]

Projective transformation of the 1. image.

**`h2`** (output_control)  hom_mat2d `→` Sequence[float]

Projective transformation of the 2. image.

## Example (HDevelop)

```
* Rectify an image pair using a map.
get_image_size (Image1, Width1, Height1)
get_image_size (Image2, Width2, Height2)
points_harris (Image1, 3, 1, 0.2, 10000, Row1, Col1)
points_harris (Image2, 3, 1, 0.2, 10000, Row2, Col2)
match_fundamental_matrix_ransac (Image1, Image2, Row1, Col1, Row2, Col2, \
                                 'ncc', 21, 0, 200, 20, 50, 0, 0.9, \
                                 'gold_standard', 0.3, 1, FMatrix, \
                                 CovFMat, Error, Points1, Points2)
gen_binocular_proj_rectification (Map1, Map2, FMatrix, [], Width1, \
                                  Height1, Width2, Height2, 1, \
                                  'bilinear_map', CovFMatRect, H1, H2)
map_image (Image1, Map1, Image1Rect)
map_image (Image2, Map2, Image2Rect)

* Rectify an image pair without using a map.
get_image_size (Image1, Width1, Height1)
get_image_size (Image2, Width2, Height2)
points_harris (Image1, 3, 1, 0.2, 10000, Row1, Col1)
points_harris (Image2, 3, 1, 0.2, 10000, Row2, Col2)
match_fundamental_matrix_ransac (Image1, Image2, Row1, Col1, Row2, Col2, \
                                 'ncc', 21, 0, 200, 20, 50, 0, 0.9, \
                                 'gold_standard', 0.3, 1, FMatrix, \
                                 CovFMat, Error, Points1, Points2)
gen_binocular_proj_rectification (Map1, Map2, FMatrix, [], Width1, \
                                  Height1, Width2, Height2, 1, \
                                  'no_map', CovFMatRect, H1, H2)
* Determine the maximum extent of the two rectified images.
projective_trans_point_2d (H1, [0,0,Height1,Height1], \
                           [0,Width1,0,Width1], [1,1,1,1], R1, C1, W1)
R1 := int(floor(R1/W1))
C1 := int(floor(C1/W1))
projective_trans_point_2d (H2, [0,0,Height2,Height2], \
                           [0,Width2,0,Width2], [1,1,1,1], R2, C2, W2)
R2 := int(floor(R2/W2))
C2 := int(floor(C2/W2))
WidthRect := max([C1,C2])
HeightRect := max([R1,R2])
projective_trans_image_size (Image1, Image1Rect, H1, 'bilinear', \
                             WidthRect, HeightRect, 'false')
projective_trans_image_size (Image2, Image2Rect, H2, 'bilinear', \
                             WidthRect, HeightRect, 'false')
```

## Possible Predecessors

`match_fundamental_matrix_ransac`,
`vector_to_fundamental_matrix`

## Possible Successors

`map_image`,
`projective_trans_image`,
`binocular_disparity`

## Alternatives

`gen_binocular_rectification_map`

## References

J. Gluckmann and S.K. Nayar: “Rectifying transformations that minimize
resampling effects”; IEEE Conference on Computer Vision and Pattern
Recognition (CVPR) 2001, vol I, pages 111-117.

## Module

3D Metrology
