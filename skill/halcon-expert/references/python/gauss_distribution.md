# gauss_distribution (Operator)

## Name

`gauss_distribution` — Generate a Gaussian noise distribution.

## Signature

`def gauss_distribution(sigma: float) -> Sequence[float]`

## Description

`gauss_distribution` generates a Gaussian noise
distribution. The parameter *`sigma`* determines the noise's
standard deviation. Usually, the result *`distribution`* is
used as input for the operator [`add_noise_distribution`](add_noise_distribution.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`sigma`** (input_control)  real `→` float

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

**`distribution`** (output_control)  distribution.values-array `→` Sequence[float]

Resulting Gaussian noise distribution.

Number of elements:
513

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
