# region_to_mean (Operator)

## Name

`region_to_mean` — Paint regions with their average gray value.

## Signature

`region_to_mean(Regions, Image : ImageMean : : )`

## Description

`region_to_mean` returns an image in which the regions
*`Regions`* are painted with their average gray value based on
the image *`Image`*. This operator is mainly
intended to visualize segmentation results.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on channel level.

## Parameters

**`Regions`** (input_object)  region(-array) `→` object

Input regions.

**`Image`** (input_object)  (multichannel-)image `→` object (byte / uint2)

original gray-value image.

**`ImageMean`** (output_object)  image `→` object (byte / uint2)

Result image with painted regions.

## Example (HDevelop)

```
read_image(Image,'fabrik')
regiongrowing(Image,Regions,3,3,6,100)
region_to_mean(Regions,Image,Disp)
dev_display(Disp)
dev_set_draw('margin')
dev_display(Regions)
```

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
