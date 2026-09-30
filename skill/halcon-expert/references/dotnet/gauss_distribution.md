# GaussDistribution (Operator)

## Name

`GaussDistribution` — Generate a Gaussian noise distribution.

## Signature

`static void HOperatorSet.GaussDistribution(HTuple sigma, out HTuple distribution)`

`static HTuple HMisc.GaussDistribution(double sigma)`

## Description

`GaussDistribution` generates a Gaussian noise
distribution. The parameter *`sigma`* determines the noise's
standard deviation. Usually, the result *`distribution`* is
used as input for the operator [`AddNoiseDistribution`](add_noise_distribution.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`sigma`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Standard deviation of the Gaussian noise
distribution.

Default:
2.0

Suggested values:
1.5, 2.0, 3.0, 5.0, 10.0

Value range:
`0.0
≤
sigma
≤
100.0`

Minimum increment:
0.1

Recommended increment:
1.0

**`distribution`** (output_control)  distribution.values-array `→` [HTuple](HTuple.md) (*double*)

Resulting Gaussian noise distribution.

Number of elements:
513

## Example (HDevelop)

```
read_image(Image,'fabrik')
dev_display (Image)
gauss_distribution(30,Dist)
add_noise_distribution(Image,ImageNoise,Dist)
dev_display (ImageNoise)
```

## Possible Successors

`AddNoiseDistribution`

## Alternatives

`SpDistribution`,
`NoiseDistributionMean`

## See also

`SpDistribution`,
`AddNoiseWhite`,
`NoiseDistributionMean`

## Module

Foundation
