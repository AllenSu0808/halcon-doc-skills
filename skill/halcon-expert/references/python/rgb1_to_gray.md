# rgb1_to_gray (Operator)

## Name

`rgb1_to_gray` — Transform an RGB image into a gray scale image.

## Signature

`def rgb1_to_gray(rgbimage: HObject) -> HObject`

## Description

`rgb1_to_gray` transforms an RGB image into a gray scale
image. The three channels of the RGB image are passed as the first
three channels of the input image. The image is transformed
according to the following formula:
gray = 0.299 * red + 0.587 * green + 0.114 * blue .

If one of the input images in *`rgbimage`* is a single-channel image
its reference will be simply copied to the output *`gray_image`*.

## Execution Information

- Supports OpenCL compute devices.
- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on domain level.

## Parameters

**`rgbimage`** (input_object)  (multichannel-)image(-array) `→` HObject (byte / int2 / uint2 / real)

Three-channel RBG image.

**`gray_image`** (output_object)  singlechannelimage(-array) `→` HObject (byte / int2 / uint2 / real)

Gray scale image.

## Possible Predecessors

`compose3`

## Alternatives

`trans_from_rgb`,
`rgb3_to_gray`

## Module

Foundation
