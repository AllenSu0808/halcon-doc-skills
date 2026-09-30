# add_channels (Operator)

## Name

`add_channels` — Add gray values to regions.

## Signature

`def add_channels(regions: HObject, image: HObject) -> HObject`

## Description

The operator `add_channels` creates an array of images
*`gray_regions`* with an element for every input region in
*`regions`*. These images correspond to the input image *`image`*
with a reduced domain, namely the intersection of the definition domain of
the input image with the region.
Thus, the new definition domain can be a subset of the region.
Thereby the size of the image matrix is not changed and all channels of
*`image`* are adopted.

## Execution Information

- Supports objects on compute devices.
- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`regions`** (input_object)  region(-array) `→` HObject

Input regions (without pixel values).

**`image`** (input_object)  (multichannel-)image `→` HObject (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Input image with pixel values for regions.

**`gray_regions`** (output_object)  image(-array) `→` HObject (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Output image(s) with regions and pixel values
(one image per input region).

Number of elements:
Regions == GrayRegions

## Possible Predecessors

`threshold`,
`regiongrowing`,
`gen_circle`,
`draw_region`

## Possible Successors

`threshold`,
`regiongrowing`,
`get_domain`

## Alternatives

`change_domain`,
`reduce_domain`

## See also

`full_domain`,
`get_domain`,
`intersection`

## Module

Foundation
