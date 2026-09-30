# AddNoiseDistribution (Operator)

## Name

`AddNoiseDistribution` — Add noise to an image.

## Signature

`static void HOperatorSet.AddNoiseDistribution(HObject image, out HObject imageNoise, HTuple distribution)`

`HImage HImage.AddNoiseDistribution(HTuple distribution)`

## Description

`AddNoiseDistribution` adds noise distributed according to
*`distribution`* to the *`image`*. The resulting gray values are
clipped to the range of the corresponding pixel type.

The *`distribution`* is stored in a tuple of length 513. The individual
values of this tuple define the frequency of noise with a specific amplitude
defined by the position within the tuple. The central value, i.e., the
value at the position 256 in the tuple defines the frequency of pixels that
are not changed. The value at the position 255 defines the frequency of
pixels for which the grayvalue is decreased by 1. The value at the position
254 defines the respective frequency for a grayvalue decrease of 2, and so
on. Analogously, the value at position 257 defines the frequency of pixels
for which the grayvalue is increased by 1.

The *`distribution`* represents salt and pepper noise if at most one
value at a position smaller than 256 is not equal to zero and at most one
value at a position larger than 256 is not equal to zero. In case of salt
and pepper noise, the added noisy pixels are set to the minimum (pepper) and
maximum (salt) values that can be represented by *`imageNoise`* if the
amount of pepper is indicated by the value at position 0 and the amount of
salt is indicated by the value at position 512 in the tuple.

The random noise is generated using the C function “drand48()”.
See the parameter *"seed_rand"* of [`SetSystem`](set_system.md) for
information on the used random seed.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on channel level.

## Parameters

**`image`** (input_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / int2)

Input image.

**`imageNoise`** (output_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / int2)

Noisy image.

Number of elements:
ImageNoise == Image

**`distribution`** (input_control)  distribution.values-array `→` [HTuple](HTuple.md) (*double*)

Noise distribution.

Number of elements:
513

## Example (HDevelop)

```
read_image(Image,'mreut')
dev_display (Image)
sp_distribution(30,30,Dist)
add_noise_distribution(Image,ImageNoise,Dist)
dev_display (ImageNoise)
```

## Result

`AddNoiseDistribution` returns 2 (
H_MSG_TRUE)
if all parameters are correct.
If the input is empty the behavior can be set via
`set_system('no_object_result',<Result>)`. If
necessary, an exception is raised.

## Possible Predecessors

`GaussDistribution`,
`SpDistribution`,
`NoiseDistributionMean`

## Alternatives

`AddNoiseWhite`

## See also

`SpDistribution`,
`GaussDistribution`,
`NoiseDistributionMean`,
`AddNoiseWhite`

## Module

Foundation
