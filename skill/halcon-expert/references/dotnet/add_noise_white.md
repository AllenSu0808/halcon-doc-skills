# AddNoiseWhite (Operator)

## Name

`AddNoiseWhite` — Add noise to an image.

## Signature

`static void HOperatorSet.AddNoiseWhite(HObject image, out HObject imageNoise, HTuple amp)`

`HImage HImage.AddNoiseWhite(double amp)`

## Description

`AddNoiseWhite` adds noise to the image *`image`*.
The noise is white noise, equally distributed in the interval
[-*`amp`*,*`amp`*]. The resulting
gray values are clipped to the range of the corresponding pixel type.

The random noise is generated using the C function “drand48”.
See the parameter *"seed_rand"* of [`SetSystem`](set_system.md) for
information on the used random seed.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on channel level.

## Parameters

**`image`** (input_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / int2 / uint2 / real)

Input image.

**`imageNoise`** (output_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / int2 / uint2 / real)

Noisy image.

Number of elements:
ImageNoise == Image

**`amp`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Maximum noise amplitude.

Default:
60.0

Suggested values:
1.0, 2.0, 5.0, 10.0, 20.0, 40.0, 60.0, 90.0

Value range:
`0.0
≤
amp`

Minimum increment:
0.001

Recommended increment:
10.0

## Example (HDevelop)

```
read_image(Image,'fabrik')
dev_display (Image)
add_noise_white(Image,ImageNoise,90)
dev_display (ImageNoise)
```

## Result

`AddNoiseWhite` returns 2 (
H_MSG_TRUE)
if all parameters are correct.
If the input is empty the behavior can be set via
`set_system('no_object_result',<Result>)`. If
necessary, an exception is raised.

## Alternatives

`AddNoiseDistribution`

## See also

`AddNoiseDistribution`,
`NoiseDistributionMean`,
`GaussDistribution`,
`SpDistribution`

## Module

Foundation
