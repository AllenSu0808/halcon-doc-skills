# FreiAmp (Operator)

## Name

`FreiAmp` — Detect edges (amplitude) using the Frei-Chen operator.

## Signature

`static void HOperatorSet.FreiAmp(HObject image, out HObject imageEdgeAmp)`

`HImage HImage.FreiAmp()`

## Description

`FreiAmp` calculates an approximation of the first
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

**`image`** (input_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / int2 / uint2)

Input image.

**`imageEdgeAmp`** (output_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / int2 / uint2)

Edge amplitude (gradient magnitude) image.

## Example (HDevelop)

```
read_image(Image,'fabrik')
frei_amp(Image,Frei_amp)
threshold(Frei_amp,Edges,128,255)
```

## Result

`FreiAmp` always returns 2 (
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
`KirschAmp`,
`PrewittAmp`,
`RobinsonAmp`,
`Roberts`

## See also

`BandpassImage`,
`LaplaceOfGauss`

## Module

Foundation
