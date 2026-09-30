# real_to_complex (Operator)

## Name

`real_to_complex` — Convert two real images into a complex image.

## Signature

`def real_to_complex(image_real: HObject, image_imaginary: HObject) -> HObject`

## Description

`real_to_complex` converts two real images
*`image_real`* and *`image_imaginary`*, which contain
the real and imaginary part of a complex image, into a complex image
*`image_complex`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`image_real`** (input_object)  singlechannelimage(-array) `→` HObject (real)

Real part.

**`image_imaginary`** (input_object)  singlechannelimage(-array) `→` HObject (real)

Imaginary part.

**`image_complex`** (output_object)  image(-array) `→` HObject (complex)

Complex image.

## See also

`complex_to_real`

## Module

Foundation
