# GenSavitzkyGolayFilter (Operator)

## Name

`GenSavitzkyGolayFilter` — Compute the filter coefficients of a Savitzky-Golay filter.

## Signature

`static void HOperatorSet.GenSavitzkyGolayFilter(HTuple filterSize, HTuple polynomialDegree, HTuple derivative, out HTuple filter)`

`static HTuple HImage.GenSavitzkyGolayFilter(int filterSize, int polynomialDegree, int derivative)`

## Description

`GenSavitzkyGolayFilter` generates the coefficients of a
Savitzky–Golay filter of size *`filterSize`* with a polynomial of
order *`polynomialDegree`*.
The coefficients are calculated for the derivative *`derivative`*
of the fitted polynomial.
A value of *0* for *`derivative`* specifies that the filter
performs smoothing of the original function.

The Savitzky–Golay filter is a linear filter.
It operates by fitting a polynomial to neighboring function values
sampled at equally spaced support points, and evaluating the polynomial
at the central support point.
This process can be used for data smoothing.
If required, the polynomial may be differentiated before evaluation,
enabling, for example, the removal of linear trends from the data.

These filter parameters can be applied, for instance, to smooth
hyperspectral images along the channel axis using the
[`ConvolChannels`](convol_channels.md) operator.

For numerical stability, *`polynomialDegree`* must not exceed *9*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`filterSize`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Size of the filter.

Default:
11

Suggested values:
5, 7, 9, 11, 13, 15, 17

**`polynomialDegree`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Degree of the approximating polynomial.

Default:
3

Suggested values:
3, 5

**`derivative`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Derivative of the polynomial.

Default:
0

Suggested values:
0, 1, 2

**`filter`** (output_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Filter coefficients.

## Possible Successors

`ConvolChannels`

## See also

`ConvolChannels`

## Module

Foundation
