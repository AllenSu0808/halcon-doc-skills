# real_to_complex (Operator)

## Name

`real_to_complex` — Convert two real images into a complex image.

## Signature

`real_to_complex(ImageReal, ImageImaginary : ImageComplex : : )`

## Description

`real_to_complex` converts two real images
*`ImageReal`* and *`ImageImaginary`*, which contain
the real and imaginary part of a complex image, into a complex image
*`ImageComplex`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`ImageReal`** (input_object)  singlechannelimage(-array) `→` object (real)

Real part.

**`ImageImaginary`** (input_object)  singlechannelimage(-array) `→` object (real)

Imaginary part.

**`ImageComplex`** (output_object)  image(-array) `→` object (complex)

Complex image.

## See also

`complex_to_real`

## Module

Foundation
