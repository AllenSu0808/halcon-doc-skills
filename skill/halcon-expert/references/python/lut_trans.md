# lut_trans (Operator)

## Name

`lut_trans` — Transform an image with a gray-value look-up-table

## Signature

`def lut_trans(image: HObject, lut: Sequence[int]) -> HObject`

## Description

`lut_trans` transforms an image *`image`* by using a gray
value look-up-table *`lut`*. This table acts as a
transformation function. In the case of byte-images, *`lut`*
has to be a tuple of length 256. In the case of int2-images,
*`lut`* has to be a tuple of length 256 <= length <= 65536. If
the length of the *`lut`* is <= 32768, the transformation is
applied to the positive gray values only, i.e., the first element of
the *`lut`* specifies the new gray value for the gray value 0.
If the *`lut`* is longer than 32768, exactly 65536 must be
passed. In this case, the positive and negative gray values are
transformed. In this case, the first element indicates the new gray
value for the gray value -32768 of the input image, while the last
element of the tuple indicates the new gray value for the gray value
32767. In all cases, the gray values of values outside the range of
*`lut`* are set to 0. In the case of uint2-images,
*`lut`* has to be a tuple of length 256 <= length <=
65536. Gray values outside the range of *`lut`* are set to 0.

## Attention

`lut_trans` can be executed on OpenCL devices.

## Execution Information

- Supports OpenCL compute devices.
- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on channel level.
- Automatically parallelized on domain level.

## Parameters

**`image`** (input_object)  (multichannel-)image(-array) `→` HObject (byte* / int2* / uint2*) **allowed for compute devices*

Image whose gray values are to be transformed.

**`image_result`** (output_object)  (multichannel-)image(-array) `→` HObject (byte / int2 / uint2)

Transformed image.

**`lut`** (input_control)  integer-array `→` Sequence[int]

Table containing the transformation.

## Example (HDevelop)

```
* Apply a gamma correction to an image.
Gamma := 2.2
GammaLUT := []
for G := 0 to 255 by 1
    GammaLUT := [GammaLUT,round(255.0*pow(G/255.0,1.0/Gamma))]
endfor
read_image (Image, 'mreut')
lut_trans (Image, ImageGamma, GammaLUT)
```

## Result

The operator `lut_trans` returns the value 2 (
H_MSG_TRUE)
if the
parameters are correct. Otherwise an exception is raised.

## Module

Foundation
