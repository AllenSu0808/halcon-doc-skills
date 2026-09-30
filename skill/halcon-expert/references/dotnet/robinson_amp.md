# RobinsonAmp (Operator)

## Name

`RobinsonAmp` — Detect edges (amplitude) using the Robinson operator.

## Signature

`static void HOperatorSet.RobinsonAmp(HObject image, out HObject imageEdgeAmp)`

`HImage HImage.RobinsonAmp()`

## Description

`RobinsonAmp` calculates an approximation of the first
derivative of the image data and is used as an edge detector. In
`RobinsonAmp` the following four of the originally
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

**`image`** (input_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / int2 / uint2)

Input image.

**`imageEdgeAmp`** (output_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / int2 / uint2)

Edge amplitude (gradient magnitude) image.

## Example (HDevelop)

```
read_image(Image,'fabrik')
robinson_amp(Image,Robinson_amp)
threshold(Robinson_amp,Edges,128,255)
```

## Result

`RobinsonAmp` always returns 2 (
H_MSG_TRUE)
. If the input is empty
the behavior can be set via
`set_system('no_object_result',<Result>)`.
If necessary, an exception is raised.

## Possible Predecessors

`BinomialFilter`,
`GaussFilter`,
`SigmaImage`,
`MedianImage`,
`SmoothImage`

## Alternatives

`SobelAmp`,
`FreiAmp`,
`PrewittAmp`,
`Roberts`

## See also

`BandpassImage`,
`LaplaceOfGauss`

## Module

Foundation
