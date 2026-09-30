# SubImage (Operator)

## Name

`SubImage` — Subtract two images.

## Signature

`static void HOperatorSet.SubImage(HObject imageMinuend, HObject imageSubtrahend, out HObject imageSub, HTuple mult, HTuple add)`

`HImage HImage.SubImage(HImage imageSubtrahend, HTuple mult, HTuple add)`

`HImage HImage.SubImage(HImage imageSubtrahend, double mult, double add)`

## Description

The operator `SubImage` subtracts two images. The gray values
(g1,g2) of the input images (*`imageMinuend`* and
*`imageSubtrahend`*) are transformed as follows:
g' := (g1 - g2) * Mult + Add
If an overflow or an underflow occurs the values are clipped.
Note that this is not the case with cyclic and direction images.

Several images can be processed in one call. In this case
both input parameters contain the same number of images
which are then processed in pairs.
An output image is generated for every pair.

Please note that the runtime of the operator varies with different
control parameters. For frequently used combinations special
optimizations are used. Additionally, for byte, int2, and uint2
images special optimizations are implemented that use SIMD technology.
The actual application of these special optimizations is controlled by the
system parameter *"mmx_enable"* (see [`SetSystem`](set_system.md)).
If *"mmx_enable"* is set to *"true"* (and the SIMD
instruction set is available), the internal calculations are performed
using SIMD technology.

`SubImage` can be executed on an OpenCL device for byte, int1, int2,
uint2, int4, real, direction, cyclic, and complex images. However, since
for OpenCL 1.0 only single precision floating point is supported for all
devices, and not all rounding modes are supported, the OpenCL implementation
can produce slightly different results from the scalar or SIMD
implementations.

## Attention

Note that the acceleration gained by SIMD technology is highest on large,
compact input regions. However, in rare cases, the execution of
`SubImage` might take significantly longer with SIMD technology
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

**`imageMinuend`** (input_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte* / int1* / int2* / uint2* / int4* / int8 / real* / direction* / cyclic* / complex*) **allowed for compute devices*

Minuend(s).

**`imageSubtrahend`** (input_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte* / int1* / int2* / uint2* / int4* / int8 / real* / direction* / cyclic* / complex*) **allowed for compute devices*

Subtrahend(s).

**`imageSub`** (output_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / int1 / int2 / uint2 / int4 / int8 / real / direction / cyclic / complex)

Result image(s) by the subtraction.

**`mult`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / int / long)

Correction factor.

Default:
1.0

Suggested values:
0.0, 1.0, 2.0, 3.0, 4.0

Value range:
`-255.0
≤
mult
≤
255.0`

Minimum increment:
0.001

Recommended increment:
0.1

**`add`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / int / long)

Correction value.

Default:
128.0

Suggested values:
0.0, 128.0, 256.0

Value range:
`-512.0
≤
add
≤
512.0`

Minimum increment:
0.01

Recommended increment:
1.0

## Example (HDevelop)

```
read_image(Image1,'fabrik')
dev_display (Image1)
read_image(Image2,'monkey')
dev_display (Image2)
sub_image (Image1, Image2, Result, 1, 100)
dev_display (Result)
```

## Result

The operator `SubImage` returns the value 2 (
H_MSG_TRUE)
if the
parameters are correct. The behavior in case of empty input (no
input images available) is set via the operator
`set_system(::'no_object_result',<Result>:)`
If necessary an exception is raised.

## Possible Successors

`DualThreshold`

## Alternatives

`MultImage`,
`AddImage`

## See also

`AddImage`,
`MultImage`,
`DynThreshold`,
`CheckDifference`

## Module

Foundation
