# MergeRegionsLineScan (Operator)

## Name

`MergeRegionsLineScan` — Merge regions from line scan images.

## Signature

`static void HOperatorSet.MergeRegionsLineScan(HObject currRegions, HObject prevRegions, out HObject currMergedRegions, out HObject prevMergedRegions, HTuple imageHeight, HTuple mergeBorder, HTuple maxImagesRegion)`

`HRegion HRegion.MergeRegionsLineScan(HRegion prevRegions, out HRegion prevMergedRegions, int imageHeight, string mergeBorder, int maxImagesRegion)`

## Description

The operator `MergeRegionsLineScan` connects adjacent
regions, which were segmented from adjacent images with the height
*`imageHeight`*. This operator was especially designed to
process regions that were extracted from images grabbed by a
line scan camera. *`currRegions`* contains the regions from the
current image and *`prevRegions`* the regions from the previous
one.

With the help of the parameter *`mergeBorder`* two cases can be
distinguished: If the top (first) line of the current image touches
the bottom (last) line of the previous image, *`mergeBorder`*
must be set to *"top"*, otherwise set *`mergeBorder`* to
*"bottom"*.

If the operator `MergeRegionsLineScan` is used
recursively, the parameter *`maxImagesRegion`* determines the
maximum number of images which are covered by a merged region. All
older region parts are removed.

The operator `MergeRegionsLineScan` returns two region
arrays. *`prevMergedRegions`* contains all those regions from
the previous input regions *`prevRegions`*, which could not be
merged with a current region. *`currMergedRegions`* collects
all current regions together with the merged parts from the previous
images. Merged regions will exceed the original image, because the
previous regions are moved upward
(*`mergeBorder`*=*"top"*) or downward
(*`mergeBorder`*=*"bottom"*) according to the image
height. For this the system parameter *"clip_region"* (see
also [`SetSystem`](set_system.md)) will internally be set to *"false"*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`currRegions`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Current input regions.

**`prevRegions`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Merged regions from the previous iteration.

**`currMergedRegions`** (output_object)  region(-array) `→` [HRegion](HRegion.md)

Current regions, merged with old ones where applicable.

**`prevMergedRegions`** (output_object)  region(-array) `→` [HRegion](HRegion.md)

Regions from the previous iteration which could not be
merged with the current ones.

**`imageHeight`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Height of the line scan images.

Default:
512

Suggested values:
240, 480, 512, 1024

**`mergeBorder`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Image line of the current image, which touches the
previous image.

Default:
"top"

List of values:
"bottom", "top"

**`maxImagesRegion`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Maximum number of images for a single region.

Default:
3

Suggested values:
1, 2, 3, 4, 5

## Result

The operator `MergeRegionsLineScan` returns the value 2 (
H_MSG_TRUE)
if the given parameters are correct.
Otherwise, an exception will be raised.

## Module

Foundation
