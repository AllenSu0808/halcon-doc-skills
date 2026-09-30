# DeviationN (Operator)

## Name

`DeviationN` — Calculate standard deviation over several channels.

## Signature

`static void HOperatorSet.DeviationN(HObject image, out HObject imageDeviation)`

`HImage HImage.DeviationN()`

## Description

`DeviationN` generates the pixel-by-pixel standard deviation of
a multichannel gray value image. For each coordinate point p the expected
value is defined as the arithmetic mean:
$$E = \frac{\sum_c g_c(p)}{n}$$ ![figure](../assets/623f92917da30c4a.svg)
where g_{c}(p) denominates the gray value at p on channel
c. n is the number of channels in the image.

The standard deviation itself is then calculated as:
$$s = 2 \cdot \sqrt{\frac{1}{n - 1} \cdot \sum (g_c(p) - E)^2}$$ ![figure](../assets/6588861ea4914147.svg)
Note that this formula produces the *sample* standard deviation. The
factor 2 is used to make better use of
the range of values of the output image format. The output image has one
channel.

## Attention

Note that filter operators may return unexpected results if
an image with a reduced domain is used as input. Please refer to the
chapter [Filters](toc_filters.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on domain level.
- Automatically parallelized on tuple level.

## Parameters

**`image`** (input_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / int2 / uint2 / int4 / real)

Multichannel gray image.

**`imageDeviation`** (output_object)  image(-array) `→` [HImage](HImage.md) (byte / int2 / uint2 / int4 / real)

Result of calculation.

## Possible Predecessors

`Compose2`,
`Compose3`,
`Compose4`,
`Compose5`,
`AddChannels`

## See also

`MeanN`

## Module

Foundation
