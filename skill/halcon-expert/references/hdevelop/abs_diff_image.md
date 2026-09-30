# abs_diff_image (Operator)

## Name

`abs_diff_image` — Calculate the absolute difference of two images.

## Signature

`abs_diff_image(Image1, Image2 : ImageAbsDiff : Mult : )`

## Description

`abs_diff_image` calculates the absolute difference between
two images. The gray values g' of the output image
*`ImageAbsDiff`* are calculated from the gray values (g1,g2)
of the input images (*`Image1`* and *`Image2`*) as
follows:
g' = |(g1 - g2)| * Mult
If an overflow or an underflow occurs the resulting values are
clipped.

Several images can be processed in one call. In this case, both
input parameters contain the same number of images which are then
processed in pairs. An output image is generated for every pair.

Please note that the runtime of the operator depends on the value of
*`Mult`*. For *`Mult`* = 1, a special optimization is
used. Since values of *`Mult`* different from 1 cannot yield
additional information, *`Mult`* = 1 should be used in
applications. All other values of *`Mult`* should only be used
for visualization purposes. Additionally, for byte, int1, int2, and
uint2 images special optimizations are implemented for
*`Mult`* = 1 that use SIMD technology. The actual
application of these special optimizations is controlled by the
system parameter *'mmx_enable'* (see [`set_system`](set_system.md)).
If *'mmx_enable'* is set to *'true'* (and the SIMD
instruction set is available), the internal calculations are
performed using SIMD technology.

`abs_diff_image` can be executed on an OpenCL device for byte, int1,
int2, uint2, int4, and real images. However, since for OpenCL 1.0 only
single precision floating point is supported for all devices, and not all
rounding modes are supported, the OpenCL implementation can produce slightly
different results from the scalar or SIMD implementations.

## Attention

Note that the acceleration gained by SIMD technology is highest on large,
compact input regions. However, in rare cases, the execution of
`abs_diff_image` might take significantly longer with SIMD technology
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

**`Image1`** (input_object)  (multichannel-)image(-array) `→` object (byte* / int1* / int2* / uint2* / int4* / int8 / real*) **allowed for compute devices*

Input image 1.

**`Image2`** (input_object)  (multichannel-)image(-array) `→` object (byte* / int1* / int2* / uint2* / int4* / int8 / real*) **allowed for compute devices*

Input image 2.

**`ImageAbsDiff`** (output_object)  (multichannel-)image(-array) `→` object (byte / int1 / int2 / uint2 / int4 / int8 / real)

Absolute value of the difference of the input images.

**`Mult`** (input_control)  number `→`  (real / integer)

Scale factor.

Default:
1.0

Suggested values:
1.0, 2.0, 3.0, 4.0

Restriction:
`Mult > 0`

## Result

The operator `abs_diff_image` returns the value 2 (
H_MSG_TRUE)
if the
parameters are correct. The behavior in case of empty input (no
input images available) is set via the operator
`set_system(::'no_object_result',<Result>:)`. If necessary an
exception is raised.

## Possible Successors

`threshold`

## Alternatives

`sub_image`

## See also

`add_image`,
`scale_image`,
`dyn_threshold`

## Module

Foundation
