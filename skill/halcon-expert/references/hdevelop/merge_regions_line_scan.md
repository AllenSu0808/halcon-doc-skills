# merge_regions_line_scan (Operator)

## Name

`merge_regions_line_scan` — Merge regions from line scan images.

## Signature

`merge_regions_line_scan(CurrRegions, PrevRegions : CurrMergedRegions, PrevMergedRegions : ImageHeight, MergeBorder, MaxImagesRegion : )`

## Description

The operator `merge_regions_line_scan` connects adjacent
regions, which were segmented from adjacent images with the height
*`ImageHeight`*. This operator was especially designed to
process regions that were extracted from images grabbed by a
line scan camera. *`CurrRegions`* contains the regions from the
current image and *`PrevRegions`* the regions from the previous
one.

With the help of the parameter *`MergeBorder`* two cases can be
distinguished: If the top (first) line of the current image touches
the bottom (last) line of the previous image, *`MergeBorder`*
must be set to *'top'*, otherwise set *`MergeBorder`* to
*'bottom'*.

If the operator `merge_regions_line_scan` is used
recursively, the parameter *`MaxImagesRegion`* determines the
maximum number of images which are covered by a merged region. All
older region parts are removed.

The operator `merge_regions_line_scan` returns two region
arrays. *`PrevMergedRegions`* contains all those regions from
the previous input regions *`PrevRegions`*, which could not be
merged with a current region. *`CurrMergedRegions`* collects
all current regions together with the merged parts from the previous
images. Merged regions will exceed the original image, because the
previous regions are moved upward
(*`MergeBorder`*=*'top'*) or downward
(*`MergeBorder`*=*'bottom'*) according to the image
height. For this the system parameter *'clip_region'* (see
also [`set_system`](set_system.md)) will internally be set to *'false'*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`CurrRegions`** (input_object)  region(-array) `→` object

Current input regions.

**`PrevRegions`** (input_object)  region(-array) `→` object

Merged regions from the previous iteration.

**`CurrMergedRegions`** (output_object)  region(-array) `→` object

Current regions, merged with old ones where applicable.

**`PrevMergedRegions`** (output_object)  region(-array) `→` object

Regions from the previous iteration which could not be
merged with the current ones.

**`ImageHeight`** (input_control)  integer `→`  (integer)

Height of the line scan images.

Default:
512

Suggested values:
240, 480, 512, 1024

**`MergeBorder`** (input_control)  string `→`  (string)

Image line of the current image, which touches the
previous image.

Default:
'top'

List of values:
'bottom', 'top'

**`MaxImagesRegion`** (input_control)  integer `→`  (integer)

Maximum number of images for a single region.

Default:
3

Suggested values:
1, 2, 3, 4, 5

## Result

The operator `merge_regions_line_scan` returns the value 2 (
H_MSG_TRUE)
if the given parameters are correct.
Otherwise, an exception will be raised.

## Module

Foundation
