# get_image_pointer1 (Operator)

## Name

`get_image_pointer1` — Access the pointer of a channel.

## Signature

`get_image_pointer1(Image : : : Pointer, Type, Width, Height)`

## Description

The operator `get_image_pointer1` returns a pointer to the
first channel of the image *`Image`*. Additionally, the image
type (*`Type`* = 'byte', 'int2', 'uint2', etc.) and the image
size (width and height) are returned. Consequently, a direct access
to the image data in the HALCON database via the pointer is
possible from the programming language in which HALCON is used.
An image is stored in HALCON linearized in row major order, i.e.,
line by line. Note that the image types 'complex' and 'vector_type'
are handled in a specific way. In particular, 'complex' images are
interleaved, i.e., the real and the imaginary parts are alternating.
In contrast, 'vector_field' images consist of two matrices, one for
the rows and one for the columns, which are stored in the HALCON database
one after the other.

## Attention

The pointer returned by `get_image_pointer1` may only be used
as long as the corresponding image object exists in the HALCON
database. This is the case as long as the corresponding variable in
the programming language in which HALCON is used is valid. If
this is not observed, unexpected behavior or program crashes may
result.

If data is written to an existing image via the pointer, all image
objects that reference the image are modified. If, for example, the
domain of an image is restricted via [`reduce_domain`](reduce_domain.md), the
original image object with the full domain and the image object with
the reduced domain share the same image matrix (i.e.,
`get_image_pointer1` returns the same pointer for both
images). Consequently, if one of the two images in this example is
modified, both image objects are affected. Therefore, if the
pointer is used to write image data in the programming language
in which HALCON is used, the image data should be written into an
image object that has been created solely for this purpose, e.g.,
using [`gen_image1`](gen_image1.md).
For multi-channel input images the type and the pointer of the first channel
is returned.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Image`** (input_object)  singlechannelimage(-array) `→` object (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Input image.

**`Pointer`** (output_control)  pointer(-array) `→`  (integer)

Pointer to the image data in the HALCON database.

**`Type`** (output_control)  string(-array) `→`  (string)

Type of image.

List of values:
'byte', 'complex', 'cyclic', 'direction', 'int1', 'int2', 'int4', 'int8', 'real', 'uint2', 'vector_field_absolute', 'vector_field_relative'

**`Width`** (output_control)  extent.x(-array) `→`  (integer)

Width of image.

**`Height`** (output_control)  extent.y(-array) `→`  (integer)

Height of image.

## Example (C)

```
Hobject  Image;
char     typ[128];
Hlong     width,height;
unsigned char *ptr;

read_image(&Image,"fabrik");
get_image_pointer1(Image,(Hlong*)&ptr,typ,&width,&height);
```

## Result

The operator `get_image_pointer1` returns the value 2 (
H_MSG_TRUE)
if
exactly one image was passed.
The behavior in case of empty input (no input images available) is set via
the operator `set_system('no_object_result',<Result>)`.
If necessary an exception is raised.

## Possible Predecessors

`read_image`

## Alternatives

`set_grayval`,
`get_grayval`,
`get_image_pointer3`,
`get_image_size`,
`get_image_type`

## See also

`paint_region`,
`paint_gray`

## Module

Foundation
