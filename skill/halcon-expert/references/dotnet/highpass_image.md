# HighpassImage (Operator)

## Name

`HighpassImage` — Extract high frequency components from an image.

## Signature

`static void HOperatorSet.HighpassImage(HObject image, out HObject highpass, HTuple width, HTuple height)`

`HImage HImage.HighpassImage(int width, int height)`

## Description

`HighpassImage` extracts high frequency components in an
image by applying a linear filter with the following matrix (in case
of a 7x5 matrix):
1 1 1 1 1 1 1
1 1 1 1 1 1 1
1 1 1 -35 1 1 1
1 1 1 1 1 1 1
1 1 1 1 1 1 1
This corresponds to applying a mean operator ([`MeanImage`](mean_image.md)),
and then subtracting the original gray value. For byte images, a value
of 128 is added to the result, i.e., zero crossings occur for 128.
Correspondingly for uint2 images, 32767 is added.

This filter emphasizes high frequency components (edges and
corners). The cutoff frequency is determined by the size (Height
x Width) of the
filter matrix: the larger the matrix, the smaller the cutoff
frequency is.

At the image borders the pixels' gray values are mirrored. In case
of over- or underflow the gray values are clipped (255 and 0,
resp.).

## Attention

If even values are passed for *`height`* or *`width`*,
the operator uses the next larger odd value instead. Thus, the
center of the filter mask is always uniquely determined.

`HighpassImage` can be executed on OpenCL devices. The same
limitations as for [`MeanImage`](mean_image.md) and [`SubImage`](sub_image.md) apply.

Note that filter operators may return unexpected results if
an image with a reduced domain is used as input. Please refer to the
chapter [Filters](toc_filters.md).

## Execution Information

- Supports OpenCL compute devices.
- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on channel level.
- Automatically parallelized on domain level.

## Parameters

**`image`** (input_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte* / uint2*) **allowed for compute devices*

Input image.

**`highpass`** (output_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / uint2)

High-pass-filtered result image.

**`width`** (input_control)  extent.x `→` [HTuple](HTuple.md) (*int* / long)

Width of the filter mask.

Default:
9

Suggested values:
3, 5, 7, 9, 11, 13, 17, 21, 29, 41, 51, 73, 101

Value range:
`1
≤
width`

Minimum increment:
2

Recommended increment:
2

**`height`** (input_control)  extent.y `→` [HTuple](HTuple.md) (*int* / long)

Height of the filter mask.

Default:
9

Suggested values:
3, 5, 7, 9, 11, 13, 17, 21, 29, 41, 51, 73, 101

Value range:
`1
≤
height`

Minimum increment:
2

Recommended increment:
2

## Example (C)

```
highpass_image(Image,&Highpass,7,5);
threshold(Highpass,&Region,60.0,255.0);
skeleton(Region,&Skeleton);
```

## Result

`HighpassImage` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. If the input is empty the behavior can be set via
`set_system('no_object_result',<Result>)`. If
necessary, an exception is raised.

## Possible Successors

`Threshold`,
`Skeleton`

## Alternatives

`MeanImage`,
`SubImage`,
`ConvolImage`,
`BandpassImage`

## See also

`DynThreshold`

## Module

Foundation
