# inpainting_mcf (Operator)

## Name

`inpainting_mcf` — Perform an inpainting by smoothing of level lines.

## Signature

`inpainting_mcf(Image, Region : InpaintedImage : Sigma, Theta, Iterations : )`

## Description

The operator `inpainting_mcf` extends the image edges that
adjoin the region *`Region`* of the input image *`Image`*
into the interior of *`Region`* and connects their ends by
smoothing the level lines of the gray value function of
*`Image`*.

This happens through the application of the mean curvature flow or
intrinsic heat equation
$$u_t = \operatorname{div}\left(\frac{\nabla u}{|\nabla u|}\right)|\nabla u| = \operatorname{curv}(u)|\nabla u|$$ ![figure](../assets/4ff1d8dfca9a3270.svg)
on the gray value function u defined in the region *`Region`*
by the input image *`Image`* at a time $t_{0}=0$. The discretized equation is solved in *`Iterations`*
time steps of length *`Theta`*, so that the output image
*`InpaintedImage`* contains the gray value function at the time
$\texttt{Iterations}\cdot\texttt{Theta}$.

A stationary state of the mean curvature flow equation, which is
also the basis of the operator [`mean_curvature_flow`](mean_curvature_flow.md), has the
special property that the level lines of u all have the curvature
*0*. This means that after sufficiently many iterations there
are only straight edges left inside the computation area of the
output image *`InpaintedImage`*. By this, the structure of
objects inside of *`Region`* can be simplified, while the
remaining edges are continuously connected to those of the
surrounding image matrix. This allows for a removal of image errors
and unwanted objects in the input image, a so called image
inpainting, which is only weakly visible to a human beholder since
there remain no obvious artifacts or smudges.

To detect the image direction more robustly, in particular on noisy
input data, an additional isotropic smoothing step can precede the
computation of the gray value gradients. The parameter
*`Sigma`* determines the magnitude of the smoothing by means of
the standard deviation of a corresponding Gaussian convolution
kernel, as used in the operator [`isotropic_diffusion`](isotropic_diffusion.md) for
isotropic image smoothing.

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

**`Region`** (input_object)  region `→` object

Inpainting region.

**`InpaintedImage`** (output_object)  image(-array) `→` object (byte / uint2 / real)

Output image.

**`Sigma`** (input_control)  real `→`  (real)

Smoothing for derivative operator.

Default:
0.5

Suggested values:
0.0, 0.1, 0.5, 1.0

Restriction:
`Sigma >= 0`

**`Theta`** (input_control)  real `→`  (real)

Time step.

Default:
0.5

Suggested values:
0.1, 0.2, 0.3, 0.4, 0.5

Restriction:
`0 < Theta <= 0.5`

**`Iterations`** (input_control)  integer `→`  (integer)

Number of iterations.

Default:
10

Suggested values:
1, 5, 10, 20, 50, 100, 500

Restriction:
`Iterations >= 1`

## Alternatives

`harmonic_interpolation`,
`inpainting_ct`,
`inpainting_aniso`,
`inpainting_ced`,
`inpainting_texture`

## References

M. G. Crandall, P. Lions; “Convergent Difference Schemes for
Nonlinear Parabolic Equations and Mean Curvature Motion”;
Numer. Math. 75 pp. 17-41; 1996.
  
G. Aubert, P. Kornprobst; “Mathematical Problems in Image
Processing”; Applied Mathematical Sciences 147; Springer, New
York; 2002.

## Module

Foundation
