# affine_trans_image_size (Operator)

## Name

`affine_trans_image_size` — Apply an arbitrary affine 2D transformation to an image and specify
the output image size.

## Signature

`def affine_trans_image_size(image: HObject, hom_mat_2d: Sequence[float], interpolation: str, width: int, height: int) -> HObject`

## Description

`affine_trans_image_size` applies an arbitrary affine 2D
transformation, i.e., scaling, rotation, translation, and slant
(skewing), to the images given in *`image`* and returns the
transformed images in *`image_affine_trans`*. The affine
transformation is described by the homogeneous transformation matrix
given in *`hom_mat_2d`*, which can be created using the operators
[`hom_mat2d_identity`](hom_mat2d_identity.md), [`hom_mat2d_scale`](hom_mat2d_scale.md),
[`hom_mat2d_rotate`](hom_mat2d_rotate.md), [`hom_mat2d_translate`](hom_mat2d_translate.md), etc., or be
the result of operators like [`vector_angle_to_rigid`](vector_angle_to_rigid.md).

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
[`set_system`](set_system.md)) affects the accuracy of the transformation. If
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
variation model (see [`compare_variation_model`](compare_variation_model.md)), because with
this mechanism only the parts of the image that should be examined,
are transformed.

## Attention

The region of the input image is ignored.

`affine_trans_image_size` does not use the HALCON standard
coordinate system (with the origin in the center of the upper left
pixel), but instead uses the same coordinate system as in
[`affine_trans_pixel`](affine_trans_pixel.md), i.e., the origin lies in the upper left
corner of the upper left pixel. Therefore, applying
`affine_trans_image_size` corresponds to a chain of
transformations (see [`affine_trans_pixel`](affine_trans_pixel.md)), which is applied
to each point of the image (input and output pixels as homogeneous
vectors). As an effect, you might get unexpected results when
creating affine transformations based on coordinates that are
derived from the image, e.g., by operators like
[`area_center_gray`](area_center_gray.md). For example, if you use this operator to
calculate the center of gravity of a rotationally symmetric image
and then rotate the image around this point using
[`hom_mat2d_rotate`](hom_mat2d_rotate.md), the resulting image will not lie on the
original one. In such a case, you can compensate this effect by
applying the following translations to *`hom_mat_2d`* before
using it in `affine_trans_image_size`:

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

**`image`** (input_object)  (multichannel-)image(-array) `→` HObject (byte / int2 / uint2 / real)

Input image.

**`image_affine_trans`** (output_object)  (multichannel-)image(-array) `→` HObject (byte / int2 / uint2 / real)

Transformed image.

**`hom_mat_2d`** (input_control)  hom_mat2d `→` Sequence[float]

Input transformation matrix.

**`interpolation`** (input_control)  string `→` str

Type of interpolation.

Default:
"constant"

List of values:
"bicubic", "bilinear", "constant", "nearest_neighbor", "weighted"

**`width`** (input_control)  extent.x `→` int

Width of the output image.

Default:
640

Suggested values:
128, 160, 192, 256, 320, 384, 512, 640, 768

**`height`** (input_control)  extent.y `→` int

Height of the output image.

Default:
480

Suggested values:
120, 128, 144, 240, 256, 288, 480, 512, 576

## Result

If the matrix *`hom_mat_2d`* represents an affine transformation
(i.e., not a projective transformation),
`affine_trans_image_size` returns 2 (
H_MSG_TRUE)
. If the input is empty
the behavior can be set via
`set_system(::'no_object_result',<Result>:)`. If necessary,
an exception is raised.

## Possible Predecessors

`hom_mat2d_identity`,
`hom_mat2d_translate`,
`hom_mat2d_rotate`,
`hom_mat2d_scale`,
`hom_mat2d_reflect`

## Alternatives

`affine_trans_image`,
`zoom_image_size`,
`zoom_image_factor`,
`mirror_image`,
`rotate_image`,
`affine_trans_region`

## See also

`set_part_style`

## Module

Foundation
