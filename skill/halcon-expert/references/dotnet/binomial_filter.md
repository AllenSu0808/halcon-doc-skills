# BinomialFilter (Operator)

## Name

`BinomialFilter` — Smooth an image using the binomial filter.

## Signature

`static void HOperatorSet.BinomialFilter(HObject image, out HObject imageBinomial, HTuple maskWidth, HTuple maskHeight)`

`HImage HImage.BinomialFilter(int maskWidth, int maskHeight)`

## Description

`BinomialFilter` smooths the image *`image`* using a
binomial filter with a mask size of *`maskWidth`* * *`maskHeight`*
pixels and returns the smoothed image in *`imageBinomial`*.
The binomial filter is a very good approximation of a Gaussian
filter that can be implemented extremely efficiently using only
integer operations. Hence, `BinomialFilter` is very fast.
Let m = *`maskHeight`* and n = *`maskWidth`*. Then,
the filter coefficients $b_{ij}$ are given by binomial
coefficients
$$\begin{pmatrix} l \\ k \end{pmatrix} = \frac{l!}{k!(l-k)!}$$ ![figure](../assets/07e9be7e31f663ea.svg)
as follows:
$$b_{ij} = \frac{1}{2^{n}+m-2}\left(m-1 \choose i\right)\left(n-1 \choose j\right)$$ ![figure](../assets/c2a5f358c7bb5bd2.svg)
Here, i = 0, ..., m-1 and j = 0, ..., n-1. The binomial filter performs
approximately the same smoothing as a Gaussian filter with $\sigma = \sqrt{n - \tfrac{1}{2}}$ ![figure](../assets/14cad11a09037a55.svg), where for simplicity it is
assumed that m = n. In detail, the relationship between n and
$\sigma$ is:

| n | $\sigma$ |
| --- | --- |
| 3 | 0.7523 |
| 5 | 1.0317 |
| 7 | 1.2505 |
| 9 | 1.4365 |
| 11 | 1.6010 |
| 13 | 1.7502 |
| 15 | 1.8876 |
| 17 | 2.0157 |
| 19 | 2.1361 |
| 21 | 2.2501 |
| 23 | 2.3586 |
| 25 | 2.4623 |
| 27 | 2.5618 |
| 29 | 2.6576 |
| 31 | 2.7500 |
| 33 | 2.8395 |
| 35 | 2.9262 |
| 37 | 3.0104 |

If different values are chosen for *`maskHeight`* and
*`maskWidth`*, the above relation between n and
$\sigma$ still holds and refers to the amount of
smoothing in the row and column directions.

`BinomialFilter` can be executed on OpenCL devices for all supported
image types.

For an explanation of the concept of smoothing filters see the introduction
of chapter [Filters / Smoothing](toc_filters_smoothing.md).

## Attention

Note that filter operators may return unexpected results if
an image with a reduced domain is used as input. Please refer to the
chapter [Filters](toc_filters.md).

## Execution Information

- Supports OpenCL compute devices.
- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on channel level.
- Automatically parallelized on domain level.

## Parameters

**`image`** (input_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte* / uint2* / real*) **allowed for compute devices*

Input image.

**`imageBinomial`** (output_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / uint2 / real)

Smoothed image.

**`maskWidth`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Filter width.

Default:
5

List of values:
1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37

**`maskHeight`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Filter height.

Default:
5

List of values:
1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37

## Result

If the parameter values are correct the operator
`BinomialFilter` returns the value 2 (
H_MSG_TRUE)
. The behavior in
case of empty input (no input images available) is set via the
operator `set_system('no_object_result',<Result>)`. If
necessary an exception is raised.

## Possible Predecessors

`ReadImage`,
`GrabImage`

## Possible Successors

`Regiongrowing`,
`Threshold`,
`SubImage`,
`DynThreshold`,
`AutoThreshold`

## Alternatives

`GaussFilter`,
`SmoothImage`,
`DerivateGauss`,
`IsotropicDiffusion`

## See also

`MeanImage`,
`AnisotropicDiffusion`,
`SigmaImage`,
`GenLowpass`

## Module

Foundation
