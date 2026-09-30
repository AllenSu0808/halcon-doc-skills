# GenImageConst (Operator)

## Name

`GenImageConst` — Create an image with constant gray value.

## Signature

`static void HOperatorSet.GenImageConst(out HObject image, HTuple type, HTuple width, HTuple height)`

`public HImage(string type, int width, int height)`

`void HImage.GenImageConst(string type, int width, int height)`

## Description

The operator `GenImageConst` creates an image of the indicated
size. The width and height of the image are determined by
*`width`* and *`height`*. HALCON supports the following
image types:

- ***"byte"*** —

  1 byte per pixel, unsigned

  Value range:
   (0..255)
- ***"int1"*** —

  1 byte per pixel, signed

  Value range:
   (-128..127)
- ***"uint2"*** —

  2 bytes per pixel, unsigned

  Value range:
   (0..65535)
- ***"int2"*** —

  2 bytes per pixel, signed

  Value range:
   (-32768..32767)
- ***"int4"*** —

  4 bytes per pixel, signed

  Value range:
   (-2147483648..2147483647)
- ***"int8"*** —

  8 bytes per pixel, signed
  (only available on 64 bit systems)

  Value range:
   (-9223372036854775808..9223372036854775807)
- ***"real"*** —

  4 bytes per pixel, floating point

  *Precision:* 6 significant decimal digits

  Value range:
   (-3.4e38..3.4e38)
- ***"complex"*** —

  Two matrices of type *"real"*
- ***"vector_field_relative"*** —

  Two matrices of type *"real"*

  *Interpretation:* Vectors
- ***"vector_field_absolute"*** —

  Two matrices of type *"real"*

  *Interpretation:* Absolute coordinates
- ***"direction"*** —

  1 byte per pixel, unsigned

  *Interpretation:* Angle divided by two

  Value range:
   (0..179)

  Attention:
   The values 180..254 are automatically set to the value
  255, which is interpreted as undefined angle.
- ***"cyclic"*** —

  1 byte per pixel, unsigned, cyclic arithmetics

  Value range:
   (0..255)

With the operator
`set_system('init_new_image',<'true'/'false'>)`, it can be
controlled whether the created image is initialized with 0 or not.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`image`** (output_object)  image `→` [HImage](HImage.md) (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Created image with new image matrix.

**`type`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Pixel type.

Default:
"byte"

List of values:
"byte", "complex", "cyclic", "direction", "int1", "int2", "int4", "int8", "real", "uint2", "vector_field_absolute", "vector_field_relative"

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

## Example (C)

```
gen_image_const(&New,"byte",width,height);
get_image_pointer1(New,(Hlong*)&pointer,type,&width,&height);
for (row=0; row<height-1; row++)
{
  for (col=0; col<width-1; col++)
  {
    pointer[row*width+col] = (row + col) % 256;
  }
}
```

## Result

If the parameter values are correct, the operator `GenImageConst`
returns the value 2 (
H_MSG_TRUE)
. Otherwise an exception is raised.

## Possible Successors

`PaintRegion`,
`ReduceDomain`,
`GetImagePointer1`,
`CopyObj`

## Alternatives

`GenImage1`,
`GenImage3`

## See also

`ReduceDomain`,
`PaintGray`,
`PaintRegion`,
`SetGrayval`,
`GetImagePointer1`

## Module

Foundation
