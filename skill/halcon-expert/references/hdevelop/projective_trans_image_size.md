# projective_trans_image_size (Operator)

## Name

`projective_trans_image_size` — Apply a projective transformation to an image and specify the output
image size.

## Signature

`projective_trans_image_size(Image : TransImage : HomMat2D, Interpolation, Width, Height, TransformDomain : )`

## Description

`projective_trans_image_size` applies the projective
transformation (homography) determined by the homogeneous
transformation matrix *`HomMat2D`* on the input image
*`Image`* and stores the result into the output image
*`TransImage`*.

*`TransImage`* will be clipped at the output dimensions
*`Height`*x*`Width`*. Apart from this,
`projective_trans_image_size` is identical to its alternative
version [`projective_trans_image`](projective_trans_image.md).

## Attention

The used coordinate system is the same as in
[`affine_trans_pixel`](affine_trans_pixel.md). This means that in fact not
*`HomMat2D`* is applied but a modified version. Therefore,
applying `projective_trans_image_size` corresponds to the following
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
before using it in `projective_trans_image_size`:

|  |
| --- |
| `hom_mat2d_translate(HomMat2D, 0.5, 0.5, HomMat2DTmp)` |
| `hom_mat2d_translate_local(HomMat2DTmp, -0.5, -0.5, HomMat2DAdapted)` |
| `projective_trans_image_size(Image, TransImage, HomMat2DAdapted, 'bilinear', Width, Height, 'false')` |

For an explanation of the different 2D coordinate systems
used in HALCON, see the introduction of chapter
[Transformations / 2D Transformations](toc_transformations_2dtransformations.md).

`projective_trans_image_size` can be executed on OpenCL devices if
the input image does not exceed the maximum size of image objects of the
selected device and the parameter *`TransformDomain`* is set to
*'false'*.
The result can diverge slightly from that calculated on the CPU.

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

**`Width`** (input_control)  extent.x `→`  (integer)

Output image width.

**`Height`** (input_control)  extent.y `→`  (integer)

Output image height.

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

`projective_trans_image`,
`projective_trans_contour_xld`,
`projective_trans_region`,
`projective_trans_point_2d`,
`projective_trans_pixel`

## Module

Foundation
