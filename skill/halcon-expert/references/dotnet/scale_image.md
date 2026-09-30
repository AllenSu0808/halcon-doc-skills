# ScaleImage (Operator)

## Name

`ScaleImage` — Scale the gray values of an image.

## Signature

`static void HOperatorSet.ScaleImage(HObject image, out HObject imageScaled, HTuple mult, HTuple add)`

`HImage HImage.ScaleImage(HTuple mult, HTuple add)`

`HImage HImage.ScaleImage(double mult, double add)`

## Description

The operator `ScaleImage` scales the input images
(*`image`*) by the following transformation:
g' := g * Mult + Add
If an overflow or an underflow occurs the values are clipped.
Note that this is not the case with cyclic and direction images.

This operator can be applied, e.g., to map the gray values of an image, i.e.,
the interval [GMin,GMax], to the maximum range [0:255]. For this, the
parameters are chosen as follows:
$$Mult = \frac{255}{GMax - GMin} \\ Add = -Mult * GMIn$$ ![figure](../assets/305bc562fb0f5ae8.svg)
The values for GMin and GMax can be determined, e.g., with the operator
[`MinMaxGray`](min_max_gray.md).

Please note that the runtime of the operator varies with different
control parameters. For frequently used combinations special
optimizations are used. Additionally, special optimizations are implemented
that use fixed point arithmetic (for int2 and uint2 images),
and further optimizations that use SIMD technology (for byte, int2, and
uint2 images).
The actual application of these special optimizations is controlled by the
system parameters *"int_zooming"* and *"mmx_enable"*
(see [`SetSystem`](set_system.md)).
If *"int_zooming"* is set to *"true"*, the internal
calculation is performed using fixed point arithmetic, leading
to much shorter execution times. However, the accuracy of the transformed
gray values is slightly lower in this mode. The difference to the more
accurate calculation (using *"int_zooming"* = *"false"*)
is typically less than two gray levels.
If *"mmx_enable"* is set to *"true"*(and the SIMD
instruction set is available), the internal
calculations are performed using fixed point arithmetic and SIMD technology.
In this case the setting of *"int_zooming"* is ignored.

`ScaleImage` can be executed on an OpenCL device for byte, int1, int2,
uint2, int4, real, direction, cyclic, and complex images. However, since
for OpenCL 1.0 only single precision floating point is supported for all
devices, and not all rounding modes are supported, the OpenCL implementation
can produce slightly different results from the scalar or SIMD
implementations.

## Attention

Note that the acceleration gained by SIMD technology is highest on large,
compact input regions. However, in rare cases, the execution of
`ScaleImage` might take significantly longer with SIMD technology
than without, depending on the input region and the capabilities of
the hardware. In these cases, the use of SIMD
technology can be avoided by `set_system(::'mmx_enable','false':)`.

## Execution Information

- Supports OpenCL compute devices.
- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on channel level.
- Automatically parallelized on domain level.

## Parameters

**`image`** (input_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte* / int1* / int2* / uint2* / int4* / int8 / real* / direction* / cyclic* / complex*) **allowed for compute devices*

Image(s) whose gray values are to be scaled.

**`imageScaled`** (output_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte* / int1* / int2* / uint2* / int4* / int8 / real* / direction* / cyclic* / complex*) **allowed for compute devices*

Result image(s) by the scale.

**`mult`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / int / long)

Scale factor.

Default:
0.01

Suggested values:
0.001, 0.003, 0.005, 0.008, 0.01, 0.02, 0.03, 0.05, 0.08, 0.1, 0.5, 1.0

Minimum increment:
0.001

Recommended increment:
0.1

**`add`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / int / long)

Offset.

Default:
0

Suggested values:
0, 10, 50, 100, 200, 500

Minimum increment:
0.01

Recommended increment:
1.0

## Example (HDevelop)

```
* Complement of the gray values:
scale_image(Image,Invert,-1.0,255.0)
```

## Result

The operator `ScaleImage` returns the value 2 (
H_MSG_TRUE)
if the
parameters are correct. The behavior in case of empty input (no
input images available) is set via the operator
`set_system(::'no_object_result',<Result>:)`
Otherwise an exception treatment is carried out.

## Possible Predecessors

`MinMaxGray`

## Alternatives

`MultImage`,
`AddImage`,
`SubImage`

## See also

`MinMaxGray`

## Module

Foundation
