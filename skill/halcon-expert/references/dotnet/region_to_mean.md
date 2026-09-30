# RegionToMean (Operator)

## Name

`RegionToMean` — Paint regions with their average gray value.

## Signature

`static void HOperatorSet.RegionToMean(HObject regions, HObject image, out HObject imageMean)`

`HImage HImage.RegionToMean(HRegion regions)`

`HImage HRegion.RegionToMean(HImage image)`

## Description

`RegionToMean` returns an image in which the regions
*`regions`* are painted with their average gray value based on
the image *`image`*. This operator is mainly
intended to visualize segmentation results.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on channel level.

## Parameters

**`regions`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Input regions.

**`image`** (input_object)  (multichannel-)image `→` [HImage](HImage.md) (byte / uint2)

original gray-value image.

**`imageMean`** (output_object)  image `→` [HImage](HImage.md) (byte / uint2)

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

`RegionToMean` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. If the input is empty the behavior can be set via
`set_system('no_object_result',<Result>)`.
If necessary, an exception is raised.

## Possible Predecessors

`Regiongrowing`,
`Connection`

## Possible Successors

`DispImage`

## Alternatives

`PaintRegion`,
`Intensity`

## Module

Foundation
