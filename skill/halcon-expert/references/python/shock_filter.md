# shock_filter (Operator)

## Name

`shock_filter` — Apply a shock filter to an image.

## Signature

`def shock_filter(image: HObject, theta: float, iterations: int, mode: str, sigma: float) -> HObject`

## Description

The operator `shock_filter` applies a shock filter to the
input image *`image`* to sharpen the edges contained in it.
The principle of the shock filter is based on the transport of the
gray values of the image towards an edge from both sides through
dilation and erosion and satisfies the differential equation
$$u_{t}=s|\nabla u|$$
on the function u defined by the gray values in *`image`* at
a time $t_{0}=0$. The discretized equation is solved
in *`iterations`* time steps of length *`theta`*, so that
the output image *`sharpened_image`* contains the gray value
function at the time $\texttt{Iterations}\cdot\texttt{Theta}$.

The decision between dilation and erosion is made using the sign
function s with values {-1,0,+1} on a
conventional edge detector. The detector of Canny
$$s = -sgn\left(D^2 u\left( \frac{\nabla u}{|\nabla u|}, \frac{\nabla u}{|\nabla u|} \right)\right)$$ ![figure](../assets/07d187f65a5f358c.svg)
is available with *`mode`*=*"canny"* and the detector
of Marr/Hildreth (the Laplace operator)
$$s=-sgn(\Delta u)$$
can be selected by *`mode`*=*"laplace"*.

To make the edge detection more robust, in particular on noisy
images, it can be performed on a smoothed image matrix. This is done
by giving the standard deviation of a Gaussian kernel for
convolution with the image matrix in the parameter *`sigma`*.

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

**`sharpened_image`** (output_object)  image(-array) `→` HObject (byte / uint2 / real)

Output image.

**`theta`** (input_control)  real `→` float

Time step.

Default:
0.5

Suggested values:
0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7

Restriction:
`0 < Theta <= 0.7`

**`iterations`** (input_control)  integer `→` int

Number of iterations.

Default:
10

Suggested values:
1, 3, 10, 100

Restriction:
`Iterations >= 1`

**`mode`** (input_control)  string `→` str

Type of edge detector.

Default:
"canny"

List of values:
"canny", "laplace"

**`sigma`** (input_control)  real `→` float

Smoothing of edge detector.

Default:
1.0

Suggested values:
0.0, 0.5, 1.0, 2.0, 5.0

Restriction:
`Theta >= 0`

## References

F. Guichard, J. Morel; “A Note on Two Classical Shock Filters and
Their Asymptotics”; Michael Kerckhove (Ed.): Scale-Space and
Morphology in Computer Vision, LNCS 2106, pp. 75-84; Springer, New
York; 2001.
  
G. Aubert, P. Kornprobst; “Mathematical Problems in Image
Processing”; Applied Mathematical Sciences 147; Springer, New
York; 2002.

## Module

Foundation
