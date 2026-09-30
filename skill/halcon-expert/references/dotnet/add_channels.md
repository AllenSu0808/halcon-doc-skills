# AddChannels (Operator)

## Name

`AddChannels` — Add gray values to regions.

## Signature

`static void HOperatorSet.AddChannels(HObject regions, HObject image, out HObject grayRegions)`

`HImage HRegion.AddChannels(HImage image)`

## Description

The operator `AddChannels` creates an array of images
*`grayRegions`* with an element for every input region in
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

**`regions`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Input regions (without pixel values).

**`image`** (input_object)  (multichannel-)image `→` [HImage](HImage.md) (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Input image with pixel values for regions.

**`grayRegions`** (output_object)  image(-array) `→` [HImage](HImage.md) (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Output image(s) with regions and pixel values
(one image per input region).

Number of elements:
Regions == GrayRegions

## Possible Predecessors

`Threshold`,
`Regiongrowing`,
`GenCircle`,
`DrawRegion`

## Possible Successors

`Threshold`,
`Regiongrowing`,
`GetDomain`

## Alternatives

`ChangeDomain`,
`ReduceDomain`

## See also

`FullDomain`,
`GetDomain`,
`Intersection`

## Module

Foundation
