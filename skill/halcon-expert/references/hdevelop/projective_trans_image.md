# projective_trans_image (Operator)

## Name

`projective_trans_image` — Apply a projective transformation to an image.

## Signature

`projective_trans_image(Image : TransImage : HomMat2D, Interpolation, AdaptImageSize, TransformDomain : )`

## Description

`projective_trans_image` applies the projective transformation
(homography) determined by the homogeneous transformation matrix
*`HomMat2D`* on the input image *`Image`* and stores the
result into the output image *`TransImage`*.

If the parameter *`AdaptImageSize`* is set to
*'false'*, *`TransImage`* will have the same size as
*`Image`*; if *`AdaptImageSize`* is *'true'*, the
output image size will be automatically adapted so that all
non-negative points of the transformed image are visible.

The parameter *`Interpolation`* determines, which interpolation
method is used to determine the gray values of the output image.
For *`Interpolation`* = *'nearest_neighbor'*, the gray
value is determined from the nearest pixel in the input image. This
mode is very fast, but also leads to the typical “jagged”
appearance for large enlargements of the image. For
*`Interpolation`* = *'bilinear'*, the gray values are
interpolated bilinearly, leading to longer runtimes, but also to
significantly improved results.

The parameter *`TransformDomain`* can be used to determine
whether the domain of *`Image`* is also transformed. Since the
transformation of the domain costs runtime, this parameter should be
used to specify whether this is desired or not. If
*`TransformDomain`* is set to *'false'* the domain of
the input image is ignored and the complete image is transformed.

The projective transformation matrix could for example be created
using the operator [`vector_to_proj_hom_mat2d`](vector_to_proj_hom_mat2d.md).

In a homography the points to be projected are represented by
homogeneous vectors of the form (x,y,w). A Euclidean point can be
derived as (x',y') = $\left( \frac{x}{w}, \frac{y}{w} \right)$ ![figure](../assets/db9a73da5e74500b.svg).

Just like in [`affine_trans_image`](affine_trans_image.md), x represents the row
coordinate while y represents the column coordinate in
`projective_trans_image`. With this convention, affine
transformations are a special case of projective transformations in
which the last row of *`HomMat2D`* is of the form (0,0,c).

For images of type byte or uint2 the system
parameter *'int_zooming'* selects between fast calculation in
floating point arithmetics (*'int_zooming'* = *'true'*)
and highly accurate floating point arithmetics
(*'int_zooming'* = *'false'*). Especially for
*`Interpolation`* = *'bilinear'*, however, the faster
calculation can lead to minor gray value deviations since the
faster algorithm is less accurate and only has an accuracy around
$10^{-7}$ times the size of the image. Therefore, when
applying large scales *'int_zooming'* = *'false'*
is recommended.

## Attention

The used coordinate system is the same as in
[`affine_trans_pixel`](affine_trans_pixel.md). This means that in fact not
*`HomMat2D`* is applied but a modified version. Therefore,
applying `projective_trans_image` corresponds to the following
chain of transformations, which is applied to each point
$(Row_{i},Col_{i})$ of the image (input and output
pixels as homogeneous vectors):

$$\left(\begin{array}{c}RowTrans_{i} \\\ColTrans_{i} \\\ 1\end{array}\right) = \left[\begin{array}{ccc}1 & 0 & -0.5 \\0 & 1 & -0.5 \\0 & 0 & 1\end{array}\right] \cdot \text{HomMat2D} \cdot \left[\begin{array}{ccc}1 & 0 & +0.5 \\0 & 1 & +0.5 \\0 & 0 & 1\end{array}\right] \cdot \left(\begin{array}{c}Row_i \\Col_i \\ 1\end{array}\right)$$ ![figure](../assets/f9a1b905f5066ea4.svg)

As an effect, you might get unexpected results when creating projective
transformations based on coordinates that are derived from the
image, e.g., by operators like [`area_center_gray`](area_center_gray.md). For
example, if you use this operator to calculate the center of gravity
of a rotationally symmetric image and then rotate the image around
this point using [`hom_mat2d_rotate`](hom_mat2d_rotate.md), the resulting image will
not lie on the original one. In such a case, you can compensate this
effect by applying the following translations to *`HomMat2D`*
before using it in `projective_trans_image`:

|  |
| --- |
| `hom_mat2d_translate(HomMat2D, 0.5, 0.5, HomMat2DTmp)` |
| `hom_mat2d_translate_local(HomMat2DTmp, -0.5, -0.5, HomMat2DAdapted)` |
| `projective_trans_image(Image, TransImage, HomMat2DAdapted, 'bilinear', 'false', 'false')` |

For an explanation of the different 2D coordinate systems
used in HALCON, see the introduction of chapter
[Transformations / 2D Transformations](toc_transformations_2dtransformations.md).

`projective_trans_image` can be executed on OpenCL devices if the input
image does not exceed the maximum size of image objects of the selected
device and the parameter *`TransformDomain`* is set to
*'false'*. The result can diverge slightly from that calculated on
the CPU.

## Execution Information

- Supports OpenCL compute devices.
- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on channel level.
- Automatically parallelized on internal data level.

## Parameters

**`Image`** (input_object)  (multichannel-)image(-array) `→` object (byte* / uint2* / real*) **allowed for compute devices*

Input image.

**`TransImage`** (output_object)  (multichannel-)image(-array) `→` object (byte / uint2 / real)

Output image.

**`HomMat2D`** (input_control)  hom_mat2d `→`  (real)

Homogeneous projective transformation matrix.

**`Interpolation`** (input_control)  string `→`  (string)

Interpolation method for the transformation.

Default:
'bilinear'

List of values:
'bilinear', 'nearest_neighbor'

**`AdaptImageSize`** (input_control)  string `→`  (string)

Adapt the size of the output image automatically?

Default:
'false'

List of values:
'false', 'true'

**`TransformDomain`** (input_control)  string `→`  (string)

Should the domain of the input image also be
transformed?

Default:
'false'

List of values:
'false', 'true'

List of values (for compute devices):
'false'

## Possible Predecessors

`vector_to_proj_hom_mat2d`,
`hom_vector_to_proj_hom_mat2d`,
`proj_match_points_ransac`,
`proj_match_points_ransac_guided`,
`hom_mat3d_project`

## See also

`projective_trans_image_size`,
`projective_trans_contour_xld`,
`projective_trans_region`,
`projective_trans_point_2d`,
`projective_trans_pixel`

## Module

Foundation
