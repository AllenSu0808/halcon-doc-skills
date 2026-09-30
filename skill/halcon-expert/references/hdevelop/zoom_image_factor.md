# zoom_image_factor (Operator)

## Name

`zoom_image_factor` — Zoom an image by a given factor.

## Signature

`zoom_image_factor(Image : ImageZoomed : ScaleWidth, ScaleHeight, Interpolation : )`

## Description

`zoom_image_factor` scales the image *`Image`* by a
factor of *`ScaleWidth`* in width and a factor
*`ScaleHeight`* in height. The parameter
*`Interpolation`* determines the type of interpolation used
(see [`affine_trans_image`](affine_trans_image.md)). The domain of the input image is
ignored, i.e., assumed to be the full rectangle of the image.

## Attention

If the system parameter *'int_zooming'* is set to
*'true'*, the internally used integer arithmetic may lead to
errors in the following three cases: First, if
`zoom_image_factor` is used on an uint2 or int2 image with
high dynamics (i.e. images containing values close to the respective
limits) in combination with scale factors smaller than 0.5, then
the gray values of the output image may be erroneous.
Second, if *`Interpolation`* is set to a value other than
*'nearest_neighbor'*, a large scale factor is applied, and a
large output image is obtained, then undefined gray values at the
lower and at the right image border may result. The maximum width
$B_{max}$ of this border of undefined gray values can be
estimated as $B_{max}=0.5\cdot S\cdot I/2^{15}$, where S is the scale factor in one dimension
and I is the size of the output image in the corresponding
dimension.
Third, for real images undefined gray values can occur on all image
borders, if *`Interpolation`* is set to *'nearest_neighbor'*,
and if both the input and output image is large.
In all cases, it is recommended to set
*'int_zooming'* to *'false'* via the operator
[`set_system`](set_system.md).

If *'nearest_neighbor'* is set as interpolation method
the results can differ slightly for different image types.
This is due to the usage of image type specific optimizations of the applied
interpolation algorithm.

`zoom_image_factor` is not parallelized internally if
*`ScaleWidth`* = 0.5 and *`ScaleHeight`* =
0.5. Further `zoom_image_factor` is not parallelized
internally with *`Interpolation`*=*'nearest_neighbor'*.

`zoom_image_factor` can be executed on OpenCL devices if the
input image does not exceed the maximum size of image objects of the
selected device. Due to numerical reasons, there can be slight
differences in the output compared to the execution on the CPU.

## Execution Information

- Supports OpenCL compute devices.
- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on channel level.
- Automatically parallelized on internal data level.

## Parameters

**`Image`** (input_object)  (multichannel-)image(-array) `→` object (byte* / int2* / uint2* / real*) **allowed for compute devices*

Input image.

**`ImageZoomed`** (output_object)  (multichannel-)image(-array) `→` object (byte / int2 / uint2 / real)

Scaled image.

**`ScaleWidth`** (input_control)  extent.x `→`  (real)

Scale factor for the width of the image.

Default:
0.5

Suggested values:
0.25, 0.5, 1.5, 2.0

Value range:
`0.001
≤
ScaleWidth
≤
10.0`

Minimum increment:
0.001

Recommended increment:
0.1

**`ScaleHeight`** (input_control)  extent.y `→`  (real)

Scale factor for the height of the image.

Default:
0.5

Suggested values:
0.25, 0.5, 1.5, 2.0

Value range:
`0.001
≤
ScaleHeight
≤
10.0`

Minimum increment:
0.001

Recommended increment:
0.1

**`Interpolation`** (input_control)  string `→`  (string)

Type of interpolation.

Default:
'constant'

List of values:
'bicubic', 'bilinear', 'constant', 'nearest_neighbor', 'weighted'

## Example (HDevelop)

```
read_image(Image,'monkey')
dev_display (Image)
zoom_image_factor (Image, ZoomImage, 0.25, 0.25, 'constant')
dev_display (ZoomImage)
```

## Alternatives

`zoom_image_size`,
`affine_trans_image`,
`hom_mat2d_scale`

## See also

`hom_mat2d_scale`,
`affine_trans_image`

## Module

Foundation
