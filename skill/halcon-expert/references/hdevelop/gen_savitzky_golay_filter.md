# gen_savitzky_golay_filter (Operator)

## Name

`gen_savitzky_golay_filter` — Compute the filter coefficients of a Savitzky-Golay filter.

## Signature

`gen_savitzky_golay_filter( : : FilterSize, PolynomialDegree, Derivative : Filter)`

## Description

`gen_savitzky_golay_filter` generates the coefficients of a
Savitzky–Golay filter of size *`FilterSize`* with a polynomial of
order *`PolynomialDegree`*.
The coefficients are calculated for the derivative *`Derivative`*
of the fitted polynomial.
A value of *0* for *`Derivative`* specifies that the filter
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
[`convol_channels`](convol_channels.md) operator.

For numerical stability, *`PolynomialDegree`* must not exceed *9*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`FilterSize`** (input_control)  integer `→`  (integer)

Size of the filter.

Default:
11

Suggested values:
5, 7, 9, 11, 13, 15, 17

**`PolynomialDegree`** (input_control)  integer `→`  (integer)

Degree of the approximating polynomial.

Default:
3

Suggested values:
3, 5

**`Derivative`** (input_control)  integer `→`  (integer)

Derivative of the polynomial.

Default:
0

Suggested values:
0, 1, 2

**`Filter`** (output_control)  real-array `→`  (real)

Filter coefficients.

## Possible Successors

`convol_channels`

## See also

`convol_channels`

## Module

Foundation
