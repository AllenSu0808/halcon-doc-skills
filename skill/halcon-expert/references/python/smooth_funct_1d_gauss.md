# smooth_funct_1d_gauss (Operator)

## Name

`smooth_funct_1d_gauss` — Smooth an equidistant 1D function with a Gaussian function.

## Signature

`def smooth_funct_1d_gauss(function: Sequence[Union[float, int]], sigma: float) -> Sequence[Union[float, int]]`

## Description

The operator `smooth_funct_1d_gauss` smooths a one-dimensional
function with a Gaussian function. The function must be equidistant, i.e.,
created with [`create_funct_1d_array`](create_funct_1d_array.md), [`sample_funct_1d`](sample_funct_1d.md)
or similar. At the function borders the function values are mirrored.

Note that the smoothing parameter *`sigma`* must not be larger
than
$(\texttt{Length}\text{-2) / 7.8 *}\texttt{Function}\text{[1]}$,
with $\texttt{Length}\text{-2}$
being the number of control points of *`function`* and
$\texttt{Function}\text{[1]}$ specifying the equidistance
of the x values.
The value of `length` can, e.g., be determined with
[`num_points_funct_1d`](num_points_funct_1d.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`function`** (input_control)  function_1d `→` Sequence[Union[float, int]]

Function to be smoothed.

**`sigma`** (input_control)  number `→` float

Sigma of the Gaussian function for the smoothing.

Default:
2.0

Suggested values:
0.5, 1.0, 2.0, 3.0, 4.0, 5.0

Value range:
`0.1
≤
sigma
≤
50.0` (lin)

Minimum increment:
0.01

Recommended increment:
0.2

**`smoothed_function`** (output_control)  function_1d `→` Sequence[Union[float, int]]

Smoothed function.

## Possible Predecessors

`create_funct_1d_array`,
`sample_funct_1d`

## Possible Successors

`match_funct_1d_trans`,
`distance_funct_1d`

## Alternatives

`smooth_funct_1d_mean`

## Module

Foundation
