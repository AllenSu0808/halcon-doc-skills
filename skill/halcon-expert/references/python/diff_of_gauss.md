# diff_of_gauss (Operator)

## Name

`diff_of_gauss` — Approximate the LoG operator (Laplace of Gaussian).

## Signature

`def diff_of_gauss(image: HObject, sigma: float, sig_factor: float) -> HObject`

## Description

`diff_of_gauss` approximates the Laplace-of-Gauss
operator by a difference of Gaussians. The standard deviations of
these Gaussians can be calculated, according to Marr, from the
Parameter *`sigma`* of the LoG and the ratio of the two
standard deviations (*`sig_factor`*) as:
$$\sigma_1 = \frac{\mathrm{Sigma}}{\sqrt{-2\frac{\log\left( \mathrm{SigFactor1} \right)}{\mathrm{SigFactor2}^{2}-1}}} \sigma_2 = \frac{\mathrm{sigma1}}{\mathrm{SigFactor}} \mathrm{DiffOfGauss} = \mathrm{Image} * \mathrm{gauss}(\sigma1) - \mathrm{Image} * \mathrm{gauss}(\sigma2)$$ ![figure](../assets/ca024fae190393ec.svg)

For a $\texttt{SigFactor}=1.6$, according
to Marr, an approximation to the Mexican-Hat-Operator results. The
resulting image is stored in *`diff_of_gauss`*.

## Attention

Note that filter operators may return unexpected results if
an image with a reduced domain is used as input. Please refer to the
chapter [Filters](toc_filters.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on channel level.
- Automatically parallelized on domain level.

## Parameters

**`image`** (input_object)  (multichannel-)image(-array) `→` HObject (byte / uint2)

Input image

**`diff_of_gauss`** (output_object)  (multichannel-)image(-array) `→` HObject (int2)

LoG image.

**`sigma`** (input_control)  real `→` float

Smoothing parameter of the Laplace operator to
approximate.

Default:
3.0

Suggested values:
2.0, 3.0, 4.0, 5.0

Minimum increment:
0.01

Recommended increment:
0.1

Restriction:
`Sigma > 0.0`

**`sig_factor`** (input_control)  real `→` float

Ratio of the standard deviations used (Marr
recommends 1.6).

Default:
1.6

Minimum increment:
0.01

Recommended increment:
0.1

Restriction:
`SigFactor > 0.0`

## Complexity

The execution time depends linearly on the number of pixels and the
size of sigma.

## Result

`diff_of_gauss` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. If the input is empty the behavior can be set via
`set_system('no_object_result',<Result>)`. If
necessary, an exception is raised.

## Possible Successors

`zero_crossing`,
`dual_threshold`

## Alternatives

`laplace`,
`derivate_gauss`

## References

D. Marr: “Vision (A computational investigation into human
representation and processing of visual information)”; New York,
W.H. Freeman and Company; 1982.

## Module

Foundation
