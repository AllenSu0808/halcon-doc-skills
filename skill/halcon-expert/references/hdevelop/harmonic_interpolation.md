# harmonic_interpolation (Operator)

## Name

`harmonic_interpolation` — Perform a harmonic interpolation on an image region.

## Signature

`harmonic_interpolation(Image, Region : InpaintedImage : Precision : )`

## Description

The operator `harmonic_interpolation` reconstructs the
destroyed image data of *`Image`* inside the region
*`Region`* by solving the discrete Laplace equation
$u_{xx}+u_{yy}=0$ for the corresponding
gray value function u. The unique solution, which exists under
Dirichlet boundary conditions given by *`Image`* outside of
*`Region`*, is returned in *`InpaintedImage`*.

This technique is called harmonic interpolation since in function
theory the solutions of the Laplace equation are referred to as
harmonic functions.

If *`Region`* touches the border of the gray value matrix of
*`Image`* and thus some Dirichlet boundary values do not exist,
von Neumann boundary conditions are used instead. This means that
the gray values are mirrored at the border of *`Image`*. If no
Dirichlet boundary values exist at all, a constant image with gray
value *0* is returned.

The spatial derivatives are discretized as
$u_{xx}(x,y)=u(x-1,y)-2u(x,y)+u(x+1,y)$ and
$u_{yy}(x,y)=u(x,y-1)-2u(x,y)+u(x,y+1)$.
The equation is solved by an
iterative conjugate gradient solver, which iteratively improves the
computational error until the maximum norm of its update step
becomes a smaller fraction than *`Precision`* of the norm of
the input data or a maximum of *1000* iterations is
reached. *`Precision`* = *0.01* thus means a relative
computational accuracy of 1%.

## Attention

Note that filter operators may return unexpected results if
an image with a reduced domain is used as input. Please refer to the
chapter [Filters](toc_filters.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on channel level.
- Automatically parallelized on internal data level.

This operator supports canceling timeouts and interrupts.

## Parameters

**`Image`** (input_object)  (multichannel-)image(-array) `→` object (byte / uint2 / real)

Input image.

**`Region`** (input_object)  region `→` object

Inpainting region.

**`InpaintedImage`** (output_object)  image(-array) `→` object (byte / uint2 / real)

Output image.

**`Precision`** (input_control)  real `→`  (real)

Computational accuracy.

Default:
0.001

Suggested values:
0.0, 0.0001, 0.001, 0.01

Restriction:
`Precision >= 0.0`

## Alternatives

`inpainting_ct`,
`inpainting_aniso`,
`inpainting_mcf`,
`inpainting_texture`,
`inpainting_ced`

## References

L.C. Evans; “Partial Differential Equations”; AMS, Providence;
1998.
  
W. Hackbusch; “Iterative Lösung großer schwachbesetzter
Gleichungssysteme”; Teubner, Stuttgart;1991.

## Module

Foundation
