# GenImage1 (Operator)

## Name

`GenImage1` — Create an image from a pointer to the pixels.

## Signature

`static void HOperatorSet.GenImage1(out HObject image, HTuple type, HTuple width, HTuple height, HTuple pixelPointer)`

`public HImage(string type, int width, int height, IntPtr pixelPointer)`

`void HImage.GenImage1(string type, int width, int height, IntPtr pixelPointer)`

## Description

The operator `GenImage1` creates an image of the size
*`width`* * *`height`*.
The pixels in *`pixelPointer`* are stored line-sequentially.
The type of the given pixels (*`pixelPointer`*) must correspond
to *`type`* (see [`GenImageConst`](gen_image_const.md) for a more detailed
description of the pixel types).
The storage for the new image is newly created by HALCON.
Thus, the storage on the *`pixelPointer`* can be released
after the call.
Note that how to pass a pointer value depends on the used operator
signature and programming environment. Make sure to pass the
actual memory address where the image data is stored, not the
address of a pointer variable. Care must be taken not to
truncate 64-bit pointers on 64-bit architectures.

## Attention

`GenImage1` does not check whether the *`pixelPointer`* is
valid or not. Thus, it must be ensured by the user that it is valid.
Otherwise, the program may crash!

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`image`** (output_object)  image `→` [HImage](HImage.md) (byte / direction / cyclic / int1 / int2 / uint2 / int4 / real)

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

**`pixelPointer`** (input_control)  pointer `→` [HTuple](HTuple.md) (*IntPtr*)

Pointer to first gray value.

## Example (C)

```
void NewImage(Hobject *new)
{
  unsigned char  image[768*525];
  int            r,c;
  for (r=0; r<525; r++)
    for (c=0; c<768; c++)
      image[r*768+c] = c % 255;
  gen_image1(new,"byte",768,525,(Hlong)image);
}
```

## Result

If the parameter values are correct, the operator `GenImage1`
returns the value 2 (
H_MSG_TRUE)
.
Otherwise an exception is raised.

## Possible Predecessors

`GenImageConst`,
`GetImagePointer1`

## Alternatives

`GenImage3`,
`GenImage1Extern`,
`GenImageConst`,
`GetImagePointer1`

## See also

`ReduceDomain`,
`PaintGray`,
`PaintRegion`,
`SetGrayval`

## Module

Foundation
