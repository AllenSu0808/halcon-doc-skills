# gen_image3 (Operator)

## Name

`gen_image3` — Create an image from three pointers to the pixels (red/green/blue).

## Signature

`gen_image3( : ImageRGB : Type, Width, Height, PixelPointerRed, PixelPointerGreen, PixelPointerBlue : )`

## Description

The operator `gen_image3` creates a three-channel image of the
size *`Width`* * *`Height`*.
The pixels in *`PixelPointerRed`*, *`PixelPointerGreen`* and
*`PixelPointerBlue`* are stored line-sequentially.
The type of the given pixels
(*`PixelPointerRed`* etc.) must correspond to *`Type`*
(see [`gen_image_const`](gen_image_const.md) for a more detailed description of the
pixel types).
The storage for the new image is newly created by HALCON.
Thus, it can be released after the call.
Note that how to pass a pointer value depends on the used operator
signature and programming environment. Make sure to pass the
actual memory address where the image data is stored, not the
address of a pointer variable. Care must be taken not to
truncate 64-bit pointers on 64-bit architectures.

## Attention

`gen_image3` does not check whether the pixels in
*`PixelPointerRed`*,*`PixelPointerGreen`*, and
*`PixelPointerBlue`* are valid or not.
Thus, it must be ensured by the user that they are valid.
Otherwise, the program may crash!

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`ImageRGB`** (output_object)  image `→` object (byte / direction / cyclic / int1 / int2 / uint2 / int4 / real)

Created image with new image matrix.

**`Type`** (input_control)  string `→`  (string)

Pixel type.

Default:
'byte'

List of values:
'byte', 'cyclic', 'direction', 'int1', 'int2', 'int4', 'real', 'uint2'

**`Width`** (input_control)  extent.x `→`  (integer)

Width of image.

Default:
512

Suggested values:
128, 256, 512, 1024

Value range:
`1
≤
Width` (lin)

Minimum increment:
1

Recommended increment:
10

**`Height`** (input_control)  extent.y `→`  (integer)

Height of image.

Default:
512

Suggested values:
128, 256, 512, 1024

Value range:
`1
≤
Height` (lin)

Minimum increment:
1

Recommended increment:
10

**`PixelPointerRed`** (input_control)  pointer `→`  (integer)

Pointer to first red value (channel 1).

**`PixelPointerGreen`** (input_control)  pointer `→`  (integer)

Pointer to first green value (channel 2).

**`PixelPointerBlue`** (input_control)  pointer `→`  (integer)

Pointer to first blue value (channel 3).

## Example (C)

```
void NewRGBImage(Hobject *new)
{
  unsigned char  red[768*525];
  unsigned char  green[768*525];
  unsigned char  blue[768*525];
  int            r,c;
  for (r=0; r<525; r++)
    for (c=0; c<768; c++)
    {
      red[r*768+c]   = c % 255;
      green[r*768+c] = (767 - c) % 255;
      blue[r*768+c]  = r % 255;
    }
    gen_image3(new,"byte",768,525,(Hlong)red,(long)green,(long)blue);
}

main()
{
  Hobject  rgb;
  open_window(0,0,768,525,0,"","",&WindowHandle);
  NewRGBImage(&rgb);
  disp_color(rgb,WindowHandle);
}
```

## Result

If the parameter values are correct, the operator `gen_image3`
returns the value 2 (
H_MSG_TRUE)
.
Otherwise an exception is raised.

## Possible Predecessors

`gen_image_const`,
`get_image_pointer1`

## Possible Successors

`disp_color`

## Alternatives

`gen_image1`,
`compose3`,
`gen_image_const`

## See also

`reduce_domain`,
`paint_gray`,
`paint_region`,
`set_grayval`,
`get_image_pointer1`,
`decompose3`

## Module

Foundation
