# Rgb1ToGray (Operator)

## Name

`Rgb1ToGray` — Transform an RGB image into a gray scale image.

## Signature

`static void HOperatorSet.Rgb1ToGray(HObject RGBImage, out HObject grayImage)`

`HImage HImage.Rgb1ToGray()`

## Description

`Rgb1ToGray` transforms an RGB image into a gray scale
image. The three channels of the RGB image are passed as the first
three channels of the input image. The image is transformed
according to the following formula:
gray = 0.299 * red + 0.587 * green + 0.114 * blue .

If one of the input images in *`RGBImage`* is a single-channel image
its reference will be simply copied to the output *`grayImage`*.

## Execution Information

- Supports OpenCL compute devices.
- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on domain level.

## Parameters

**`RGBImage`** (input_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / int2 / uint2 / real)

Three-channel RBG image.

**`grayImage`** (output_object)  singlechannelimage(-array) `→` [HImage](HImage.md) (byte / int2 / uint2 / real)

Gray scale image.

## Example (HDevelop)

```
* Transformation from rgb to gray
read_image(Image,'patras')
dev_display(Image)
rgb1_to_gray(Image,GrayImage)
dev_display(GrayImage)
```

## Possible Predecessors

`Compose3`

## Alternatives

`TransFromRgb`,
`Rgb3ToGray`

## Module

Foundation
