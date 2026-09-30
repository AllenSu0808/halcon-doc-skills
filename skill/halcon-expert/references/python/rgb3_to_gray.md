# rgb3_to_gray (Operator)

## Name

`rgb3_to_gray` — Transform an RGB image to a gray scale image.

## Signature

`def rgb3_to_gray(image_red: HObject, image_green: HObject, image_blue: HObject) -> HObject`

## Description

`rgb3_to_gray` transforms an RGB image into a gray scale
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

**`image_red`** (input_object)  singlechannelimage(-array) `→` HObject (byte / int2 / uint2 / real)

Input image (red channel).

**`image_green`** (input_object)  singlechannelimage(-array) `→` HObject (byte / int2 / uint2 / real)

Input image (green channel).

**`image_blue`** (input_object)  singlechannelimage(-array) `→` HObject (byte / int2 / uint2 / real)

Input image (blue channel).

**`image_gray`** (output_object)  singlechannelimage(-array) `→` HObject (byte / int2 / uint2 / real)

Gray scale image.

## Possible Predecessors

`decompose3`

## Alternatives

`rgb1_to_gray`,
`trans_from_rgb`

## Module

Foundation
