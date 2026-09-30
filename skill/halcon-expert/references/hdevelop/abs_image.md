# abs_image (Operator)

## Name

`abs_image` — Calculate the absolute value (modulus) of an image.

## Signature

`abs_image(Image : ImageAbs : : )`

## Description

The operator `abs_image` calculates the absolute gray values
of images of any type and stores the result in *`ImageAbs`*.
The power spectrum of complex images is calculated as a `real` image.
For a *`Image`* of type 'int1', *`ImageAbs`* is of type
`byte`. For *`Image`* of other signed types the type of the input
image is used for *`ImageAbs`*. The behavior in case of overflows or
underflows is undefined. The operator `abs_image` generates a logical
copy of unsigned images.

`abs_image` can be executed on an OpenCL device for `int1`,
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

**`Image`** (input_object)  (multichannel-)image(-array) `→` object (int1* / int2* / int4* / int8 / real* / complex*) **allowed for compute devices*

Image(s) for which the absolute gray values are
to be calculated.

**`ImageAbs`** (output_object)  (multichannel-)image(-array) `→` object (byte / int2 / int4 / int8 / real)

Result image(s).

## Example (HDevelop)

```
convert_image_type (Image, ImageInt2, 'int2')
texture_laws (ImageInt2, ImageTexture, 'el', 2, 5)
abs_image (ImageTexture, ImageTexture)
```

## Result

The operator `abs_image` returns the value 2 (
H_MSG_TRUE)
. The
behavior in case of empty input (no input images available) is set
via the operator
`set_system(::'no_object_result',<Result>:)`

## See also

`convert_image_type`,
`power_byte`

## Module

Foundation
