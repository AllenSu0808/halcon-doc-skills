# isotropic_diffusion (Operator)

## Name

`isotropic_diffusion` — Perform an isotropic diffusion of an image.

## Signature

`isotropic_diffusion(Image : SmoothedImage : Sigma, Iterations : )`

## Description

The operator `isotropic_diffusion` performs an isotropic
diffusion of the input image *`Image`*. This corresponds to a
convolution of the image matrix with a Gaussian mask of standard
deviation *`Sigma`*. If the parameter *`Iterations`* is
set to *0*, such a convolution is performed explicitly. For
input images with a full ROI, `isotropic_diffusion` returns
the same results as the operator [`derivate_gauss`](derivate_gauss.md) when
choosing *'none'* for its parameter `Component`. If
the gray value matrix is larger than the ROI of *`Image`* the
two operators differ since [`derivate_gauss`](derivate_gauss.md) takes the gray
values outside of the ROI into account, while
`isotropic_diffusion` mirrors the values at the boundary of
the ROI in any case. The computational complexity increases linearly
with the value of *`Sigma`*.

If *`Iterations`* has a positive value the smoothing process
is considered as an application of the heat equation
$$u_{t}=\Delta u$$
on the gray value function u with the initial value $u=u_{0}$ defined by the gray values of *`Image`* at a time
$t_{0}$. This equation is then solved up to a time $t_0 + \tfrac{1}{2} \sigma_i^2$ ![figure](../assets/44ea3b9f8d9a0dc9.svg), which
is equivalent to the above convolution, using an iterative procedure
for parabolic partial differential equations. The computational
complexity is proportional to the value of *`Iterations`* and
independent of *`Sigma`* in this case. For small values of
*`Iterations`*, the computational accuracy is very low,
however. For this reason, choosing *`Iterations`* <
*3* is not recommended.

For smaller values of *`Sigma`*, the convolution implementation
is typically the faster method. Since the runtime of the partial
differential equation solver only depends on the number of
iterations and not on the value of *`Sigma`*, it is typically
faster for large values of *`Sigma`* if few iterations are
chosen (e.g., *`Iterations`* = *3*).

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

**`Image`** (input_object)  (multichannel-)image(-array) `→` object (byte / uint2 / real)

Input image.

**`SmoothedImage`** (output_object)  image(-array) `→` object (byte / uint2 / real)

Output image.

**`Sigma`** (input_control)  real `→`  (real)

Standard deviation of the Gauss distribution.

Default:
1.0

Suggested values:
0.1, 0.5, 1.0, 3.0, 10.0, 20.0, 50.0

Restriction:
`Sigma > 0`

**`Iterations`** (input_control)  integer `→`  (integer)

Number of iterations.

Default:
10

Suggested values:
0, 3, 10, 100, 500

Restriction:
`Iterations >= 0`

## Module

Foundation
