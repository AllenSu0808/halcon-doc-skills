# zoom_image_factor (Operator)

## Name

`zoom_image_factor` — Zoom an image by a given factor.

## Signature

`def zoom_image_factor(image: HObject, scale_width: float, scale_height: float, interpolation: str) -> HObject`

## Description

`zoom_image_factor` scales the image *`image`* by a
factor of *`scale_width`* in width and a factor
*`scale_height`* in height. The parameter
*`interpolation`* determines the type of interpolation used
(see [`affine_trans_image`](affine_trans_image.md)). The domain of the input image is
ignored, i.e., assumed to be the full rectangle of the image.

## Attention

If the system parameter *"int_zooming"* is set to
*"true"*, the internally used integer arithmetic may lead to
errors in the following three cases: First, if
`zoom_image_factor` is used on an uint2 or int2 image with
high dynamics (i.e. images containing values close to the respective
limits) in combination with scale factors smaller than 0.5, then
the gray values of the output image may be erroneous.
Second, if *`interpolation`* is set to a value other than
*"nearest_neighbor"*, a large scale factor is applied, and a
large output image is obtained, then undefined gray values at the
lower and at the right image border may result. The maximum width
$B_{max}$ of this border of undefined gray values can be
estimated as $B_{max}=0.5\cdot S\cdot I/2^{15}$, where S is the scale factor in one dimension
and I is the size of the output image in the corresponding
dimension.
Third, for real images undefined gray values can occur on all image
borders, if *`interpolation`* is set to *"nearest_neighbor"*,
and if both the input and output image is large.
In all cases, it is recommended to set
*"int_zooming"* to *"false"* via the operator
[`set_system`](set_system.md).

If *"nearest_neighbor"* is set as interpolation method
the results can differ slightly for different image types.
This is due to the usage of image type specific optimizations of the applied
interpolation algorithm.

`zoom_image_factor` is not parallelized internally if
*`scale_width`* = 0.5 and *`scale_height`* =
0.5. Further `zoom_image_factor` is not parallelized
internally with *`interpolation`*=*"nearest_neighbor"*.

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

**`image`** (input_object)  (multichannel-)image(-array) `→` HObject (byte* / int2* / uint2* / real*) **allowed for compute devices*

Input image.

**`image_zoomed`** (output_object)  (multichannel-)image(-array) `→` HObject (byte / int2 / uint2 / real)

Scaled image.

**`scale_width`** (input_control)  extent.x `→` float

Scale factor for the width of the image.

Default:
0.5

Suggested values:
0.25, 0.5, 1.5, 2.0

Value range:
`0.001
≤
scale_width
≤
10.0`

Minimum increment:
0.001

Recommended increment:
0.1

**`scale_height`** (input_control)  extent.y `→` float

Scale factor for the height of the image.

Default:
0.5

Suggested values:
0.25, 0.5, 1.5, 2.0

Value range:
`0.001
≤
scale_height
≤
10.0`

Minimum increment:
0.001

Recommended increment:
0.1

**`interpolation`** (input_control)  string `→` str

Type of interpolation.

Default:
"constant"

List of values:
"bicubic", "bilinear", "constant", "nearest_neighbor", "weighted"

## Alternatives

`zoom_image_size`,
`affine_trans_image`,
`hom_mat2d_scale`

## See also

`hom_mat2d_scale`,
`affine_trans_image`

## Module

Foundation
