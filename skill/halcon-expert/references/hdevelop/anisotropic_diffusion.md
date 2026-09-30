# anisotropic_diffusion (Operator)

## Name

`anisotropic_diffusion` — Perform an anisotropic diffusion of an image.

## Signature

`anisotropic_diffusion(Image : ImageAniso : Mode, Contrast, Theta, Iterations : )`

## Description

The operator `anisotropic_diffusion` performs an anisotropic
diffusion on the input image *`Image`* according to the model
of Perona and Malik. This procedure is also referred to as nonlinear
isotropic diffusion. Considering the image as a gray value function
u, the algorithm is a discretization of the partial
differential equation
$$u_{t}=div(g(|\nabla u|^{2},c)\nabla u)$$
with the initial value $u=u_{0}$ defined by
*`Image`* at a time $t_{0}$. The equation is iterated
*`Iterations`* times in time steps of length *`Theta`*, so
that the output image *`ImageAniso`* contains the gray value
function at the time $t_{0}+\texttt{Iterations}\cdot\texttt{Theta}$.

The goal of the anisotropic diffusion is the elimination of image
noise in constant image patches while preserving the edges in the
image. The distinction between edges and constant patches is
achieved using the threshold *`Contrast`* on the size of the
gray value differences between adjacent pixels. *`Contrast`* is
referred to as the contrast parameter and abbreviated with the
letter c.

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
diffusion even across edges of a height larger than c.
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

**`ImageAniso`** (output_object)  image(-array) `→` object (byte / uint2 / real)

Output image.

**`Mode`** (input_control)  string `→`  (string)

Diffusion coefficient as a function of the edge
amplitude.

Default:
'weickert'

List of values:
'parabolic', 'perona-malik', 'weickert'

**`Contrast`** (input_control)  real `→`  (real)

Contrast parameter.

Default:
5.0

Suggested values:
2.0, 5.0, 10.0, 20.0, 50.0, 100.0

Restriction:
`Contrast > 0`

**`Theta`** (input_control)  real `→`  (real)

Time step.

Default:
1.0

Suggested values:
0.5, 1.0, 3.0

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

## Alternatives

`bilateral_filter`,
`guided_filter`

## References

J. Weickert; “'Anisotropic Diffusion in Image Processing'; PhD
Thesis; Fachbereich Mathematik, Universität Kaiserslautern; 1996.
  
P. Perona, J. Malik; “Scale-space and edge detection using
anisotropic diffusion”; Transactions on Pattern Analysis and
Machine Intelligence 12(7), pp. 629-639; IEEE; 1990.
  
G. Aubert, P. Kornprobst; “Mathematical Problems in Image
Processing”; Applied Mathematical Sciences 147; Springer, New
York; 2002.

## Module

Foundation
