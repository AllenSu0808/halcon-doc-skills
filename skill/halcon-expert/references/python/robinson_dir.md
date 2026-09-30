# robinson_dir (Operator)

## Name

`robinson_dir` — Detect edges (amplitude and direction) using the Robinson operator.

## Signature

`def robinson_dir(image: HObject) -> Tuple[HObject, HObject]`

## Description

`robinson_dir` calculates an approximation of the first
derivative of the image data and is used as an edge detector. In
[`robinson_amp`](robinson_amp.md) the following four of the originally
proposed eight 3x3 filter masks are convolved with
the image. The other four masks are obtained by a multiplication by
-1. All masks contain only the values 0,1,-1,2,-2.
-1 0 1 2 1 0
-2 0 2 1 0 -1
-1 0 1 0 -1 -2
0 1 2 1 2 1
-1 0 1 0 0 0
-2 -1 0 -1 -2 -1
The result image contains the maximum response of all masks. The
edge directions are returned in *`image_edge_dir`*, and are
stored as $x/2$. They correspond to the direction of
the mask yielding the maximum response.

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

**`image_edge_dir`** (output_object)  (multichannel-)image(-array) `→` HObject (direction)

Edge direction image.

## Result

`robinson_dir` always returns 2 (
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

## Possible Successors

`hysteresis_threshold`,
`threshold`,
`gray_skeleton`,
`nonmax_suppression_dir`,
`close_edges`,
`close_edges_length`

## Alternatives

`edges_image`,
`sobel_dir`,
`kirsch_dir`,
`prewitt_dir`,
`frei_dir`

## See also

`bandpass_image`,
`laplace_of_gauss`

## Module

Foundation
