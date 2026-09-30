# add_noise_white (Operator)

## Name

`add_noise_white` — Add noise to an image.

## Signature

`add_noise_white(Image : ImageNoise : Amp : )`

## Description

`add_noise_white` adds noise to the image *`Image`*.
The noise is white noise, equally distributed in the interval
[-*`Amp`*,*`Amp`*]. The resulting
gray values are clipped to the range of the corresponding pixel type.

The random noise is generated using the C function “drand48”.
See the parameter *'seed_rand'* of [`set_system`](set_system.md) for
information on the used random seed.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on channel level.

## Parameters

**`Image`** (input_object)  (multichannel-)image(-array) `→` object (byte / int2 / uint2 / real)

Input image.

**`ImageNoise`** (output_object)  (multichannel-)image(-array) `→` object (byte / int2 / uint2 / real)

Noisy image.

Number of elements:
ImageNoise == Image

**`Amp`** (input_control)  real `→`  (real)

Maximum noise amplitude.

Default:
60.0

Suggested values:
1.0, 2.0, 5.0, 10.0, 20.0, 40.0, 60.0, 90.0

Value range:
`0.0
≤
Amp`

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

`add_noise_white` returns 2 (
H_MSG_TRUE)
if all parameters are correct.
If the input is empty the behavior can be set via
`set_system('no_object_result',<Result>)`. If
necessary, an exception is raised.

## Alternatives

`add_noise_distribution`

## See also

`add_noise_distribution`,
`noise_distribution_mean`,
`gauss_distribution`,
`sp_distribution`

## Module

Foundation
