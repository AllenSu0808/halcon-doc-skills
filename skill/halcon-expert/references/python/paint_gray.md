# paint_gray (Operator)

## Name

`paint_gray` — Paint the gray values of an image into another image.

## Signature

`def paint_gray(image_source: HObject, image_destination: HObject) -> HObject`

## Description

`paint_gray` paints the gray values of the image given in
*`image_source`* into the image in *`image_destination`* and returns
the resulting image in *`mixed_image`*. Only the gray values of the
domain of *`image_source`* are copied (see [`reduce_domain`](reduce_domain.md)).

As an alternative to `paint_gray`, you can use the operator
[`overpaint_gray`](overpaint_gray.md), which directly paints the gray values into
*`image_destination`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`image_source`** (input_object)  (multichannel-)image `→` HObject (byte / direction / cyclic / int1 / int2 / uint2 / int4 / real / complex / vector_field)

Input image containing the desired gray values.

**`image_destination`** (input_object)  (multichannel-)image `→` HObject (byte / direction / cyclic / int1 / int2 / uint2 / int4 / real / complex / vector_field)

Input image to be painted over.

**`mixed_image`** (output_object)  image `→` HObject (byte / direction / cyclic / int1 / int2 / uint2 / int4 / real / complex / vector_field)

Result image.

## Result

`paint_gray` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. If necessary, an exception is raised.

## Possible Predecessors

`read_image`,
`gen_image_const`,
`gen_image_proto`

## Alternatives

`get_image_pointer1`,
`set_grayval`,
`copy_image`,
`overpaint_gray`

## See also

`paint_region`,
`overpaint_region`

## Module

Foundation
