# gen_image_interleaved (Operator)

## Name

`gen_image_interleaved` — Create a three-channel image from a pointer to the interleaved pixels.

## Signature

`def gen_image_interleaved(pixel_pointer: int, color_format: str, original_width: int, original_height: int, alignment: int, type: str, image_width: int, image_height: int, start_row: int, start_column: int, bits_per_channel: int, bit_shift: int) -> HObject`

## Description

The operator `gen_image_interleaved` creates a three-channel image
from an input image, whose pixels are stored line-sequentially in
*`pixel_pointer`*. The size of the input image has to be passed in
*`original_width`* and *`original_height`*, the format of the
interleaved pixels in *`color_format`*.

The output image will be sized
*`image_width`* * *`image_height`*. Together with the
coordinates of upper left corner *`start_row`* and
*`start_column`* any section of the input image can be extracted.
When a *0* is passed to *`image_width`*, *`image_height`*,
*`start_row`*, and *`start_column`*, the output image will have the
same dimensions as the input image.

Note that the image type *`type`* (see [`gen_image_const`](gen_image_const.md))
of the output image *`image_rgb`*
has to be chosen such that the whole range of possible color values of the
input image can be represented. I.e. `gen_image_interleaved` does not
allow to create a byte image from an input image with *`color_format`*
*"rgb48"*.

When the formats *"rgb48"*, *"bgr48"*, *"rgbx64"*, and
*"bgr64"* do not use the full range of 16 bits per channel and pixel,
the number of actually used bits should be passed in *`bits_per_channel`*.
Furthermore, the pixel values of the input image can be shifted by
*`bit_shift`* bits to the right.

The fourth channel of four-channel input images in the formats *"rgbx"*,
*"bgrx"*, *"rgbx64"*, and *"bgrx64"* is simply discarded.

The storage for the new image is newly created by HALCON.
Thus, it can be released after the call.
Note that how to pass a pointer value depends on the used operator signature
and programming environment. Make sure to pass the actual memory address
where the image data is stored, not the address of a pointer variable. Care
must be taken not to truncate 64-bit pointers on 64-bit architectures.

Possible values for *`color_format`*:

- **'rgb555':** —

  16 bit rgb triple (5 bit per pixel and channel), the padding bit (X) being
  the first bit. The bit pattern is XRRRRRGG|GGGBBBBB.
- **'bgr555':** —

  16 bit bgr triple (5 bit per pixel and channel), the padding bit (X) being
  the first bit. The bit pattern is XBBBBBGG|GGGRRRRR.
- **'rgb5551':** —

  16 bit rgb triple (5 bit per pixel and channel), the padding bit (X) being
  the last bit. The bit pattern is RRRRRGGG|GGBBBBBX.
- **'bgr5551':** —

  16 bit bgr triple (5 bit per pixel and channel), the padding bit (X) being
  the last bit. The bit pattern is BBBBBGGG|GGRRRRRX.
- **'rgb565':** —

  16 bit rgb triple (5 bit per pixel and channel, 6 bit for the green
  channel). The bit pattern is RRRRRGGG|GGGBBBBB.
- **'bgr565':** —

  16 bit bgr triple (5 bit per pixel and channel, 6 bit for the green
  channel). The bit pattern is BBBBBGGG|GGGRRRRR.
- **'rgb':** —

  24 bit rgb triple (8 bit per pixel and channel)
- **'bgr':** —

  24 bit bgr triple (8 bit per pixel and channel)
- **'rgbx':** —

  32 bit rgb quadruple (8 bit per pixel and channel)
- **'bgrx':** —

  32 bit bgr quadruple (8 bit per pixel and channel)
- **'rgb48':** —

  48 bit rgb triple (16 bit per pixel and channel)
- **'bgr48':** —

  48 bit bgr triple (16 bit per pixel and channel)
- **'rgbx64':** —

  64 bit rgb quadruple (16 bit per pixel and channel)
