# InpaintingCt (Operator)

## Name

`InpaintingCt` — Perform an inpainting by coherence transport.

## Signature

`static void HOperatorSet.InpaintingCt(HObject image, HObject region, out HObject inpaintedImage, HTuple epsilon, HTuple kappa, HTuple sigma, HTuple rho, HTuple channelCoefficients)`

`HImage HImage.InpaintingCt(HRegion region, double epsilon, double kappa, double sigma, double rho, HTuple channelCoefficients)`

`HImage HImage.InpaintingCt(HRegion region, double epsilon, double kappa, double sigma, double rho, double channelCoefficients)`

## Description

The operator `InpaintingCt` inpaints a missing region
*`region`* of an image *`image`* by transporting image
information from the region's boundary along the coherence direction
into this region.

Since this operator's basic concept is inpainting by continuing
broken contour lines, the image content and inpainting region must
be such that this idea makes sense. That is, if a contour line hits
the region to inpaint at a pixel p, there should be some opposite
point q where this contour line continues so that the continuation
of contour lines from two opposite sides can succeed. In cases
where there is less geometry in the image, a diffusion-based
inpainter, e.g., [`HarmonicInterpolation`](harmonic_interpolation.md) may yield better
results. Alternatively, *`kappa`* can be set to *0*.
An extreme situation with little global geometries are pure
textures. Then the idea behind this operator will fail to produce
good results (think of a checkerboard with a big region to inpaint
relative to the checker fields). For these kinds of images, a
texture-based inpainting, e.g., [`InpaintingTexture`](inpainting_texture.md), can be
used instead.

The operator uses a so-called upwind scheme to assign gray values to
the missing pixels, i.e.,:

- The order of the pixels to process is given by their
  Euclidean distance to the boundary of the region to inpaint.
- A new value $u_{i}$ is computed as a weighted average of
  already known values $u_{j}$ within a disc of radius
  *`epsilon`* around the current pixel. The disc is
  restricted to already known pixels.
- The size of this scheme's mask depends on *`epsilon`*.

The initially used image data comes from a stripe of thickness
*`epsilon`* around the region to inpaint. Thus,
*`epsilon`* must be at least 1 for the scheme to work, but
should be greater. The maximum value for *`epsilon`* depends
on the gray values that should be transported into the region.
Choosing *`epsilon`* = *5* can be used in many cases.

Since the goal is to close broken contour lines, the direction of
the level lines must be estimated and used in the weight. This
estimated direction is called the coherence direction, and is
computed by means of the structure tensor S.
$$S=G_{\rho}\ast DvDv^{T}$$
and
$$v=G_{\sigma}\ast u$$
where * denotes the convolution, u denotes the gray
value image, D the derivative and G Gaussian kernels with
standard deviation $\sigma$ and $\rho$. These
standard deviations are defined by the operator's parameters
*`sigma`* and *`rho`*. *`sigma`* should have the
size of the noise or unimportant little objects, which are then not
considered in the estimation step by the pre-smoothing.
*`rho`* gives the size of the window around a pixel that will
be used for direction estimation. The coherence direction c then
is given by the eigendirection of S with respect to the minimal
eigenvalue $\lambda$, i.e.
$$Sc=\lambda c,|c|=1$$

For multichannel or color images, the scheme above is applied to
each channel separately, but the weights must be the same for all
channels to propagate information in the same direction. Since the
weight depends on the coherence direction, the common direction is
given by the eigendirection of a composite structure tensor. If
$u_{1},...,u_{n}$ denote the n channels of the image,
the channel structure tensors $S_{1},...,S_{n}$ are
computed and then combined to the composite structure tensor S.
$$S = \sum_{i=1}^{n} a_i S_i$$ ![figure](../assets/f34cc7694e4e964d.svg)
The coefficients $a_{i}$ are passed in *`channelCoefficients`*,
which is a tuple of length n or length 1. If the tuple length
is 1, the arithmetic mean is used, i.e., $a_{i}=1/n$. If the
length of *`channelCoefficients`* matches the number of
channels, the $a_{i}$ are set to
$$a_i = \frac{\text{ChannelCoefficients}_i}{\sum_{i=1}^{n} \text{ChannelCoefficients}_i}$$ ![figure](../assets/a78296a80cc7d072.svg)
in order to get a well-defined convex combination. Hence, the
*`channelCoefficients`* must be greater than or equal to zero
and their sum must be greater than zero. If the tuple length is
neither 1 nor the number of channels or the requirement above is
not satisfied, the operator returns an error message.

