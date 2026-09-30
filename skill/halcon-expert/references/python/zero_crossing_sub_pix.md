# zero_crossing_sub_pix (Operator)

## Name

`zero_crossing_sub_pix` — Extract zero crossings from an image with subpixel accuracy.

## Signature

`def zero_crossing_sub_pix(image: HObject) -> HObject`

## Description

`zero_crossing_sub_pix` extracts the zero crossings of the
input image *`image`* with subpixel accuracy. The extracted
zero crossings are returned as XLD-contours in
*`zero_crossings`*. Thus, `zero_crossing_sub_pix` can be
used as a sub-pixel precise edge extractor if the input image is a
Laplace-filtered image (see [`laplace`](laplace.md),
[`laplace_of_gauss`](laplace_of_gauss.md), [`derivate_gauss`](derivate_gauss.md)).

For the extraction, the input image is regarded as a surface, in
which the gray values are interpolated bilinearly between the
centers of the individual pixels. Consistent with the surface thus
defined, zero crossing lines are extracted for each pixel and linked
into topologically sound contours. This means that the zero
crossing contours are correctly split at junction points. If the
image contains extended areas of constant gray value 0, only the
border of such areas is returned as zero crossings.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`image`** (input_object)  singlechannelimage `→` HObject (int1 / int2 / int4 / real)

Input image.

**`zero_crossings`** (output_object)  xld_cont-array `→` HObject

Extracted zero crossings.

## Result

`zero_crossing_sub_pix` usually returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`laplace`,
`laplace_of_gauss`,
`diff_of_gauss`,
`derivate_gauss`

## Alternatives

`zero_crossing`

## See also

`threshold_sub_pix`

## Module

2D Metrology
