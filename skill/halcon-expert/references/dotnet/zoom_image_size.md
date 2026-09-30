# ZoomImageSize (Operator)

## Name

`ZoomImageSize` — Zoom an image to a given size.

## Signature

`static void HOperatorSet.ZoomImageSize(HObject image, out HObject imageZoom, HTuple width, HTuple height, HTuple interpolation)`

`HImage HImage.ZoomImageSize(int width, int height, string interpolation)`

## Description

`ZoomImageSize` scales the image *`image`* to the size
given by *`width`* and *`height`*. The parameter
*`interpolation`* determines the type of interpolation used
(see [`AffineTransImage`](affine_trans_image.md)). The domain of the input image is
ignored, i.e., assumed to be the full rectangle of the image.

## Attention

If the system parameter *"int_zooming"* is set to
*"true"*, the internally used integer arithmetic may lead to
errors in the following three cases: First, if `ZoomImageSize`
is used on an uint2 or int2 image with high dynamics (i.e. images
containing values close to the respective limits) in combination
with scale factors (ratio of output to input image size) smaller
than 0.5, then the gray values of the output image may be
erroneous.
Second, if *`interpolation`* is set to a value other
than *"nearest_neighbor"*, a large scale factor is applied,
and a large output image is obtained, then undefined gray values at
the lower and at the right image border may result. The maximum
width $B_{max}$ of this border of undefined gray values
can be estimated as
$B_{max}=0.5\cdot S\cdot I/2^{15}$,
where S is the scale factor in one
dimension and I is the size of the output image in the
corresponding dimension.
Third, for real images undefined gray values can occur on all image
borders, if *`interpolation`* is set to *"nearest_neighbor"*,
and if both the input and output image is large.
In all cases, it is recommended to set
*"int_zooming"* to *"false"* via the operator
[`SetSystem`](set_system.md).

If *"nearest_neighbor"* is set as interpolation method
the results can differ slightly for different image types.
This is due to the usage of image type specific optimizations of the applied
interpolation algorithm.

`ZoomImageSize` is not parallelized internally if
*`width`* and *`height`* correspond to half the dimensions
of *`image`*. Further `ZoomImageSize` is not
parallelized internally with
*`interpolation`*=*"nearest_neighbor"*.

`ZoomImageSize` can be executed on OpenCL devices if the
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

**`image`** (input_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte* / int2* / uint2* / real*) **allowed for compute devices*

Input image.

**`imageZoom`** (output_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / int2 / uint2 / real)

Scaled image.

**`width`** (input_control)  extent.x `→` [HTuple](HTuple.md) (*int* / long)

Width of the resulting image.

Default:
512

Suggested values:
128, 256, 512

Value range:
`2
≤
width
≤
512`

Minimum increment:
1

Recommended increment:
10

**`height`** (input_control)  extent.y `→` [HTuple](HTuple.md) (*int* / long)

Height of the resulting image.

Default:
512

Suggested values:
128, 256, 512

Value range:
`2
≤
height
≤
512`

Minimum increment:
1

Recommended increment:
10

**`interpolation`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Type of interpolation.

Default:
"constant"

List of values:
"bicubic", "bilinear", "constant", "nearest_neighbor", "weighted"

## Example (HDevelop)

```
read_image(Image,'monkey')
dev_display (Image)
zoom_image_size(Image,ZoomImage,200,200,'constant')
dev_display (ZoomImage)
```

## Alternatives

`ZoomImageFactor`,
`AffineTransImage`,
`HomMat2dScale`

## See also

`HomMat2dScale`,
`AffineTransImage`

## Module

Foundation
