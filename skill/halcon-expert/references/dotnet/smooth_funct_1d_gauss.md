# SmoothFunct1dGauss (Operator)

## Name

`SmoothFunct1dGauss` — Smooth an equidistant 1D function with a Gaussian function.

## Signature

`static void HOperatorSet.SmoothFunct1dGauss(HTuple function, HTuple sigma, out HTuple smoothedFunction)`

`HFunction1D HFunction1D.SmoothFunct1dGauss(double sigma)`

## Description

The operator `SmoothFunct1dGauss` smooths a one-dimensional
function with a Gaussian function. The function must be equidistant, i.e.,
created with [`CreateFunct1dArray`](create_funct_1d_array.md), [`SampleFunct1d`](sample_funct_1d.md)
or similar. At the function borders the function values are mirrored.

Note that the smoothing parameter *`sigma`* must not be larger
than
$(\texttt{Length}\text{-2) / 7.8 *}\texttt{Function}\text{[1]}$,
with $\texttt{Length}\text{-2}$
being the number of control points of *`function`* and
$\texttt{Function}\text{[1]}$ specifying the equidistance
of the x values.
The value of `length` can, e.g., be determined with
[`NumPointsFunct1d`](num_points_funct_1d.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`function`** (input_control)  function_1d `→` [HFunction1D](HFunction1D.md), [HTuple](HTuple.md) (*double* / int / long)

Function to be smoothed.

**`sigma`** (input_control)  number `→` [HTuple](HTuple.md) (*double*)

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

**`smoothedFunction`** (output_control)  function_1d `→` [HFunction1D](HFunction1D.md), [HTuple](HTuple.md) (*double* / int / long)

Smoothed function.

## Possible Predecessors

`CreateFunct1dArray`,
`SampleFunct1d`

## Possible Successors

`MatchFunct1dTrans`,
`DistanceFunct1d`

## Alternatives

`SmoothFunct1dMean`

## Module

Foundation
