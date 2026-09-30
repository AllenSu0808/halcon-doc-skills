# GenImageProto (Operator)

## Name

`GenImageProto` — Create an image with a specified constant gray value.

## Signature

`static void HOperatorSet.GenImageProto(HObject image, out HObject imageCleared, HTuple grayval)`

`HImage HImage.GenImageProto(HTuple grayval)`

`HImage HImage.GenImageProto(double grayval)`

## Description

`GenImageProto` creates an output image
*`imageCleared`* with the constant gray value *`grayval`*.
If the input image is of type `direction`, gray values in result
image that are not in the value range that is valid for `direction`
images are set to the value 255 to mark them as invalid.
*`imageCleared`* has the same dimensions and pixel type as the
input image *`image`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`image`** (input_object)  singlechannelimage `→` [HImage](HImage.md) (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Input image.

**`imageCleared`** (output_object)  image `→` [HImage](HImage.md) (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Image with constant gray value.

**`grayval`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / int / long)

Gray value to be used for the output image.

Default:
0

Suggested values:
0, 1, 2, 5, 10, 16, 32, 64, 128, 253, 254, 255

## Result

`GenImageProto` returns 2 (
H_MSG_TRUE)
if all parameters are correct.
If necessary, an exception is raised.

## Alternatives

`SetGrayval`,
`PaintGray`,
`GenImageConst`,
`CopyImage`

## See also

`GetImagePointer1`

## Module

Foundation
