# copy_image (Operator)

## Name

`copy_image` — Copy an image and allocate new memory for it.

## Signature

`copy_image(Image : DupImage : : )`

## Description

`copy_image` copies the input image into a new image with the
same domain as the input image. In contrast to HALCON operators
such as [`copy_obj`](copy_obj.md), physical copies of all channels are
created. This can be used, for example, to modify the gray values
of the new image (see [`get_image_pointer1`](get_image_pointer1.md)).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Image`** (input_object)  (multichannel-)image(-array) `→` object (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Image to be copied.

**`DupImage`** (output_object)  (multichannel-)image(-array) `→` object (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Copied image.

## Possible Predecessors

`read_image`,
`gen_image_const`

## Possible Successors

`set_grayval`,
`get_image_pointer1`

## Alternatives

`set_grayval`,
`paint_gray`,
`gen_image_const`,
`gen_image_proto`

## See also

`get_image_pointer1`

## Module

Foundation
