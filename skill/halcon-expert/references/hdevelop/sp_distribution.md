# sp_distribution (Operator)

## Name

`sp_distribution` — Generate a salt-and-pepper noise distribution.

## Signature

`sp_distribution( : : PercentSalt, PercentPepper : Distribution)`

## Description

`sp_distribution` generates a noise distribution with the
values 0 and 255. The parameters *`PercentSalt`* and
*`PercentPepper`* determine the percentage of white and black
noise pixels, respectively. The sum of these parameters must be
smaller than 100. Usually, the result *`Distribution`* is
used as input for the operator [`add_noise_distribution`](add_noise_distribution.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`PercentSalt`** (input_control)  number `→`  (real / integer)

Percentage of salt (white noise pixels).

Default:
5.0

Suggested values:
1.0, 2.0, 5.0, 7.0, 10.0, 15.0, 20.0, 30.0

Value range:
`0.0
≤
PercentSalt
≤
100.0`

Minimum increment:
0.1

Recommended increment:
1.0

Restriction:
`PercentSalt + PercentPepper <= 100`

**`PercentPepper`** (input_control)  number `→`  (real / integer)

Percentage of pepper (black noise pixels).

Default:
5.0

Suggested values:
1.0, 2.0, 5.0, 7.0, 10.0, 15.0, 20.0, 30.0

Value range:
`0.0
≤
PercentPepper
≤
100.0`

Minimum increment:
0.1

Recommended increment:
1.0

Restriction:
`PercentSalt + PercentPepper <= 100`

**`Distribution`** (output_control)  distribution.values-array `→`  (real)

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

`add_noise_distribution`

## Alternatives

`gauss_distribution`,
`noise_distribution_mean`

## See also

`gauss_distribution`,
`noise_distribution_mean`,
`add_noise_white`

## Module

Foundation
