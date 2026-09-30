# ProjectiveTransImageSize (Operator)

## Name

`ProjectiveTransImageSize` — Apply a projective transformation to an image and specify the output
image size.

## Signature

`static void HOperatorSet.ProjectiveTransImageSize(HObject image, out HObject transImage, HTuple homMat2D, HTuple interpolation, HTuple width, HTuple height, HTuple transformDomain)`

`HImage HImage.ProjectiveTransImageSize(HHomMat2D homMat2D, string interpolation, int width, int height, string transformDomain)`

`HImage HHomMat2D.ProjectiveTransImageSize(HImage image, string interpolation, int width, int height, string transformDomain)`

## Description

`ProjectiveTransImageSize` applies the projective
transformation (homography) determined by the homogeneous
transformation matrix *`homMat2D`* on the input image
*`image`* and stores the result into the output image
*`transImage`*.

*`transImage`* will be clipped at the output dimensions
*`height`*x*`width`*. Apart from this,
`ProjectiveTransImageSize` is identical to its alternative
version [`ProjectiveTransImage`](projective_trans_image.md).

## Attention

The used coordinate system is the same as in
[`AffineTransPixel`](affine_trans_pixel.md). This means that in fact not
*`homMat2D`* is applied but a modified version. Therefore,
applying `ProjectiveTransImageSize` corresponds to the following
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
before using it in `ProjectiveTransImageSize`:

|  |
| --- |
| `hom_mat2d_translate(HomMat2D, 0.5, 0.5, HomMat2DTmp)` |
| `hom_mat2d_translate_local(HomMat2DTmp, -0.5, -0.5, HomMat2DAdapted)` |
| `projective_trans_image_size(Image, TransImage, HomMat2DAdapted, 'bilinear', Width, Height, 'false')` |

For an explanation of the different 2D coordinate systems
used in HALCON, see the introduction of chapter
[Transformations / 2D Transformations](toc_transformations_2dtransformations.md).

`ProjectiveTransImageSize` can be executed on OpenCL devices if
the input image does not exceed the maximum size of image objects of the
selected device and the parameter *`transformDomain`* is set to
*"false"*.
The result can diverge slightly from that calculated on the CPU.

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

**`width`** (input_control)  extent.x `→` [HTuple](HTuple.md) (*int* / long)

Output image width.

**`height`** (input_control)  extent.y `→` [HTuple](HTuple.md) (*int* / long)

Output image height.

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

`ProjectiveTransImage`,
`ProjectiveTransContourXld`,
`ProjectiveTransRegion`,
`ProjectiveTransPoint2d`,
`ProjectiveTransPixel`

## Module

Foundation
