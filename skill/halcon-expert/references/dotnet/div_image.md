# DivImage (Operator)

## Name

`DivImage` — Divide two images.

## Signature

`static void HOperatorSet.DivImage(HObject image1, HObject image2, out HObject imageResult, HTuple mult, HTuple add)`

`HImage HImage.DivImage(HImage image2, HTuple mult, HTuple add)`

`HImage HImage.DivImage(HImage image2, double mult, double add)`

## Description

The operator `DivImage` divides two images. The gray values
(g1,g2) of the input images (*`image1`*) are
transformed as follows:
g' := g1 / g2 * Mult + Add
If an overflow or an underflow occurs the values are clipped.
For a division by zero the result is set to zero.

Several images can be processed in one call. In this case
both input parameters contain the same number of images
which are then processed in pairs.
An output image is generated for every pair.

`DivImage` can be executed on an OpenCL device for byte, int1, int2,
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

**`image1`** (input_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte* / int1* / int2* / uint2* / int4* / int8 / real* / complex*) **allowed for compute devices*

Image(s) 1.

**`image2`** (input_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte* / int1* / int2* / uint2* / int4* / int8 / real* / complex*) **allowed for compute devices*

Image(s) 2.

**`imageResult`** (output_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / int1 / int2 / uint2 / int4 / int8 / real / complex)

Result image(s) by the division.

**`mult`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / int / long)

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

**`add`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / int / long)

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

## Example (HDevelop)

```
read_image(Image1,'fabrik')
dev_display (Image1)
read_image(Image2,'monkey')
dev_display (Image2)
div_image (Image1, Image2, Result, 200, 10)
dev_display (Result)
```

## Result

The operator `DivImage` returns the value 2 (
H_MSG_TRUE)
if the
parameters are correct. The behavior in case of empty input (no
input images available) is set via the operator
`set_system(::'no_object_result',<Result>:)`
If necessary an exception is raised.

## Alternatives

`AddImage`,
`SubImage`,
`MultImage`

## See also

`AddImage`,
`SubImage`,
`MultImage`

## Module

Foundation
