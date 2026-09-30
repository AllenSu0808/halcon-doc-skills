# kirsch_amp (Operator)

## Name

`kirsch_amp` — Detect edges (amplitude) using the Kirsch operator.

## Signature

`def kirsch_amp(image: HObject) -> HObject`

## Description

`kirsch_amp` calculates an approximation of the first
derivative of the image data and is used as an edge detector. The
filter is based on the following filter masks:
-3 -3 5 -3 5 5 5 5 5 5 5 -3
-3 0 5 -3 0 5 -3 0 -3 5 0 -3
-3 -3 5 -3 -3 -3 -3 -3 -3 -3 -3 -3
5 -3 -3 -3 -3 -3 -3 -3 -3 -3 -3 -3
5 0 -3 5 0 -3 -3 0 -3 -3 0 5
5 -3 -3 5 5 -3 5 5 5 -3 5 5
The result image contains the maximum response of all masks.

## Attention

Note that filter operators may return unexpected results if
an image with a reduced domain is used as input. Please refer to the
chapter [Filters](toc_filters.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on channel level.
- Automatically parallelized on domain level.

## Parameters

**`image`** (input_object)  (multichannel-)image(-array) `→` HObject (byte / int2 / uint2)

Input image.

**`image_edge_amp`** (output_object)  image(-array) `→` HObject (byte / int2 / uint2)

Edge amplitude (gradient magnitude) image.

## Result

`kirsch_amp` always returns 2 (
H_MSG_TRUE)
. If the input is empty
the behavior can be set via
`set_system('no_object_result',<Result>)`.
If necessary, an exception is raised.

## Possible Predecessors

`binomial_filter`,
`gauss_filter`,
`sigma_image`,
`median_image`,
`smooth_image`

## Alternatives

`sobel_amp`,
`frei_amp`,
`prewitt_amp`,
`robinson_amp`,
`roberts`

## See also

`bandpass_image`,
`laplace_of_gauss`

## Module

Foundation
