# GenImage1Rect (Operator)

## Name

`GenImage1Rect` — Create an image with a rectangular domain from a pointer on the pixels
(with storage management).

## Signature

`static void HOperatorSet.GenImage1Rect(out HObject image, HTuple pixelPointer, HTuple width, HTuple height, HTuple verticalPitch, HTuple horizontalBitPitch, HTuple bitsPerPixel, HTuple doCopy, HTuple clearProc)`

`void HImage.GenImage1Rect(IntPtr pixelPointer, int width, int height, int verticalPitch, int horizontalBitPitch, int bitsPerPixel, string doCopy, IntPtr clearProc)`

## Description

The operator `GenImage1Rect` creates an image of size
(*`verticalPitch`* / (*`horizontalBitPitch`*/8)) * *`height`*.
The pixels pointed to by
*`pixelPointer`* are stored line by line.
Note that how to pass a pointer value depends on the used operator
signature and programming environment. Make sure to pass the
actual memory address where the image data is stored, not the
address of a pointer variable. Care must be taken not to
truncate 64-bit pointers on 64-bit architectures.

*`verticalPitch`* determines the distance (in bytes) between pixel m
in row n and pixel m in row n+1 inside of memory.
All rows of the 'input image' have the same vertical pitch.
The width of the output image is *`verticalPitch`* /
(*`horizontalBitPitch`* / 8), its height is *`height`*.
The domain of the output image *`image`* is a rectangle of the size
*`width`* * *`height`*.
The parameter *`horizontalBitPitch`* is the horizontal distance
(in bits) between two neighboring pixels. *`bitsPerPixel`* is
the number of used bits per pixel.

If *`doCopy`* is set *"true"*, the image data pointed to by
*`pixelPointer`* is copied and memory for the new image is
newly allocated by HALCON.
Else the image data is not duplicated and the memory space that
*`pixelPointer`*
points to must be released when deleting the object *`image`*.
This is done by the procedure *`clearProc`* provided by
the caller. This procedure must have the following signature

```
    void ClearProc(void* ptr);
```

and will be called using `__cdecl` calling convention
when deleting *`image`*.
If the memory shall not be released (in the case of
frame grabbers or static memory) a procedure
”without trunk” or the NULL-pointer can be passed.
Analogously to the parameter *`pixelPointer`* the
pointer has to be passed to the procedure depending on
the used operator signature and programming environment.
If *`doCopy`* is *"true"* then *`clearProc`* is irrelevant.
The operator `GenImage1Rect` is symmetrical to
[`GetImagePointer1Rect`](get_image_pointer1_rect.md).

## Attention

`GenImage1Rect` does not check whether the *`pixelPointer`* is
valid or not. Thus, it must be ensured by the user that it is valid.
Otherwise, the program may crash!

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`image`** (output_object)  image `→` [HImage](HImage.md) (byte / uint2 / int4)

Created HALCON image.

**`pixelPointer`** (input_control)  pointer `→` [HTuple](HTuple.md) (*IntPtr*)

Pointer to the first pixel.

**`width`** (input_control)  extent.x `→` [HTuple](HTuple.md) (*int* / long)

Width of the image.

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

Height of the image.

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

**`verticalPitch`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Distance (in bytes) between pixel m in row n
and pixel m in row n+1 of the 'input image'.

Restriction:
`VerticalPitch >= Width * HorizontalBitPitch / 8`

**`horizontalBitPitch`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Distance between two neighboring pixels in bits .

Default:
8

List of values:
8, 16, 32

**`bitsPerPixel`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Number of used bits per pixel.

Default:
8

List of values:
8, 9, 10, 11, 12, 13, 14, 15, 16, 32

Restriction:
`BitsPerPixel <= HorizontalBitPitch`

**`doCopy`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Copy image data.

Default:
"false"

Suggested values:
"true", "false"

**`clearProc`** (input_control)  pointer `→` [HTuple](HTuple.md) (*IntPtr*)

Pointer to the procedure releasing the memory
of the image when deleting the object.

Default:
0

## Example (C)

```
void NewImage(Hobject *new)
{
  unsigned char       *image;
  int                 r,c;

  image = malloc(640*480);
  for (r=0; r<480; r++)
    for (c=0; c<640; c++)
      image[r*640+c] = c % 255;
  gen_image1_rect(new,(Hlong)image,400,480,640,8,8,'false',(long)free);
}
```

## Result

The operator `GenImage1Rect` returns the value 2 (
H_MSG_TRUE)
if the parameter values are correct.
Otherwise an exception is raised.

## Possible Successors

`GetImagePointer1Rect`

## Alternatives

`GenImage1`,
`GenImage1Extern`,
`GenImageConst`

## See also

`GetImagePointer1Rect`

## Module

Foundation
