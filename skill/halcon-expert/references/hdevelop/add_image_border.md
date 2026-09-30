# add_image_border (Operator)

## Name

`add_image_border` — Add a border to an image.

## Signature

`add_image_border(Image : ImageBorder : Size, Value : )`

## Description

Adds a border to the input image *`Image`* and returns the resulting image in
*`ImageBorder`*.

The size of the border in pixels must be passed in *`Size`*.
It can be set as follows:

- Single number: Border size in all four directions
  left/right/top/bottom.
- Two numbers: Border size on left/right and top/bottom side:
  `[l/r, t/b]`.
- Four numbers: Border size on left, right, top, bottom side:
  `[l,r,t,b]`.

The gray value of the added border must be passed in *`Value`*.
It can be set as follows:

- Single number: Value will be applied to all channels of
  *`Image`*.
- Multiple numbers: Values will be applied to the channels of
  the image separately.
  Thus, the first value will be applied to the
  first channel, the second value will be applied
  to the second channel and so on.

  *Restriction:* Number of values must be
  equal to the number of channels.

Note that `add_image_border` will ignore the input domain and will always return
an image with a full domain in *`ImageBorder`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`Image`** (input_object)  multichannel-image-array `→` object (byte / direction / int1 / int2 / uint2 / int4 / int8 / real)

Input image.

**`ImageBorder`** (output_object)  multichannel-image-array `→` object (byte / direction / int1 / int2 / uint2 / int4 / int8 / real)

Output image.

**`Size`** (input_control)  attribute.name(-array) `→`  (integer)

Size of the border in pixels.

Default:
10

**`Value`** (input_control)  attribute.name(-array) `→`  (integer / string)

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
