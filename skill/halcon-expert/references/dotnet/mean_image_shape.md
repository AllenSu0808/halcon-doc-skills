# MeanImageShape (Operator)

## Name

`MeanImageShape` — Smooth image using a mean filter with arbitrary mask.

## Signature

`static void HOperatorSet.MeanImageShape(HObject image, HObject mask, out HObject imageMean)`

`HImage HImage.MeanImageShape(HRegion mask)`

## Description

`MeanImageShape` performs a mean filter operation on the input image
*`image`* with a mask that is specified by the region
*`mask`* and returns the filtered image in *`imageMean`*.
The shape of the mask can be chosen arbitrarily and can, for
example, be created with operators like [`GenCircle`](gen_circle.md) or
[`DrawRegion`](draw_region.md). The position of the mask does not influence
the result since the center of gravity of the mask region is used as
the reference point of the mask. For border treatment the gray values are
reflected at the image edges.

For `MeanImageShape` special optimizations are implemented that use SIMD
technology. The actual application of these special optimizations is
controlled by the system parameter *"avx2_enable"*
(see [`SetSystem`](set_system.md)).
If *"avx2_enable"* is set to *"true"* (and the SIMD
instruction set is available), the internal calculations are performed
using SIMD technology. Furthermore, these optimizations are only used
for byte images and if the area of the filter mask provided by
*`mask`* is smaller than 129.

Note that `MeanImageShape` performs best on compact input regions.

At any rate, it is advantageous for the performance of `MeanImageShape`
to choose the input region of *`image`* such that any border treatment
is avoided.

For an explanation of the concept of smoothing filters see the introduction
of chapter [Filters / Smoothing](toc_filters_smoothing.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on channel level.
- Automatically parallelized on internal data level.

## Parameters

**`image`** (input_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / uint2 / real)

Image to be filtered.

**`mask`** (input_object)  region `→` [HRegion](HRegion.md)

Filter mask.

**`imageMean`** (output_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / uint2 / real)

Filtered image.

## Example (HDevelop)

```
read_image (Image, 'fabrik')
gen_circle (Circle, 10, 10, 2)
mean_image_shape (Image, Circle, ImageMean)
dev_display (ImageMean)
```

## Result

If the parameter values are correct the operator `MeanImageShape`
returns the value 2 (
H_MSG_TRUE)
. The behavior in case of empty input (no
input images available) is set via the operator
`set_system('no_object_result',<Result>)`.
If necessary an exception is raised.

## Possible Predecessors

`ReadImage`,
`ReduceDomain`,
`Rectangle1Domain`,
`GenCircle`

## Possible Successors

`DynThreshold`,
`Regiongrowing`

## Alternatives

`BinomialFilter`,
`GaussFilter`,
`SmoothImage`,
`MeanImage`

## See also

`AnisotropicDiffusion`,
`SigmaImage`,
`ConvolImage`,
`GenLowpass`

## Module

Foundation