The purpose of using other *`channelCoefficients`* than the
arithmetic mean is to adapt to different color codes. The coherence
direction is a geometrical information of the composite image, which
is given by high contrasts such as edges. Thus the more contrast a
channel has, the more geometrical information it contains, and
consequently the greater its coefficient should be chosen (relative
to the others). For RGB images, *[0.299, 0.587, 0.114]* is a
good choice.

The weight in the scheme is the product of a directional component
and a distance component. If p is the 2D coordinate vector of the
current pixel to be inpainted and q the 2D coordinate of a pixel
in the neighborhood (the disc restricted to already known pixels),
the directional component measures the deviation of the vector p-q
from the coherence direction. If the deviation exponentially scaled
by $\beta$ is large, a low directional component is
assigned, whereas if it is small, a large directional component is
assigned. $\beta$ is controlled by *`kappa`* (in
percent):
$$\beta=20\ast\texttt{Epsilon}\ast\texttt{Kappa}/100$$
*`kappa`* defines how important it is to propagate information
along the coherence direction, so a large *`kappa`* yields
sharp edges, while a low *`kappa`* allows for more diffusion.

A special case is when *`kappa`* is zero: In this case the
directional component of the weight is constant (one). The
direction estimation step is then skipped to save computational
costs and the parameters *`sigma`*, *`rho`*,
*`channelCoefficients`* become meaningless, i.e, the
propagation of information is not based on the structures visible in
the image.

The distance component is 1/|p-q|. Consequently, if q is far
away from p, a low distance component is assigned, whereas if it
is near to p, a high distance component is assigned.

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

**`inpaintedImage`** (output_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / uint2 / real)

Output image.

**`epsilon`** (input_control)  number `→` [HTuple](HTuple.md) (*double*)

Radius of the pixel neighborhood.

Default:
5.0

Value range:
`1.0
≤
epsilon
≤
20.0`

Minimum increment:
1.0

Recommended increment:
1.0

**`kappa`** (input_control)  number `→` [HTuple](HTuple.md) (*double*)

Sharpness parameter in percent.

Default:
25.0

Value range:
`0.0
≤
kappa
≤
100.0`

Minimum increment:
1.0

Recommended increment:
1.0

**`sigma`** (input_control)  number `→` [HTuple](HTuple.md) (*double*)

Pre-smoothing parameter.

Default:
1.41

Value range:
`0.0
≤
sigma
≤
20.0`

Minimum increment:
0.001

Recommended increment:
0.01

**`rho`** (input_control)  number `→` [HTuple](HTuple.md) (*double*)

Smoothing parameter for the direction estimation.

Default:
4.0

Value range:
`0.001
≤
rho
≤
20.0`

Minimum increment:
0.001

Recommended increment:
0.01

**`channelCoefficients`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*double*)

Channel weights.

Default:
1

## Example (HDevelop)

```
read_image (Image, 'claudia')
gen_circle (Circle, 333, 164, 35)
inpainting_ct (Image, Circle, InpaintedImage, 15, 25, 1.5, 3,1.0)
```

## Alternatives

`HarmonicInterpolation`,
`InpaintingAniso`,
`InpaintingMcf`,
`InpaintingCed`,
`InpaintingTexture`

## References

Folkmar Bornemann, Tom März: “Fast Image Inpainting Based On
Coherence Transport”; Journal of Mathematical Imaging and Vision;
vol. 28, no. 3; pp. 259-278; 2007.

## Module

Foundation
