# robinson_amp (Operator)

## Name

`robinson_amp` — Detect edges (amplitude) using the Robinson operator.

## Signature

`def robinson_amp(image: HObject) -> HObject`

## Description

`robinson_amp` calculates an approximation of the first
derivative of the image data and is used as an edge detector. In
`robinson_amp` the following four of the originally
proposed eight 3x3 filter masks are convolved with
the image. The other four masks are obtained by a multiplication by
-1. All masks contain only the values 0,1,-1,2,-2.
-1 0 1 2 1 0
-2 0 2 1 0 -1
-1 0 1 0 -1 -2
0 1 2 1 2 1
-1 0 1 0 0 0
-2 -1 0 -1 -2 -1
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

**`image_edge_amp`** (output_object)  (multichannel-)image(-array) `→` HObject (byte / int2 / uint2)

Edge amplitude (gradient magnitude) image.

## Result

`robinson_amp` always returns 2 (
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
`roberts`

## See also

`bandpass_image`,
`laplace_of_gauss`

## Module

Foundation