- **'bgrx64':** —

  64 bit bgr quadruple (16 bit per pixel and channel)

The values *"rgb555"*, *"bgr555"*, *"rgb565"*,
*"bgr565"*, *"rgb5551"* and *"bgr5551"* can be used with the
suffix 'le' (Little Endian: Lower byte is expected first) or - which is
the default if the suffix is omitted - 'be' (Big Endian: Higher byte is
expected first). For example,
the bit pattern for
*`color_format`* = *"rgb555"* is XRRRRRGG|GGGBBBBB, while the bit
pattern for *`color_format`* = *"rgb555le"* is GGGBBBBB|XRRRRRGG.

## Attention

`gen_image_interleaved` does not check whether the
*`pixel_pointer`* is valid or not.
Thus, it must be ensured by the user that it is valid.
Otherwise, the program may crash!

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`image_rgb`** (output_object)  image `→` HObject (byte / uint2)

Created image with new image matrix.

**`pixel_pointer`** (input_control)  pointer `→` int

Pointer to interleaved pixels.

**`color_format`** (input_control)  string `→` str

Format of the input pixels.

Default:
"rgb"

List of values:
"bgr", "bgr48", "bgr555", "bgr5551", "bgr5551be", "bgr5551le", "bgr555be", "bgr555le", "bgr565", "bgr565be", "bgr565le", "bgrx", "bgrx64", "rgb", "rgb48", "rgb555", "rgb5551", "rgb5551be", "rgb5551le", "rgb555be", "rgb555le", "rgb565", "rgb565be", "rgb565le", "rgbx", "rgbx64"

**`original_width`** (input_control)  extent.x `→` int

Width of input image.

Default:
512

Suggested values:
128, 256, 512, 1024

Value range:
`1
≤
original_width` (lin)

Minimum increment:
1

Recommended increment:
10

**`original_height`** (input_control)  extent.y `→` int

Height of input image.

Default:
512

Suggested values:
128, 256, 512, 1024

Value range:
`1
≤
original_height` (lin)

Minimum increment:
1

Recommended increment:
10

**`alignment`** (input_control)  integer `→` int

Reserved.

**`type`** (input_control)  string `→` str

Pixel type of output image.

Default:
"byte"

List of values:
"byte", "uint2"

**`image_width`** (input_control)  rectangle.extent.x `→` int

Width of output image.

Default:
0

Suggested values:
128, 256, 512, 1024

Value range:
`0
≤
image_width` (lin)

Minimum increment:
1

Recommended increment:
10

**`image_height`** (input_control)  rectangle.extent.y `→` int

Height of output image.

Default:
0

Suggested values:
128, 256, 512, 1024

Value range:
`0
≤
image_height` (lin)

Minimum increment:
1

Recommended increment:
10

**`start_row`** (input_control)  rectangle.origin.y `→` int

Line number of upper left corner of desired
image part.

Default:
0

Suggested values:
-1, 0

**`start_column`** (input_control)  rectangle.origin.x `→` int

Column number of upper left corner of desired
image part.

Default:
0

Suggested values:
-1, 0

**`bits_per_channel`** (input_control)  integer `→` int

Number of used bits per pixel and channel of the
output image (-1: All bits are used).

Default:
-1

Suggested values:
5, 8, 10, 12, 16, -1

**`bit_shift`** (input_control)  integer `→` int

Number of bits that the color values of the input
pixels are shifted to the right (only uint2 images).

Default:
0

Suggested values:
0, 2, 4, 6

## Result

If the parameter values are correct, the operator
`gen_image_interleaved` returns the value 2 (
H_MSG_TRUE)
. Otherwise an
exception is raised.

## Possible Successors

`disp_color`

## See also

`reduce_domain`,
`paint_gray`,
`paint_region`,
`set_grayval`,
`gen_image_const`

## Module

Foundation
