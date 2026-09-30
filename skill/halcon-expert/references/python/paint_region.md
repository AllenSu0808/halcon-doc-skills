# paint_region (Operator)

## Name

`paint_region` — Paint regions into an image.

## Signature

`def paint_region(region: HObject, image: HObject, grayval: MaybeSequence[Union[int, float]], type: str) -> HObject`

## Description

`paint_region` paints the regions given in *`region`* with a
constant gray value into the image given in *`image`* and returns the
result in *`image_result`*. These gray values can either be specified
for each channel once, valid for all regions, or for each region
separately. To define the latter, group the channel gray values g of each region and concatenate them to a tuple according to the regions'
order, e.g., for a three channel image:

[g(channel1,region1), g(channel2,region1), g(channel3,region1), g(channel1,region2), ... ].
If the input image is of type `direction`, gray values that are not
in the value range that is valid for `direction` images are set to
the value 255 to mark them as invalid.
The parameter *`type`* determines whether the region should be painted
filled (*"fill"*) or whether only its boundary should be painted
(*"margin"*).

As an alternative to `paint_region`, you can use the operator
[`overpaint_region`](overpaint_region.md), which directly paints the regions into
*`image`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`region`** (input_object)  region(-array) `→` HObject

Regions to be painted into the input image.

**`image`** (input_object)  (multichannel-)image `→` HObject (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex)

Image in which the regions are to be painted.

**`image_result`** (output_object)  image `→` HObject (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex)

Image containing the result.

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

`paint_region` returns 2 (
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
`overpaint_region`,
`paint_xld`

## See also

`reduce_domain`,
`paint_gray`,
`overpaint_gray`,
`set_draw`,
`gen_image_const`

## Module

Foundation
