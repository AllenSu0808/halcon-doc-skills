# sp_distribution (Operator)

## Name

`sp_distribution` — Generate a salt-and-pepper noise distribution.

## Signature

`def sp_distribution(percent_salt: Union[float, int], percent_pepper: Union[float, int]) -> Sequence[float]`

## Description

`sp_distribution` generates a noise distribution with the
values 0 and 255. The parameters *`percent_salt`* and
*`percent_pepper`* determine the percentage of white and black
noise pixels, respectively. The sum of these parameters must be
smaller than 100. Usually, the result *`distribution`* is
used as input for the operator [`add_noise_distribution`](add_noise_distribution.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`percent_salt`** (input_control)  number `→` Union[float, int]

Percentage of salt (white noise pixels).

Default:
5.0

Suggested values:
1.0, 2.0, 5.0, 7.0, 10.0, 15.0, 20.0, 30.0

Value range:
`0.0
≤
percent_salt
≤
100.0`

Minimum increment:
0.1

Recommended increment:
1.0

Restriction:
`PercentSalt + PercentPepper <= 100`

**`percent_pepper`** (input_control)  number `→` Union[float, int]

Percentage of pepper (black noise pixels).

Default:
5.0

Suggested values:
1.0, 2.0, 5.0, 7.0, 10.0, 15.0, 20.0, 30.0

Value range:
`0.0
≤
percent_pepper
≤
100.0`

Minimum increment:
0.1

Recommended increment:
1.0

Restriction:
`PercentSalt + PercentPepper <= 100`

**`distribution`** (output_control)  distribution.values-array `→` Sequence[float]

Resulting noise distribution.

Number of elements:
513

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
