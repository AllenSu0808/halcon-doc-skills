# add_image_border (Operator)

## Name

`add_image_border` — Add a border to an image.

## Signature

`def add_image_border(image: HObject, size: MaybeSequence[int], value: MaybeSequence[Union[int, str]]) -> HObject`

## Description

Adds a border to the input image *`image`* and returns the resulting image in
*`image_border`*.

The size of the border in pixels must be passed in *`size`*.
It can be set as follows:

- Single number: Border size in all four directions
  left/right/top/bottom.
- Two numbers: Border size on left/right and top/bottom side:
  `[l/r, t/b]`.
- Four numbers: Border size on left, right, top, bottom side:
  `[l,r,t,b]`.

The gray value of the added border must be passed in *`value`*.
It can be set as follows:

- Single number: Value will be applied to all channels of
  *`image`*.
- Multiple numbers: Values will be applied to the channels of
  the image separately.
  Thus, the first value will be applied to the
  first channel, the second value will be applied
  to the second channel and so on.

  *Restriction:* Number of values must be
  equal to the number of channels.

Note that `add_image_border` will ignore the input domain and will always return
an image with a full domain in *`image_border`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`image`** (input_object)  multichannel-image-array `→` HObject (byte / direction / int1 / int2 / uint2 / int4 / int8 / real)

Input image.

**`image_border`** (output_object)  multichannel-image-array `→` HObject (byte / direction / int1 / int2 / uint2 / int4 / int8 / real)

Output image.

**`size`** (input_control)  attribute.name(-array) `→` MaybeSequence[int]

Size of the border in pixels.

Default:
10

**`value`** (input_control)  attribute.name(-array) `→` MaybeSequence[Union[int, str]]

Gray value of the border.

Default:
100

## Example (HDevelop)

```
* Add a border of 20 pixels with a constant gray value of 255
* on all four sides of Image
read_image (Image, 'printer_chip/printer_chip_01')
add_image_border (Image, ImageBorder, 20, 255)

* Add a 10-pixel border with a constant gray value of 255 to
* the left and right side and a 20-pixel border with the same
* gray value to the top and bottom of Image.
read_image (Image, 'printer_chip/printer_chip_01')
add_image_border (Image, ImageBorder, [10, 20], 255)
```

## Alternatives

`tile_images_offset`

## Module

Foundation
