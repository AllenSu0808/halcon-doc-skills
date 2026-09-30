# merge_cont_line_scan_xld (Operator)

## Name

`merge_cont_line_scan_xld` — Merge XLD contours from successive line scan images.

## Signature

`merge_cont_line_scan_xld(CurrConts, PrevConts : CurrMergedConts, PrevMergedConts : ImageHeight, Margin, MergeBorder, MaxImagesCont : )`

## Description

The operator `merge_cont_line_scan_xld` connects adjacent XLD
contours, which were extracted from adjacent images with the height
*`ImageHeight`*. This operator was especially designed to
connect contours that were extracted from images grabbed by a
line scan camera. *`CurrConts`* contains the contours from the
current image and *`PrevConts`* the contours from the previous
one.

With the help of the parameter *`MergeBorder`* two cases can be
distinguished: If the top (first) line of the current image touches
the bottom (last) line of the previous image, *`MergeBorder`*
must be set to *'top'*, otherwise set *`MergeBorder`* to
*'bottom'*. *`MergeBorder`* defines a margin to the
border. Only those end points of the contours which are inside this
margin are considered for the following merging process.

If the operator `merge_cont_line_scan_xld` is used
recursively, the parameter *`MaxImagesCont`* determines the
maximum number of images which are covered by a merged contour. All
points of the merged contour from an older image are removed.

The operator `merge_cont_line_scan_xld` returns two contour
arrays. *`PrevMergedConts`* contains all those contours from the
previous input contours *`PrevConts`*, which could not be merged
with a current contour. *`CurrMergedConts`* collects all current
contours together with the merged parts from the previous images.
Merged contours will exceed the original image, because the previous
contours are moved upward (*`MergeBorder`*=*'top'*) or
downward (*`MergeBorder`*=*'bottom'*) according to the
image height.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`CurrConts`** (input_object)  xld_cont(-array) `→` object

Current input contours.

**`PrevConts`** (input_object)  xld_cont(-array) `→` object

Merged contours from the previous iteration.

**`CurrMergedConts`** (output_object)  xld_cont(-array) `→` object

Current contours, merged with old ones where applicable.

**`PrevMergedConts`** (output_object)  xld_cont(-array) `→` object

Contours from the previous iteration which could not be
merged with the current ones.

**`ImageHeight`** (input_control)  integer `→`  (integer)

Height of the line scan images.

Default:
512

Suggested values:
240, 480, 512

**`Margin`** (input_control)  real `→`  (real / integer)

Maximum distance of contours from the image border.

Default:
0.0

Suggested values:
0.0, 1.0, 2.0, 3.0, 4.0, 5.0

**`MergeBorder`** (input_control)  string `→`  (string)

Image line of the current image, which touches the
previous image.

Default:
'top'

List of values:
'bottom', 'top'

**`MaxImagesCont`** (input_control)  integer `→`  (integer)

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
