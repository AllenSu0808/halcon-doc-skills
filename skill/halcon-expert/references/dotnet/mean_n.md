# MeanN (Operator)

## Name

`MeanN` — Average gray values over several channels.

## Signature

`static void HOperatorSet.MeanN(HObject image, out HObject imageMean)`

`HImage HImage.MeanN()`

## Description

The operator `MeanN` generates the pixel-by-pixel mean
value of all channels . For each coordinate point the sum of all
gray values at this coordinate is calculated. The result is the
mean of the gray values (sum divided by the number of channels).
The output image has one channel.

For an explanation of the concept of smoothing filters see the introduction
of chapter [Filters / Smoothing](toc_filters_smoothing.md).

## Attention

Note that filter operators may return unexpected results if
an image with a reduced domain is used as input. Please refer to the
chapter [Filters](toc_filters.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on domain level.

## Parameters

**`image`** (input_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / int2 / uint2 / int4 / real)

Multichannel gray image.

**`imageMean`** (output_object)  singlechannelimage(-array) `→` [HImage](HImage.md) (byte / int2 / uint2 / int4 / real)

Result of averaging.

## Example (C)

```
compose3(Channel1,Channel2,Channel3,&MultiChannel);
mean_n(MultiChannel,&Mean);
```

## Possible Predecessors

`Compose2`,
`Compose3`,
`Compose4`,
`Compose5`,
`AddChannels`

## Alternatives

`RankN`

## See also

`CountChannels`,
`MeanImage`

## Module

Foundation
