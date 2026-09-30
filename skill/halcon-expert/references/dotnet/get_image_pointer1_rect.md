# GetImagePointer1Rect (Operator)

## Name

`GetImagePointer1Rect` — Access to the image data pointer and the image data inside
the smallest rectangle of the domain of the input image.

## Signature

`static void HOperatorSet.GetImagePointer1Rect(HObject image, out HTuple pixelPointer, out HTuple width, out HTuple height, out HTuple verticalPitch, out HTuple horizontalBitPitch, out HTuple bitsPerPixel)`

`IntPtr HImage.GetImagePointer1Rect(out int width, out int height, out int verticalPitch, out int horizontalBitPitch, out int bitsPerPixel)`

## Description

The operator `GetImagePointer1Rect` returns the pointer
*`pixelPointer`* which points to the beginning of the image
data inside the smallest rectangle of the domain of *`image`*.
*`verticalPitch`* corresponds to the width of the input image
*`image`* multiplied with the number of bytes per pixel
(*`horizontalBitPitch`* / 8). *`width`* and
*`height`* correspond to the size of the smallest rectangle of
the input region. *`horizontalBitPitch`* is the horizontal
distance (in bits) between two neighboring pixels.
*`bitsPerPixel`* is the number of used bits per pixel.
`GetImagePointer1Rect` is symmetrical to
[`GenImage1Rect`](gen_image1_rect.md).

## Attention

The operator `GetImagePointer1Rect` should only be used for entry
into newly created images, since otherwise the gray values of other images
might be overwritten (see relational structure).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`image`** (input_object)  singlechannelimage `→` [HImage](HImage.md) (byte / uint2 / int4)

Input image (HImage).

**`pixelPointer`** (output_control)  pointer `→` [HTuple](HTuple.md) (*IntPtr*)

Pointer to the image data.

**`width`** (output_control)  extent.x `→` [HTuple](HTuple.md) (*int* / long)

Width of the output image.

**`height`** (output_control)  extent.y `→` [HTuple](HTuple.md) (*int* / long)

Height of the output image.

**`verticalPitch`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Width(input image)*(HorizontalBitPitch/8).

**`horizontalBitPitch`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Distance between two neighboring pixels in bits .

**`bitsPerPixel`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

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

The operator `GetImagePointer1Rect` returns the value 2 (
H_MSG_TRUE)
if
exactly one image was passed.
The behavior in case of empty input (no input images available) is set via
the operator `set_system('no_object_result',<Result>)`.
If necessary an exception is raised.

## Possible Predecessors

`ReadImage`,
`GenImage1Rect`

## Alternatives

`SetGrayval`,
`GetGrayval`,
`GetImagePointer3`,
`GetImagePointer1`

## See also

`PaintRegion`,
`PaintGray`,
`GenImage1Rect`

## Module

Foundation
