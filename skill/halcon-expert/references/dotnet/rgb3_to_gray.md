# Rgb3ToGray (Operator)

## Name

`Rgb3ToGray` — Transform an RGB image to a gray scale image.

## Signature

`static void HOperatorSet.Rgb3ToGray(HObject imageRed, HObject imageGreen, HObject imageBlue, out HObject imageGray)`

`HImage HImage.Rgb3ToGray(HImage imageGreen, HImage imageBlue)`

## Description

`Rgb3ToGray` transforms an RGB image into a gray scale
image. The three channels of the RGB image are passed as three
separate images. The image is transformed according to the
following formula:
gray = 0.299 * red + 0.587 * green + 0.114 * blue .

## Execution Information

- Supports OpenCL compute devices.
- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on domain level.

## Parameters

**`imageRed`** (input_object)  singlechannelimage(-array) `→` [HImage](HImage.md) (byte / int2 / uint2 / real)

Input image (red channel).

**`imageGreen`** (input_object)  singlechannelimage(-array) `→` [HImage](HImage.md) (byte / int2 / uint2 / real)

Input image (green channel).

**`imageBlue`** (input_object)  singlechannelimage(-array) `→` [HImage](HImage.md) (byte / int2 / uint2 / real)

Input image (blue channel).

**`imageGray`** (output_object)  singlechannelimage(-array) `→` [HImage](HImage.md) (byte / int2 / uint2 / real)

Gray scale image.

## Example (HDevelop)

```
* Transformation from rgb to gray
read_image(Image,'patras')
dev_display(Image)
decompose3(Image, ImageR, ImageG, ImageB)
rgb3_to_gray(ImageR,ImageG,ImageB,GrayImage)
dev_display(GrayImage)
```

## Possible Predecessors

`Decompose3`

## Alternatives

`Rgb1ToGray`,
`TransFromRgb`

## Module

Foundation
