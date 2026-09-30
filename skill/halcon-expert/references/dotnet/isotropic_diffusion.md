# IsotropicDiffusion (Operator)

## Name

`IsotropicDiffusion` — Perform an isotropic diffusion of an image.

## Signature

`static void HOperatorSet.IsotropicDiffusion(HObject image, out HObject smoothedImage, HTuple sigma, HTuple iterations)`

`HImage HImage.IsotropicDiffusion(double sigma, int iterations)`

## Description

The operator `IsotropicDiffusion` performs an isotropic
diffusion of the input image *`image`*. This corresponds to a
convolution of the image matrix with a Gaussian mask of standard
deviation *`sigma`*. If the parameter *`iterations`* is
set to *0*, such a convolution is performed explicitly. For
input images with a full ROI, `IsotropicDiffusion` returns
the same results as the operator [`DerivateGauss`](derivate_gauss.md) when
choosing *"none"* for its parameter `component`. If
the gray value matrix is larger than the ROI of *`image`* the
two operators differ since [`DerivateGauss`](derivate_gauss.md) takes the gray
values outside of the ROI into account, while
`IsotropicDiffusion` mirrors the values at the boundary of
the ROI in any case. The computational complexity increases linearly
with the value of *`sigma`*.

If *`iterations`* has a positive value the smoothing process
is considered as an application of the heat equation
$$u_{t}=\Delta u$$
on the gray value function u with the initial value $u=u_{0}$ defined by the gray values of *`image`* at a time
$t_{0}$. This equation is then solved up to a time $t_0 + \tfrac{1}{2} \sigma_i^2$ ![figure](../assets/44ea3b9f8d9a0dc9.svg), which
is equivalent to the above convolution, using an iterative procedure
for parabolic partial differential equations. The computational
complexity is proportional to the value of *`iterations`* and
independent of *`sigma`* in this case. For small values of
*`iterations`*, the computational accuracy is very low,
however. For this reason, choosing *`iterations`* <
*3* is not recommended.

For smaller values of *`sigma`*, the convolution implementation
is typically the faster method. Since the runtime of the partial
differential equation solver only depends on the number of
iterations and not on the value of *`sigma`*, it is typically
faster for large values of *`sigma`* if few iterations are
chosen (e.g., *`iterations`* = *3*).

For an explanation of the concept of smoothing filters see the introduction
of chapter [Filters / Smoothing](toc_filters_smoothing.md).

## Attention

Note that filter operators may return unexpected results if
an image with a reduced domain is used as input. Please refer to the
chapter [Filters](toc_filters.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on channel level.

## Parameters

**`image`** (input_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / uint2 / real)

Input image.

**`smoothedImage`** (output_object)  image(-array) `→` [HImage](HImage.md) (byte / uint2 / real)

Output image.

**`sigma`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Standard deviation of the Gauss distribution.

Default:
1.0

Suggested values:
0.1, 0.5, 1.0, 3.0, 10.0, 20.0, 50.0

Restriction:
`Sigma > 0`

**`iterations`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Number of iterations.

Default:
10

Suggested values:
0, 3, 10, 100, 500

Restriction:
`Iterations >= 0`

## Module

Foundation
