# get_image_pointer1_rect (Operator)

## Name

`get_image_pointer1_rect` — Access to the image data pointer and the image data inside
the smallest rectangle of the domain of the input image.

## Signature

`def get_image_pointer1_rect(image: HObject) -> Tuple[int, int, int, int, int, int]`

## Description

The operator `get_image_pointer1_rect` returns the pointer
*`pixel_pointer`* which points to the beginning of the image
data inside the smallest rectangle of the domain of *`image`*.
*`vertical_pitch`* corresponds to the width of the input image
*`image`* multiplied with the number of bytes per pixel
(*`horizontal_bit_pitch`* / 8). *`width`* and
*`height`* correspond to the size of the smallest rectangle of
the input region. *`horizontal_bit_pitch`* is the horizontal
distance (in bits) between two neighboring pixels.
*`bits_per_pixel`* is the number of used bits per pixel.
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

**`image`** (input_object)  singlechannelimage `→` HObject (byte / uint2 / int4)

Input image (HImage).

**`pixel_pointer`** (output_control)  pointer `→` int

Pointer to the image data.

**`width`** (output_control)  extent.x `→` int

Width of the output image.

**`height`** (output_control)  extent.y `→` int

Height of the output image.

**`vertical_pitch`** (output_control)  integer `→` int

Width(input image)*(HorizontalBitPitch/8).

**`horizontal_bit_pitch`** (output_control)  integer `→` int

Distance between two neighboring pixels in bits .

**`bits_per_pixel`** (output_control)  integer `→` int

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
