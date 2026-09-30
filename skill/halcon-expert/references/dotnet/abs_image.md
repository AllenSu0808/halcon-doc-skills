# AbsImage (Operator)

## Name

`AbsImage` — Calculate the absolute value (modulus) of an image.

## Signature

`static void HOperatorSet.AbsImage(HObject image, out HObject imageAbs)`

`HImage HImage.AbsImage()`

## Description

The operator `AbsImage` calculates the absolute gray values
of images of any type and stores the result in *`imageAbs`*.
The power spectrum of complex images is calculated as a `real` image.
For a *`image`* of type 'int1', *`imageAbs`* is of type
`byte`. For *`image`* of other signed types the type of the input
image is used for *`imageAbs`*. The behavior in case of overflows or
underflows is undefined. The operator `AbsImage` generates a logical
copy of unsigned images.

`AbsImage` can be executed on an OpenCL device for `int1`,
`int2`, `int4`, `real`, and `complex` images.
However, since for OpenCL 1.0 only single precision floating point is
supported for all devices, and not all rounding modes are supported,
the OpenCL implementation can produce slightly different results from the
scalar or SIMD implementations.

## Execution Information

- Supports OpenCL compute devices.
- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on channel level.
- Automatically parallelized on domain level.

## Parameters

**`image`** (input_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (int1* / int2* / int4* / int8 / real* / complex*) **allowed for compute devices*

Image(s) for which the absolute gray values are
to be calculated.

**`imageAbs`** (output_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / int2 / int4 / int8 / real)

Result image(s).

## Example (HDevelop)

```
convert_image_type (Image, ImageInt2, 'int2')
texture_laws (ImageInt2, ImageTexture, 'el', 2, 5)
abs_image (ImageTexture, ImageTexture)
```

## Result

The operator `AbsImage` returns the value 2 (
H_MSG_TRUE)
. The
behavior in case of empty input (no input images available) is set
via the operator
`set_system(::'no_object_result',<Result>:)`

## See also

`ConvertImageType`,
`PowerByte`

## Module

Foundation
