# complex_to_real (Operator)

## Name

`complex_to_real` — Convert a complex image into two real images.

## Signature

`complex_to_real(ImageComplex : ImageReal, ImageImaginary : : )`

## Description

`complex_to_real` converts a complex image
*`ImageComplex`* into two real images *`ImageReal`*
and *`ImageImaginary`*, which contain the real and imaginary
part of the complex image.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`ImageComplex`** (input_object)  singlechannelimage(-array) `→` object (complex)

Complex image.

**`ImageReal`** (output_object)  image(-array) `→` object (real)

Real part.

**`ImageImaginary`** (output_object)  image(-array) `→` object (real)

Imaginary part.

## See also

`real_to_complex`

## Module

Foundation
