# SmoothFunct1dMean (Operator)

## Name

`SmoothFunct1dMean` — Smooth an equidistant 1D function by averaging its values.

## Signature

`static void HOperatorSet.SmoothFunct1dMean(HTuple function, HTuple smoothSize, HTuple iterations, out HTuple smoothedFunction)`

`HFunction1D HFunction1D.SmoothFunct1dMean(int smoothSize, int iterations)`

## Description

The operator `SmoothFunct1dMean` smooths a
one dimensional function by applying an average
(mean) filter multiple times. The function must be equidistant, i.e.,
created with [`CreateFunct1dArray`](create_funct_1d_array.md), [`SampleFunct1d`](sample_funct_1d.md)
or similar. At the function borders the function values are mirrored.

## Attention

If an even value instead of an odd value is given for
*`smoothSize`*, the routine uses the
next larger odd value instead (this way the center of the filter
mask is always explicitly determined).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`function`** (input_control)  function_1d `→` [HFunction1D](HFunction1D.md), [HTuple](HTuple.md) (*int* / long / double)

1D function.

**`smoothSize`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Size of the averaging mask.

Default:
9

Suggested values:
1, 3, 5, 7, 9, 11, 13, 15, 21, 31, 51

Value range:
`0
≤
smoothSize
≤
1001` (lin)

Minimum increment:
1

Recommended increment:
2

**`iterations`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Number of iterations for the smoothing.

Default:
3

Suggested values:
1, 2, 3, 4, 5, 6, 7, 8, 9

Value range:
`1
≤
iterations
≤
100` (lin)

Minimum increment:
1

Recommended increment:
1

**`smoothedFunction`** (output_control)  function_1d `→` [HFunction1D](HFunction1D.md), [HTuple](HTuple.md) (*double* / int / long)

Smoothed function.

## Possible Predecessors

`CreateFunct1dArray`,
`SampleFunct1d`

## Alternatives

`SmoothFunct1dGauss`

## Module

Foundation
