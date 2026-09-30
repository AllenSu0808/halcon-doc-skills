# GenImage1Extern (Operator)

## Name

`GenImage1Extern` — Create an image from a pointer on the pixels with storage management.

## Signature

`static void HOperatorSet.GenImage1Extern(out HObject image, HTuple type, HTuple width, HTuple height, HTuple pixelPointer, HTuple clearProc)`

`void HImage.GenImage1Extern(string type, int width, int height, IntPtr pixelPointer, IntPtr clearProc)`

## Description

The operator `GenImage1Extern` creates an image of the size
*`width`* * *`height`*.
The pixels in *`pixelPointer`* are stored line-sequentially.
The type of the given pixels
(*`pixelPointer`*) must correspond to *`type`*
(see [`GenImageConst`](gen_image_const.md) for a more detailed description of the
image types).
Note that how to pass a pointer value depends on the used operator
signature and programming environment. Make sure to pass the
actual memory address where the image data is stored, not the
address of a pointer variable. Care must be taken not to
truncate 64-bit pointers on 64-bit architectures.

The memory for the new image is not newly allocated
by HALCON,
contrary to [`GenImage1`](gen_image1.md), and thus is not copied either.
This means that the memory space that *`pixelPointer`* points
to must be released by deleting the object *`image`*.
This is done by the procedure *`clearProc`* provided by
the caller. This procedure must have the following signature

```
    void ClearProc(void* ptr);
```

and will be called using `__cdecl` calling convention
when deleting *`image`*.
If the memory shall not be released (in the case of
frame grabbers or static memory) a procedure
“without trunk” or the NULL-Pointer can be passed.
Analogous to the parameter *`pixelPointer`* the
pointer has to be passed to the procedure depending
on the used operator signature and programming environment.

## Attention

`GenImage1Extern` does not check if enough memory for an image of
*`width`* * *`height`* is allocated in
*`pixelPointer`*.

Also, `GenImage1Extern` does not check whether the
*`pixelPointer`* is valid or not.
Thus, it must be ensured by the user that it is valid.
Otherwise, the program may crash!

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`image`** (output_object)  image `→` [HImage](HImage.md) (byte / direction / cyclic / int1 / int2 / uint2 / int4 / real)

Created HALCON image.

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

Pointer to the first gray value.

**`clearProc`** (input_control)  pointer `→` [HTuple](HTuple.md) (*IntPtr*)

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

The operator `GenImage1Extern` returns the value 2 (
H_MSG_TRUE)
if the parameter values are correct.
Otherwise an exception is raised.

## Alternatives

`GenImage1`,
`GenImageConst`,
`GetImagePointer1`,
`GenImage3Extern`

## See also

`ReduceDomain`,
`PaintGray`,
`PaintRegion`,
`SetGrayval`

## Module

Foundation
