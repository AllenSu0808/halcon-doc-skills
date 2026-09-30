# get_image_pointer1_rect (Operator)

## Name

`get_image_pointer1_rect` — Access to the image data pointer and the image data inside
the smallest rectangle of the domain of the input image.

## Signature

`get_image_pointer1_rect(Image : : : PixelPointer, Width, Height, VerticalPitch, HorizontalBitPitch, BitsPerPixel)`

## Description

The operator `get_image_pointer1_rect` returns the pointer
*`PixelPointer`* which points to the beginning of the image
data inside the smallest rectangle of the domain of *`Image`*.
*`VerticalPitch`* corresponds to the width of the input image
*`Image`* multiplied with the number of bytes per pixel
(*`HorizontalBitPitch`* / 8). *`Width`* and
*`Height`* correspond to the size of the smallest rectangle of
the input region. *`HorizontalBitPitch`* is the horizontal
distance (in bits) between two neighboring pixels.
*`BitsPerPixel`* is the number of used bits per pixel.
`get_image_pointer1_rect` is symmetrical to
[`gen_image1_rect`](gen_image1_rect.md).

## Attention

The operator `get_image_pointer1_rect` should only be used for entry
into newly created images, since otherwise the gray values of other images
might be overwritten (see relational structure).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Image`** (input_object)  singlechannelimage `→` object (byte / uint2 / int4)

Input image (HImage).

**`PixelPointer`** (output_control)  pointer `→`  (integer)

Pointer to the image data.

**`Width`** (output_control)  extent.x `→`  (integer)

Width of the output image.

**`Height`** (output_control)  extent.y `→`  (integer)

Height of the output image.

**`VerticalPitch`** (output_control)  integer `→`  (integer)

Width(input image)*(HorizontalBitPitch/8).

**`HorizontalBitPitch`** (output_control)  integer `→`  (integer)

Distance between two neighboring pixels in bits .

**`BitsPerPixel`** (output_control)  integer `→`  (integer)

Number of used bits per pixel.

## Example (C)

```
Hobject       image,reg,imagereduced;
char          typ[128];
Hlong          width,height,vert_pitch,hori_bit_pitch,bits_per_pix, winID;
unsigned char *ptr;

open_window(0,0,512,512,"black",winID);
read_image(&image,"monkey");
draw_region(&reg,winID);
reduce_domain(image,reg,&imagereduced);
get_image_pointer1_rect(imagereduced,(Hlong*)&ptr,&width,&height,
                        &vert_pitch,&hori_bit_pitch,&bits_per_pix);
```

## Result

The operator `get_image_pointer1_rect` returns the value 2 (
H_MSG_TRUE)
if
exactly one image was passed.
The behavior in case of empty input (no input images available) is set via
the operator `set_system('no_object_result',<Result>)`.
If necessary an exception is raised.

## Possible Predecessors

`read_image`,
`gen_image1_rect`

## Alternatives

`set_grayval`,
`get_grayval`,
`get_image_pointer3`,
`get_image_pointer1`

## See also

`paint_region`,
`paint_gray`,
`gen_image1_rect`

## Module

Foundation
