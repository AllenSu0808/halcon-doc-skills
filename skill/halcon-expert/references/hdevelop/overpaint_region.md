# overpaint_region (Operator)

## Name

`overpaint_region` — Overpaint regions in an image.

## Signature

`overpaint_region(Image, Region : : Grayval, Type : )`

## Description

`overpaint_region` paints the regions given in
*`Region`* with a constant gray value into the image given in
*`Image`*. These gray values can either
be specified for each channel once, valid for all regions, or for each
region separately. To define the latter, group the channel gray values
g of each region and concatenate them to a tuple according to
the regions' order, e.g., for a three channel image:
[g(channel1,region1), g(channel2,region1), g(channel3,region1), g(channel1,region2), ... ].
If the input image is of type `direction`, gray values that are not
in the value range that is valid for `direction` images are set to
the value 255 to mark them as invalid.
The parameter *`Type`* determines whether
the region should be painted filled (*'fill'*) or whether
only its boundary should be painted (*'margin'*).

If you do not want to modify *`Image`* itself, you can use the operator
[`paint_region`](paint_region.md), which returns the result in a newly created image.

## Attention

`overpaint_region` modifies the content of an already existing image
(*`Image`*). Besides, even other image objects may be affected: For
example, if you created *`Image`* via [`copy_obj`](copy_obj.md) from another
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

- Image

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`Image`** (input_object, state is modified)  (multichannel-)image `→` object (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex)

Image in which the regions are to be painted.

**`Region`** (input_object)  region(-array) `→` object

Regions to be painted into the input image.

**`Grayval`** (input_control)  number(-array) `→`  (real / integer)

Desired gray values of the regions.

Default:
255.0

Suggested values:
0.0, 1.0, 2.0, 5.0, 10.0, 16.0, 32.0, 64.0, 128.0, 253.0, 254.0, 255.0

**`Type`** (input_control)  string `→`  (string)

Paint regions filled or as boundaries.

Default:
'fill'

List of values:
'fill', 'margin'

## Example (HDevelop)

```
* Paint a rectangle into a new image (New1)

gen_rectangle1(Rectangle,100.0,100.0,300.0,300.0)
* generate a black image
gen_image_const(New1,'byte', 768, 576)
* paint a white rectangle
overpaint_region(New1,Rectangle,255.0,'fill')
```

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
