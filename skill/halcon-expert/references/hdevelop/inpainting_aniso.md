# inpainting_aniso (Operator)

## Name

`inpainting_aniso` — Perform an inpainting by anisotropic diffusion.

## Signature

`inpainting_aniso(Image, Region : InpaintedImage : Mode, Contrast, Theta, Iterations, Rho : )`

## Description

The operator `inpainting_aniso` uses the anisotropic diffusion
according to the model of Perona and Malik, to continue image edges
that cross the border of the region *`Region`* and to connect
them inside of *`Region`*.

With this, the structure of the edges in *`Region`* will be
made consistent with the surrounding image matrix, so that an
occlusion of errors or unwanted objects in the input image, a so
called inpainting, is less visible to the human beholder, since
there remain no obvious artifacts or smudges.

Considering the image as a gray value function u, the algorithm is
a discretization of the partial differential equation
$$u_{t}=div(g(|\nabla u|^{2},c)\nabla u)$$
with the initial value $u=u_{0}$ defined by
*`Image`* at a time $t_{0}=0$. The equation is
iterated *`Iterations`* times in time steps of length
*`Theta`*, so that the output image *`InpaintedImage`*
contains the gray value function at the time $\texttt{Iterations}\cdot\texttt{Theta}$.

The primary goal of the anisotropic diffusion, which is also
referred to as nonlinear isotropic diffusion, is the elimination of
image noise in constant image patches while preserving the edges in
the image. The distinction between edges and constant patches is
achieved using the threshold *`Contrast`* on the magnitude of
the gray value differences between adjacent
pixels. *`Contrast`* is referred to as the contrast parameter
and is abbreviated with the letter c. If the edge information is
distributed in an environment of the already existing edges by
smoothing the edge amplitude matrix, it is furthermore possible to
continue edges into the computation area *`Region`*. The
standard deviation of this smoothing process is determined by the
parameter *`Rho`*.

The algorithm used is basically the same as in the anisotropic
diffusion filter [`anisotropic_diffusion`](anisotropic_diffusion.md), except that here,
border treatment is not done by mirroring the gray values at the
border of *`Region`*. Instead, this procedure is only
applicable on regions that keep a distance of at least 3 pixels to
the border of the image matrix of *`Image`*, since the gray
values on this band around *`Region`* are used to define the
boundary conditions for the respective differential equation and
thus assure consistency with the neighborhood of
*`Region`*. Please note that the inpainting progress is
restricted to those pixels that are included in the ROI of the input
image *`Image`*. If the ROI does not include the entire region
*`Region`*, a band around the intersection of *`Region`*
and the ROI is used to define the boundary values.

The result of the diffusion process depends on the gray values in
the computation area of the input image *`Image`*. It must be
pointed out that already existing image edges are preserved within
*`Region`*. In particular, this holds for gray value jumps at
the border of *`Region`*, which can result for example from a
previous inpainting with constant gray value. If the procedure is to
be used for inpainting, it is recommended to apply the operator
[`harmonic_interpolation`](harmonic_interpolation.md) first to remove all unwanted edges
inside the computation area and to minimize the gray value
difference between adjacent pixels, unless the input image already
contains information inside *`Region`* that should be
preserved.

The variable diffusion coefficient g can be chosen to follow
different monotonically decreasing functions with values between
*0* and *1* and determines the response of the
diffusion process to an edge. With the parameter *`Mode`*, the
following functions can be selected:
$$g_{1}(x, c) = \frac{1}{\sqrt{1 + \frac{2x}{c^{2}}}}$$ ![figure](../assets/2f444083ffe9f264.svg)
Choosing the function $g_{1}$ by setting *`Mode`* to
*'parabolic'* guarantees that the associated differential
equation is parabolic, so that a well-posedness theory exists for
the problem and the procedure is stable for an arbitrary step size
*`Theta`*. In this case however, there remains a slight
diffusion even across edges of an amplitude larger than c.
$$g_2(x,c) = \frac{1}{1 + \frac{x}{c^2}}$$ ![figure](../assets/9fc42232febb3048.svg)
The choice of *'perona-malik'* for *`Mode`*, as used in
the publication of Perona and Malik, does not possess the
theoretical properties of $g_{1}$, but in practice it has
proved to be sufficiently stable and is thus widely used. The
theoretical instability results in a slight sharpening of strong
edges.
$$g_3(x,c) = 1 - \exp\left(-C^c \frac{8}{x^4}\right)$$ ![figure](../assets/dbf0587a38a071ad.svg)
The function $g_{3}$ with the constant C=3.31488,
proposed by Weickert, and selectable by setting *`Mode`* to
*'weickert'* is an improvement of $g_{2}$ with
respect to edge sharpening. The transition between smoothing and
sharpening happens very abruptly at x = c^2.

