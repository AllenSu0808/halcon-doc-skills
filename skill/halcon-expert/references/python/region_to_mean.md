# region_to_mean (Operator)

## Name

`region_to_mean` — Paint regions with their average gray value.

## Signature

`def region_to_mean(regions: HObject, image: HObject) -> HObject`

## Description

`region_to_mean` returns an image in which the regions
*`regions`* are painted with their average gray value based on
the image *`image`*. This operator is mainly
intended to visualize segmentation results.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on channel level.

## Parameters

**`regions`** (input_object)  region(-array) `→` HObject

Input regions.

**`image`** (input_object)  (multichannel-)image `→` HObject (byte / uint2)

original gray-value image.

**`image_mean`** (output_object)  image `→` HObject (byte / uint2)

Result image with painted regions.

## Result

`region_to_mean` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. If the input is empty the behavior can be set via
`set_system('no_object_result',<Result>)`.
If necessary, an exception is raised.

## Possible Predecessors

`regiongrowing`,
`connection`

## Possible Successors

`disp_image`

## Alternatives

`paint_region`,
`intensity`

## Module

Foundation
