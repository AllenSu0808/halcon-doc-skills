# ComplexToReal (Operator)

## Name

`ComplexToReal` — Convert a complex image into two real images.

## Signature

`static void HOperatorSet.ComplexToReal(HObject imageComplex, out HObject imageReal, out HObject imageImaginary)`

`HImage HImage.ComplexToReal(out HImage imageImaginary)`

## Description

`ComplexToReal` converts a complex image
*`imageComplex`* into two real images *`imageReal`*
and *`imageImaginary`*, which contain the real and imaginary
part of the complex image.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`imageComplex`** (input_object)  singlechannelimage(-array) `→` [HImage](HImage.md) (complex)

Complex image.

**`imageReal`** (output_object)  image(-array) `→` [HImage](HImage.md) (real)

Real part.

**`imageImaginary`** (output_object)  image(-array) `→` [HImage](HImage.md) (real)

Imaginary part.

## See also

`RealToComplex`

## Module

Foundation
