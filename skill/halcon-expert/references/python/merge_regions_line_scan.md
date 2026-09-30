# merge_regions_line_scan (Operator)

## Name

`merge_regions_line_scan` — Merge regions from line scan images.

## Signature

`def merge_regions_line_scan(curr_regions: HObject, prev_regions: HObject, image_height: int, merge_border: str, max_images_region: int) -> Tuple[HObject, HObject]`

## Description

The operator `merge_regions_line_scan` connects adjacent
regions, which were segmented from adjacent images with the height
*`image_height`*. This operator was especially designed to
process regions that were extracted from images grabbed by a
line scan camera. *`curr_regions`* contains the regions from the
current image and *`prev_regions`* the regions from the previous
one.

With the help of the parameter *`merge_border`* two cases can be
distinguished: If the top (first) line of the current image touches
the bottom (last) line of the previous image, *`merge_border`*
must be set to *"top"*, otherwise set *`merge_border`* to
*"bottom"*.

If the operator `merge_regions_line_scan` is used
recursively, the parameter *`max_images_region`* determines the
maximum number of images which are covered by a merged region. All
older region parts are removed.

The operator `merge_regions_line_scan` returns two region
arrays. *`prev_merged_regions`* contains all those regions from
the previous input regions *`prev_regions`*, which could not be
merged with a current region. *`curr_merged_regions`* collects
all current regions together with the merged parts from the previous
images. Merged regions will exceed the original image, because the
previous regions are moved upward
(*`merge_border`*=*"top"*) or downward
(*`merge_border`*=*"bottom"*) according to the image
height. For this the system parameter *"clip_region"* (see
also [`set_system`](set_system.md)) will internally be set to *"false"*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`curr_regions`** (input_object)  region(-array) `→` HObject

Current input regions.

**`prev_regions`** (input_object)  region(-array) `→` HObject

Merged regions from the previous iteration.

**`curr_merged_regions`** (output_object)  region(-array) `→` HObject

Current regions, merged with old ones where applicable.

**`prev_merged_regions`** (output_object)  region(-array) `→` HObject

Regions from the previous iteration which could not be
merged with the current ones.

**`image_height`** (input_control)  integer `→` int

Height of the line scan images.

Default:
512

Suggested values:
240, 480, 512, 1024

**`merge_border`** (input_control)  string `→` str

Image line of the current image, which touches the
previous image.

Default:
"top"

List of values:
"bottom", "top"

**`max_images_region`** (input_control)  integer `→` int

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
