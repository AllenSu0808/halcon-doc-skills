# div_image (Operator)

## Name

`div_image` — Divide two images.

## Signature

`def div_image(image_1: HObject, image_2: HObject, mult: Union[int, float], add: Union[int, float]) -> HObject`

## Description

The operator `div_image` divides two images. The gray values
(g1,g2) of the input images (*`image_1`*) are
transformed as follows:
g' := g1 / g2 * Mult + Add
If an overflow or an underflow occurs the values are clipped.
For a division by zero the result is set to zero.

Several images can be processed in one call. In this case
both input parameters contain the same number of images
which are then processed in pairs.
An output image is generated for every pair.

`div_image` can be executed on an OpenCL device for byte, int1, int2,
uint2, int4, real and complex images. However, since for OpenCL 1.0 only
single precision floating point is supported for all devices, and not all
rounding modes are supported, the OpenCL implementation can produce slightly
different results from the scalar implementation.

## Execution Information

- Supports OpenCL compute devices.
- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on channel level.
- Automatically parallelized on domain level.

## Parameters

**`image_1`** (input_object)  (multichannel-)image(-array) `→` HObject (byte* / int1* / int2* / uint2* / int4* / int8 / real* / complex*) **allowed for compute devices*

Image(s) 1.

**`image_2`** (input_object)  (multichannel-)image(-array) `→` HObject (byte* / int1* / int2* / uint2* / int4* / int8 / real* / complex*) **allowed for compute devices*

Image(s) 2.

**`image_result`** (output_object)  (multichannel-)image(-array) `→` HObject (byte / int1 / int2 / uint2 / int4 / int8 / real / complex)

Result image(s) by the division.

**`mult`** (input_control)  number `→` Union[int, float]

Factor for gray range adaption.

Default:
255

Suggested values:
0.1, 0.2, 0.5, 1.0, 2.0, 3.0, 10, 100, 500, 1000

Value range:
`-1000
≤
mult
≤
1000`

Minimum increment:
0.001

Recommended increment:
1

**`add`** (input_control)  number `→` Union[int, float]

Value for gray range adaption.

Default:
0

Suggested values:
0.0, 128.0, 256.0, 1025

Value range:
`-1000
≤
add
≤
1000`

Minimum increment:
0.01

Recommended increment:
1.0

## Result

The operator `div_image` returns the value 2 (
H_MSG_TRUE)
if the
parameters are correct. The behavior in case of empty input (no
input images available) is set via the operator
`set_system(::'no_object_result',<Result>:)`
If necessary an exception is raised.

## Alternatives

`add_image`,
`sub_image`,
`mult_image`

## See also

`add_image`,
`sub_image`,
`mult_image`

## Module

Foundation
