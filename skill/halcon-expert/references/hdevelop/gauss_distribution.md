# gauss_distribution (Operator)

## Name

`gauss_distribution` — Generate a Gaussian noise distribution.

## Signature

`gauss_distribution( : : Sigma : Distribution)`

## Description

`gauss_distribution` generates a Gaussian noise
distribution. The parameter *`Sigma`* determines the noise's
standard deviation. Usually, the result *`Distribution`* is
used as input for the operator [`add_noise_distribution`](add_noise_distribution.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Sigma`** (input_control)  real `→`  (real)

Standard deviation of the Gaussian noise
distribution.

Default:
2.0

Suggested values:
1.5, 2.0, 3.0, 5.0, 10.0

Value range:
`0.0
≤
Sigma
≤
100.0`

Minimum increment:
0.1

Recommended increment:
1.0

**`Distribution`** (output_control)  distribution.values-array `→`  (real)

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

`add_noise_distribution`

## Alternatives

`sp_distribution`,
`noise_distribution_mean`

## See also

`sp_distribution`,
`add_noise_white`,
`noise_distribution_mean`

## Module

Foundation
