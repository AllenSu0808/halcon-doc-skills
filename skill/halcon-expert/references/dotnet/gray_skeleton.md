# GraySkeleton (Operator)

## Name

`GraySkeleton` — Thinning of gray value images.

## Signature

`static void HOperatorSet.GraySkeleton(HObject image, out HObject graySkeleton)`

`HImage HImage.GraySkeleton()`

## Description

`GraySkeleton` applies a gray value thinning operation
to the input image *`image`*. Figuratively, the gray value
“mountain range” is reduced to its ridge lines by setting the gray
value of “hillsides” to the gray value at the corresponding valley
bottom. The resulting ridge lines are at most two pixels wide.
This operator is especially useful for thinning edge images, and is
thus an alternative to [`NonmaxSuppressionAmp`](nonmax_suppression_amp.md). In
contrast to [`NonmaxSuppressionAmp`](nonmax_suppression_amp.md),
`GraySkeleton` preserves contours, but is much slower.
In contrast to [`Skeleton`](skeleton.md), this operator changes the gray
values of an image while leaving its region unchanged.

## Attention

Note that filter operators may return unexpected results if
an image with a reduced domain is used as input. Please refer to the
chapter [Filters](toc_filters.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on channel level.

## Parameters

**`image`** (input_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / uint2)

Image to be thinned.

**`graySkeleton`** (output_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / uint2)

Thinned image.

## Example (HDevelop)

```
* Seeking leafs of a beech tree in an aerial picture:
read_image(Image,'forest')
gray_skeleton(Image,Skelett)
mean_image(Skelett,MeanSkelett,7,7)
dyn_threshold(Skelett,MeanSkelett,Leafs,3,'light')
```

## Result

`GraySkeleton` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. If the input is empty the behavior can be set via
`set_system('no_object_result',<Result>)`.
If necessary, an exception is raised.

## Possible Successors

`MeanImage`

## Alternatives

`NonmaxSuppressionAmp`,
`NonmaxSuppressionDir`,
`LocalMax`

## See also

`Skeleton`,
`GrayDilationRect`

## Module

Foundation
