# CopyImage (Operator)

## Name

`CopyImage` — Copy an image and allocate new memory for it.

## Signature

`static void HOperatorSet.CopyImage(HObject image, out HObject dupImage)`

`HImage HImage.CopyImage()`

## Description

`CopyImage` copies the input image into a new image with the
same domain as the input image. In contrast to HALCON operators
such as [`CopyObj`](copy_obj.md), physical copies of all channels are
created. This can be used, for example, to modify the gray values
of the new image (see [`GetImagePointer1`](get_image_pointer1.md)).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`image`** (input_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Image to be copied.

**`dupImage`** (output_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Copied image.

## Possible Predecessors

`ReadImage`,
`GenImageConst`

## Possible Successors

`SetGrayval`,
`GetImagePointer1`

## Alternatives

`SetGrayval`,
`PaintGray`,
`GenImageConst`,
`GenImageProto`

## See also

`GetImagePointer1`

## Module

Foundation
