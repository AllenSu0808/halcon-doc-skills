# KirschDir (Operator)

## Name

`KirschDir` — Detect edges (amplitude and direction) using the Kirsch operator.

## Signature

`static void HOperatorSet.KirschDir(HObject image, out HObject imageEdgeAmp, out HObject imageEdgeDir)`

`HImage HImage.KirschDir(out HImage imageEdgeDir)`

## Description

`KirschDir` calculates an approximation of the first
derivative of the image data and is used as an edge detector. The
filter is based on the following filter masks:
-3 -3 5 -3 5 5 5 5 5 5 5 -3
-3 0 5 -3 0 5 -3 0 -3 5 0 -3
-3 -3 5 -3 -3 -3 -3 -3 -3 -3 -3 -3
5 -3 -3 -3 -3 -3 -3 -3 -3 -3 -3 -3
5 0 -3 5 0 -3 -3 0 -3 -3 0 5
5 -3 -3 5 5 -3 5 5 5 -3 5 5
The result image contains the maximum response of all masks. The
edge directions are returned in *`imageEdgeDir`*, and are
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

**`image`** (input_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / int2 / uint2)

Input image.

**`imageEdgeAmp`** (output_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / int2 / uint2)

Edge amplitude (gradient magnitude) image.

**`imageEdgeDir`** (output_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (direction)

Edge direction image.

## Example (HDevelop)

```
read_image(Image,'fabrik')
kirsch_dir(Image,Kirsch_dirA,Kirsch_dirD)
threshold(Kirsch_dirA,Res,128,255)
```

## Result

`KirschDir` always returns 2 (
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

## Possible Successors

`HysteresisThreshold`,
`Threshold`,
`GraySkeleton`,
`NonmaxSuppressionDir`,
`CloseEdges`,
`CloseEdgesLength`

## Alternatives

`EdgesImage`,
`SobelDir`,
`RobinsonDir`,
`PrewittDir`,
`FreiDir`

## See also

`BandpassImage`,
`LaplaceOfGauss`

## Module

Foundation
