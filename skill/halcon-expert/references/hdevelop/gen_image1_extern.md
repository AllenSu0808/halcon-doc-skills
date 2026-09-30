# gen_image1_extern (Operator)

## Name

`gen_image1_extern` — Create an image from a pointer on the pixels with storage management.

## Signature

`gen_image1_extern( : Image : Type, Width, Height, PixelPointer, ClearProc : )`

## Description

The operator `gen_image1_extern` creates an image of the size
*`Width`* * *`Height`*.
The pixels in *`PixelPointer`* are stored line-sequentially.
The type of the given pixels
(*`PixelPointer`*) must correspond to *`Type`*
(see [`gen_image_const`](gen_image_const.md) for a more detailed description of the
image types).
Note that how to pass a pointer value depends on the used operator
signature and programming environment. Make sure to pass the
actual memory address where the image data is stored, not the
address of a pointer variable. Care must be taken not to
truncate 64-bit pointers on 64-bit architectures.

The memory for the new image is not newly allocated
by HALCON,
contrary to [`gen_image1`](gen_image1.md), and thus is not copied either.
This means that the memory space that *`PixelPointer`* points
to must be released by deleting the object *`Image`*.
This is done by the procedure *`ClearProc`* provided by
the caller. This procedure must have the following signature

```
    void ClearProc(void* ptr);
```

and will be called using `__cdecl` calling convention
when deleting *`Image`*.
If the memory shall not be released (in the case of
frame grabbers or static memory) a procedure
“without trunk” or the NULL-Pointer can be passed.
Analogous to the parameter *`PixelPointer`* the
pointer has to be passed to the procedure depending
on the used operator signature and programming environment.

## Attention

`gen_image1_extern` does not check if enough memory for an image of
*`Width`* * *`Height`* is allocated in
*`PixelPointer`*.

Also, `gen_image1_extern` does not check whether the
*`PixelPointer`* is valid or not.
Thus, it must be ensured by the user that it is valid.
Otherwise, the program may crash!

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Image`** (output_object)  image `→` object (byte / direction / cyclic / int1 / int2 / uint2 / int4 / real)

Created HALCON image.

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

**`PixelPointer`** (input_control)  pointer `→`  (integer)

Pointer to the first gray value.

**`ClearProc`** (input_control)  pointer `→`  (integer)

Pointer to the procedure re-releasing the memory
of the image when deleting the object.

Default:
0

## Example (C)

```
void NewImage(Hobject *new)
{
  unsigned char  *image;
  int            r,c;
  image = malloc(640*480);
  for (r=0; r<480; r++)
    for (c=0; c<640; c++)
      image[r*640+c] = c % 255;
  gen_image1_extern(new,"byte",640,480,(Hlong)image,(Hlong)free);
}
```

## Result

The operator `gen_image1_extern` returns the value 2 (
H_MSG_TRUE)
if the parameter values are correct.
Otherwise an exception is raised.

## Alternatives

`gen_image1`,
`gen_image_const`,
`get_image_pointer1`,
`gen_image3_extern`

## See also

`reduce_domain`,
`paint_gray`,
`paint_region`,
`set_grayval`

## Module

Foundation
