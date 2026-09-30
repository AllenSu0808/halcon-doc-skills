# KirschAmp (Operator)

## Name

`KirschAmp` — Detect edges (amplitude) using the Kirsch operator.

## Signature

`static void HOperatorSet.KirschAmp(HObject image, out HObject imageEdgeAmp)`

`HImage HImage.KirschAmp()`

## Description

`KirschAmp` calculates an approximation of the first
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

**`image`** (input_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / int2 / uint2)

Input image.

**`imageEdgeAmp`** (output_object)  image(-array) `→` [HImage](HImage.md) (byte / int2 / uint2)

Edge amplitude (gradient magnitude) image.

## Example (HDevelop)

```
read_image(Image,'fabrik')
kirsch_amp(Image,Kirsch_amp)
threshold(Kirsch_amp,Edges,128,255)
```

## Result

`KirschAmp` always returns 2 (
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
`RobinsonAmp`,
`Roberts`

## See also

`BandpassImage`,
`LaplaceOfGauss`

## Module

Foundation
