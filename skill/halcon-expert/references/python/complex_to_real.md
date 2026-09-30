# complex_to_real (Operator)

## Name

`complex_to_real` — Convert a complex image into two real images.

## Signature

`def complex_to_real(image_complex: HObject) -> Tuple[HObject, HObject]`

## Description

`complex_to_real` converts a complex image
*`image_complex`* into two real images *`image_real`*
and *`image_imaginary`*, which contain the real and imaginary
part of the complex image.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`image_complex`** (input_object)  singlechannelimage(-array) `→` HObject (complex)

Complex image.

**`image_real`** (output_object)  image(-array) `→` HObject (real)

Real part.

**`image_imaginary`** (output_object)  image(-array) `→` HObject (real)

Imaginary part.

## See also

`real_to_complex`

## Module

Foundation
