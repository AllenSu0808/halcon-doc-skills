# coherence_enhancing_diff (Operator)

## Name

`coherence_enhancing_diff` — Perform a coherence enhancing diffusion of an image.

## Signature

`def coherence_enhancing_diff(image: HObject, sigma: float, rho: float, theta: float, iterations: int) -> HObject`

## Description

The operator `coherence_enhancing_diff` performs an
anisotropic diffusion process on the input image *`image`* to
increase the coherence of the image structures contained in
*`image`*. In particular, noncontinuous image edges are
connected by diffusion, without being smoothed perpendicular to
their dominating direction. For this,
`coherence_enhancing_diff` uses the anisotropic diffusion
equation
$$u_{t}=div(G(u)\nabla u)$$
formulated by Weickert. With a 2x2 coefficient
matrix G that depends on the gray values in *`image`*, this
is an enhancement of the mean curvature flow or intrinsic heat
equation
$$u_t = \operatorname{div}\left(\frac{\nabla u}{|\nabla u|}\right)|\nabla u| = \operatorname{curv}(u)|\nabla u|$$ ![figure](../assets/4ff1d8dfca9a3270.svg)
on the gray value function u defined by the input image
*`image`* at a time $t_{0}=0$. The smoothing
operator [`mean_curvature_flow`](mean_curvature_flow.md) is a direct application of the
mean curvature flow equation. The discrete diffusion equation is
solved in *`iterations`* time steps of length *`theta`*,
so that the output image *`image_ced`* contains the gray value
function at the time $\texttt{Iterations}\cdot\texttt{Theta}$.

To detect the edge direction more robustly, in particular on noisy
input data, an additional isotropic smoothing step can precede the
computation of the gray value gradients. The parameter
*`sigma`* determines the magnitude of the smoothing by means of
the standard deviation of a corresponding Gaussian convolution
kernel, as used in the operator [`isotropic_diffusion`](isotropic_diffusion.md) for
isotropic image smoothing.

While the matrix G is given by
$$G_{MCF}(u)=I-\frac{1}{\|\nabla u\|^{2}}\nabla u(\nabla u)^{\top}$$ ![figure](../assets/b1dd5bc8507fd50e.svg)
in the case of the operator [`mean_curvature_flow`](mean_curvature_flow.md), where I
denotes the unit matrix, $G_{MCF}$ is again
smoothed componentwise by a Gaussian filter of standard deviation
*`rho`* for `coherence_enhancing_diff`. Then, the final
coefficient matrix
$$GCED = g_1 \Big((\lambda_1 - \lambda_2)^2\Big) w_1(w_1)^T + g_2 \Big((\lambda_1 - \lambda_2)^2\Big) w_2(w_2)^T$$ ![figure](../assets/d4ebe27325e8d928.svg)
is constructed from the eigenvalues
$\lambda_{1},\lambda_{2}$ and eigenvectors
$w_{1},w_{2}$ of the resulting intermediate matrix,
where the functions
$$g_1(p) = 0.001 g_2(p) = 0.001 + 0.999 \exp\left(-\frac{1}{p}\right)$$ ![figure](../assets/39691190c4261342.svg)
were determined empirically and taken from the publication of
Weickert.

Hence, the diffusion direction in [`mean_curvature_flow`](mean_curvature_flow.md) is
only determined by the local direction of the gray value gradient,
while $G_{CED}$ considers the macroscopic structure of
the image objects on the scale *`rho`* and the magnitude of the
diffusion in `coherence_enhancing_diff` depends on how well
this structure is defined.

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

**`image`** (input_object)  (multichannel-)image(-array) `→` HObject (byte / uint2 / real)

Input image.

**`image_ced`** (output_object)  image(-array) `→` HObject (byte / uint2 / real)

Output image.

**`sigma`** (input_control)  real `→` float

Smoothing for derivative operator.

Default:
0.5

Suggested values:
0.0, 0.1, 0.5, 1.0

Restriction:
`Sigma >= 0`

**`rho`** (input_control)  real `→` float

Smoothing for diffusion coefficients.

Default:
3.0

Suggested values:
0.0, 1.0, 3.0, 5.0, 10.0, 30.0

Restriction:
`Rho >= 0`

**`theta`** (input_control)  real `→` float

Time step.

Default:
0.5

Suggested values:
0.1, 0.2, 0.3, 0.4, 0.5

Restriction:
`0 < Theta <= 0.5`

**`iterations`** (input_control)  integer `→` int

Number of iterations.

Default:
10

Suggested values:
1, 5, 10, 20, 50, 100, 500

Restriction:
`Iterations >= 1`

## References

J. Weickert, V. Hlavac, R. Sara; “Multiscale texture
enhancement”; Computer analysis of images and patterns, Lecture
Notes in Computer Science, Vol. 970, pp. 230-237; Springer,
Berlin; 1995.
  
J. Weickert, B. ter Haar Romeny, L. Florack, J. Koenderink,
M. Viergever; “A review of nonlinear diffusion filtering”;
Scale-Space Theory in Computer Vision, Lecture Notes in
Comp. Science, Vol. 1252, pp. 3-28; Springer, Berlin; 1997.

## Module

Foundation
