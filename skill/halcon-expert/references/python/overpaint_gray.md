# overpaint_gray (Operator)

## Name

`overpaint_gray` — Overpaint the gray values of an image.

## Signature

`def overpaint_gray(image_destination: HObject, image_source: HObject) -> None`

## Description

`overpaint_gray` copies the gray values of the image given
in *`image_source`* into the image in
*`image_destination`*. Only the gray values of the domain of
*`image_source`* are copied (see [`reduce_domain`](reduce_domain.md)).

If you do not want to modify *`image_destination`* itself, you can use
the operator [`paint_gray`](paint_gray.md), which returns the result in a newly created
image.

## Attention

`overpaint_gray` modifies the content of an already existing image
(*`image_destination`*). Besides, even other image objects may be
affected: For example, if you created *`image_destination`* via
[`copy_obj`](copy_obj.md) from another image object (or vice versa),
`overpaint_gray` will also modify the image matrix of this other image
object. Therefore, `overpaint_gray` should only be used to overpaint
newly created image objects. Typical operators for this task are, e.g.,
[`gen_image_const`](gen_image_const.md) (creates a new image with a specified size),
[`gen_image_proto`](gen_image_proto.md) (creates an image with the size of a specified
prototype image) or [`copy_image`](copy_image.md) (creates an image as the copy of
a specified image).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- image_destination

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`image_destination`** (input_object, state is modified)  (multichannel-)image `→` HObject (byte / direction / cyclic / int1 / int2 / uint2 / int4 / real / complex / vector_field)

Input image to be painted over.

**`image_source`** (input_object)  (multichannel-)image `→` HObject (byte / direction / cyclic / int1 / int2 / uint2 / int4 / real / complex / vector_field)

Input image containing the desired gray values.

## Result

`overpaint_gray` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. If necessary, an exception is raised.

## Possible Predecessors

`read_image`,
`gen_image_const`,
`gen_image_proto`

## Alternatives

`get_image_pointer1`,
`paint_gray`,
`set_grayval`,
`copy_image`

## See also

`paint_region`,
`overpaint_region`

## Module

Foundation
