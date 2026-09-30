# AffineTransImageSize (Operator)

## Name

`AffineTransImageSize` — Apply an arbitrary affine 2D transformation to an image and specify
the output image size.

## Signature

`static void HOperatorSet.AffineTransImageSize(HObject image, out HObject imageAffineTrans, HTuple homMat2D, HTuple interpolation, HTuple width, HTuple height)`

`HImage HImage.AffineTransImageSize(HHomMat2D homMat2D, string interpolation, int width, int height)`

`HImage HHomMat2D.AffineTransImageSize(HImage image, string interpolation, int width, int height)`

## Description

`AffineTransImageSize` applies an arbitrary affine 2D
transformation, i.e., scaling, rotation, translation, and slant
(skewing), to the images given in *`image`* and returns the
transformed images in *`imageAffineTrans`*. The affine
transformation is described by the homogeneous transformation matrix
given in *`homMat2D`*, which can be created using the operators
[`HomMat2dIdentity`](hom_mat2d_identity.md), [`HomMat2dScale`](hom_mat2d_scale.md),
[`HomMat2dRotate`](hom_mat2d_rotate.md), [`HomMat2dTranslate`](hom_mat2d_translate.md), etc., or be
the result of operators like [`VectorAngleToRigid`](vector_angle_to_rigid.md).

The components of the homogeneous transformation matrix are
interpreted as follows: The *row* coordinate of the image
corresponds to x and the *column* coordinate corresponds to
y of the coordinate system in which the transformation matrix was
defined. This is necessary to obtain a right-handed coordinate
system for the image. In particular, this assures that rotations
are performed in the correct direction. Note that the (x,y)
order of the matrices quite naturally corresponds to the usual
(row,column) order for coordinates in the image.

The region of the input image is ignored, i.e., assumed to be the
full rectangle of the image. The region of the resulting image is
set to the transformed rectangle of the input image. If necessary,
the resulting image is filled with zero (black) outside of the
region of the original image.

Generally, transformed points will lie between pixel coordinates.
Therefore, an appropriate interpolation scheme has to be used. The
interpolation can also be used to avoid aliasing effects for scaled
images. The quality and speed of the interpolation can be set by
the parameter *`interpolation`*:

- **nearest_neighbor** —

  Nearest-neighbor interpolation: The
  gray value is determined from the nearest pixel's gray value
  (possibly low quality, very fast).
- **bilinear** —

  Bilinear interpolation. The gray value is
  determined from the four nearest pixels through bilinear
  interpolation. If the affine transformation contains a scaling
  with a scale factor < 1, no smoothing is performed, which may
  cause severe aliasing effects (medium quality and run time).
- **bicubic** —

  Bicubic interpolation. The gray value is
  determined from the $4\times4$ nearest pixels through
  bicubic interpolation. If the affine transformation contains a
  scaling with a scale factor < 1, no smoothing is performed,
  which may cause severe aliasing effects (high quality for
  enlargements, slow).
- **constant** —

  Bilinear interpolation. The gray value is
  determined from the four nearest pixels through bilinear
  interpolation. If the affine transformation contains a scaling
  with a scale factor < 1, a kind of mean filter is used to
  prevent aliasing effects (medium quality and run time).
- **weighted** —

  Bilinear interpolation. The gray value is
  determined from the four nearest pixels through bilinear
  interpolation. If the affine transformation contains a scaling
  with a scale factor < 1, a kind of Gaussian filter is used to
  prevent aliasing effects (high quality, slow).

In addition, the system parameter *"int_zooming"* (see
[`SetSystem`](set_system.md)) affects the accuracy of the transformation. If
*"int_zooming"* is set to *"true"*, the transformation
for byte, int2 and uint2 images is carried out internally using
fixed point arithmetic, leading to much shorter execution times.
However, the accuracy of the transformed gray values is smaller in
this case. For byte images, the differences to the more accurate
calculation (using *"int_zooming"* = *"false"*) is
typically less than two gray levels. Correspondingly, for int2 and
uint2 images, the gray value differences are less than 1/128 times
the dynamic gray value range of the image, i.e., they can be as
large as 512 gray levels if the entire dynamic range of 16 bit is
used. When using fixed point arithmetic, the domain of
resulting images can differ as well.
Additionally, if a large scale factor is applied and a large
output image is obtained, then undefined gray values at the lower
and at the right image border may result. The maximum width
$B_{max}$ of this border of undefined gray values can be
estimated as $B_{max}=0.5\cdot S\cdot I/2^{15}$, where S is the scale factor in one dimension
and I is the size of the output image in the corresponding
dimension. For real images, the parameter *"int_zooming"*
does not affect the accuracy, since the internal calculations are
always done using floating point arithmetic.

