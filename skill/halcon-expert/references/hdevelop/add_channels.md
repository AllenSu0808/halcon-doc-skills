# add_channels (Operator)

## Name

`add_channels` — Add gray values to regions.

## Signature

`add_channels(Regions, Image : GrayRegions : : )`

## Description

The operator `add_channels` creates an array of images
*`GrayRegions`* with an element for every input region in
*`Regions`*. These images correspond to the input image *`Image`*
with a reduced domain, namely the intersection of the definition domain of
the input image with the region.
Thus, the new definition domain can be a subset of the region.
Thereby the size of the image matrix is not changed and all channels of
*`Image`* are adopted.

## Execution Information

- Supports objects on compute devices.
- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`Regions`** (input_object)  region(-array) `→` object

Input regions (without pixel values).

**`Image`** (input_object)  (multichannel-)image `→` object (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Input image with pixel values for regions.

**`GrayRegions`** (output_object)  image(-array) `→` object (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

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
