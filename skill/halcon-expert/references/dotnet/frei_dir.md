# FreiDir (Operator)

## Name

`FreiDir` — Detect edges (amplitude and direction) using the Frei-Chen operator.

## Signature

`static void HOperatorSet.FreiDir(HObject image, out HObject imageEdgeAmp, out HObject imageEdgeDir)`

`HImage HImage.FreiDir(out HImage imageEdgeDir)`

## Description

`FreiDir` calculates an approximation of the first
derivative of the image data and is used as an edge detector. The
filter is based on the following filter masks:
$$A = \begin{pmatrix} 1 & \sqrt{2} & 1 \\ 0 & 0 & 0 \\ -1 & -\sqrt{2} & -1 \end{pmatrix}, \quad B = \begin{pmatrix} 1 & 0 & -1 \\ \sqrt{2} & 0 & -\sqrt{2} \\ 1 & 0 & -1 \end{pmatrix}$$ ![figure](../assets/9c49aee9539fc482.svg)

The result image contains the maximum response of the masks A and
B. The edge directions are returned in *`imageEdgeDir`*,
and are stored in 2-degree steps, i.e., an edge direction of
$x$ degrees in mathematically positive sense and
with respect to the horizontal axis is stored as
$x/2$ in the edge direction image. Furthermore, the
direction of the change of intensity is taken into account. Let
$[E_{x},E_{y}]$ denote the image gradient. Then the
following edge directions are returned as $r/2$:
$$\mathrm{E}_{x}/\mathrm{E}_{y}$$ ![figure](../assets/b6369c3c39fd2405.svg)
Points with edge amplitude 0 are assigned the edge direction 255
(undefined direction).

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
frei_dir(Image,Frei_dirA,Frei_dirD)
threshold(Frei_dirA,Res,128,255)
```

## Result

`FreiDir` always returns 2 (
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
`KirschDir`

## See also

`BandpassImage`,
`LaplaceOfGauss`

## Module

Foundation
