# mean_image (Operator)

## Name

`mean_image` — Smooth by averaging.

## Signature

`mean_image(Image : ImageMean : MaskWidth, MaskHeight : )`

## Description

The operator `mean_image` carries out a linear smoothing with
the gray values of all input images (*`Image`*). The filter
matrix consists of ones (evaluated equally) and has the size
MaskHeight x MaskWidth. The result of the convolution is divided
by MaskHeight x MaskWidth. For border treatment the gray values are
reflected at the image edges.

For `mean_image` special optimizations are implemented that use SIMD
technology. The actual application of these special optimizations is
controlled by the system parameter *'mmx_enable'*
(see [`set_system`](set_system.md)).
If *'mmx_enable'* is set to *'true'* (and the SIMD
instruction set is available), the internal calculations are performed
using SIMD technology.
Note that SIMD technology performs best on large, compact input regions.
Depending on the input region and the capabilities of the hardware the
execution of `mean_image` might even take significantly
more time with SIMD technology than without.

At any rate, it is advantageous for the performance of `mean_image`
to choose the input region of *`Image`* such that any border treatment
is avoided.

For an explanation of the concept of smoothing filters see the introduction
of chapter [Filters / Smoothing](toc_filters_smoothing.md).

## Attention

If even values instead of odd values are given for
*`MaskHeight`* or *`MaskWidth`*, the routine uses the
next larger odd values instead (this way the center of the filter
mask is always explicitly determined).

The mean filter value on real images is calculated internally using single
precision floating point. This can lead to overflows (and thus incorrect
results) if the full dynamic range is used.

`mean_image` can be executed on OpenCL devices for byte, int2, uint2,
int4 and real images if *`MaskHeight`* is less than twice the height
of *`Image`*. For OpenCL, the mean filter value is calculated
internally using either 32 bit signed integers (for all integer image
types) or single precision floating point (for real images). This can lead
to overflows (and thus incorrect results) if *`Image`* is either an
int4 or real image and the full dynamic range is used. Additionally, to
improve performance a full scan of each row of *`Image`* is calculated
(again using either 32 bit integer or single precision floating point
arithmetic) if *`MaskWidth`* is bigger than 9. This can also lead to
overflows with very wide images even for byte, int2, or uint2 images. In
these cases, the CPU version of `mean_image` should be used.

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

**`Image`** (input_object)  (multichannel-)image(-array) `→` object (byte* / int2* / uint2* / int4* / int8 / real* / vector_field) **allowed for compute devices*

Image to be smoothed.

**`ImageMean`** (output_object)  (multichannel-)image(-array) `→` object (byte / int2 / uint2 / int4 / int8 / real / vector_field)

Smoothed image.

**`MaskWidth`** (input_control)  extent.x `→`  (integer)

Width of filter mask.

Default:
9

Suggested values:
3, 5, 7, 9, 11, 15, 23, 31, 43, 61, 101

Value range:
`1
≤
MaskWidth`

Minimum increment:
2

Recommended increment:
2

Restriction:
`odd(MaskWidth) && MaskWidth < width(Image) * 2`

**`MaskHeight`** (input_control)  extent.y `→`  (integer)

Height of filter mask.

Default:
9

Suggested values:
3, 5, 7, 9, 11, 15, 23, 31, 43, 61, 101

Value range:
`1
≤
MaskHeight`

Minimum increment:
2

Recommended increment:
2

Restriction:
`odd(MaskHeight) && MaskHeight < height(Image) * 2`

## Example (HDevelop)

```
read_image(Image,'fabrik')
mean_image(Image,Mean,3,3)
dev_display(Mean)
```

## Complexity

For each pixel: O(15).

## Result

If the parameter values are correct the operator `mean_image`
returns the value 2 (
H_MSG_TRUE)
. The behavior in case of empty input (no
input images available) is set via the operator
`set_system('no_object_result',<Result>)`.
If necessary an exception is raised.

## Possible Predecessors

`reduce_domain`,
`rectangle1_domain`

## Possible Successors

`dyn_threshold`,
`regiongrowing`

## Alternatives

`binomial_filter`,
`gauss_filter`,
`smooth_image`,
`mean_image_shape`

## See also

`anisotropic_diffusion`,
`sigma_image`,
`convol_image`,
`gen_lowpass`

## Module

Foundation
