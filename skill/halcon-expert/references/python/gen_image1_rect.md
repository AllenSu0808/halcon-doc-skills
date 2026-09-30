# gen_image1_rect (Operator)

## Name

`gen_image1_rect` — Create an image with a rectangular domain from a pointer on the pixels
(with storage management).

## Signature

`def gen_image1_rect(pixel_pointer: int, width: int, height: int, vertical_pitch: int, horizontal_bit_pitch: int, bits_per_pixel: int, do_copy: str, clear_proc: int) -> HObject`

## Description

The operator `gen_image1_rect` creates an image of size
(*`vertical_pitch`* / (*`horizontal_bit_pitch`*/8)) * *`height`*.
The pixels pointed to by
*`pixel_pointer`* are stored line by line.
Note that how to pass a pointer value depends on the used operator
signature and programming environment. Make sure to pass the
actual memory address where the image data is stored, not the
address of a pointer variable. Care must be taken not to
truncate 64-bit pointers on 64-bit architectures.

*`vertical_pitch`* determines the distance (in bytes) between pixel m
in row n and pixel m in row n+1 inside of memory.
All rows of the 'input image' have the same vertical pitch.
The width of the output image is *`vertical_pitch`* /
(*`horizontal_bit_pitch`* / 8), its height is *`height`*.
The domain of the output image *`image`* is a rectangle of the size
*`width`* * *`height`*.
The parameter *`horizontal_bit_pitch`* is the horizontal distance
(in bits) between two neighboring pixels. *`bits_per_pixel`* is
the number of used bits per pixel.

If *`do_copy`* is set *"true"*, the image data pointed to by
*`pixel_pointer`* is copied and memory for the new image is
newly allocated by HALCON.
Else the image data is not duplicated and the memory space that
*`pixel_pointer`*
points to must be released when deleting the object *`image`*.
This is done by the procedure *`clear_proc`* provided by
the caller. This procedure must have the following signature

```
    void ClearProc(void* ptr);
```

and will be called using `__cdecl` calling convention
when deleting *`image`*.
If the memory shall not be released (in the case of
frame grabbers or static memory) a procedure
”without trunk” or the NULL-pointer can be passed.
Analogously to the parameter *`pixel_pointer`* the
pointer has to be passed to the procedure depending on
the used operator signature and programming environment.
If *`do_copy`* is *"true"* then *`clear_proc`* is irrelevant.
The operator `gen_image1_rect` is symmetrical to
[`get_image_pointer1_rect`](get_image_pointer1_rect.md).

## Attention

`gen_image1_rect` does not check whether the *`pixel_pointer`* is
valid or not. Thus, it must be ensured by the user that it is valid.
Otherwise, the program may crash!

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`image`** (output_object)  image `→` HObject (byte / uint2 / int4)

Created HALCON image.

**`pixel_pointer`** (input_control)  pointer `→` int

Pointer to the first pixel.

**`width`** (input_control)  extent.x `→` int

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

**`height`** (input_control)  extent.y `→` int

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

**`vertical_pitch`** (input_control)  integer `→` int

Distance (in bytes) between pixel m in row n
and pixel m in row n+1 of the 'input image'.

Restriction:
`VerticalPitch >= Width * HorizontalBitPitch / 8`

**`horizontal_bit_pitch`** (input_control)  integer `→` int

Distance between two neighboring pixels in bits .

Default:
8

List of values:
8, 16, 32

**`bits_per_pixel`** (input_control)  integer `→` int

Number of used bits per pixel.

Default:
8

List of values:
8, 9, 10, 11, 12, 13, 14, 15, 16, 32

Restriction:
`BitsPerPixel <= HorizontalBitPitch`

**`do_copy`** (input_control)  string `→` str

Copy image data.

Default:
"false"

Suggested values:
"true", "false"

**`clear_proc`** (input_control)  pointer `→` int

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
