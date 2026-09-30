# integrate_funct_1d (Operator)

## Name

`integrate_funct_1d` — Compute the positive and negative areas of a function.

## Signature

`def integrate_funct_1d(function: Sequence[float]) -> Tuple[float, Sequence[float]]`

## Description

`integrate_funct_1d` integrates the function *`function`*
(see [`create_funct_1d_array`](create_funct_1d_array.md) and [`create_funct_1d_pairs`](create_funct_1d_pairs.md))
and returns the integral of the positive and negative parts of the
function in *`positive`* and *`negative`*, respectively.
Hence, the integral of the function is the difference
*`positive`* - *`negative`*. The integration is done on
the interval on which the function is defined. For the integration,
the function is interpolated linearly.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`function`** (input_control)  function_1d `→` Sequence[float]

Input function.

**`positive`** (output_control)  number `→` float

Area under the positive part of the function.

**`negative`** (output_control)  number-array `→` Sequence[float]

Area under the negative part of the function.

## Possible Predecessors

`create_funct_1d_pairs`,
`create_funct_1d_array`

## See also

`create_funct_1d_array`,
`create_funct_1d_pairs`

## Module

Foundation