The size of the target image is specified by the parameters
*`width`* and *`height`*. Note that the image is always
clipped at the left and upper edge, i.e., all image parts that have
negative coordinates after the transformation are clipped. If the
affine transformation (in particular, the translation) is chosen
appropriately, a part of the image can be transformed as well as
cropped in one call. This is useful, for example, when using the
variation model (see [`CompareVariationModel`](compare_variation_model.md)), because with
this mechanism only the parts of the image that should be examined,
are transformed.

## Attention

The region of the input image is ignored.

`AffineTransImageSize` does not use the HALCON standard
coordinate system (with the origin in the center of the upper left
pixel), but instead uses the same coordinate system as in
[`AffineTransPixel`](affine_trans_pixel.md), i.e., the origin lies in the upper left
corner of the upper left pixel. Therefore, applying
`AffineTransImageSize` corresponds to a chain of
transformations (see [`AffineTransPixel`](affine_trans_pixel.md)), which is applied
to each point of the image (input and output pixels as homogeneous
vectors). As an effect, you might get unexpected results when
creating affine transformations based on coordinates that are
derived from the image, e.g., by operators like
[`AreaCenterGray`](area_center_gray.md). For example, if you use this operator to
calculate the center of gravity of a rotationally symmetric image
and then rotate the image around this point using
[`HomMat2dRotate`](hom_mat2d_rotate.md), the resulting image will not lie on the
original one. In such a case, you can compensate this effect by
applying the following translations to *`homMat2D`* before
using it in `AffineTransImageSize`:

|  |
| --- |
| `hom_mat2d_translate(HomMat2D, 0.5, 0.5, HomMat2DTmp)` |
| `hom_mat2d_translate_local(HomMat2DTmp, -0.5, -0.5, HomMat2DAdapted)` |
| `affine_trans_image_size(Image, ImageAffineTrans, HomMat2DAdapted, 'constant', Width, Height)` |

For an explanation of the different 2D coordinate systems
used in HALCON, see the introduction of chapter
[Transformations / 2D Transformations](toc_transformations_2dtransformations.md).

## Execution Information

- Supports OpenCL compute devices.
- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on channel level.
- Automatically parallelized on internal data level.

## Parameters

**`image`** (input_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / int2 / uint2 / real)

Input image.

**`imageAffineTrans`** (output_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / int2 / uint2 / real)

Transformed image.

**`homMat2D`** (input_control)  hom_mat2d `→` [HHomMat2D](HHomMat2D.md), [HTuple](HTuple.md) (*double*)

Input transformation matrix.

**`interpolation`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Type of interpolation.

Default:
"constant"

List of values:
"bicubic", "bilinear", "constant", "nearest_neighbor", "weighted"

**`width`** (input_control)  extent.x `→` [HTuple](HTuple.md) (*int* / long)

Width of the output image.

Default:
640

Suggested values:
128, 160, 192, 256, 320, 384, 512, 640, 768

**`height`** (input_control)  extent.y `→` [HTuple](HTuple.md) (*int* / long)

Height of the output image.

Default:
480

Suggested values:
120, 128, 144, 240, 256, 288, 480, 512, 576

## Result

If the matrix *`homMat2D`* represents an affine transformation
(i.e., not a projective transformation),
`AffineTransImageSize` returns 2 (
H_MSG_TRUE)
. If the input is empty
the behavior can be set via
`set_system(::'no_object_result',<Result>:)`. If necessary,
an exception is raised.

## Possible Predecessors

`HomMat2dIdentity`,
`HomMat2dTranslate`,
`HomMat2dRotate`,
`HomMat2dScale`,
`HomMat2dReflect`

## Alternatives

`AffineTransImage`,
`ZoomImageSize`,
`ZoomImageFactor`,
`MirrorImage`,
`RotateImage`,
`AffineTransRegion`

## See also

`SetPartStyle`

## Module

Foundation
