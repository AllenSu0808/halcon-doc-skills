# overpaint_region (Operator)

## Name

`overpaint_region` — Overpaint regions in an image.

## Signature

`def overpaint_region(image: HObject, region: HObject, grayval: MaybeSequence[Union[int, float]], type: str) -> None`

## Description

`overpaint_region` paints the regions given in
*`region`* with a constant gray value into the image given in
*`image`*. These gray values can either
be specified for each channel once, valid for all regions, or for each
region separately. To define the latter, group the channel gray values
g of each region and concatenate them to a tuple according to
the regions' order, e.g., for a three channel image:
[g(channel1,region1), g(channel2,region1), g(channel3,region1), g(channel1,region2), ... ].
If the input image is of type `direction`, gray values that are not
in the value range that is valid for `direction` images are set to
the value 255 to mark them as invalid.
The parameter *`type`* determines whether
the region should be painted filled (*"fill"*) or whether
only its boundary should be painted (*"margin"*).

If you do not want to modify *`image`* itself, you can use the operator
[`paint_region`](paint_region.md), which returns the result in a newly created image.

## Attention

`overpaint_region` modifies the content of an already existing image
(*`image`*). Besides, even other image objects may be affected: For
example, if you created *`image`* via [`copy_obj`](copy_obj.md) from another
image object (or vice versa), `overpaint_region` will also modify the
image matrix of this other image object. Therefore, `overpaint_region`
should only be used to overpaint newly created image objects. Typical
operators for this task are, e.g., [`gen_image_const`](gen_image_const.md) (creates a new
image with a specified size), [`gen_image_proto`](gen_image_proto.md) (creates an image with
the size of a specified prototype image) or [`copy_image`](copy_image.md) (creates an
image as the copy of a specified image).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- image

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`image`** (input_object, state is modified)  (multichannel-)image `→` HObject (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex)

Image in which the regions are to be painted.

**`region`** (input_object)  region(-array) `→` HObject

Regions to be painted into the input image.

**`grayval`** (input_control)  number(-array) `→` MaybeSequence[Union[int, float]]

Desired gray values of the regions.

Default:
255.0

Suggested values:
0.0, 1.0, 2.0, 5.0, 10.0, 16.0, 32.0, 64.0, 128.0, 253.0, 254.0, 255.0

**`type`** (input_control)  string `→` str

Paint regions filled or as boundaries.

Default:
"fill"

List of values:
"fill", "margin"

## Result

`overpaint_region` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. If the input is empty the behavior can be set via
`set_system(::'no_object_result',<Result>:)`.
If necessary, an exception is raised.

## Possible Predecessors

`read_image`,
`gen_image_const`,
`gen_image_proto`,
`reduce_domain`

## Alternatives

`set_grayval`,
`paint_region`,
`paint_xld`

## See also

`reduce_domain`,
`set_draw`,
`paint_gray`,
`overpaint_gray`,
`gen_image_const`

## Module

Foundation
