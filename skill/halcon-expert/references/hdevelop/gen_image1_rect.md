# gen_image1_rect (Operator)

## Name

`gen_image1_rect` — Create an image with a rectangular domain from a pointer on the pixels
(with storage management).

## Signature

`gen_image1_rect( : Image : PixelPointer, Width, Height, VerticalPitch, HorizontalBitPitch, BitsPerPixel, DoCopy, ClearProc : )`

## Description

The operator `gen_image1_rect` creates an image of size
(*`VerticalPitch`* / (*`HorizontalBitPitch`*/8)) * *`Height`*.
The pixels pointed to by
*`PixelPointer`* are stored line by line.
Note that how to pass a pointer value depends on the used operator
signature and programming environment. Make sure to pass the
actual memory address where the image data is stored, not the
address of a pointer variable. Care must be taken not to
truncate 64-bit pointers on 64-bit architectures.

*`VerticalPitch`* determines the distance (in bytes) between pixel m
in row n and pixel m in row n+1 inside of memory.
All rows of the 'input image' have the same vertical pitch.
The width of the output image is *`VerticalPitch`* /
(*`HorizontalBitPitch`* / 8), its height is *`Height`*.
The domain of the output image *`Image`* is a rectangle of the size
*`Width`* * *`Height`*.
The parameter *`HorizontalBitPitch`* is the horizontal distance
(in bits) between two neighboring pixels. *`BitsPerPixel`* is
the number of used bits per pixel.

If *`DoCopy`* is set *'true'*, the image data pointed to by
*`PixelPointer`* is copied and memory for the new image is
newly allocated by HALCON.
Else the image data is not duplicated and the memory space that
*`PixelPointer`*
points to must be released when deleting the object *`Image`*.
This is done by the procedure *`ClearProc`* provided by
the caller. This procedure must have the following signature

```
    void ClearProc(void* ptr);
```

and will be called using `__cdecl` calling convention
when deleting *`Image`*.
If the memory shall not be released (in the case of
frame grabbers or static memory) a procedure
”without trunk” or the NULL-pointer can be passed.
Analogously to the parameter *`PixelPointer`* the
pointer has to be passed to the procedure depending on
the used operator signature and programming environment.
If *`DoCopy`* is *'true'* then *`ClearProc`* is irrelevant.
The operator `gen_image1_rect` is symmetrical to
[`get_image_pointer1_rect`](get_image_pointer1_rect.md).

## Attention

`gen_image1_rect` does not check whether the *`PixelPointer`* is
valid or not. Thus, it must be ensured by the user that it is valid.
Otherwise, the program may crash!

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Image`** (output_object)  image `→` object (byte / uint2 / int4)

Created HALCON image.

**`PixelPointer`** (input_control)  pointer `→`  (integer)

Pointer to the first pixel.

**`Width`** (input_control)  extent.x `→`  (integer)

Width of the image.

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

Height of the image.

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

**`VerticalPitch`** (input_control)  integer `→`  (integer)

Distance (in bytes) between pixel m in row n
and pixel m in row n+1 of the 'input image'.

Restriction:
`VerticalPitch >= Width * HorizontalBitPitch / 8`

**`HorizontalBitPitch`** (input_control)  integer `→`  (integer)

Distance between two neighboring pixels in bits .

Default:
8

List of values:
8, 16, 32

**`BitsPerPixel`** (input_control)  integer `→`  (integer)

Number of used bits per pixel.

Default:
8

List of values:
8, 9, 10, 11, 12, 13, 14, 15, 16, 32

Restriction:
`BitsPerPixel <= HorizontalBitPitch`

**`DoCopy`** (input_control)  string `→`  (string)

Copy image data.

Default:
'false'

Suggested values:
'true', 'false'

**`ClearProc`** (input_control)  pointer `→`  (integer)

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

The operator `gen_image1_rect` returns the value 2 (
H_MSG_TRUE)
if the parameter values are correct.
Otherwise an exception is raised.

## Possible Successors

`get_image_pointer1_rect`

## Alternatives

`gen_image1`,
`gen_image1_extern`,
`gen_image_const`

## See also

`get_image_pointer1_rect`

## Module

Foundation
