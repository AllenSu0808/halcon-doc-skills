# RotateImage (Operator)

## Name

`RotateImage` — Rotate an image about its center.

## Signature

`static void HOperatorSet.RotateImage(HObject image, out HObject imageRotate, HTuple phi, HTuple interpolation)`

`HImage HImage.RotateImage(HTuple phi, string interpolation)`

`HImage HImage.RotateImage(double phi, string interpolation)`

## Description

`RotateImage` rotates the *`image`* counterclockwise by
*`phi`* degrees about its center and stores the result in the
output image *`imageRotate`*. The output image has the same
size as the input image. The only exception are rotations by 90 and
270 degrees where width and height will be exchanged. The domain of
the input image is ignored, i.e., assumed to be the full rectangle
of the image. The domain of the output image is the intersection of
the transformed rectangle and the rectangle of the output image.

If *`phi`* is a multiple of 90 degrees, this operator is much
faster, especially than the general operator
[`AffineTransImage`](affine_trans_image.md). The effect of the parameter
*`interpolation`* is the same as in [`AffineTransImage`](affine_trans_image.md).
It is ignored for rotations by 90, 180, and 270 degrees. If it is
necessary to rotate the domain, too, the operator
[`ProjectiveTransImage`](projective_trans_image.md) must be used.

Additionally, for images of type byte, int2 or
uint2 the system parameter *"int_zooming"* selects between
fast calculation in fixed point arithmetics
(*"int_zooming"* = *"true"*)
and highly accurate calculation in floating point arithmetics
(*"int_zooming"* = *"false"*). Except for
rotations by 90, 180, or 270 degrees, fixed point calculation
can lead to minor gray value deviations. Furthermore, the
domain of resulting images can differ as well.

## Attention

The domain of the input image is ignored, i.e., assumed to be the
full rectangle of the image. The domain of the output image is the
intersection of the transformed rectangle and the rectangle of the
output image. The angle *`phi`* is given in degrees, not in
radians. For rotations by 90, 180, and 270 degrees
`RotateImage` is not parallelized internally.

`RotateImage` can be executed on OpenCL devices if the input
image does not exceed the maximum size of image objects of the
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

**`imageRotate`** (output_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / int2 / uint2 / real)

Rotated image.

**`phi`** (input_control)  angle.deg `→` [HTuple](HTuple.md) (*double* / int / long)

Rotation angle.

Default:
90

Suggested values:
90, 180, 270

Value range:
`0
≤
phi
≤
360`

Minimum increment:
0.001

Recommended increment:
0.2

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
rotate_image(Image,RotImage,270,'constant')
dev_display (RotImage)
```

## Alternatives

`HomMat2dRotate`,
`AffineTransImage`

## See also

`MirrorImage`

## Module

Foundation
