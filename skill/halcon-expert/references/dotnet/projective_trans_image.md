# ProjectiveTransImage (Operator)

## Name

`ProjectiveTransImage` — Apply a projective transformation to an image.

## Signature

`static void HOperatorSet.ProjectiveTransImage(HObject image, out HObject transImage, HTuple homMat2D, HTuple interpolation, HTuple adaptImageSize, HTuple transformDomain)`

`HImage HImage.ProjectiveTransImage(HHomMat2D homMat2D, string interpolation, string adaptImageSize, string transformDomain)`

`HImage HHomMat2D.ProjectiveTransImage(HImage image, string interpolation, string adaptImageSize, string transformDomain)`

## Description

`ProjectiveTransImage` applies the projective transformation
(homography) determined by the homogeneous transformation matrix
*`homMat2D`* on the input image *`image`* and stores the
result into the output image *`transImage`*.

If the parameter *`adaptImageSize`* is set to
*"false"*, *`transImage`* will have the same size as
*`image`*; if *`adaptImageSize`* is *"true"*, the
output image size will be automatically adapted so that all
non-negative points of the transformed image are visible.

The parameter *`interpolation`* determines, which interpolation
method is used to determine the gray values of the output image.
For *`interpolation`* = *"nearest_neighbor"*, the gray
value is determined from the nearest pixel in the input image. This
mode is very fast, but also leads to the typical “jagged”
appearance for large enlargements of the image. For
*`interpolation`* = *"bilinear"*, the gray values are
interpolated bilinearly, leading to longer runtimes, but also to
significantly improved results.

The parameter *`transformDomain`* can be used to determine
whether the domain of *`image`* is also transformed. Since the
transformation of the domain costs runtime, this parameter should be
used to specify whether this is desired or not. If
*`transformDomain`* is set to *"false"* the domain of
the input image is ignored and the complete image is transformed.

The projective transformation matrix could for example be created
using the operator [`VectorToProjHomMat2d`](vector_to_proj_hom_mat2d.md).

In a homography the points to be projected are represented by
homogeneous vectors of the form (x,y,w). A Euclidean point can be
derived as (x',y') = $\left( \frac{x}{w}, \frac{y}{w} \right)$ ![figure](../assets/db9a73da5e74500b.svg).

Just like in [`AffineTransImage`](affine_trans_image.md), x represents the row
coordinate while y represents the column coordinate in
`ProjectiveTransImage`. With this convention, affine
transformations are a special case of projective transformations in
which the last row of *`homMat2D`* is of the form (0,0,c).

For images of type byte or uint2 the system
parameter *"int_zooming"* selects between fast calculation in
floating point arithmetics (*"int_zooming"* = *"true"*)
and highly accurate floating point arithmetics
(*"int_zooming"* = *"false"*). Especially for
*`interpolation`* = *"bilinear"*, however, the faster
calculation can lead to minor gray value deviations since the
faster algorithm is less accurate and only has an accuracy around
$10^{-7}$ times the size of the image. Therefore, when
applying large scales *"int_zooming"* = *"false"*
is recommended.

## Attention

The used coordinate system is the same as in
[`AffineTransPixel`](affine_trans_pixel.md). This means that in fact not
*`homMat2D`* is applied but a modified version. Therefore,
applying `ProjectiveTransImage` corresponds to the following
chain of transformations, which is applied to each point
$(Row_{i},Col_{i})$ of the image (input and output
pixels as homogeneous vectors):

$$\left(\begin{array}{c}RowTrans_{i} \\\ColTrans_{i} \\\ 1\end{array}\right) = \left[\begin{array}{ccc}1 & 0 & -0.5 \\0 & 1 & -0.5 \\0 & 0 & 1\end{array}\right] \cdot \text{HomMat2D} \cdot \left[\begin{array}{ccc}1 & 0 & +0.5 \\0 & 1 & +0.5 \\0 & 0 & 1\end{array}\right] \cdot \left(\begin{array}{c}Row_i \\Col_i \\ 1\end{array}\right)$$ ![figure](../assets/f9a1b905f5066ea4.svg)

As an effect, you might get unexpected results when creating projective
transformations based on coordinates that are derived from the
image, e.g., by operators like [`AreaCenterGray`](area_center_gray.md). For
example, if you use this operator to calculate the center of gravity
of a rotationally symmetric image and then rotate the image around
this point using [`HomMat2dRotate`](hom_mat2d_rotate.md), the resulting image will
not lie on the original one. In such a case, you can compensate this
effect by applying the following translations to *`homMat2D`*
before using it in `ProjectiveTransImage`:

|  |
| --- |
| `hom_mat2d_translate(HomMat2D, 0.5, 0.5, HomMat2DTmp)` |
| `hom_mat2d_translate_local(HomMat2DTmp, -0.5, -0.5, HomMat2DAdapted)` |
| `projective_trans_image(Image, TransImage, HomMat2DAdapted, 'bilinear', 'false', 'false')` |

For an explanation of the different 2D coordinate systems
used in HALCON, see the introduction of chapter
[Transformations / 2D Transformations](toc_transformations_2dtransformations.md).

`ProjectiveTransImage` can be executed on OpenCL devices if the input
image does not exceed the maximum size of image objects of the selected
device and the parameter *`transformDomain`* is set to
*"false"*. The result can diverge slightly from that calculated on
the CPU.

## Execution Information

- Supports OpenCL compute devices.
- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on channel level.
- Automatically parallelized on internal data level.

## Parameters

**`image`** (input_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte* / uint2* / real*) **allowed for compute devices*

Input image.

**`transImage`** (output_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / uint2 / real)

Output image.

**`homMat2D`** (input_control)  hom_mat2d `→` [HHomMat2D](HHomMat2D.md), [HTuple](HTuple.md) (*double*)

Homogeneous projective transformation matrix.

**`interpolation`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Interpolation method for the transformation.

Default:
"bilinear"

List of values:
"bilinear", "nearest_neighbor"

**`adaptImageSize`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Adapt the size of the output image automatically?

Default:
"false"

List of values:
"false", "true"

**`transformDomain`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Should the domain of the input image also be
transformed?

Default:
"false"

List of values:
"false", "true"

List of values (for compute devices):
"false"

## Possible Predecessors

`VectorToProjHomMat2d`,
`HomVectorToProjHomMat2d`,
`ProjMatchPointsRansac`,
`ProjMatchPointsRansacGuided`,
`HomMat3dProject`

## See also

`ProjectiveTransImageSize`,
`ProjectiveTransContourXld`,
`ProjectiveTransRegion`,
`ProjectiveTransPoint2d`,
`ProjectiveTransPixel`

## Module

Foundation
