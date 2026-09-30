# merge_cont_line_scan_xld (Operator)

## Name

`merge_cont_line_scan_xld` — Merge XLD contours from successive line scan images.

## Signature

`def merge_cont_line_scan_xld(curr_conts: HObject, prev_conts: HObject, image_height: int, margin: Union[float, int], merge_border: str, max_images_cont: int) -> Tuple[HObject, HObject]`

## Description

The operator `merge_cont_line_scan_xld` connects adjacent XLD
contours, which were extracted from adjacent images with the height
*`image_height`*. This operator was especially designed to
connect contours that were extracted from images grabbed by a
line scan camera. *`curr_conts`* contains the contours from the
current image and *`prev_conts`* the contours from the previous
one.

With the help of the parameter *`merge_border`* two cases can be
distinguished: If the top (first) line of the current image touches
the bottom (last) line of the previous image, *`merge_border`*
must be set to *"top"*, otherwise set *`merge_border`* to
*"bottom"*. *`merge_border`* defines a margin to the
border. Only those end points of the contours which are inside this
margin are considered for the following merging process.

If the operator `merge_cont_line_scan_xld` is used
recursively, the parameter *`max_images_cont`* determines the
maximum number of images which are covered by a merged contour. All
points of the merged contour from an older image are removed.

The operator `merge_cont_line_scan_xld` returns two contour
arrays. *`prev_merged_conts`* contains all those contours from the
previous input contours *`prev_conts`*, which could not be merged
with a current contour. *`curr_merged_conts`* collects all current
contours together with the merged parts from the previous images.
Merged contours will exceed the original image, because the previous
contours are moved upward (*`merge_border`*=*"top"*) or
downward (*`merge_border`*=*"bottom"*) according to the
image height.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`curr_conts`** (input_object)  xld_cont(-array) `→` HObject

Current input contours.

**`prev_conts`** (input_object)  xld_cont(-array) `→` HObject

Merged contours from the previous iteration.

**`curr_merged_conts`** (output_object)  xld_cont(-array) `→` HObject

Current contours, merged with old ones where applicable.

**`prev_merged_conts`** (output_object)  xld_cont(-array) `→` HObject

Contours from the previous iteration which could not be
merged with the current ones.

**`image_height`** (input_control)  integer `→` int

Height of the line scan images.

Default:
512

Suggested values:
240, 480, 512

**`margin`** (input_control)  real `→` Union[float, int]

Maximum distance of contours from the image border.

Default:
0.0

Suggested values:
0.0, 1.0, 2.0, 3.0, 4.0, 5.0

**`merge_border`** (input_control)  string `→` str

Image line of the current image, which touches the
previous image.

Default:
"top"

List of values:
"bottom", "top"

**`max_images_cont`** (input_control)  integer `→` int

Maximum number of images covered by one contour.

Default:
3

Suggested values:
1, 2, 3, 4, 5

## Result

The operator `merge_cont_line_scan_xld` returns the value 2 (
H_MSG_TRUE)
if the given parameters are correct.
Otherwise, an exception will be raised.

## Module

Foundation
