# gen_image3_extern (Operator)

## Name

`gen_image3_extern` — Create a three-channel image from three pointers on the pixels with storage
management.

## Signature

`def gen_image3_extern(type: str, width: int, height: int, pointer_red: int, pointer_green: int, pointer_blue: int, clear_proc: int) -> HObject`

## Description

The operator `gen_image3_extern` creates a three-channel image of the
size *`width`* * *`height`*.
The pixels in *`pointer_red`*, *`pointer_green`*, and
*`pointer_blue`* are stored line-sequentially.
The type of the given pixels must correspond to *`type`*
(see [`gen_image_const`](gen_image_const.md) for a more detailed description of the
image types).
Note that how to pass a pointer value depends on the used operator
signature and programming environment. Make sure to pass the
actual memory address where the image data is stored, not the
address of a pointer variable. Care must be taken not to
truncate 64-bit pointers on 64-bit architectures.

The memory for the new image is not newly allocated
by HALCON,
contrary to [`gen_image3`](gen_image3.md), and thus is not copied either.
This means that the memory space that *`pointer_red`*,
*`pointer_green`*, and *`pointer_blue`* point
to must be released by deleting the object *`image`*.
This is done by the procedure *`clear_proc`* provided by
the caller. This procedure must have the following signature

```
    void ClearProc(void* ptr);
```

and will be called using `__cdecl` calling convention
when deleting *`image`*.
If the memory shall not be released (in the case of
frame grabbers or static memory) a procedure
“without trunk” or the NULL-Pointer can be passed.
Analogous to the parameters *`pointer_red`*, *`pointer_green`*,
and *`pointer_blue`* the
pointer has to be passed to the procedure depending
on the used operator signature and programming environment.

## Attention

`gen_image3_extern` does not check if enough memory for an image of
*`width`* * *`height`* is allocated in
*`pointer_red`*, *`pointer_green`*, and *`pointer_blue`*.

Also, `gen_image3_extern` does not check whether the pixels in
*`pointer_red`*, *`pointer_green`*, and *`pointer_blue`* are
valid or not.
Thus, it must be ensured by the user that they are valid.
Otherwise, the program may crash!

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`image`** (output_object)  image `→` HObject (byte / direction / cyclic / int1 / int2 / uint2 / int4 / real)

Created HALCON image.

**`type`** (input_control)  string `→` str

Pixel type.

Default:
"byte"

List of values:
"byte", "cyclic", "direction", "int1", "int2", "int4", "real", "uint2"

**`width`** (input_control)  extent.x `→` int

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

**`height`** (input_control)  extent.y `→` int

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

**`pointer_red`** (input_control)  pointer `→` int

Pointer to the first gray value of the first channel.

**`pointer_green`** (input_control)  pointer `→` int

Pointer to the first gray value of the second channel.

**`pointer_blue`** (input_control)  pointer `→` int

Pointer to the first gray value of the third channel.

**`clear_proc`** (input_control)  pointer `→` int

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

The operator `gen_image3_extern` returns the value 2 (
H_MSG_TRUE)
if the parameter values are correct.
Otherwise an exception is raised.

## Alternatives

`gen_image3`,
`gen_image_const`,
`get_image_pointer3`,
`gen_image1_extern`

## See also

`reduce_domain`,
`paint_gray`,
`paint_region`,
`set_grayval`

## Module

Foundation
