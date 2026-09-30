# GenImage3Extern (Operator)

## Name

`GenImage3Extern` — Create a three-channel image from three pointers on the pixels with storage
management.

## Signature

`static void HOperatorSet.GenImage3Extern(out HObject image, HTuple type, HTuple width, HTuple height, HTuple pointerRed, HTuple pointerGreen, HTuple pointerBlue, HTuple clearProc)`

`void HImage.GenImage3Extern(string type, int width, int height, IntPtr pointerRed, IntPtr pointerGreen, IntPtr pointerBlue, IntPtr clearProc)`

## Description

The operator `GenImage3Extern` creates a three-channel image of the
size *`width`* * *`height`*.
The pixels in *`pointerRed`*, *`pointerGreen`*, and
*`pointerBlue`* are stored line-sequentially.
The type of the given pixels must correspond to *`type`*
(see [`GenImageConst`](gen_image_const.md) for a more detailed description of the
image types).
Note that how to pass a pointer value depends on the used operator
signature and programming environment. Make sure to pass the
actual memory address where the image data is stored, not the
address of a pointer variable. Care must be taken not to
truncate 64-bit pointers on 64-bit architectures.

The memory for the new image is not newly allocated
by HALCON,
contrary to [`GenImage3`](gen_image3.md), and thus is not copied either.
This means that the memory space that *`pointerRed`*,
*`pointerGreen`*, and *`pointerBlue`* point
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
Analogous to the parameters *`pointerRed`*, *`pointerGreen`*,
and *`pointerBlue`* the
pointer has to be passed to the procedure depending
on the used operator signature and programming environment.

## Attention

`GenImage3Extern` does not check if enough memory for an image of
*`width`* * *`height`* is allocated in
*`pointerRed`*, *`pointerGreen`*, and *`pointerBlue`*.

Also, `GenImage3Extern` does not check whether the pixels in
*`pointerRed`*, *`pointerGreen`*, and *`pointerBlue`* are
valid or not.
Thus, it must be ensured by the user that they are valid.
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

**`pointerRed`** (input_control)  pointer `→` [HTuple](HTuple.md) (*IntPtr*)

Pointer to the first gray value of the first channel.

**`pointerGreen`** (input_control)  pointer `→` [HTuple](HTuple.md) (*IntPtr*)

Pointer to the first gray value of the second channel.

**`pointerBlue`** (input_control)  pointer `→` [HTuple](HTuple.md) (*IntPtr*)

Pointer to the first gray value of the third channel.

**`clearProc`** (input_control)  pointer `→` [HTuple](HTuple.md) (*IntPtr*)

Pointer to the procedure re-releasing the memory
of the image when deleting the object.

Default:
0

## Example (C)

```
void NewImage(Hobject *new)
{
  unsigned char  *image_red;
  unsigned char  *image_green;
  unsigned char  *image_blue;
  int            r,c;
  image_red = malloc(640*480);
  image_green = malloc(640*480);
  image_blue = malloc(640*480);
  for (r=0; r<480; r++)
    for (c=0; c<640; c++)
    {
      image_red[r*640+c] = c % 255;
      image_green[r*640+c] = (c+64) % 255;
      image_blue[r*640+c] = (c+128) % 255;
    }
  gen_image3_extern(new,"byte",640,480,(Hlong)image_red,\
(Hlong)image_green,(Hlong)image_blue,(Hlong)free);
}
```

## Result

The operator `GenImage3Extern` returns the value 2 (
H_MSG_TRUE)
if the parameter values are correct.
Otherwise an exception is raised.

## Alternatives

`GenImage3`,
`GenImageConst`,
`GetImagePointer3`,
`GenImage1Extern`

## See also

`ReduceDomain`,
`PaintGray`,
`PaintRegion`,
`SetGrayval`

## Module

Foundation
