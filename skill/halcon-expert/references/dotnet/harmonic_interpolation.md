# HarmonicInterpolation (Operator)

## Name

`HarmonicInterpolation` — Perform a harmonic interpolation on an image region.

## Signature

`static void HOperatorSet.HarmonicInterpolation(HObject image, HObject region, out HObject inpaintedImage, HTuple precision)`

`HImage HImage.HarmonicInterpolation(HRegion region, double precision)`

## Description

The operator `HarmonicInterpolation` reconstructs the
destroyed image data of *`image`* inside the region
*`region`* by solving the discrete Laplace equation
$u_{xx}+u_{yy}=0$ for the corresponding
gray value function u. The unique solution, which exists under
Dirichlet boundary conditions given by *`image`* outside of
*`region`*, is returned in *`inpaintedImage`*.

This technique is called harmonic interpolation since in function
theory the solutions of the Laplace equation are referred to as
harmonic functions.

If *`region`* touches the border of the gray value matrix of
*`image`* and thus some Dirichlet boundary values do not exist,
von Neumann boundary conditions are used instead. This means that
the gray values are mirrored at the border of *`image`*. If no
Dirichlet boundary values exist at all, a constant image with gray
value *0* is returned.

The spatial derivatives are discretized as
$u_{xx}(x,y)=u(x-1,y)-2u(x,y)+u(x+1,y)$ and
$u_{yy}(x,y)=u(x,y-1)-2u(x,y)+u(x,y+1)$.
The equation is solved by an
iterative conjugate gradient solver, which iteratively improves the
computational error until the maximum norm of its update step
becomes a smaller fraction than *`precision`* of the norm of
the input data or a maximum of *1000* iterations is
reached. *`precision`* = *0.01* thus means a relative
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

**`image`** (input_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / uint2 / real)

Input image.

**`region`** (input_object)  region `→` [HRegion](HRegion.md)

Inpainting region.

**`inpaintedImage`** (output_object)  image(-array) `→` [HImage](HImage.md) (byte / uint2 / real)

Output image.

**`precision`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Computational accuracy.

Default:
0.001

Suggested values:
0.0, 0.0001, 0.001, 0.01

Restriction:
`Precision >= 0.0`

## Alternatives

`InpaintingCt`,
`InpaintingAniso`,
`InpaintingMcf`,
`InpaintingTexture`,
`InpaintingCed`

## References

L.C. Evans; “Partial Differential Equations”; AMS, Providence;
1998.
  
W. Hackbusch; “Iterative Lösung großer schwachbesetzter
Gleichungssysteme”; Teubner, Stuttgart;1991.

## Module

Foundation
