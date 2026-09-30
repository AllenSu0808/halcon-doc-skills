# sub_image (Operator)

## Name

`sub_image` — Subtract two images.

## Signature

`sub_image(ImageMinuend, ImageSubtrahend : ImageSub : Mult, Add : )`

## Description

The operator `sub_image` subtracts two images. The gray values
(g1,g2) of the input images (*`ImageMinuend`* and
*`ImageSubtrahend`*) are transformed as follows:
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
system parameter *'mmx_enable'* (see [`set_system`](set_system.md)).
If *'mmx_enable'* is set to *'true'* (and the SIMD
instruction set is available), the internal calculations are performed
using SIMD technology.

`sub_image` can be executed on an OpenCL device for byte, int1, int2,
uint2, int4, real, direction, cyclic, and complex images. However, since
for OpenCL 1.0 only single precision floating point is supported for all
devices, and not all rounding modes are supported, the OpenCL implementation
can produce slightly different results from the scalar or SIMD
implementations.

## Attention

Note that the acceleration gained by SIMD technology is highest on large,
compact input regions. However, in rare cases, the execution of
`sub_image` might take significantly longer with SIMD technology
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

**`ImageMinuend`** (input_object)  (multichannel-)image(-array) `→` object (byte* / int1* / int2* / uint2* / int4* / int8 / real* / direction* / cyclic* / complex*) **allowed for compute devices*

Minuend(s).

**`ImageSubtrahend`** (input_object)  (multichannel-)image(-array) `→` object (byte* / int1* / int2* / uint2* / int4* / int8 / real* / direction* / cyclic* / complex*) **allowed for compute devices*

Subtrahend(s).

**`ImageSub`** (output_object)  (multichannel-)image(-array) `→` object (byte / int1 / int2 / uint2 / int4 / int8 / real / direction / cyclic / complex)

Result image(s) by the subtraction.

**`Mult`** (input_control)  number `→`  (real / integer)

Correction factor.

Default:
1.0

Suggested values:
0.0, 1.0, 2.0, 3.0, 4.0

Value range:
`-255.0
≤
Mult
≤
255.0`

Minimum increment:
0.001

Recommended increment:
0.1

**`Add`** (input_control)  number `→`  (real / integer)

Correction value.

Default:
128.0

Suggested values:
0.0, 128.0, 256.0

Value range:
`-512.0
≤
Add
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

The operator `sub_image` returns the value 2 (
H_MSG_TRUE)
if the
parameters are correct. The behavior in case of empty input (no
input images available) is set via the operator
`set_system(::'no_object_result',<Result>:)`
If necessary an exception is raised.

## Possible Successors

`dual_threshold`

## Alternatives

`mult_image`,
`add_image`

## See also

`add_image`,
`mult_image`,
`dyn_threshold`,
`check_difference`

## Module

Foundation
