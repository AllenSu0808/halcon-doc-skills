# RealToComplex (Operator)

## Name

`RealToComplex` — Convert two real images into a complex image.

## Signature

`static void HOperatorSet.RealToComplex(HObject imageReal, HObject imageImaginary, out HObject imageComplex)`

`HImage HImage.RealToComplex(HImage imageImaginary)`

## Description

`RealToComplex` converts two real images
*`imageReal`* and *`imageImaginary`*, which contain
the real and imaginary part of a complex image, into a complex image
*`imageComplex`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`imageReal`** (input_object)  singlechannelimage(-array) `→` [HImage](HImage.md) (real)

Real part.

**`imageImaginary`** (input_object)  singlechannelimage(-array) `→` [HImage](HImage.md) (real)

Imaginary part.

**`imageComplex`** (output_object)  image(-array) `→` [HImage](HImage.md) (complex)

Complex image.

## See also

`ComplexToReal`

## Module

Foundation