Furthermore, the choice of the value *'shock'* is possible
for *`Mode`* to select a contrast invariant modification of the
anisotropic diffusion. In this variant, the generation of edges is
not achieved by variation of the diffusion coefficient g, but the
constant coefficient g=1 and thus isotropic diffusion is
used. Additionally, a shock filter of type
$$u_{t}=-sgn(\nabla|\nabla u|)|\nabla u|$$
is applied, which, just like a negative diffusion coefficient,
causes a sharpening of the edges, but works independent of the
absolute value of $|\nabla u|$. In this mode,
*`Contrast`* does not have the meaning of a contrast parameter,
but specifies the ratio between the diffusion and the shock filter
part applied at each iteration step. Hence, the value *0*
would correspond to pure isotropic diffusion, as used in the
operator [`isotropic_diffusion`](isotropic_diffusion.md). The parameter is scaled in
such a way that diffusion and sharpening cancel each other out for
*`Contrast`*=*1*. A value
*`Contrast`*>*1* should not be used, since it would
make the algorithm unstable.

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

**`Mode`** (input_control)  string `→`  (string)

Type of edge sharpening algorithm.

Default:
'weickert'

List of values:
'parabolic', 'perona-malik', 'shock', 'weickert'

**`Contrast`** (input_control)  real `→`  (real)

Contrast parameter.

Default:
5.0

Suggested values:
0.5, 2.0, 5.0, 10.0, 20.0, 50.0, 100.0

Restriction:
`Contrast > 0`

**`Theta`** (input_control)  real `→`  (real)

Step size.

Default:
0.5

Suggested values:
0.5, 1.0, 5.0, 10.0, 30.0, 100.0

Restriction:
`Theta > 0`

**`Iterations`** (input_control)  integer `→`  (integer)

Number of iterations.

Default:
10

Suggested values:
1, 3, 10, 100, 500

Restriction:
`Iterations >= 1`

**`Rho`** (input_control)  real `→`  (real)

Smoothing coefficient for edge information.

Default:
3.0

Suggested values:
0.0, 0.1, 0.5, 1.0, 3.0, 10.0

Restriction:
`Rho >= 0`

## Example (HDevelop)

```
read_image (Image, 'fabrik')
gen_rectangle1 (Rectangle, 270, 180, 320, 230)
harmonic_interpolation (Image, Rectangle, InpaintedImage, 0.01)
inpainting_aniso (InpaintedImage, Rectangle, InpaintedImage2, \
                  'perona-malik', 5.0, 100, 50, 0.5)
dev_display(InpaintedImage2)
```

## Alternatives

`harmonic_interpolation`,
`inpainting_ct`,
`inpainting_mcf`,
`inpainting_texture`,
`inpainting_ced`

## References

J. Weickert; “Anisotropic Diffusion in Image Processing”; PhD
Thesis; Fachbereich Mathematik, Universität Kaiserslautern; 1996.
  
P. Perona, J. Malik; “Scale-space and edge detection using
anisotropic diffusion”; Transactions on Pattern Analysis and
Machine Intelligence 12(7), pp. 629-639; IEEE; 1990.
  
G. Aubert, P. Kornprobst; “Mathematical Problems in Image
Processing”; Applied Mathematical Sciences 147; Springer, New
York; 2002.

## Module

Foundation
