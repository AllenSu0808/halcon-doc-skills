# InpaintingCed (Operator)

## Name

`InpaintingCed` — Perform an inpainting by coherence enhancing diffusion.

## Signature

`static void HOperatorSet.InpaintingCed(HObject image, HObject region, out HObject inpaintedImage, HTuple sigma, HTuple rho, HTuple theta, HTuple iterations)`

`HImage HImage.InpaintingCed(HRegion region, double sigma, double rho, double theta, int iterations)`

## Description

The operator `InpaintingCed` performs an anisotropic
diffusion process on the region *`region`* of the input image
*`image`* with the objective of completing discontinuous image
edges diffusively by increasing the coherence of the image
structures contained in *`image`* and without smoothing these
edges perpendicular to their dominating direction. The mechanism is
the same as in the operator [`CoherenceEnhancingDiff`](coherence_enhancing_diff.md), which
is based on a discretization of the anisotropic diffusion equation
$$u_{t}=div(G(u)\nabla u)$$
formulated by Weickert. With a 2x2 coefficient
matrix G that depends on the gray values in *`image`*, this
is an enhancement of the mean curvature flow or intrinsic heat
equation
$$u_t = \operatorname{div}\left(\frac{\nabla u}{|\nabla u|}\right)|\nabla u| = \operatorname{curv}(u)|\nabla u|$$ ![figure](../assets/4ff1d8dfca9a3270.svg)
on the gray value function u defined by the input image
*`image`* at a time $t_{0}=0$. The smoothing
operator [`MeanCurvatureFlow`](mean_curvature_flow.md) is a direct application of the
mean curvature flow equation. With the operator
[`InpaintingMcf`](inpainting_mcf.md), it can also be used for image
inpainting. The discrete diffusion equation is solved in
*`iterations`* time steps of length *`theta`*, so that the
output image *`inpaintedImage`* contains the gray value
function at the time $\texttt{Iterations}\cdot\texttt{Theta}$.

To detect the image direction more robustly, in particular on noisy
input data, an additional isotropic smoothing step can precede the
computation of the gray value gradients. The parameter
*`sigma`* determines the magnitude of the smoothing by means of
the standard deviation of a corresponding Gaussian convolution
kernel, as used in the operator [`IsotropicDiffusion`](isotropic_diffusion.md) for
isotropic image smoothing.

Similar to the operator [`InpaintingMcf`](inpainting_mcf.md), the structure of the
image data in *`region`* is simplified by smoothing the level
lines of *`image`*. By this, image errors and unwanted objects
can be removed from the image, while the edges in the neighborhood
are extended continuously. This procedure is called image
inpainting. The objective is to introduce a minimum amount of
artifacts or smoothing effects, so that the image manipulation is
least visible to a human beholder.

While the matrix G is given by
$$G_{MCF}(u)=I-\frac{1}{\|\nabla u\|^{2}}\nabla u(\nabla u)^{\top}$$ ![figure](../assets/b1dd5bc8507fd50e.svg)
in the case of the operator [`InpaintingMcf`](inpainting_mcf.md), where I
denotes the unit matrix, $G_{MCF}$ is again smoothed
componentwise by a Gaussian filter of standard deviation
*`rho`* for [`CoherenceEnhancingDiff`](coherence_enhancing_diff.md). Then, the final
coefficient matrix
$$GCED = g_1 \Big((\lambda_1 - \lambda_2)^2\Big) w_1(w_1)^T + g_2 \Big((\lambda_1 - \lambda_2)^2\Big) w_2(w_2)^T$$ ![figure](../assets/d4ebe27325e8d928.svg)
is constructed from the eigenvalues
$\lambda_{1},\lambda_{2}$ and eigenvectors
$w_{1},w_{2}$ of the resulting intermediate matrix,
where the functions
$$g_1(p) = 0.001 g_2(p) = 0.001 + 0.999 \exp\left(-\frac{1}{p}\right)$$ ![figure](../assets/39691190c4261342.svg)
were determined empirically and taken from the publication of
Weickert.

Hence, the diffusion direction in [`MeanCurvatureFlow`](mean_curvature_flow.md) is
only determined by the local direction of the gray value gradient,
while $G_{CED}$ considers the macroscopic structure of
the image objects on the scale *`rho`* and the magnitude of the
diffusion in [`CoherenceEnhancingDiff`](coherence_enhancing_diff.md) depends on how well
this structure is defined.

To achieve the highest possible consistency of the newly created
edges with the image data from the neighborhood, the gray values
are not mirrored at the border of *`region`* to compute the
convolution with the smoothing filter mask of scale *`rho`* on
the pixels close to the border, although this would be the common
approach for filter operators. Instead, the existence of gray values
on a band of width ceil(3.1*Rho)+2 pixels around *`region`*
is presumed and these values are used in the convolution. This means
that *`region`* must keep this much distance to the border of
the image matrix *`image`*. By involving the gray values and
directional information from this extended area, it can be achieved
that the continuation of the edges is not only continuous, but also
smooth, which means without kinks. Please note that the inpainting
progress is restricted to those pixels that are included in the ROI
of the input image *`image`*. If the ROI does not include the
entire region *`region`*, a band around the intersection of
*`region`* and the ROI is used to define the boundary values.

To decrease the number of iterations required for attaining a
satisfactory result, it may be useful to initialize the gray value
matrix in *`region`* with the harmonic interpolant, a
continuous function of minimal curvature, by applying the operator
[`HarmonicInterpolation`](harmonic_interpolation.md) to *`image`* before calling
`InpaintingCed`.

## Attention

Note that filter operators may return unexpected results if
an image with a reduced domain is used as input. Please refer to the
chapter [Filters](toc_filters.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`image`** (input_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / uint2 / real)

Input image.

**`region`** (input_object)  region `→` [HRegion](HRegion.md)

Inpainting region.

**`inpaintedImage`** (output_object)  image(-array) `→` [HImage](HImage.md) (byte / uint2 / real)

Output image.

**`sigma`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Smoothing for derivative operator.

Default:
0.5

Suggested values:
0.0, 0.1, 0.5, 1.0

Restriction:
`Sigma >= 0`

**`rho`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Smoothing for diffusion coefficients.

Default:
3.0

Suggested values:
0.0, 1.0, 3.0, 5.0, 10.0, 30.0

Restriction:
`Rho >= 0`

**`theta`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Time step.

Default:
0.5

Suggested values:
0.1, 0.2, 0.3, 0.4, 0.5

Restriction:
`0 < Theta <= 0.5`

**`iterations`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Number of iterations.

Default:
10

Suggested values:
1, 5, 10, 20, 50, 100, 500

Restriction:
`Iterations >= 1`

## Example (HDevelop)

```
read_image (Image, 'fabrik')
gen_rectangle1 (Rectangle, 270, 180, 320, 230)
harmonic_interpolation (Image, Rectangle, InpaintedImage, 0.01)
inpainting_ced (InpaintedImage, Rectangle, InpaintedImage2, \
                0.5, 3.0, 0.5, 1000)
dev_display(InpaintedImage2)
```

## Alternatives

`HarmonicInterpolation`,
`InpaintingCt`,
`InpaintingAniso`,
`InpaintingMcf`,
`InpaintingTexture`

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
