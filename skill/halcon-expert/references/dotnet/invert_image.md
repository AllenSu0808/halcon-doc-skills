# InvertImage (Operator)

## Name

`InvertImage` — Invert an image.

## Signature

`static void HOperatorSet.InvertImage(HObject image, out HObject imageInvert)`

`HImage HImage.InvertImage()`

## Description

The operator `InvertImage` inverts the gray values of an image.
For images of the `byte` and `cyclic` type the result is
calculated
as:
g' = 255 - g
Images of the 'direction' type are transformed by
g' = (g + 90) modulo 180
In the case of signed types the values are negated. The resulting
image has the same pixel type as the input image.

Several images can be processed in one call.
An output image is generated for every input image.

`InvertImage` can be executed on an OpenCL device for `byte`,
`direction`, `cyclic`, `int1`, `int2`,
`uint2`, `int4`, and `real` images.

## Execution Information

- Supports OpenCL compute devices.
- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on channel level.
- Automatically parallelized on domain level.

## Parameters

**`image`** (input_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte* / direction* / cyclic* / int1* / int2* / uint2* / int4* / int8 / real*) **allowed for compute devices*

Input image(s).

**`imageInvert`** (output_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real)

Image(s) with inverted gray values.

## Example (HDevelop)

```
read_image(Orig,'fabrik')
invert_image(Orig,Invert)
dev_display(Invert)
```

## Possible Successors

`Watersheds`

## Alternatives

`ScaleImage`

## See also

`ScaleImage`,
`AddImage`,
`SubImage`

## Module

Foundation
