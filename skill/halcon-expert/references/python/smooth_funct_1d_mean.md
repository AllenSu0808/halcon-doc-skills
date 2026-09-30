# smooth_funct_1d_mean (Operator)

## Name

`smooth_funct_1d_mean` — Smooth an equidistant 1D function by averaging its values.

## Signature

`def smooth_funct_1d_mean(function: Sequence[Union[float, int]], smooth_size: int, iterations: int) -> Sequence[Union[float, int]]`

## Description

The operator `smooth_funct_1d_mean` smooths a
one dimensional function by applying an average
(mean) filter multiple times. The function must be equidistant, i.e.,
created with [`create_funct_1d_array`](create_funct_1d_array.md), [`sample_funct_1d`](sample_funct_1d.md)
or similar. At the function borders the function values are mirrored.

## Attention

If an even value instead of an odd value is given for
*`smooth_size`*, the routine uses the
next larger odd value instead (this way the center of the filter
mask is always explicitly determined).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`function`** (input_control)  function_1d `→` Sequence[Union[float, int]]

1D function.

**`smooth_size`** (input_control)  integer `→` int

Size of the averaging mask.

Default:
9

Suggested values:
1, 3, 5, 7, 9, 11, 13, 15, 21, 31, 51

Value range:
`0
≤
smooth_size
≤
1001` (lin)

Minimum increment:
1

Recommended increment:
2

**`iterations`** (input_control)  integer `→` int

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

**`smoothed_function`** (output_control)  function_1d `→` Sequence[Union[float, int]]

Smoothed function.

## Possible Predecessors

`create_funct_1d_array`,
`sample_funct_1d`

## Alternatives

`smooth_funct_1d_gauss`

## Module

Foundation
