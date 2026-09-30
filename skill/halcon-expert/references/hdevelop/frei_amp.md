# frei_amp (Operator)

## Name

`frei_amp` — Detect edges (amplitude) using the Frei-Chen operator.

## Signature

`frei_amp(Image : ImageEdgeAmp : : )`

## Description

`frei_amp` calculates an approximation of the first
derivative of the image data and is used as an edge detector. The
filter is based on the following filter masks:
A =
1 sqrt(2) 1
0 0 0
-1 -sqrt(2) -1
B =
1 0 -1
sqrt(2) 0 -sqrt(2)
1 0 -1
The result image contains the maximum response of the masks A and
B.

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

**`Image`** (input_object)  (multichannel-)image(-array) `→` object (byte / int2 / uint2)

Input image.

**`ImageEdgeAmp`** (output_object)  (multichannel-)image(-array) `→` object (byte / int2 / uint2)

Edge amplitude (gradient magnitude) image.

## Example (HDevelop)

```
read_image(Image,'fabrik')
frei_amp(Image,Frei_amp)
threshold(Frei_amp,Edges,128,255)
```

## Result

`frei_amp` always returns 2 (
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
`kirsch_amp`,
`prewitt_amp`,
`robinson_amp`,
`roberts`

## See also

`bandpass_image`,
`laplace_of_gauss`

## Module

Foundation
