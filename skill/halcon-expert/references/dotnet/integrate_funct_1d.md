# IntegrateFunct1d (Operator)

## Name

`IntegrateFunct1d` — Compute the positive and negative areas of a function.

## Signature

`static void HOperatorSet.IntegrateFunct1d(HTuple function, out HTuple positive, out HTuple negative)`

`double HFunction1D.IntegrateFunct1d(out HTuple negative)`

## Description

`IntegrateFunct1d` integrates the function *`function`*
(see [`CreateFunct1dArray`](create_funct_1d_array.md) and [`CreateFunct1dPairs`](create_funct_1d_pairs.md))
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

**`function`** (input_control)  function_1d `→` [HFunction1D](HFunction1D.md), [HTuple](HTuple.md) (*double*)

Input function.

**`positive`** (output_control)  number `→` [HTuple](HTuple.md) (*double*)

Area under the positive part of the function.

**`negative`** (output_control)  number-array `→` [HTuple](HTuple.md) (*double*)

Area under the negative part of the function.

## Possible Predecessors

`CreateFunct1dPairs`,
`CreateFunct1dArray`

## See also

`CreateFunct1dArray`,
`CreateFunct1dPairs`

## Module

Foundation
