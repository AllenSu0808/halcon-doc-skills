# SpDistribution (Operator)

## Name

`SpDistribution` — Generate a salt-and-pepper noise distribution.

## Signature

`static void HOperatorSet.SpDistribution(HTuple percentSalt, HTuple percentPepper, out HTuple distribution)`

`static HTuple HMisc.SpDistribution(HTuple percentSalt, HTuple percentPepper)`

`static HTuple HMisc.SpDistribution(double percentSalt, double percentPepper)`

## Description

`SpDistribution` generates a noise distribution with the
values 0 and 255. The parameters *`percentSalt`* and
*`percentPepper`* determine the percentage of white and black
noise pixels, respectively. The sum of these parameters must be
smaller than 100. Usually, the result *`distribution`* is
used as input for the operator [`AddNoiseDistribution`](add_noise_distribution.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`percentSalt`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / int / long)

Percentage of salt (white noise pixels).

Default:
5.0

Suggested values:
1.0, 2.0, 5.0, 7.0, 10.0, 15.0, 20.0, 30.0

Value range:
`0.0
≤
percentSalt
≤
100.0`

Minimum increment:
0.1

Recommended increment:
1.0

Restriction:
`PercentSalt + PercentPepper <= 100`

**`percentPepper`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / int / long)

Percentage of pepper (black noise pixels).

Default:
5.0

Suggested values:
1.0, 2.0, 5.0, 7.0, 10.0, 15.0, 20.0, 30.0

Value range:
`0.0
≤
percentPepper
≤
100.0`

Minimum increment:
0.1

Recommended increment:
1.0

Restriction:
`PercentSalt + PercentPepper <= 100`

**`distribution`** (output_control)  distribution.values-array `→` [HTuple](HTuple.md) (*double*)

Resulting noise distribution.

Number of elements:
513

## Example (HDevelop)

```
read_image(Image,'fabrik')
dev_display (Image)
sp_distribution(30,30,Dist)
add_noise_distribution(Image,ImageNoise,Dist)
dev_display (ImageNoise)
```

## Possible Successors

`AddNoiseDistribution`

## Alternatives

`GaussDistribution`,
`NoiseDistributionMean`

## See also

`GaussDistribution`,
`NoiseDistributionMean`,
`AddNoiseWhite`

## Module

Foundation
