# gen_image_proto (Operator)

## Name

`gen_image_proto` — Create an image with a specified constant gray value.

## Signature

`gen_image_proto(Image : ImageCleared : Grayval : )`

## Description

`gen_image_proto` creates an output image
*`ImageCleared`* with the constant gray value *`Grayval`*.
If the input image is of type `direction`, gray values in result
image that are not in the value range that is valid for `direction`
images are set to the value 255 to mark them as invalid.
*`ImageCleared`* has the same dimensions and pixel type as the
input image *`Image`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Image`** (input_object)  singlechannelimage `→` object (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Input image.

**`ImageCleared`** (output_object)  image `→` object (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Image with constant gray value.

**`Grayval`** (input_control)  number `→`  (real / integer)

Gray value to be used for the output image.

Default:
0

Suggested values:
0, 1, 2, 5, 10, 16, 32, 64, 128, 253, 254, 255

## Result

`gen_image_proto` returns 2 (
H_MSG_TRUE)
if all parameters are correct.
If necessary, an exception is raised.

## Alternatives

`set_grayval`,
`paint_gray`,
`gen_image_const`,
`copy_image`

## See also

`get_image_pointer1`

## Module

Foundation
