# add_image (Operator)

## Name

`add_image` — Add two images.

## Signature

`def add_image(image_1: HObject, image_2: HObject, mult: Union[int, float], add: Union[int, float]) -> HObject`

## Description

The operator `add_image` adds two images. The gray values
(g1,g2) of the input images (*`image_1`* and
*`image_2`*) are transformed as follows:
g' := (g1 + g2) * Mult + Add

If an overflow or an underflow occurs the values are clipped.
Note that this is not the case with cyclic and direction images.
The resulting image is stored in *`image_result`*.

It is possible to add byte images with int2, uint2 or int4 images and to add
int4 to int2 or uint2 images. In this case the result will be of type int2 or
int4 respectively.

Several images can be processed in one call. In this case
both input parameters contain the same number of images
which are then processed in pairs.
An output image is generated for every pair.

Please note that the runtime of the operator varies with different
control parameters. For frequently used combinations special
optimizations are used. Additionally, for byte, int2, uint2, and int4
images special optimizations are implemented that use SIMD technology.
The actual application of these special optimizations is controlled by the
system parameter *"mmx_enable"* (see [`set_system`](set_system.md)).
If *"mmx_enable"* is set to *"true"* (and the SIMD
instruction set is available), the internal calculations are performed
using SIMD technology.

`add_image` can be executed on an OpenCL device for byte, int1, int2,
uint2, int4, real, direction, cyclic, and complex images. However, since
for OpenCL 1.0 only single precision floating point is supported for all
devices, and not all rounding modes are supported, the OpenCL implementation
can produce slightly different results from the scalar or SIMD
implementations.

## Attention

Note that the acceleration gained by SIMD technology is highest on large,
compact input regions. However, in rare cases, the execution of `add_image`
might take significantly longer with SIMD technology than without,
depending on the input region and the capabilities of
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

**`image_1`** (input_object)  (multichannel-)image(-array) `→` HObject (byte* / int1* / int2* / uint2* / int4* / int8 / real* / direction* / cyclic* / complex*) **allowed for compute devices*

Image(s) 1.

**`image_2`** (input_object)  (multichannel-)image(-array) `→` HObject (byte* / int1* / int2* / uint2* / int4* / int8 / real* / direction* / cyclic* / complex*) **allowed for compute devices*

Image(s) 2.

**`image_result`** (output_object)  (multichannel-)image(-array) `→` HObject (byte / int1 / int2 / uint2 / int4 / int8 / real / direction / cyclic / complex)

Result image(s) by the addition.

**`mult`** (input_control)  number `→` Union[int, float]

Factor for gray value adaption.

Default:
0.5

Suggested values:
0.2, 0.4, 0.6, 0.8, 1.0, 1.5, 2.0, 3.0, 5.0

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

**`add`** (input_control)  number `→` Union[int, float]

Value for gray value range adaption.

Default:
0

Suggested values:
0, 64, 128, 255, 512

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

## Result

The operator `add_image` returns the value 2 (
H_MSG_TRUE)
if the
parameters are correct. The behavior in case of empty input (no
input images available) is set via the operator
`set_system(::'no_object_result',<Result>:)`
If necessary an exception is raised.

## Alternatives

`sub_image`,
`mult_image`

## See also

`sub_image`,
`mult_image`

## Module

Foundation
