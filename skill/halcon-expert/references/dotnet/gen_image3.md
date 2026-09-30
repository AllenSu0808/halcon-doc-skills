# GenImage3 (Operator)

## Name

`GenImage3` — Create an image from three pointers to the pixels (red/green/blue).

## Signature

`static void HOperatorSet.GenImage3(out HObject imageRGB, HTuple type, HTuple width, HTuple height, HTuple pixelPointerRed, HTuple pixelPointerGreen, HTuple pixelPointerBlue)`

`void HImage.GenImage3(string type, int width, int height, IntPtr pixelPointerRed, IntPtr pixelPointerGreen, IntPtr pixelPointerBlue)`

## Description

The operator `GenImage3` creates a three-channel image of the
size *`width`* * *`height`*.
The pixels in *`pixelPointerRed`*, *`pixelPointerGreen`* and
*`pixelPointerBlue`* are stored line-sequentially.
The type of the given pixels
(*`pixelPointerRed`* etc.) must correspond to *`type`*
(see [`GenImageConst`](gen_image_const.md) for a more detailed description of the
pixel types).
The storage for the new image is newly created by HALCON.
Thus, it can be released after the call.
Note that how to pass a pointer value depends on the used operator
signature and programming environment. Make sure to pass the
actual memory address where the image data is stored, not the
address of a pointer variable. Care must be taken not to
truncate 64-bit pointers on 64-bit architectures.

## Attention

`GenImage3` does not check whether the pixels in
*`pixelPointerRed`*,*`pixelPointerGreen`*, and
*`pixelPointerBlue`* are valid or not.
Thus, it must be ensured by the user that they are valid.
Otherwise, the program may crash!

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`imageRGB`** (output_object)  image `→` [HImage](HImage.md) (byte / direction / cyclic / int1 / int2 / uint2 / int4 / real)

Created image with new image matrix.

**`type`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Pixel type.

Default:
"byte"

List of values:
"byte", "cyclic", "direction", "int1", "int2", "int4", "real", "uint2"

**`width`** (input_control)  extent.x `→` [HTuple](HTuple.md) (*int* / long)

Width of image.

Default:
512

Suggested values:
128, 256, 512, 1024

Value range:
`1
≤
width` (lin)

Minimum increment:
1

Recommended increment:
10

**`height`** (input_control)  extent.y `→` [HTuple](HTuple.md) (*int* / long)

Height of image.

Default:
512

Suggested values:
128, 256, 512, 1024

Value range:
`1
≤
height` (lin)

Minimum increment:
1

Recommended increment:
10

**`pixelPointerRed`** (input_control)  pointer `→` [HTuple](HTuple.md) (*IntPtr*)

Pointer to first red value (channel 1).

**`pixelPointerGreen`** (input_control)  pointer `→` [HTuple](HTuple.md) (*IntPtr*)

Pointer to first green value (channel 2).

**`pixelPointerBlue`** (input_control)  pointer `→` [HTuple](HTuple.md) (*IntPtr*)

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

If the parameter values are correct, the operator `GenImage3`
returns the value 2 (
H_MSG_TRUE)
.
Otherwise an exception is raised.

## Possible Predecessors

`GenImageConst`,
`GetImagePointer1`

## Possible Successors

`DispColor`

## Alternatives

`GenImage1`,
`Compose3`,
`GenImageConst`

## See also

`ReduceDomain`,
`PaintGray`,
`PaintRegion`,
`SetGrayval`,
`GetImagePointer1`,
`Decompose3`

## Module

Foundation
